# Regression pipeline tuning results

Loaded 32 result file(s) from `/Users/ogrisel/tmp/pipelines/results/regression_pipeline_tuning`.

## Apple M4 (arm64, 10 logical cores)

Runs: 16 total, 16 successful, 0 failed

### Most efficient (absolute speed)

| Rank | GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | gil | pypi | loky | Accelerate | 11.30s | 6.34s @ n_jobs=8 | [6310fc6a-37ac-4415-ae3d-71b0505f1c09](results/regression_pipeline_tuning/20260630T110737_6310fc6a-37ac-4415-ae3d-71b0505f1c09.json) |
| #2 | no-gil | conda-forge | loky | Accelerate | 12.86s | 6.49s @ n_jobs=8 | [5d87765a-ea1a-46bf-b42f-ff5992a03af4](results/regression_pipeline_tuning/20260630T113718_5d87765a-ea1a-46bf-b42f-ff5992a03af4.json) |
| #3 | no-gil | pypi | loky | Accelerate | 12.63s | 6.64s @ n_jobs=8 | [b18fc4f7-d7e6-4d79-91d0-27d330255d5b](results/regression_pipeline_tuning/20260630T110907_b18fc4f7-d7e6-4d79-91d0-27d330255d5b.json) |

### Slowest (absolute duration at any n_jobs)

| Rank | GIL | Distribution | Joblib backend | BLAS | Duration | Run |
| --- | --- | --- | --- | --- | --- | --- |
| #1 | no-gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 180.55s @ n_jobs=1 | [8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0](results/regression_pipeline_tuning/20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json) |
| #2 | no-gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 161.83s @ n_jobs=1 | [1cee5a9e-5a45-4275-b11d-5a65bb8029b8](results/regression_pipeline_tuning/20260630T112001_1cee5a9e-5a45-4275-b11d-5a65bb8029b8.json) |
| #3 | gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 159.49s @ n_jobs=1 | [3809d58b-398a-49af-9d50-52734d23fdfc](results/regression_pipeline_tuning/20260630T111559_3809d58b-398a-49af-9d50-52734d23fdfc.json) |

### Most efficient (scalability)

| Rank | GIL | Distribution | Joblib backend | BLAS | Speedup | Parallel efficiency | Duration | Baseline | Best | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | no-gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 15.98x | 2.00 | 11.30s @ n_jobs=8 | 180.55s | 11.30s @ n_jobs=8 | [8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0](results/regression_pipeline_tuning/20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json) |
| #2 | gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 10.97x | 1.37 | 14.54s @ n_jobs=8 | 159.49s | 14.54s @ n_jobs=8 | [3809d58b-398a-49af-9d50-52734d23fdfc](results/regression_pipeline_tuning/20260630T111559_3809d58b-398a-49af-9d50-52734d23fdfc.json) |
| #3 | no-gil | conda-forge | loky | OpenBLAS (VORTEX, openmp) | 2.70x | 0.34 | 9.17s @ n_jobs=8 | 24.75s | 9.17s @ n_jobs=8 | [587d9e84-6604-44a9-92d7-6302ab7cc9d6](results/regression_pipeline_tuning/20260630T113321_587d9e84-6604-44a9-92d7-6302ab7cc9d6.json) |

### Most problematic (lack of scalability)

| Rank | GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Peak speedup | Speedup @ max | Slowdown @ max | Max-core efficiency | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | gil | conda-forge | threading | Accelerate | 12.50s | 12.28s @ n_jobs=2 | 1.02x (12.28s @ n_jobs=2) | 0.84x (14.82s @ n_jobs=8) | 1.19x | 0.11 | [4828c7ef-31c9-4317-910c-f372e6242e22](results/regression_pipeline_tuning/20260630T113434_4828c7ef-31c9-4317-910c-f372e6242e22.json) |
| #2 | gil | pypi | threading | Accelerate | 12.32s | 12.32s @ n_jobs=1 | 1.00x (12.32s @ n_jobs=1) | 0.88x (14.04s @ n_jobs=8) | 1.14x | 0.11 | [acc40cf9-5d13-458f-9ac9-990a5f049670](results/regression_pipeline_tuning/20260630T110642_acc40cf9-5d13-458f-9ac9-990a5f049670.json) |
| #3 | no-gil | pypi | threading | Accelerate | 12.56s | 9.09s @ n_jobs=2 | 1.38x (9.09s @ n_jobs=2) | 0.89x (14.11s @ n_jobs=8) | 1.12x | 0.11 | [c312f52b-b576-4250-9fd1-37cc98b051f1](results/regression_pipeline_tuning/20260630T110820_c312f52b-b576-4250-9fd1-37cc98b051f1.json) |

<details>
<summary>Full results and GIL vs free-threading comparisons</summary>

### All runs

| GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Peak speedup | Speedup @ max | Peak parallel efficiency | Max-core parallel efficiency | Slowdown @ max | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no-gil | conda-forge | loky | Accelerate | 12.86s | 6.49s @ n_jobs=8 | 1.98x (6.49s @ n_jobs=8) | 1.98x (6.49s @ n_jobs=8) | 0.25 | 0.25 | 0.50x | [5d87765a-ea1a-46bf-b42f-ff5992a03af4](results/regression_pipeline_tuning/20260630T113718_5d87765a-ea1a-46bf-b42f-ff5992a03af4.json) |
| no-gil | conda-forge | threading | Accelerate | 16.02s | 10.55s @ n_jobs=2 | 1.52x (10.55s @ n_jobs=2) | 1.07x (14.96s @ n_jobs=8) | 0.76 | 0.13 | 0.93x | [950d1495-7328-4b7c-87e2-71af489e799c](results/regression_pipeline_tuning/20260630T113622_950d1495-7328-4b7c-87e2-71af489e799c.json) |
| gil | conda-forge | loky | Accelerate | 12.60s | 7.84s @ n_jobs=8 | 1.61x (7.84s @ n_jobs=8) | 1.61x (7.84s @ n_jobs=8) | 0.20 | 0.20 | 0.62x | [08f416f5-5b85-419a-81f2-0b794f554d92](results/regression_pipeline_tuning/20260630T113528_08f416f5-5b85-419a-81f2-0b794f554d92.json) |
| gil | conda-forge | threading | Accelerate | 12.50s | 12.28s @ n_jobs=2 | 1.02x (12.28s @ n_jobs=2) | 0.84x (14.82s @ n_jobs=8) | 0.51 | 0.11 | 1.19x | [4828c7ef-31c9-4317-910c-f372e6242e22](results/regression_pipeline_tuning/20260630T113434_4828c7ef-31c9-4317-910c-f372e6242e22.json) |
| no-gil | conda-forge | loky | OpenBLAS (VORTEX, openmp) | 24.75s | 9.17s @ n_jobs=8 | 2.70x (9.17s @ n_jobs=8) | 2.70x (9.17s @ n_jobs=8) | 0.34 | 0.34 | 0.37x | [587d9e84-6604-44a9-92d7-6302ab7cc9d6](results/regression_pipeline_tuning/20260630T113321_587d9e84-6604-44a9-92d7-6302ab7cc9d6.json) |
| no-gil | conda-forge | threading | OpenBLAS (VORTEX, openmp) | 25.43s | 25.43s @ n_jobs=1 | 1.00x (25.43s @ n_jobs=1) | 1.00x (25.43s @ n_jobs=1) | 1.00 | 1.00 | 1.00x | [b61d2a07-31b5-417d-a90a-1f5442fbb5ce](results/regression_pipeline_tuning/20260630T113250_b61d2a07-31b5-417d-a90a-1f5442fbb5ce.json) |
| gil | conda-forge | loky | OpenBLAS (VORTEX, openmp) | 19.91s | 7.88s @ n_jobs=8 | 2.53x (7.88s @ n_jobs=8) | 2.53x (7.88s @ n_jobs=8) | 0.32 | 0.32 | 0.40x | [bb1c7cb6-775c-412c-b09c-131f9fb9c244](results/regression_pipeline_tuning/20260630T113146_bb1c7cb6-775c-412c-b09c-131f9fb9c244.json) |
| gil | conda-forge | threading | OpenBLAS (VORTEX, openmp) | 25.72s | 25.72s @ n_jobs=1 | 1.00x (25.72s @ n_jobs=1) | 1.00x (25.72s @ n_jobs=1) | 1.00 | 1.00 | 1.00x | [269c04aa-468e-4f75-96f8-2d4e4f587b62](results/regression_pipeline_tuning/20260630T113115_269c04aa-468e-4f75-96f8-2d4e4f587b62.json) |
| no-gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 180.55s | 11.30s @ n_jobs=8 | 15.98x (11.30s @ n_jobs=8) | 15.98x (11.30s @ n_jobs=8) | 2.00 | 2.00 | 0.06x | [8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0](results/regression_pipeline_tuning/20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json) |
| no-gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 161.83s | 71.73s @ n_jobs=4 | 2.26x (71.73s @ n_jobs=4) | 2.03x (79.61s @ n_jobs=8) | 0.56 | 0.25 | 0.49x | [1cee5a9e-5a45-4275-b11d-5a65bb8029b8](results/regression_pipeline_tuning/20260630T112001_1cee5a9e-5a45-4275-b11d-5a65bb8029b8.json) |
| gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 159.49s | 14.54s @ n_jobs=8 | 10.97x (14.54s @ n_jobs=8) | 10.97x (14.54s @ n_jobs=8) | 1.37 | 1.37 | 0.09x | [3809d58b-398a-49af-9d50-52734d23fdfc](results/regression_pipeline_tuning/20260630T111559_3809d58b-398a-49af-9d50-52734d23fdfc.json) |
| gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 134.19s | 69.88s @ n_jobs=4 | 1.92x (69.88s @ n_jobs=4) | 1.70x (78.92s @ n_jobs=8) | 0.48 | 0.21 | 0.59x | [d197d79d-3774-4599-905c-63bd50f161cc](results/regression_pipeline_tuning/20260630T110954_d197d79d-3774-4599-905c-63bd50f161cc.json) |
| no-gil | pypi | loky | Accelerate | 12.63s | 6.64s @ n_jobs=8 | 1.90x (6.64s @ n_jobs=8) | 1.90x (6.64s @ n_jobs=8) | 0.24 | 0.24 | 0.53x | [b18fc4f7-d7e6-4d79-91d0-27d330255d5b](results/regression_pipeline_tuning/20260630T110907_b18fc4f7-d7e6-4d79-91d0-27d330255d5b.json) |
| no-gil | pypi | threading | Accelerate | 12.56s | 9.09s @ n_jobs=2 | 1.38x (9.09s @ n_jobs=2) | 0.89x (14.11s @ n_jobs=8) | 0.69 | 0.11 | 1.12x | [c312f52b-b576-4250-9fd1-37cc98b051f1](results/regression_pipeline_tuning/20260630T110820_c312f52b-b576-4250-9fd1-37cc98b051f1.json) |
| gil | pypi | loky | Accelerate | 11.30s | 6.34s @ n_jobs=8 | 1.78x (6.34s @ n_jobs=8) | 1.78x (6.34s @ n_jobs=8) | 0.22 | 0.22 | 0.56x | [6310fc6a-37ac-4415-ae3d-71b0505f1c09](results/regression_pipeline_tuning/20260630T110737_6310fc6a-37ac-4415-ae3d-71b0505f1c09.json) |
| gil | pypi | threading | Accelerate | 12.32s | 12.32s @ n_jobs=1 | 1.00x (12.32s @ n_jobs=1) | 0.88x (14.04s @ n_jobs=8) | 1.00 | 0.11 | 1.14x | [acc40cf9-5d13-458f-9ac9-990a5f049670](results/regression_pipeline_tuning/20260630T110642_acc40cf9-5d13-458f-9ac9-990a5f049670.json) |

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


</details>

## Intel(R) Core(TM) Ultra X7 358H (x86_64, 16 logical cores)

Runs: 16 total, 16 successful, 0 failed

### Most efficient (absolute speed)

| Rank | GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | gil | conda-forge | loky | OpenBLAS (Haswell, openmp) | 8.25s | 1.76s @ n_jobs=16 | [7dafeda5-8947-4f73-b7b3-0f46aafeabe5](results/regression_pipeline_tuning/20260630T121737_7dafeda5-8947-4f73-b7b3-0f46aafeabe5.json) |
| #2 | gil | conda-forge | loky | MKL | 8.53s | 1.76s @ n_jobs=16 | [583d411c-8ccf-4e82-be79-806aedb756e9](results/regression_pipeline_tuning/20260630T122116_583d411c-8ccf-4e82-be79-806aedb756e9.json) |
| #3 | no-gil | conda-forge | loky | MKL | 10.32s | 2.10s @ n_jobs=16 | [dc92a4d4-3f1b-449f-b999-7aad18f7c8fc](results/regression_pipeline_tuning/20260630T122251_dc92a4d4-3f1b-449f-b999-7aad18f7c8fc.json) |

### Slowest (absolute duration at any n_jobs)

| Rank | GIL | Distribution | Joblib backend | BLAS | Duration | Run |
| --- | --- | --- | --- | --- | --- | --- |
| #1 | no-gil | conda-forge | threading | MKL | 32.96s @ n_jobs=16 | [7ae1d70f-b9d1-48d0-9a7b-87d432594d1c](results/regression_pipeline_tuning/20260630T122140_7ae1d70f-b9d1-48d0-9a7b-87d432594d1c.json) |
| #2 | no-gil | conda-forge | threading | OpenBLAS (Haswell, openmp) | 30.74s @ n_jobs=16 | [5fffc163-ee00-4640-9d26-b89ab729c80f](results/regression_pipeline_tuning/20260630T121801_5fffc163-ee00-4640-9d26-b89ab729c80f.json) |
| #3 | gil | conda-forge | threading | OpenBLAS (Haswell, openmp) | 25.86s @ n_jobs=16 | [d9b19d91-1ab2-4c9f-a66d-f1502276d58e](results/regression_pipeline_tuning/20260630T121618_d9b19d91-1ab2-4c9f-a66d-f1502276d58e.json) |

### Most efficient (scalability)

| Rank | GIL | Distribution | Joblib backend | BLAS | Speedup | Parallel efficiency | Duration | Baseline | Best | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | no-gil | conda-forge | loky | MKL | 4.91x | 0.31 | 2.10s @ n_jobs=16 | 10.32s | 2.10s @ n_jobs=16 | [dc92a4d4-3f1b-449f-b999-7aad18f7c8fc](results/regression_pipeline_tuning/20260630T122251_dc92a4d4-3f1b-449f-b999-7aad18f7c8fc.json) |
| #2 | gil | conda-forge | loky | MKL | 4.83x | 0.30 | 1.76s @ n_jobs=16 | 8.53s | 1.76s @ n_jobs=16 | [583d411c-8ccf-4e82-be79-806aedb756e9](results/regression_pipeline_tuning/20260630T122116_583d411c-8ccf-4e82-be79-806aedb756e9.json) |
| #3 | gil | conda-forge | loky | OpenBLAS (Haswell, openmp) | 4.69x | 0.29 | 1.76s @ n_jobs=16 | 8.25s | 1.76s @ n_jobs=16 | [7dafeda5-8947-4f73-b7b3-0f46aafeabe5](results/regression_pipeline_tuning/20260630T121737_7dafeda5-8947-4f73-b7b3-0f46aafeabe5.json) |

### Most problematic (lack of scalability)

| Rank | GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Peak speedup | Speedup @ max | Slowdown @ max | Max-core efficiency | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | no-gil | conda-forge | threading | MKL | 10.42s | 6.54s @ n_jobs=4 | 1.59x (6.54s @ n_jobs=4) | 0.32x (32.96s @ n_jobs=16) | 3.16x | 0.02 | [7ae1d70f-b9d1-48d0-9a7b-87d432594d1c](results/regression_pipeline_tuning/20260630T122140_7ae1d70f-b9d1-48d0-9a7b-87d432594d1c.json) |
| #2 | gil | conda-forge | threading | OpenBLAS (Haswell, openmp) | 8.26s | 8.26s @ n_jobs=1 | 1.00x (8.26s @ n_jobs=1) | 0.32x (25.86s @ n_jobs=16) | 3.13x | 0.02 | [d9b19d91-1ab2-4c9f-a66d-f1502276d58e](results/regression_pipeline_tuning/20260630T121618_d9b19d91-1ab2-4c9f-a66d-f1502276d58e.json) |
| #3 | no-gil | conda-forge | threading | OpenBLAS (Haswell, openmp) | 10.30s | 8.24s @ n_jobs=2 | 1.25x (8.24s @ n_jobs=2) | 0.34x (30.74s @ n_jobs=16) | 2.98x | 0.02 | [5fffc163-ee00-4640-9d26-b89ab729c80f](results/regression_pipeline_tuning/20260630T121801_5fffc163-ee00-4640-9d26-b89ab729c80f.json) |

<details>
<summary>Full results and GIL vs free-threading comparisons</summary>

### All runs

| GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Peak speedup | Speedup @ max | Peak parallel efficiency | Max-core parallel efficiency | Slowdown @ max | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no-gil | conda-forge | loky | MKL | 10.32s | 2.10s @ n_jobs=16 | 4.91x (2.10s @ n_jobs=16) | 4.91x (2.10s @ n_jobs=16) | 0.31 | 0.31 | 0.20x | [dc92a4d4-3f1b-449f-b999-7aad18f7c8fc](results/regression_pipeline_tuning/20260630T122251_dc92a4d4-3f1b-449f-b999-7aad18f7c8fc.json) |
| no-gil | conda-forge | threading | MKL | 10.42s | 6.54s @ n_jobs=4 | 1.59x (6.54s @ n_jobs=4) | 0.32x (32.96s @ n_jobs=16) | 0.40 | 0.02 | 3.16x | [7ae1d70f-b9d1-48d0-9a7b-87d432594d1c](results/regression_pipeline_tuning/20260630T122140_7ae1d70f-b9d1-48d0-9a7b-87d432594d1c.json) |
| gil | conda-forge | loky | MKL | 8.53s | 1.76s @ n_jobs=16 | 4.83x (1.76s @ n_jobs=16) | 4.83x (1.76s @ n_jobs=16) | 0.30 | 0.30 | 0.21x | [583d411c-8ccf-4e82-be79-806aedb756e9](results/regression_pipeline_tuning/20260630T122116_583d411c-8ccf-4e82-be79-806aedb756e9.json) |
| gil | conda-forge | threading | MKL | 8.71s | 8.71s @ n_jobs=1 | 1.00x (8.71s @ n_jobs=1) | 0.35x (24.77s @ n_jobs=16) | 1.00 | 0.02 | 2.84x | [4e3e99f8-36e2-4edd-8f3c-8fa9c6dd1a0d](results/regression_pipeline_tuning/20260630T121951_4e3e99f8-36e2-4edd-8f3c-8fa9c6dd1a0d.json) |
| no-gil | conda-forge | loky | OpenBLAS (Haswell, openmp) | 10.18s | 2.74s @ n_jobs=8 | 3.72x (2.74s @ n_jobs=8) | 3.01x (3.39s @ n_jobs=16) | 0.46 | 0.19 | 0.33x | [d353ceb2-b6ff-496d-bbb5-1ca0fc9f1639](results/regression_pipeline_tuning/20260630T121920_d353ceb2-b6ff-496d-bbb5-1ca0fc9f1639.json) |
| no-gil | conda-forge | threading | OpenBLAS (Haswell, openmp) | 10.30s | 8.24s @ n_jobs=2 | 1.25x (8.24s @ n_jobs=2) | 0.34x (30.74s @ n_jobs=16) | 0.63 | 0.02 | 2.98x | [5fffc163-ee00-4640-9d26-b89ab729c80f](results/regression_pipeline_tuning/20260630T121801_5fffc163-ee00-4640-9d26-b89ab729c80f.json) |
| gil | conda-forge | loky | OpenBLAS (Haswell, openmp) | 8.25s | 1.76s @ n_jobs=16 | 4.69x (1.76s @ n_jobs=16) | 4.69x (1.76s @ n_jobs=16) | 0.29 | 0.29 | 0.21x | [7dafeda5-8947-4f73-b7b3-0f46aafeabe5](results/regression_pipeline_tuning/20260630T121737_7dafeda5-8947-4f73-b7b3-0f46aafeabe5.json) |
| gil | conda-forge | threading | OpenBLAS (Haswell, openmp) | 8.26s | 8.26s @ n_jobs=1 | 1.00x (8.26s @ n_jobs=1) | 0.32x (25.86s @ n_jobs=16) | 1.00 | 0.02 | 3.13x | [d9b19d91-1ab2-4c9f-a66d-f1502276d58e](results/regression_pipeline_tuning/20260630T121618_d9b19d91-1ab2-4c9f-a66d-f1502276d58e.json) |
| no-gil | conda-forge | loky | OpenBLAS (Haswell, pthreads) | 12.29s | 3.27s @ n_jobs=16 | 3.76x (3.27s @ n_jobs=16) | 3.76x (3.27s @ n_jobs=16) | 0.23 | 0.23 | 0.27x | [5bcea684-297c-4924-88cf-f032efe74b87](results/regression_pipeline_tuning/20260630T121540_5bcea684-297c-4924-88cf-f032efe74b87.json) |
| no-gil | conda-forge | threading | OpenBLAS (Haswell, pthreads) | 12.19s | 12.19s @ n_jobs=1 | 1.00x (12.19s @ n_jobs=1) | 0.55x (22.24s @ n_jobs=16) | 1.00 | 0.03 | 1.82x | [0c0bf7a7-b8ca-4feb-9050-fe8af0363464](results/regression_pipeline_tuning/20260630T121418_0c0bf7a7-b8ca-4feb-9050-fe8af0363464.json) |
| gil | conda-forge | loky | OpenBLAS (Haswell, pthreads) | 10.57s | 2.85s @ n_jobs=16 | 3.71x (2.85s @ n_jobs=16) | 3.71x (2.85s @ n_jobs=16) | 0.23 | 0.23 | 0.27x | [888ff5a2-cecd-492b-bc39-61d1969ed2c3](results/regression_pipeline_tuning/20260630T121345_888ff5a2-cecd-492b-bc39-61d1969ed2c3.json) |
| gil | conda-forge | threading | OpenBLAS (Haswell, pthreads) | 10.34s | 10.34s @ n_jobs=1 | 1.00x (10.34s @ n_jobs=1) | 0.66x (15.68s @ n_jobs=16) | 1.00 | 0.04 | 1.52x | [fcfa8ee5-cacb-4f57-ac7c-77936d89267a](results/regression_pipeline_tuning/20260630T121237_fcfa8ee5-cacb-4f57-ac7c-77936d89267a.json) |
| no-gil | pypi | loky | OpenBLAS (Haswell, pthreads) | 12.26s | 3.20s @ n_jobs=16 | 3.84x (3.20s @ n_jobs=16) | 3.84x (3.20s @ n_jobs=16) | 0.24 | 0.24 | 0.26x | [73ece25f-309b-4bed-a825-715ff20d2c73](results/regression_pipeline_tuning/20260630T121158_73ece25f-309b-4bed-a825-715ff20d2c73.json) |
| no-gil | pypi | threading | OpenBLAS (Haswell, pthreads) | 11.31s | 11.31s @ n_jobs=1 | 1.00x (11.31s @ n_jobs=1) | 0.54x (20.94s @ n_jobs=16) | 1.00 | 0.03 | 1.85x | [88cb30e8-bf45-4b01-b3e0-02ea55c05cee](results/regression_pipeline_tuning/20260630T121043_88cb30e8-bf45-4b01-b3e0-02ea55c05cee.json) |
| gil | pypi | loky | OpenBLAS (Haswell, pthreads) | 10.34s | 2.42s @ n_jobs=16 | 4.27x (2.42s @ n_jobs=16) | 4.27x (2.42s @ n_jobs=16) | 0.27 | 0.27 | 0.23x | [fa2454ef-cd46-4d37-996e-3b0cd4efc760](results/regression_pipeline_tuning/20260630T121011_fa2454ef-cd46-4d37-996e-3b0cd4efc760.json) |
| gil | pypi | threading | OpenBLAS (Haswell, pthreads) | 7.81s | 7.81s @ n_jobs=1 | 1.00x (7.81s @ n_jobs=1) | 0.56x (14.01s @ n_jobs=16) | 1.00 | 0.03 | 1.79x | [5f771075-b4b8-44a1-8d3b-9528d940fce2](results/regression_pipeline_tuning/20260630T120917_5f771075-b4b8-44a1-8d3b-9528d940fce2.json) |

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


</details>

