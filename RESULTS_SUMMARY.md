# Regression pipeline tuning results

Loaded 32 result file(s) from `/Users/ogrisel/tmp/pipelines/results/regression_pipeline_tuning`.

## Apple M4 (arm64, 10 logical cores)

Runs: 16 total, 16 successful, 0 failed

### Most efficient (absolute speed)

| Highlight | Setup | Baseline | Best | Run |
| --- | --- | --- | --- | --- |
| best overall | pypi-gil / loky / gil | 11.30s | 6.34s @ n_jobs=8 | [6310fc6a-37ac-4415-ae3d-71b0505f1c09](results/regression_pipeline_tuning/20260630T110737_6310fc6a-37ac-4415-ae3d-71b0505f1c09.json) |

### Most efficient (scalability)

| Highlight | Setup | Speedup | Parallel efficiency | Duration | Baseline | Best | Run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| peak speedup | openblas-pthreads-freethreading / loky / no-gil | 15.98x | n/a | 11.30s @ n_jobs=8 | 180.55s | 11.30s @ n_jobs=8 | [8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0](results/regression_pipeline_tuning/20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json) |
| best peak parallel efficiency | openblas-pthreads-freethreading / loky / no-gil | 15.98x | 2.00 | 11.30s @ n_jobs=8 | 180.55s | 11.30s @ n_jobs=8 | [8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0](results/regression_pipeline_tuning/20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json) |
| best max-core parallel efficiency | openblas-pthreads-freethreading / loky / no-gil | 15.98x | 2.00 | 11.30s @ n_jobs=8 | 180.55s | 11.30s @ n_jobs=8 | [8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0](results/regression_pipeline_tuning/20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json) |

### Most problematic (lack of scalability)

| Setup | Baseline | Best | Peak speedup | Speedup @ max | Slowdown @ max | Max-core efficiency | Run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| newaccelerate-gil / threading / gil | 12.50s | 12.28s @ n_jobs=2 | 1.02x (12.28s @ n_jobs=2) | 0.84x (14.82s @ n_jobs=8) | 1.19x | 0.11 | [4828c7ef-31c9-4317-910c-f372e6242e22](results/regression_pipeline_tuning/20260630T113434_4828c7ef-31c9-4317-910c-f372e6242e22.json) |
| pypi-gil / threading / gil | 12.32s | 12.32s @ n_jobs=1 | 1.00x (12.32s @ n_jobs=1) | 0.88x (14.04s @ n_jobs=8) | 1.14x | 0.11 | [acc40cf9-5d13-458f-9ac9-990a5f049670](results/regression_pipeline_tuning/20260630T110642_acc40cf9-5d13-458f-9ac9-990a5f049670.json) |
| pypi-freethreading / threading / no-gil | 12.56s | 9.09s @ n_jobs=2 | 1.38x (9.09s @ n_jobs=2) | 0.89x (14.11s @ n_jobs=8) | 1.12x | 0.11 | [c312f52b-b576-4250-9fd1-37cc98b051f1](results/regression_pipeline_tuning/20260630T110820_c312f52b-b576-4250-9fd1-37cc98b051f1.json) |
| newaccelerate-freethreading / threading / no-gil | 16.02s | 10.55s @ n_jobs=2 | 1.52x (10.55s @ n_jobs=2) | 1.07x (14.96s @ n_jobs=8) | 0.93x | 0.13 | [950d1495-7328-4b7c-87e2-71af489e799c](results/regression_pipeline_tuning/20260630T113622_950d1495-7328-4b7c-87e2-71af489e799c.json) |

### GIL vs free-threading comparisons

| Stack / backend | Metric | GIL | No-GIL | Verdict |
| --- | --- | --- | --- | --- |
| newaccelerate / loky | single-thread baseline | 12.60s | 12.86s | gil 1.02x faster |
| newaccelerate / loky | best duration | 7.84s @ n_jobs=8 | 6.49s @ n_jobs=8 | no-gil 1.21x faster |
| newaccelerate / loky | peak speedup | 1.61x (7.84s @ n_jobs=8) | 1.98x (6.49s @ n_jobs=8) | no-gil 1.23x better |
| newaccelerate / loky | speedup at max cores | 1.61x (7.84s @ n_jobs=8) | 1.98x (6.49s @ n_jobs=8) | no-gil 1.23x better |
| newaccelerate / threading | single-thread baseline | 12.50s | 16.02s | gil 1.28x faster |
| newaccelerate / threading | best duration | 12.28s @ n_jobs=2 | 10.55s @ n_jobs=2 | no-gil 1.16x faster |
| newaccelerate / threading | peak speedup | 1.02x (12.28s @ n_jobs=2) | 1.52x (10.55s @ n_jobs=2) | no-gil 1.49x better |
| newaccelerate / threading | speedup at max cores | 0.84x (14.82s @ n_jobs=8) | 1.07x (14.96s @ n_jobs=8) | no-gil 1.27x better |
| openblas-openmp / loky | single-thread baseline | 19.91s | 24.75s | gil 1.24x faster |
| openblas-openmp / loky | best duration | 7.88s @ n_jobs=8 | 9.17s @ n_jobs=8 | gil 1.16x faster |
| openblas-openmp / loky | peak speedup | 2.53x (7.88s @ n_jobs=8) | 2.70x (9.17s @ n_jobs=8) | no-gil 1.07x better |
| openblas-openmp / loky | speedup at max cores | 2.53x (7.88s @ n_jobs=8) | 2.70x (9.17s @ n_jobs=8) | no-gil 1.07x better |
| openblas-openmp / threading | single-thread baseline | 25.72s | 25.43s | no-gil 1.01x faster |
| openblas-openmp / threading | best duration | 25.72s @ n_jobs=1 | 25.43s @ n_jobs=1 | no-gil 1.01x faster |
| openblas-openmp / threading | peak speedup | 1.00x (25.72s @ n_jobs=1) | 1.00x (25.43s @ n_jobs=1) | tie |
| openblas-openmp / threading | speedup at max cores | 1.00x (25.72s @ n_jobs=1) | 1.00x (25.43s @ n_jobs=1) | tie |
| openblas-pthreads / loky | single-thread baseline | 159.49s | 180.55s | gil 1.13x faster |
| openblas-pthreads / loky | best duration | 14.54s @ n_jobs=8 | 11.30s @ n_jobs=8 | no-gil 1.29x faster |
| openblas-pthreads / loky | peak speedup | 10.97x (14.54s @ n_jobs=8) | 15.98x (11.30s @ n_jobs=8) | no-gil 1.46x better |
| openblas-pthreads / loky | speedup at max cores | 10.97x (14.54s @ n_jobs=8) | 15.98x (11.30s @ n_jobs=8) | no-gil 1.46x better |
| openblas-pthreads / threading | single-thread baseline | 134.19s | 161.83s | gil 1.21x faster |
| openblas-pthreads / threading | best duration | 69.88s @ n_jobs=4 | 71.73s @ n_jobs=4 | gil 1.03x faster |
| openblas-pthreads / threading | peak speedup | 1.92x (69.88s @ n_jobs=4) | 2.26x (71.73s @ n_jobs=4) | no-gil 1.17x better |
| openblas-pthreads / threading | speedup at max cores | 1.70x (78.92s @ n_jobs=8) | 2.03x (79.61s @ n_jobs=8) | no-gil 1.20x better |
| pypi / loky | single-thread baseline | 11.30s | 12.63s | gil 1.12x faster |
| pypi / loky | best duration | 6.34s @ n_jobs=8 | 6.64s @ n_jobs=8 | gil 1.05x faster |
| pypi / loky | peak speedup | 1.78x (6.34s @ n_jobs=8) | 1.90x (6.64s @ n_jobs=8) | no-gil 1.07x better |
| pypi / loky | speedup at max cores | 1.78x (6.34s @ n_jobs=8) | 1.90x (6.64s @ n_jobs=8) | no-gil 1.07x better |
| pypi / threading | single-thread baseline | 12.32s | 12.56s | gil 1.02x faster |
| pypi / threading | best duration | 12.32s @ n_jobs=1 | 9.09s @ n_jobs=2 | no-gil 1.36x faster |
| pypi / threading | peak speedup | 1.00x (12.32s @ n_jobs=1) | 1.38x (9.09s @ n_jobs=2) | no-gil 1.38x better |
| pypi / threading | speedup at max cores | 0.88x (14.04s @ n_jobs=8) | 0.89x (14.11s @ n_jobs=8) | no-gil 1.01x better |

#### Summary across paired stacks

| Metric | GIL wins | No-GIL wins |
| --- | --- | --- |
| single-thread baseline | 7 | 1 |
| best duration | 3 | 5 |
| peak speedup | 0 | 7 |
| speedup at max cores | 0 | 7 |

## Intel(R) Core(TM) Ultra X7 358H (x86_64, 16 logical cores)

Runs: 16 total, 16 successful, 0 failed

### Most efficient (absolute speed)

| Highlight | Setup | Baseline | Best | Run |
| --- | --- | --- | --- | --- |
| best overall | openblas-openmp-gil / loky / gil | 8.25s | 1.76s @ n_jobs=16 | [7dafeda5-8947-4f73-b7b3-0f46aafeabe5](results/regression_pipeline_tuning/20260630T121737_7dafeda5-8947-4f73-b7b3-0f46aafeabe5.json) |
| fastest single-thread baseline | pypi-gil / threading / gil | 7.81s | 7.81s @ n_jobs=1 | [5f771075-b4b8-44a1-8d3b-9528d940fce2](results/regression_pipeline_tuning/20260630T120917_5f771075-b4b8-44a1-8d3b-9528d940fce2.json) |

### Most efficient (scalability)

| Highlight | Setup | Speedup | Parallel efficiency | Duration | Baseline | Best | Run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| peak speedup | mkl-freethreading / loky / no-gil | 4.91x | n/a | 2.10s @ n_jobs=16 | 10.32s | 2.10s @ n_jobs=16 | [dc92a4d4-3f1b-449f-b999-7aad18f7c8fc](results/regression_pipeline_tuning/20260630T122251_dc92a4d4-3f1b-449f-b999-7aad18f7c8fc.json) |
| best peak parallel efficiency | openblas-openmp-freethreading / threading / no-gil | 1.25x | 0.63 | 8.24s @ n_jobs=2 | 10.30s | 8.24s @ n_jobs=2 | [5fffc163-ee00-4640-9d26-b89ab729c80f](results/regression_pipeline_tuning/20260630T121801_5fffc163-ee00-4640-9d26-b89ab729c80f.json) |
| best max-core parallel efficiency | mkl-freethreading / loky / no-gil | 4.91x | 0.31 | 2.10s @ n_jobs=16 | 10.32s | 2.10s @ n_jobs=16 | [dc92a4d4-3f1b-449f-b999-7aad18f7c8fc](results/regression_pipeline_tuning/20260630T122251_dc92a4d4-3f1b-449f-b999-7aad18f7c8fc.json) |

### Most problematic (lack of scalability)

| Setup | Baseline | Best | Peak speedup | Speedup @ max | Slowdown @ max | Max-core efficiency | Run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mkl-freethreading / threading / no-gil | 10.42s | 6.54s @ n_jobs=4 | 1.59x (6.54s @ n_jobs=4) | 0.32x (32.96s @ n_jobs=16) | 3.16x | 0.02 | [7ae1d70f-b9d1-48d0-9a7b-87d432594d1c](results/regression_pipeline_tuning/20260630T122140_7ae1d70f-b9d1-48d0-9a7b-87d432594d1c.json) |
| openblas-openmp-gil / threading / gil | 8.26s | 8.26s @ n_jobs=1 | 1.00x (8.26s @ n_jobs=1) | 0.32x (25.86s @ n_jobs=16) | 3.13x | 0.02 | [d9b19d91-1ab2-4c9f-a66d-f1502276d58e](results/regression_pipeline_tuning/20260630T121618_d9b19d91-1ab2-4c9f-a66d-f1502276d58e.json) |
| openblas-openmp-freethreading / threading / no-gil | 10.30s | 8.24s @ n_jobs=2 | 1.25x (8.24s @ n_jobs=2) | 0.34x (30.74s @ n_jobs=16) | 2.98x | 0.02 | [5fffc163-ee00-4640-9d26-b89ab729c80f](results/regression_pipeline_tuning/20260630T121801_5fffc163-ee00-4640-9d26-b89ab729c80f.json) |
| mkl-gil / threading / gil | 8.71s | 8.71s @ n_jobs=1 | 1.00x (8.71s @ n_jobs=1) | 0.35x (24.77s @ n_jobs=16) | 2.84x | 0.02 | [4e3e99f8-36e2-4edd-8f3c-8fa9c6dd1a0d](results/regression_pipeline_tuning/20260630T121951_4e3e99f8-36e2-4edd-8f3c-8fa9c6dd1a0d.json) |
| pypi-freethreading / threading / no-gil | 11.31s | 11.31s @ n_jobs=1 | 1.00x (11.31s @ n_jobs=1) | 0.54x (20.94s @ n_jobs=16) | 1.85x | 0.03 | [88cb30e8-bf45-4b01-b3e0-02ea55c05cee](results/regression_pipeline_tuning/20260630T121043_88cb30e8-bf45-4b01-b3e0-02ea55c05cee.json) |

### GIL vs free-threading comparisons

| Stack / backend | Metric | GIL | No-GIL | Verdict |
| --- | --- | --- | --- | --- |
| mkl / loky | single-thread baseline | 8.53s | 10.32s | gil 1.21x faster |
| mkl / loky | best duration | 1.76s @ n_jobs=16 | 2.10s @ n_jobs=16 | gil 1.19x faster |
| mkl / loky | peak speedup | 4.83x (1.76s @ n_jobs=16) | 4.91x (2.10s @ n_jobs=16) | no-gil 1.02x better |
| mkl / loky | speedup at max cores | 4.83x (1.76s @ n_jobs=16) | 4.91x (2.10s @ n_jobs=16) | no-gil 1.02x better |
| mkl / threading | single-thread baseline | 8.71s | 10.42s | gil 1.20x faster |
| mkl / threading | best duration | 8.71s @ n_jobs=1 | 6.54s @ n_jobs=4 | no-gil 1.33x faster |
| mkl / threading | peak speedup | 1.00x (8.71s @ n_jobs=1) | 1.59x (6.54s @ n_jobs=4) | no-gil 1.59x better |
| mkl / threading | speedup at max cores | 0.35x (24.77s @ n_jobs=16) | 0.32x (32.96s @ n_jobs=16) | gil 1.11x better |
| openblas-openmp / loky | single-thread baseline | 8.25s | 10.18s | gil 1.23x faster |
| openblas-openmp / loky | best duration | 1.76s @ n_jobs=16 | 2.74s @ n_jobs=8 | gil 1.56x faster |
| openblas-openmp / loky | peak speedup | 4.69x (1.76s @ n_jobs=16) | 3.72x (2.74s @ n_jobs=8) | gil 1.26x better |
| openblas-openmp / loky | speedup at max cores | 4.69x (1.76s @ n_jobs=16) | 3.01x (3.39s @ n_jobs=16) | gil 1.56x better |
| openblas-openmp / threading | single-thread baseline | 8.26s | 10.30s | gil 1.25x faster |
| openblas-openmp / threading | best duration | 8.26s @ n_jobs=1 | 8.24s @ n_jobs=2 | no-gil 1.00x faster |
| openblas-openmp / threading | peak speedup | 1.00x (8.26s @ n_jobs=1) | 1.25x (8.24s @ n_jobs=2) | no-gil 1.25x better |
| openblas-openmp / threading | speedup at max cores | 0.32x (25.86s @ n_jobs=16) | 0.34x (30.74s @ n_jobs=16) | no-gil 1.05x better |
| openblas-pthreads / loky | single-thread baseline | 10.57s | 12.29s | gil 1.16x faster |
| openblas-pthreads / loky | best duration | 2.85s @ n_jobs=16 | 3.27s @ n_jobs=16 | gil 1.15x faster |
| openblas-pthreads / loky | peak speedup | 3.71x (2.85s @ n_jobs=16) | 3.76x (3.27s @ n_jobs=16) | no-gil 1.01x better |
| openblas-pthreads / loky | speedup at max cores | 3.71x (2.85s @ n_jobs=16) | 3.76x (3.27s @ n_jobs=16) | no-gil 1.01x better |
| openblas-pthreads / threading | single-thread baseline | 10.34s | 12.19s | gil 1.18x faster |
| openblas-pthreads / threading | best duration | 10.34s @ n_jobs=1 | 12.19s @ n_jobs=1 | gil 1.18x faster |
| openblas-pthreads / threading | peak speedup | 1.00x (10.34s @ n_jobs=1) | 1.00x (12.19s @ n_jobs=1) | tie |
| openblas-pthreads / threading | speedup at max cores | 0.66x (15.68s @ n_jobs=16) | 0.55x (22.24s @ n_jobs=16) | gil 1.20x better |
| pypi / loky | single-thread baseline | 10.34s | 12.26s | gil 1.19x faster |
| pypi / loky | best duration | 2.42s @ n_jobs=16 | 3.20s @ n_jobs=16 | gil 1.32x faster |
| pypi / loky | peak speedup | 4.27x (2.42s @ n_jobs=16) | 3.84x (3.20s @ n_jobs=16) | gil 1.11x better |
| pypi / loky | speedup at max cores | 4.27x (2.42s @ n_jobs=16) | 3.84x (3.20s @ n_jobs=16) | gil 1.11x better |
| pypi / threading | single-thread baseline | 7.81s | 11.31s | gil 1.45x faster |
| pypi / threading | best duration | 7.81s @ n_jobs=1 | 11.31s @ n_jobs=1 | gil 1.45x faster |
| pypi / threading | peak speedup | 1.00x (7.81s @ n_jobs=1) | 1.00x (11.31s @ n_jobs=1) | tie |
| pypi / threading | speedup at max cores | 0.56x (14.01s @ n_jobs=16) | 0.54x (20.94s @ n_jobs=16) | gil 1.03x better |

#### Summary across paired stacks

| Metric | GIL wins | No-GIL wins |
| --- | --- | --- |
| single-thread baseline | 8 | 0 |
| best duration | 6 | 2 |
| peak speedup | 2 | 4 |
| speedup at max cores | 5 | 3 |

