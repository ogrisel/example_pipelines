Loaded 32 result file(s) from /Users/ogrisel/tmp/pipelines/results/regression_pipeline_tuning

================================================================================
Apple M4 (arm64, 10 logical cores)
Runs: 16 total, 16 successful, 0 failed

Most efficient (absolute speed)
  - pypi-gil / loky / gil
    baseline 11.30s; best 6.34s @ n_jobs=8
    run_id=6310fc6a-37ac-4415-ae3d-71b0505f1c09, file=20260630T110737_6310fc6a-37ac-4415-ae3d-71b0505f1c09.json

Most efficient (scalability)
  - openblas-pthreads-freethreading / loky / no-gil
    peak speedup 15.98x (11.30s @ n_jobs=8); baseline 180.55s; best 11.30s @ n_jobs=8
    run_id=8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0, file=20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json
  - openblas-pthreads-freethreading / loky / no-gil
    best peak parallel efficiency 2.00 (speedup 15.98x at 11.30s @ n_jobs=8); baseline 180.55s; best 11.30s @ n_jobs=8
    run_id=8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0, file=20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json
  - openblas-pthreads-freethreading / loky / no-gil
    best max-core parallel efficiency 2.00 (speedup 15.98x at 11.30s @ n_jobs=8); baseline 180.55s; best 11.30s @ n_jobs=8
    run_id=8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0, file=20260630T112653_8eaa7123-b8db-4f1a-a0e0-4b56cc0452e0.json

Most problematic (lack of scalability)
  - newaccelerate-gil / threading / gil
    speedup at max n_jobs=8: 0.84x (14.82s @ n_jobs=8); peak 1.02x (12.28s @ n_jobs=2); baseline 12.50s; best 12.28s @ n_jobs=2; slowdown at max 1.19x baseline; max-core efficiency 0.11
    run_id=4828c7ef-31c9-4317-910c-f372e6242e22, file=20260630T113434_4828c7ef-31c9-4317-910c-f372e6242e22.json
  - pypi-gil / threading / gil
    speedup at max n_jobs=8: 0.88x (14.04s @ n_jobs=8); peak 1.00x (12.32s @ n_jobs=1); baseline 12.32s; best 12.32s @ n_jobs=1; slowdown at max 1.14x baseline; max-core efficiency 0.11
    run_id=acc40cf9-5d13-458f-9ac9-990a5f049670, file=20260630T110642_acc40cf9-5d13-458f-9ac9-990a5f049670.json
  - pypi-freethreading / threading / no-gil
    speedup at max n_jobs=8: 0.89x (14.11s @ n_jobs=8); peak 1.38x (9.09s @ n_jobs=2); baseline 12.56s; best 9.09s @ n_jobs=2; slowdown at max 1.12x baseline; max-core efficiency 0.11
    run_id=c312f52b-b576-4250-9fd1-37cc98b051f1, file=20260630T110820_c312f52b-b576-4250-9fd1-37cc98b051f1.json
  - newaccelerate-freethreading / threading / no-gil
    speedup at max n_jobs=8: 1.07x (14.96s @ n_jobs=8); peak 1.52x (10.55s @ n_jobs=2); baseline 16.02s; best 10.55s @ n_jobs=2; slowdown at max 0.93x baseline; max-core efficiency 0.13
    run_id=950d1495-7328-4b7c-87e2-71af489e799c, file=20260630T113622_950d1495-7328-4b7c-87e2-71af489e799c.json

GIL vs free-threading comparisons

  newaccelerate / loky
  single-thread baseline   gil 12.60s           no-gil 12.86s
    -> gil 1.02x faster
  best duration            gil 7.84s @ n_jobs=8 no-gil 6.49s @ n_jobs=8
    -> no-gil 1.21x faster
  peak speedup             gil 1.61x (7.84s @ n_jobs=8) no-gil 1.98x (6.49s @ n_jobs=8)
    -> no-gil 1.23x better
  speedup at max cores     gil 1.61x (7.84s @ n_jobs=8) no-gil 1.98x (6.49s @ n_jobs=8)
    -> no-gil 1.23x better

  newaccelerate / threading
  single-thread baseline   gil 12.50s           no-gil 16.02s
    -> gil 1.28x faster
  best duration            gil 12.28s @ n_jobs=2 no-gil 10.55s @ n_jobs=2
    -> no-gil 1.16x faster
  peak speedup             gil 1.02x (12.28s @ n_jobs=2) no-gil 1.52x (10.55s @ n_jobs=2)
    -> no-gil 1.49x better
  speedup at max cores     gil 0.84x (14.82s @ n_jobs=8) no-gil 1.07x (14.96s @ n_jobs=8)
    -> no-gil 1.27x better

  openblas-openmp / loky
  single-thread baseline   gil 19.91s           no-gil 24.75s
    -> gil 1.24x faster
  best duration            gil 7.88s @ n_jobs=8 no-gil 9.17s @ n_jobs=8
    -> gil 1.16x faster
  peak speedup             gil 2.53x (7.88s @ n_jobs=8) no-gil 2.70x (9.17s @ n_jobs=8)
    -> no-gil 1.07x better
  speedup at max cores     gil 2.53x (7.88s @ n_jobs=8) no-gil 2.70x (9.17s @ n_jobs=8)
    -> no-gil 1.07x better

  openblas-openmp / threading
  single-thread baseline   gil 25.72s           no-gil 25.43s
    -> no-gil 1.01x faster
  best duration            gil 25.72s @ n_jobs=1 no-gil 25.43s @ n_jobs=1
    -> no-gil 1.01x faster
  peak speedup             gil 1.00x (25.72s @ n_jobs=1) no-gil 1.00x (25.43s @ n_jobs=1)
    -> tie
  speedup at max cores     gil 1.00x (25.72s @ n_jobs=1) no-gil 1.00x (25.43s @ n_jobs=1)
    -> tie

  openblas-pthreads / loky
  single-thread baseline   gil 159.49s          no-gil 180.55s
    -> gil 1.13x faster
  best duration            gil 14.54s @ n_jobs=8 no-gil 11.30s @ n_jobs=8
    -> no-gil 1.29x faster
  peak speedup             gil 10.97x (14.54s @ n_jobs=8) no-gil 15.98x (11.30s @ n_jobs=8)
    -> no-gil 1.46x better
  speedup at max cores     gil 10.97x (14.54s @ n_jobs=8) no-gil 15.98x (11.30s @ n_jobs=8)
    -> no-gil 1.46x better

  openblas-pthreads / threading
  single-thread baseline   gil 134.19s          no-gil 161.83s
    -> gil 1.21x faster
  best duration            gil 69.88s @ n_jobs=4 no-gil 71.73s @ n_jobs=4
    -> gil 1.03x faster
  peak speedup             gil 1.92x (69.88s @ n_jobs=4) no-gil 2.26x (71.73s @ n_jobs=4)
    -> no-gil 1.17x better
  speedup at max cores     gil 1.70x (78.92s @ n_jobs=8) no-gil 2.03x (79.61s @ n_jobs=8)
    -> no-gil 1.20x better

  pypi / loky
  single-thread baseline   gil 11.30s           no-gil 12.63s
    -> gil 1.12x faster
  best duration            gil 6.34s @ n_jobs=8 no-gil 6.64s @ n_jobs=8
    -> gil 1.05x faster
  peak speedup             gil 1.78x (6.34s @ n_jobs=8) no-gil 1.90x (6.64s @ n_jobs=8)
    -> no-gil 1.07x better
  speedup at max cores     gil 1.78x (6.34s @ n_jobs=8) no-gil 1.90x (6.64s @ n_jobs=8)
    -> no-gil 1.07x better

  pypi / threading
  single-thread baseline   gil 12.32s           no-gil 12.56s
    -> gil 1.02x faster
  best duration            gil 12.32s @ n_jobs=1 no-gil 9.09s @ n_jobs=2
    -> no-gil 1.36x faster
  peak speedup             gil 1.00x (12.32s @ n_jobs=1) no-gil 1.38x (9.09s @ n_jobs=2)
    -> no-gil 1.38x better
  speedup at max cores     gil 0.88x (14.04s @ n_jobs=8) no-gil 0.89x (14.11s @ n_jobs=8)
    -> no-gil 1.01x better

  Summary across paired stacks
    single-thread baseline: gil 7 wins, no-gil 1 wins
    best duration:          gil 3 wins, no-gil 5 wins
    peak speedup:           gil 0 wins, no-gil 7 wins
    speedup at max cores:   gil 0 wins, no-gil 7 wins

================================================================================
Intel(R) Core(TM) Ultra X7 358H (x86_64, 16 logical cores)
Runs: 16 total, 16 successful, 0 failed

Most efficient (absolute speed)
  - openblas-openmp-gil / loky / gil
    baseline 8.25s; best 1.76s @ n_jobs=16
    run_id=7dafeda5-8947-4f73-b7b3-0f46aafeabe5, file=20260630T121737_7dafeda5-8947-4f73-b7b3-0f46aafeabe5.json
  - pypi-gil / threading / gil
    fastest single-thread baseline 7.81s; best 7.81s @ n_jobs=1
    run_id=5f771075-b4b8-44a1-8d3b-9528d940fce2, file=20260630T120917_5f771075-b4b8-44a1-8d3b-9528d940fce2.json

Most efficient (scalability)
  - mkl-freethreading / loky / no-gil
    peak speedup 4.91x (2.10s @ n_jobs=16); baseline 10.32s; best 2.10s @ n_jobs=16
    run_id=dc92a4d4-3f1b-449f-b999-7aad18f7c8fc, file=20260630T122251_dc92a4d4-3f1b-449f-b999-7aad18f7c8fc.json
  - openblas-openmp-freethreading / threading / no-gil
    best peak parallel efficiency 0.63 (speedup 1.25x at 8.24s @ n_jobs=2); baseline 10.30s; best 8.24s @ n_jobs=2
    run_id=5fffc163-ee00-4640-9d26-b89ab729c80f, file=20260630T121801_5fffc163-ee00-4640-9d26-b89ab729c80f.json
  - mkl-freethreading / loky / no-gil
    best max-core parallel efficiency 0.31 (speedup 4.91x at 2.10s @ n_jobs=16); baseline 10.32s; best 2.10s @ n_jobs=16
    run_id=dc92a4d4-3f1b-449f-b999-7aad18f7c8fc, file=20260630T122251_dc92a4d4-3f1b-449f-b999-7aad18f7c8fc.json

Most problematic (lack of scalability)
  - mkl-freethreading / threading / no-gil
    speedup at max n_jobs=16: 0.32x (32.96s @ n_jobs=16); peak 1.59x (6.54s @ n_jobs=4); baseline 10.42s; best 6.54s @ n_jobs=4; slowdown at max 3.16x baseline; max-core efficiency 0.02
    run_id=7ae1d70f-b9d1-48d0-9a7b-87d432594d1c, file=20260630T122140_7ae1d70f-b9d1-48d0-9a7b-87d432594d1c.json
  - openblas-openmp-gil / threading / gil
    speedup at max n_jobs=16: 0.32x (25.86s @ n_jobs=16); peak 1.00x (8.26s @ n_jobs=1); baseline 8.26s; best 8.26s @ n_jobs=1; slowdown at max 3.13x baseline; max-core efficiency 0.02
    run_id=d9b19d91-1ab2-4c9f-a66d-f1502276d58e, file=20260630T121618_d9b19d91-1ab2-4c9f-a66d-f1502276d58e.json
  - openblas-openmp-freethreading / threading / no-gil
    speedup at max n_jobs=16: 0.34x (30.74s @ n_jobs=16); peak 1.25x (8.24s @ n_jobs=2); baseline 10.30s; best 8.24s @ n_jobs=2; slowdown at max 2.98x baseline; max-core efficiency 0.02
    run_id=5fffc163-ee00-4640-9d26-b89ab729c80f, file=20260630T121801_5fffc163-ee00-4640-9d26-b89ab729c80f.json
  - mkl-gil / threading / gil
    speedup at max n_jobs=16: 0.35x (24.77s @ n_jobs=16); peak 1.00x (8.71s @ n_jobs=1); baseline 8.71s; best 8.71s @ n_jobs=1; slowdown at max 2.84x baseline; max-core efficiency 0.02
    run_id=4e3e99f8-36e2-4edd-8f3c-8fa9c6dd1a0d, file=20260630T121951_4e3e99f8-36e2-4edd-8f3c-8fa9c6dd1a0d.json
  - pypi-freethreading / threading / no-gil
    speedup at max n_jobs=16: 0.54x (20.94s @ n_jobs=16); peak 1.00x (11.31s @ n_jobs=1); baseline 11.31s; best 11.31s @ n_jobs=1; slowdown at max 1.85x baseline; max-core efficiency 0.03
    run_id=88cb30e8-bf45-4b01-b3e0-02ea55c05cee, file=20260630T121043_88cb30e8-bf45-4b01-b3e0-02ea55c05cee.json

GIL vs free-threading comparisons

  mkl / loky
  single-thread baseline   gil 8.53s            no-gil 10.32s
    -> gil 1.21x faster
  best duration            gil 1.76s @ n_jobs=16 no-gil 2.10s @ n_jobs=16
    -> gil 1.19x faster
  peak speedup             gil 4.83x (1.76s @ n_jobs=16) no-gil 4.91x (2.10s @ n_jobs=16)
    -> no-gil 1.02x better
  speedup at max cores     gil 4.83x (1.76s @ n_jobs=16) no-gil 4.91x (2.10s @ n_jobs=16)
    -> no-gil 1.02x better

  mkl / threading
  single-thread baseline   gil 8.71s            no-gil 10.42s
    -> gil 1.20x faster
  best duration            gil 8.71s @ n_jobs=1 no-gil 6.54s @ n_jobs=4
    -> no-gil 1.33x faster
  peak speedup             gil 1.00x (8.71s @ n_jobs=1) no-gil 1.59x (6.54s @ n_jobs=4)
    -> no-gil 1.59x better
  speedup at max cores     gil 0.35x (24.77s @ n_jobs=16) no-gil 0.32x (32.96s @ n_jobs=16)
    -> gil 1.11x better

  openblas-openmp / loky
  single-thread baseline   gil 8.25s            no-gil 10.18s
    -> gil 1.23x faster
  best duration            gil 1.76s @ n_jobs=16 no-gil 2.74s @ n_jobs=8
    -> gil 1.56x faster
  peak speedup             gil 4.69x (1.76s @ n_jobs=16) no-gil 3.72x (2.74s @ n_jobs=8)
    -> gil 1.26x better
  speedup at max cores     gil 4.69x (1.76s @ n_jobs=16) no-gil 3.01x (3.39s @ n_jobs=16)
    -> gil 1.56x better

  openblas-openmp / threading
  single-thread baseline   gil 8.26s            no-gil 10.30s
    -> gil 1.25x faster
  best duration            gil 8.26s @ n_jobs=1 no-gil 8.24s @ n_jobs=2
    -> no-gil 1.00x faster
  peak speedup             gil 1.00x (8.26s @ n_jobs=1) no-gil 1.25x (8.24s @ n_jobs=2)
    -> no-gil 1.25x better
  speedup at max cores     gil 0.32x (25.86s @ n_jobs=16) no-gil 0.34x (30.74s @ n_jobs=16)
    -> no-gil 1.05x better

  openblas-pthreads / loky
  single-thread baseline   gil 10.57s           no-gil 12.29s
    -> gil 1.16x faster
  best duration            gil 2.85s @ n_jobs=16 no-gil 3.27s @ n_jobs=16
    -> gil 1.15x faster
  peak speedup             gil 3.71x (2.85s @ n_jobs=16) no-gil 3.76x (3.27s @ n_jobs=16)
    -> no-gil 1.01x better
  speedup at max cores     gil 3.71x (2.85s @ n_jobs=16) no-gil 3.76x (3.27s @ n_jobs=16)
    -> no-gil 1.01x better

  openblas-pthreads / threading
  single-thread baseline   gil 10.34s           no-gil 12.19s
    -> gil 1.18x faster
  best duration            gil 10.34s @ n_jobs=1 no-gil 12.19s @ n_jobs=1
    -> gil 1.18x faster
  peak speedup             gil 1.00x (10.34s @ n_jobs=1) no-gil 1.00x (12.19s @ n_jobs=1)
    -> tie
  speedup at max cores     gil 0.66x (15.68s @ n_jobs=16) no-gil 0.55x (22.24s @ n_jobs=16)
    -> gil 1.20x better

  pypi / loky
  single-thread baseline   gil 10.34s           no-gil 12.26s
    -> gil 1.19x faster
  best duration            gil 2.42s @ n_jobs=16 no-gil 3.20s @ n_jobs=16
    -> gil 1.32x faster
  peak speedup             gil 4.27x (2.42s @ n_jobs=16) no-gil 3.84x (3.20s @ n_jobs=16)
    -> gil 1.11x better
  speedup at max cores     gil 4.27x (2.42s @ n_jobs=16) no-gil 3.84x (3.20s @ n_jobs=16)
    -> gil 1.11x better

  pypi / threading
  single-thread baseline   gil 7.81s            no-gil 11.31s
    -> gil 1.45x faster
  best duration            gil 7.81s @ n_jobs=1 no-gil 11.31s @ n_jobs=1
    -> gil 1.45x faster
  peak speedup             gil 1.00x (7.81s @ n_jobs=1) no-gil 1.00x (11.31s @ n_jobs=1)
    -> tie
  speedup at max cores     gil 0.56x (14.01s @ n_jobs=16) no-gil 0.54x (20.94s @ n_jobs=16)
    -> gil 1.03x better

  Summary across paired stacks
    single-thread baseline: gil 8 wins, no-gil 0 wins
    best duration:          gil 6 wins, no-gil 2 wins
    peak speedup:           gil 2 wins, no-gil 4 wins
    speedup at max cores:   gil 5 wins, no-gil 3 wins

