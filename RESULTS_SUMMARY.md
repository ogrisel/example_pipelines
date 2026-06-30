# Regression pipeline tuning results

Loaded 32 result file(s) from `/Users/ogrisel/tmp/pipelines/results/regression_pipeline_tuning`.

## Apple M4 (arm64, 10 logical cores)

Runs: 16 total, 16 successful, 0 failed

### Most efficient (absolute speed)

| Rank | GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | gil | pypi | loky | Accelerate | 6.93s | 2.84s @ n_jobs=8 | [110c179e-51d2-4fc4-b5ac-e7bbd0583590](results/regression_pipeline_tuning/20260630T163158_110c179e-51d2-4fc4-b5ac-e7bbd0583590.json) |
| #2 | no-gil | pypi | loky | Accelerate | 7.12s | 3.92s @ n_jobs=4 | [d43b8345-1dd3-4bb2-9037-45f9edcb8830](results/regression_pipeline_tuning/20260630T163248_d43b8345-1dd3-4bb2-9037-45f9edcb8830.json) |
| #3 | no-gil | pypi | threading | Accelerate | 7.11s | 4.70s @ n_jobs=4 | [31c0ff23-f0ce-4da9-9470-f28f5e26cef5](results/regression_pipeline_tuning/20260630T163223_31c0ff23-f0ce-4da9-9470-f28f5e26cef5.json) |

### Slowest (absolute duration at any n_jobs)

| Rank | GIL | Distribution | Joblib backend | BLAS | Duration | Run |
| --- | --- | --- | --- | --- | --- | --- |
| #1 | gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 41.15s @ n_jobs=8 | [bd0e6682-7b00-4263-a8e7-18e1f7ff7ce5](results/regression_pipeline_tuning/20260630T163317_bd0e6682-7b00-4263-a8e7-18e1f7ff7ce5.json) |
| #2 | gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 30.87s @ n_jobs=2 | [bd0e6682-7b00-4263-a8e7-18e1f7ff7ce5](results/regression_pipeline_tuning/20260630T163317_bd0e6682-7b00-4263-a8e7-18e1f7ff7ce5.json) |
| #3 | no-gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 30.82s @ n_jobs=1 | [9ca88ae0-320a-4f0e-b556-3e42fe1172b0](results/regression_pipeline_tuning/20260630T163635_9ca88ae0-320a-4f0e-b556-3e42fe1172b0.json) |

### Most efficient (scalability)

| Rank | GIL | Distribution | Joblib backend | BLAS | Speedup | Parallel efficiency | Duration | Baseline | Best | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | no-gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 2.93x | 0.37 | 9.77s @ n_jobs=8 | 28.59s | 9.77s @ n_jobs=8 | [5e1adc54-08f5-406f-bd33-140955875769](results/regression_pipeline_tuning/20260630T163824_5e1adc54-08f5-406f-bd33-140955875769.json) |
| #2 | gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 2.66x | 0.33 | 8.45s @ n_jobs=8 | 22.50s | 8.45s @ n_jobs=8 | [d0182909-5e43-47e5-a5cb-c256a113a847](results/regression_pipeline_tuning/20260630T163524_d0182909-5e43-47e5-a5cb-c256a113a847.json) |
| #3 | gil | pypi | loky | Accelerate | 2.44x | 0.31 | 2.84s @ n_jobs=8 | 6.93s | 2.84s @ n_jobs=8 | [110c179e-51d2-4fc4-b5ac-e7bbd0583590](results/regression_pipeline_tuning/20260630T163158_110c179e-51d2-4fc4-b5ac-e7bbd0583590.json) |

### Most problematic (lack of scalability)

| Rank | GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Peak speedup | Speedup @ max | Slowdown @ max | Max-core efficiency | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 22.93s | 22.93s @ n_jobs=1 | 1.00x (22.93s @ n_jobs=1) | 0.56x (41.15s @ n_jobs=8) | 1.79x | 0.07 | [bd0e6682-7b00-4263-a8e7-18e1f7ff7ce5](results/regression_pipeline_tuning/20260630T163317_bd0e6682-7b00-4263-a8e7-18e1f7ff7ce5.json) |
| #2 | no-gil | conda-forge | threading | Accelerate | 7.66s | 6.91s @ n_jobs=2 | 1.11x (6.91s @ n_jobs=2) | 0.62x (12.27s @ n_jobs=8) | 1.60x | 0.08 | [768889e7-f680-4b54-b1a2-4d816eb064d0](results/regression_pipeline_tuning/20260630T164255_768889e7-f680-4b54-b1a2-4d816eb064d0.json) |
| #3 | no-gil | pypi | threading | Accelerate | 7.11s | 4.70s @ n_jobs=4 | 1.51x (4.70s @ n_jobs=4) | 0.89x (8.02s @ n_jobs=8) | 1.13x | 0.11 | [31c0ff23-f0ce-4da9-9470-f28f5e26cef5](results/regression_pipeline_tuning/20260630T163223_31c0ff23-f0ce-4da9-9470-f28f5e26cef5.json) |

<details>
<summary>Full results and GIL vs free-threading comparisons</summary>

### All runs

| GIL | Distribution | Joblib backend | BLAS | Baseline | Best | Peak speedup | Speedup @ max | Peak parallel efficiency | Max-core parallel efficiency | Slowdown @ max | Run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no-gil | conda-forge | loky | Accelerate | 7.97s | 6.23s @ n_jobs=4 | 1.28x (6.23s @ n_jobs=4) | 1.26x (6.32s @ n_jobs=8) | 0.32 | 0.16 | 0.79x | [03762451-2627-4b3c-9348-e6a02b180d35](results/regression_pipeline_tuning/20260630T164331_03762451-2627-4b3c-9348-e6a02b180d35.json) |
| no-gil | conda-forge | threading | Accelerate | 7.66s | 6.91s @ n_jobs=2 | 1.11x (6.91s @ n_jobs=2) | 0.62x (12.27s @ n_jobs=8) | 0.55 | 0.08 | 1.60x | [768889e7-f680-4b54-b1a2-4d816eb064d0](results/regression_pipeline_tuning/20260630T164255_768889e7-f680-4b54-b1a2-4d816eb064d0.json) |
| gil | conda-forge | loky | Accelerate | 7.52s | 5.13s @ n_jobs=8 | 1.47x (5.13s @ n_jobs=8) | 1.47x (5.13s @ n_jobs=8) | 0.18 | 0.18 | 0.68x | [2564caea-bde7-40b2-a705-1e18e9733fe7](results/regression_pipeline_tuning/20260630T164221_2564caea-bde7-40b2-a705-1e18e9733fe7.json) |
| gil | conda-forge | threading | Accelerate | 7.72s | 7.29s @ n_jobs=2 | 1.06x (7.29s @ n_jobs=2) | 0.97x (7.94s @ n_jobs=8) | 0.53 | 0.12 | 1.03x | [335b67a5-cac7-4726-bb3b-b37953c367af](results/regression_pipeline_tuning/20260630T164149_335b67a5-cac7-4726-bb3b-b37953c367af.json) |
| no-gil | conda-forge | loky | OpenBLAS (VORTEX, openmp) | 11.89s | 7.34s @ n_jobs=8 | 1.62x (7.34s @ n_jobs=8) | 1.62x (7.34s @ n_jobs=8) | 0.20 | 0.20 | 0.62x | [923bc01b-6ae2-409d-a76a-5a739bdbf8e3](results/regression_pipeline_tuning/20260630T164103_923bc01b-6ae2-409d-a76a-5a739bdbf8e3.json) |
| no-gil | conda-forge | threading | OpenBLAS (VORTEX, openmp) | 12.34s | 12.34s @ n_jobs=1 | 1.00x (12.34s @ n_jobs=1) | 1.00x (12.34s @ n_jobs=1) | 1.00 | 1.00 | 1.00x | [f5dc57b0-102a-4787-9306-e2dff0730a8e](results/regression_pipeline_tuning/20260630T164046_f5dc57b0-102a-4787-9306-e2dff0730a8e.json) |
| gil | conda-forge | loky | OpenBLAS (VORTEX, openmp) | 12.22s | 7.90s @ n_jobs=4 | 1.55x (7.90s @ n_jobs=4) | 1.49x (8.23s @ n_jobs=8) | 0.39 | 0.19 | 0.67x | [a1893585-e4f9-4fed-b426-843588251b4e](results/regression_pipeline_tuning/20260630T163958_a1893585-e4f9-4fed-b426-843588251b4e.json) |
| gil | conda-forge | threading | OpenBLAS (VORTEX, openmp) | 11.72s | 11.72s @ n_jobs=1 | 1.00x (11.72s @ n_jobs=1) | 1.00x (11.72s @ n_jobs=1) | 1.00 | 1.00 | 1.00x | [f5e206a4-b8fc-43dc-89d6-1904aaa2c426](results/regression_pipeline_tuning/20260630T163943_f5e206a4-b8fc-43dc-89d6-1904aaa2c426.json) |
| no-gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 28.59s | 9.77s @ n_jobs=8 | 2.93x (9.77s @ n_jobs=8) | 2.93x (9.77s @ n_jobs=8) | 0.37 | 0.37 | 0.34x | [5e1adc54-08f5-406f-bd33-140955875769](results/regression_pipeline_tuning/20260630T163824_5e1adc54-08f5-406f-bd33-140955875769.json) |
| no-gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 30.82s | 23.01s @ n_jobs=2 | 1.34x (23.01s @ n_jobs=2) | 1.08x (28.64s @ n_jobs=8) | 0.67 | 0.13 | 0.93x | [9ca88ae0-320a-4f0e-b556-3e42fe1172b0](results/regression_pipeline_tuning/20260630T163635_9ca88ae0-320a-4f0e-b556-3e42fe1172b0.json) |
| gil | conda-forge | loky | OpenBLAS (VORTEX, pthreads) | 22.50s | 8.45s @ n_jobs=8 | 2.66x (8.45s @ n_jobs=8) | 2.66x (8.45s @ n_jobs=8) | 0.33 | 0.33 | 0.38x | [d0182909-5e43-47e5-a5cb-c256a113a847](results/regression_pipeline_tuning/20260630T163524_d0182909-5e43-47e5-a5cb-c256a113a847.json) |
| gil | conda-forge | threading | OpenBLAS (VORTEX, pthreads) | 22.93s | 22.93s @ n_jobs=1 | 1.00x (22.93s @ n_jobs=1) | 0.56x (41.15s @ n_jobs=8) | 1.00 | 0.07 | 1.79x | [bd0e6682-7b00-4263-a8e7-18e1f7ff7ce5](results/regression_pipeline_tuning/20260630T163317_bd0e6682-7b00-4263-a8e7-18e1f7ff7ce5.json) |
| no-gil | pypi | loky | Accelerate | 7.12s | 3.92s @ n_jobs=4 | 1.82x (3.92s @ n_jobs=4) | 1.32x (5.42s @ n_jobs=8) | 0.45 | 0.16 | 0.76x | [d43b8345-1dd3-4bb2-9037-45f9edcb8830](results/regression_pipeline_tuning/20260630T163248_d43b8345-1dd3-4bb2-9037-45f9edcb8830.json) |
| no-gil | pypi | threading | Accelerate | 7.11s | 4.70s @ n_jobs=4 | 1.51x (4.70s @ n_jobs=4) | 0.89x (8.02s @ n_jobs=8) | 0.38 | 0.11 | 1.13x | [31c0ff23-f0ce-4da9-9470-f28f5e26cef5](results/regression_pipeline_tuning/20260630T163223_31c0ff23-f0ce-4da9-9470-f28f5e26cef5.json) |
| gil | pypi | loky | Accelerate | 6.93s | 2.84s @ n_jobs=8 | 2.44x (2.84s @ n_jobs=8) | 2.44x (2.84s @ n_jobs=8) | 0.31 | 0.31 | 0.41x | [110c179e-51d2-4fc4-b5ac-e7bbd0583590](results/regression_pipeline_tuning/20260630T163158_110c179e-51d2-4fc4-b5ac-e7bbd0583590.json) |
| gil | pypi | threading | Accelerate | 6.57s | 6.08s @ n_jobs=2 | 1.08x (6.08s @ n_jobs=2) | 0.94x (6.98s @ n_jobs=8) | 0.54 | 0.12 | 1.06x | [5a3dda15-7e5e-4b77-a544-ea40d8eace95](results/regression_pipeline_tuning/20260630T163131_5a3dda15-7e5e-4b77-a544-ea40d8eace95.json) |

### GIL vs free-threading comparisons

| Stack / backend | Metric | GIL | No-GIL | Verdict |
| --- | --- | --- | --- | --- |
| newaccelerate / loky | single-thread baseline | 7.52s | 7.97s | gil 1.06x faster |
| newaccelerate / loky | best duration | 5.13s @ n_jobs=8 | 6.23s @ n_jobs=4 | gil 1.21x faster |
| newaccelerate / loky | peak speedup | 1.47x (5.13s @ n_jobs=8) | 1.28x (6.23s @ n_jobs=4) | gil 1.15x better |
| newaccelerate / loky | speedup at max cores | 1.47x (5.13s @ n_jobs=8) | 1.26x (6.32s @ n_jobs=8) | gil 1.16x better |
| newaccelerate / threading | single-thread baseline | 7.72s | 7.66s | no-gil 1.01x faster |
| newaccelerate / threading | best duration | 7.29s @ n_jobs=2 | 6.91s @ n_jobs=2 | no-gil 1.06x faster |
| newaccelerate / threading | peak speedup | 1.06x (7.29s @ n_jobs=2) | 1.11x (6.91s @ n_jobs=2) | no-gil 1.05x better |
| newaccelerate / threading | speedup at max cores | 0.97x (7.94s @ n_jobs=8) | 0.62x (12.27s @ n_jobs=8) | gil 1.56x better |
| openblas-openmp / loky | single-thread baseline | 12.22s | 11.89s | no-gil 1.03x faster |
| openblas-openmp / loky | best duration | 7.90s @ n_jobs=4 | 7.34s @ n_jobs=8 | no-gil 1.08x faster |
| openblas-openmp / loky | peak speedup | 1.55x (7.90s @ n_jobs=4) | 1.62x (7.34s @ n_jobs=8) | no-gil 1.05x better |
| openblas-openmp / loky | speedup at max cores | 1.49x (8.23s @ n_jobs=8) | 1.62x (7.34s @ n_jobs=8) | no-gil 1.09x better |
| openblas-openmp / threading | single-thread baseline | 11.72s | 12.34s | gil 1.05x faster |
| openblas-openmp / threading | best duration | 11.72s @ n_jobs=1 | 12.34s @ n_jobs=1 | gil 1.05x faster |
| openblas-openmp / threading | peak speedup | 1.00x (11.72s @ n_jobs=1) | 1.00x (12.34s @ n_jobs=1) | tie |
| openblas-openmp / threading | speedup at max cores | 1.00x (11.72s @ n_jobs=1) | 1.00x (12.34s @ n_jobs=1) | tie |
| openblas-pthreads / loky | single-thread baseline | 22.50s | 28.59s | gil 1.27x faster |
| openblas-pthreads / loky | best duration | 8.45s @ n_jobs=8 | 9.77s @ n_jobs=8 | gil 1.16x faster |
| openblas-pthreads / loky | peak speedup | 2.66x (8.45s @ n_jobs=8) | 2.93x (9.77s @ n_jobs=8) | no-gil 1.10x better |
| openblas-pthreads / loky | speedup at max cores | 2.66x (8.45s @ n_jobs=8) | 2.93x (9.77s @ n_jobs=8) | no-gil 1.10x better |
| openblas-pthreads / threading | single-thread baseline | 22.93s | 30.82s | gil 1.34x faster |
| openblas-pthreads / threading | best duration | 22.93s @ n_jobs=1 | 23.01s @ n_jobs=2 | gil 1.00x faster |
| openblas-pthreads / threading | peak speedup | 1.00x (22.93s @ n_jobs=1) | 1.34x (23.01s @ n_jobs=2) | no-gil 1.34x better |
| openblas-pthreads / threading | speedup at max cores | 0.56x (41.15s @ n_jobs=8) | 1.08x (28.64s @ n_jobs=8) | no-gil 1.93x better |
| pypi / loky | single-thread baseline | 6.93s | 7.12s | gil 1.03x faster |
| pypi / loky | best duration | 2.84s @ n_jobs=8 | 3.92s @ n_jobs=4 | gil 1.38x faster |
| pypi / loky | peak speedup | 2.44x (2.84s @ n_jobs=8) | 1.82x (3.92s @ n_jobs=4) | gil 1.34x better |
| pypi / loky | speedup at max cores | 2.44x (2.84s @ n_jobs=8) | 1.32x (5.42s @ n_jobs=8) | gil 1.86x better |
| pypi / threading | single-thread baseline | 6.57s | 7.11s | gil 1.08x faster |
| pypi / threading | best duration | 6.08s @ n_jobs=2 | 4.70s @ n_jobs=4 | no-gil 1.29x faster |
| pypi / threading | peak speedup | 1.08x (6.08s @ n_jobs=2) | 1.51x (4.70s @ n_jobs=4) | no-gil 1.40x better |
| pypi / threading | speedup at max cores | 0.94x (6.98s @ n_jobs=8) | 0.89x (8.02s @ n_jobs=8) | gil 1.06x better |

#### Summary across paired stacks

| Metric | GIL wins | No-GIL wins |
| --- | --- | --- |
| single-thread baseline | 6 | 2 |
| best duration | 5 | 3 |
| peak speedup | 2 | 5 |
| speedup at max cores | 4 | 3 |


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

