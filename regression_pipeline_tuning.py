# %%
import argparse
import os
from functools import partial
from importlib import import_module
import time
from pprint import pprint
import warnings

import joblib
import numpy as np
import pandas as pd

import sklearn
from sklearn.compose import (
    ColumnTransformer,
    TransformedTargetRegressor,
    make_column_selector,
)
from sklearn.datasets import fetch_openml
from sklearn.kernel_approximation import Nystroem
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import RandomizedSearchCV, ShuffleSplit, KFold
from sklearn.pipeline import FeatureUnion, make_pipeline
from sklearn.preprocessing import (
    FunctionTransformer,
    MinMaxScaler,
    OneHotEncoder,
    SplineTransformer,
    TargetEncoder,
    PowerTransformer,
)

# %%
warnings.filterwarnings("ignore", category=UserWarning, message=".*A worker stopped.*")
# %%
X, y = fetch_openml(data_id=42165, as_frame=True, return_X_y=True)
y = y.astype(np.float32).values
cv = ShuffleSplit(n_splits=3, test_size=0.2, random_state=42)


# %%
# Parse the CLI arguments to retrieve the array API namespace, device and number of workers, but
# only when not run as a Jupyter notebook.
def in_notebook():
    try:
        cfg = get_ipython().config  # pyright: ignore[reportUndefinedVariable]
        if "IPKernelApp" in cfg:
            return True
    except NameError:
        return False


xp = np
device_name = "cpu"
joblib_backend = "loky"

if not in_notebook():
    parser = argparse.ArgumentParser()
    parser.add_argument("--array-api-namespace", type=str, default="numpy")
    parser.add_argument("--device", type=str, default="cpu")
    parser.add_argument("--max-n-workers", type=int, default=1)
    parser.add_argument("--joblib-backend", type=str, default=None)
    args = parser.parse_args()

    if args.joblib_backend is not None:
        joblib_backend = args.joblib_backend

    if args.array_api_namespace is not None:
        os.environ["SCIPY_ARRAY_API"] = "1"
        os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
        warnings.filterwarnings(
            "ignore",
            category=UserWarning,
            message=".*is not currently supported on the MPS.*",
        )
        sklearn.set_config(array_api_dispatch=True)
        xp = import_module(args.array_api_namespace)
        device_name = args.device

print(f"Array API namespace: {xp.__name__}")
print(f"Device: {device_name}")
joblib.parallel_config(backend=joblib_backend)
print(f"Joblib backend: {joblib_backend}")

# %%
print("Runtime environment:")
sklearn.show_versions()
print()

# %%
target_encoder = make_pipeline(
    TargetEncoder(
        target_type="continuous", cv=KFold(n_splits=5, shuffle=True, random_state=42)
    ),
    MinMaxScaler(),
)
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            FeatureUnion(
                [
                    (
                        "onehot",
                        OneHotEncoder(
                            sparse_output=False,
                            handle_unknown="infrequent_if_exist",
                            max_categories=10,
                            min_frequency=5,
                        ),
                    ),
                    ("target", target_encoder),
                ]
            ),
            make_column_selector(dtype_include=["category", "string"]),
        ),
        (
            "numeric",
            SplineTransformer(n_knots=10, degree=2, handle_missing="zeros"),
            make_column_selector(dtype_include=["number"]),
        ),
    ]
)

poly_reg = make_pipeline(
    preprocessor,
    FunctionTransformer(
        lambda X: X.astype(np.float32),
        feature_names_out="one-to-one",
        check_inverse=False,
    ),
    FunctionTransformer(
        partial(xp.asarray, device=device_name),
        feature_names_out="one-to-one",
        check_inverse=False,
    ),
    Nystroem(kernel="poly", degree=2, n_components=300, random_state=42),
    # TODO: add array API support for PowerTransformer and TransformedTargetRegressor.
    # TransformedTargetRegressor(
    #     RidgeCV(alphas=np.logspace(-6, 6, 13)),
    #     transformer=PowerTransformer(),
    # ),
    RidgeCV(alphas=np.logspace(-6, 6, 13)),
)


param_grid = {
    "columntransformer__numeric__n_knots": [5, 10, 20, 50],
    "columntransformer__categorical__onehot__max_categories": [
        2,
        5,
        10,
        20,
        50,
    ],
    "columntransformer__categorical__onehot__min_frequency": [None, 2, 5, 10, 20],
    "columntransformer__categorical__target": ["drop", target_encoder],
    "nystroem__n_components": [10, 30, 100, 300],
    "nystroem__kernel": ["poly", "rbf"],
    "nystroem__degree": [2, 3],
    "nystroem__gamma": np.logspace(-6, 6, 25),
}
# TODO: run for various values of n_jobs and plot a scalability curve.
cpu_count = joblib.cpu_count(only_physical_cores=True)
n_jobs_list = 2 ** np.arange(int(np.log2(cpu_count) + 1))
results = []

n_iter = 30
print(f"Benchmarking hyper-parameter tuning with {n_iter=} and {cv.n_splits=}...")
for n_jobs in n_jobs_list:
    # Warm-up joblib workers.
    joblib.Parallel(n_jobs=n_jobs)([joblib.delayed(lambda: None)() for _ in range(10)])

    # Measure the time taken to tuned hyperparameters.
    tic = time.time()
    hp_search = RandomizedSearchCV(
        poly_reg,
        param_grid,
        n_iter=n_iter,
        cv=cv,
        n_jobs=n_jobs,
        scoring="r2",
        error_score="raise",
        random_state=42,
    )
    hp_search.fit(X, y)
    toc = time.time()
    duration = toc - tic
    results.append(
        {
            "n_jobs": n_jobs,
            "duration": duration,
            "speedup": results[0]["duration"] / duration if results else 1,
        }
    )
    print(
        f"n_jobs: {n_jobs}, duration: {duration:.3f} s, speedup: {results[-1]['speedup']:.2f}x, Best R2: {hp_search.best_score_:.4f}"
    )


# %%
