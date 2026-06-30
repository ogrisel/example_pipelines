# Parallel scalability of scikit-learn pipelines

The purpose of this repo is to easily collect some performance results for
scikit-learn pipelines in various settings:

- Nested OpenBLAS/OpenMP threading under Python level threads or process;
- GIL Python vs free-threading Python
- pypi packages vs conda-forge packages
- OpenBLAS vs Accelerate vs MKL
- pthreads OpenBLAS vs OpenMP OpenBLAS
- Intel/Linux vs Apple M4/macOS
- ...


## Run benchmarks

```
pix run run-all
```

## Analyze results

```
pixi run -e pypi-gil refresh-results-summary
```

Browse results: [RESULTS_SUMMARY.md](./RESULTS_SUMMARY.md).