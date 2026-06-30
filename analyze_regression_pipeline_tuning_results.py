#!/usr/bin/env python3
"""Analyze regression pipeline tuning benchmark results by hardware."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

RESULTS_DIR = (
    Path(__file__).resolve().parent / "results" / "regression_pipeline_tuning"
)
REPORT_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class HardwareKey:
    model: str | None
    architecture: str | None
    logical_cores: int | None

    def label(self) -> str:
        model = self.model or "unknown CPU"
        arch = self.architecture or "unknown arch"
        cores = self.logical_cores if self.logical_cores is not None else "?"
        return f"{model} ({arch}, {cores} logical cores)"


@dataclass(frozen=True)
class SetupKey:
    pixi_environment: str | None
    joblib_backend: str | None
    gil_enabled: bool | None

    def label(self) -> str:
        env = self.pixi_environment or "unknown-env"
        backend = self.joblib_backend or "unknown-backend"
        gil = "gil" if self.gil_enabled else "no-gil" if self.gil_enabled is False else "gil=?"
        return f"{env} / {backend} / {gil}"


@dataclass(frozen=True)
class GilComparisonKey:
    stack_family: str
    joblib_backend: str

    def label(self) -> str:
        return f"{self.stack_family} / {self.joblib_backend}"


@dataclass
class GilComparison:
    key: GilComparisonKey
    gil_run: RunAnalysis | None
    freethreading_run: RunAnalysis | None


@dataclass(frozen=True)
class BlasInfo:
    implementation: str | None
    openblas_coretype: str | None
    openblas_threading_layer: str | None

    def label(self) -> str:
        if self.implementation is None:
            return "n/a"
        if self.implementation == "OpenBLAS":
            details = [
                detail
                for detail in (
                    self.openblas_coretype,
                    self.openblas_threading_layer,
                )
                if detail
            ]
            if details:
                return f"OpenBLAS ({', '.join(details)})"
            return "OpenBLAS"
        return self.implementation


@dataclass
class RunAnalysis:
    run_id: str
    results_file: str
    hardware: HardwareKey
    setup: SetupKey
    distribution: str | None
    blas: BlasInfo
    baseline_duration_s: float | None
    best_duration_s: float | None
    best_n_jobs: int | None
    peak_duration_s: float | None
    peak_speedup: float | None
    peak_speedup_n_jobs: int | None
    max_n_jobs: int | None
    max_duration_s: float | None
    speedup_at_max_n_jobs: float | None
    parallel_efficiency_at_peak: float | None
    parallel_efficiency_at_max: float | None
    slowdown_at_max: float | None
    failed: bool

    @property
    def setup_label(self) -> str:
        return self.setup.label()

    @property
    def sort_key(self) -> tuple:
        return (
            self.distribution or "",
            stack_family(self.setup.pixi_environment) or "",
            self.setup.pixi_environment or "",
            self.setup.joblib_backend or "",
            0 if self.setup.gil_enabled else 1 if self.setup.gil_enabled is False else 2,
        )


RUN_CONFIG_HEADERS = ["GIL", "Distribution", "Joblib backend"]


def distribution_from_record(record: dict) -> str | None:
    packages = record.get("system", {}).get("packages", {})
    numpy_info = packages.get("numpy", {})
    channel = numpy_info.get("channel")
    if channel == "pypi.org":
        return "pypi"
    if channel == "conda-forge":
        return "conda-forge"
    return channel


def fmt_gil(gil_enabled: bool | None) -> str:
    if gil_enabled is True:
        return "gil"
    if gil_enabled is False:
        return "no-gil"
    return "n/a"


def fmt_distribution(distribution: str | None) -> str:
    return distribution or "n/a"


def fmt_joblib_backend(joblib_backend: str | None) -> str:
    return joblib_backend or "n/a"


def run_config_columns(run: RunAnalysis) -> list[str]:
    return [
        fmt_gil(run.setup.gil_enabled),
        fmt_distribution(run.distribution),
        fmt_joblib_backend(run.setup.joblib_backend),
    ]


def hardware_key(record: dict) -> HardwareKey:
    cpu = record["system"]["cpu"]
    return HardwareKey(
        model=cpu.get("model"),
        architecture=cpu.get("architecture"),
        logical_cores=cpu.get("logical_cores"),
    )


def setup_key(record: dict) -> SetupKey:
    return SetupKey(
        pixi_environment=record["system"]["pixi"].get("environment"),
        joblib_backend=record["run"].get("joblib_backend"),
        gil_enabled=record["system"]["python"].get("gil_enabled"),
    )


def blas_info_from_record(record: dict) -> BlasInfo:
    libraries = record.get("system", {}).get("threadpool_libraries", [])
    blas_libraries = [
        library for library in libraries if library.get("user_api") == "blas"
    ]
    if not blas_libraries:
        return BlasInfo(
            implementation=None,
            openblas_coretype=None,
            openblas_threading_layer=None,
        )

    library = blas_libraries[0]
    internal_api = library.get("internal_api")
    coretype = library.get("architecture")
    threading_layer = library.get("threading_layer")

    if internal_api == "newaccelerate":
        return BlasInfo(
            implementation="Accelerate",
            openblas_coretype=None,
            openblas_threading_layer=None,
        )
    if internal_api == "mkl":
        return BlasInfo(
            implementation="MKL",
            openblas_coretype=None,
            openblas_threading_layer=None,
        )
    if internal_api == "openblas":
        return BlasInfo(
            implementation="OpenBLAS",
            openblas_coretype=coretype,
            openblas_threading_layer=threading_layer,
        )

    return BlasInfo(
        implementation=internal_api,
        openblas_coretype=coretype,
        openblas_threading_layer=threading_layer,
    )


def stack_family(pixi_environment: str | None) -> str | None:
    if not pixi_environment:
        return None
    for suffix in ("-freethreading", "-gil"):
        if pixi_environment.endswith(suffix):
            return pixi_environment[: -len(suffix)]
    return pixi_environment


def gil_comparison_key(analysis: RunAnalysis) -> GilComparisonKey | None:
    family = stack_family(analysis.setup.pixi_environment)
    backend = analysis.setup.joblib_backend
    if family is None or backend is None:
        return None
    return GilComparisonKey(stack_family=family, joblib_backend=backend)


def group_gil_comparisons(runs: list[RunAnalysis]) -> list[GilComparison]:
    buckets: dict[GilComparisonKey, dict[bool | None, RunAnalysis]] = {}
    for run in runs:
        key = gil_comparison_key(run)
        if key is None:
            continue
        buckets.setdefault(key, {})[run.setup.gil_enabled] = run

    comparisons = []
    for key in sorted(buckets, key=lambda item: item.label()):
        variants = buckets[key]
        comparisons.append(
            GilComparison(
                key=key,
                gil_run=variants.get(True),
                freethreading_run=variants.get(False),
            )
        )
    return comparisons


def successful_timings(record: dict) -> list[dict]:
    return [
        timing
        for timing in record.get("timings", [])
        if timing.get("error") is None and timing.get("duration_s") is not None
    ]


def analyze_record(record: dict) -> RunAnalysis:
    timings = successful_timings(record)
    hardware = hardware_key(record)
    setup = setup_key(record)
    distribution = distribution_from_record(record)
    blas = blas_info_from_record(record)

    if not timings:
        return RunAnalysis(
            run_id=record.get("run_id", ""),
            results_file=record.get("results_file", ""),
            hardware=hardware,
            setup=setup,
            distribution=distribution,
            blas=blas,
            baseline_duration_s=None,
            best_duration_s=None,
            best_n_jobs=None,
            peak_duration_s=None,
            peak_speedup=None,
            peak_speedup_n_jobs=None,
            max_n_jobs=None,
            max_duration_s=None,
            speedup_at_max_n_jobs=None,
            parallel_efficiency_at_peak=None,
            parallel_efficiency_at_max=None,
            slowdown_at_max=None,
            failed=True,
        )

    baseline = next((t for t in timings if t["n_jobs"] == 1), timings[0])
    baseline_duration_s = baseline["duration_s"]

    best = min(timings, key=lambda timing: timing["duration_s"])
    best_duration_s = best["duration_s"]
    best_n_jobs = best["n_jobs"]

    speedup_timings = [
        timing for timing in timings if timing.get("speedup") is not None
    ]
    if speedup_timings:
        peak = max(speedup_timings, key=lambda timing: timing["speedup"])
        peak_speedup = peak["speedup"]
        peak_speedup_n_jobs = peak["n_jobs"]
        peak_duration_s = peak["duration_s"]
    else:
        peak_speedup = None
        peak_speedup_n_jobs = None
        peak_duration_s = None

    max_n_jobs = max(timing["n_jobs"] for timing in timings)
    at_max = next(timing for timing in timings if timing["n_jobs"] == max_n_jobs)
    max_duration_s = at_max["duration_s"]
    speedup_at_max = at_max.get("speedup")
    if speedup_at_max is None and baseline_duration_s:
        speedup_at_max = baseline_duration_s / at_max["duration_s"]

    parallel_efficiency_at_peak = (
        peak_speedup / peak_speedup_n_jobs
        if peak_speedup is not None and peak_speedup_n_jobs
        else None
    )
    parallel_efficiency_at_max = (
        speedup_at_max / max_n_jobs
        if speedup_at_max is not None and max_n_jobs
        else None
    )
    slowdown_at_max = (
        at_max["duration_s"] / baseline_duration_s
        if baseline_duration_s
        else None
    )

    return RunAnalysis(
        run_id=record.get("run_id", ""),
        results_file=record.get("results_file", ""),
        hardware=hardware,
        setup=setup,
        distribution=distribution,
        blas=blas,
        baseline_duration_s=baseline_duration_s,
        best_duration_s=best_duration_s,
        best_n_jobs=best_n_jobs,
        peak_duration_s=peak_duration_s,
        peak_speedup=peak_speedup,
        peak_speedup_n_jobs=peak_speedup_n_jobs,
        max_n_jobs=max_n_jobs,
        max_duration_s=max_duration_s,
        speedup_at_max_n_jobs=speedup_at_max,
        parallel_efficiency_at_peak=parallel_efficiency_at_peak,
        parallel_efficiency_at_max=parallel_efficiency_at_max,
        slowdown_at_max=slowdown_at_max,
        failed=False,
    )


def load_results(results_dir: Path) -> list[dict]:
    records = []
    for path in sorted(results_dir.glob("*.json")):
        with path.open(encoding="utf-8") as file:
            records.append(json.load(file))
    return records


def setup_hardware_key(record: dict) -> tuple[HardwareKey, SetupKey]:
    return (hardware_key(record), setup_key(record))


def record_recency_key(record: dict) -> tuple[str, str]:
    timestamp = record.get("completed_at") or record.get("recorded_at") or ""
    return (timestamp, record.get("results_file", ""))


def dedupe_records(records: list[dict]) -> tuple[list[dict], int]:
    """Keep the most recent result for each hardware/setup combination."""
    latest: dict[tuple[HardwareKey, SetupKey], dict] = {}
    latest_recency: dict[tuple[HardwareKey, SetupKey], tuple[str, str]] = {}

    for record in records:
        key = setup_hardware_key(record)
        recency = record_recency_key(record)
        if key not in latest or recency > latest_recency[key]:
            latest[key] = record
            latest_recency[key] = recency

    deduped = list(latest.values())
    return deduped, len(records) - len(deduped)


def group_by_hardware(analyses: list[RunAnalysis]) -> dict[HardwareKey, list[RunAnalysis]]:
    grouped: dict[HardwareKey, list[RunAnalysis]] = {}
    for analysis in analyses:
        grouped.setdefault(analysis.hardware, []).append(analysis)
    return grouped


def fmt_blas(blas: BlasInfo) -> str:
    return blas.label()


def fmt_seconds(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f}s"


def fmt_speedup(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f}x"


def fmt_ratio(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f}"


def fmt_duration_at_n_jobs(
    duration_s: float | None,
    n_jobs: int | None,
) -> str:
    if duration_s is None:
        return "n/a"
    if n_jobs is None:
        return fmt_seconds(duration_s)
    return f"{fmt_seconds(duration_s)} @ n_jobs={n_jobs}"


def faster_label(
    left: float,
    right: float,
    *,
    left_name: str,
    right_name: str,
) -> str:
    if left == right:
        return "tie"
    if left < right:
        return f"{left_name} {right / left:.2f}x faster"
    return f"{right_name} {left / right:.2f}x faster"


def better_scaling_label(
    left: float,
    right: float,
    *,
    left_name: str,
    right_name: str,
) -> str:
    if left == right:
        return "tie"
    if left > right:
        return f"{left_name} {left / right:.2f}x better"
    return f"{right_name} {right / left:.2f}x better"


def duration_delta_pct(reference_s: float, candidate_s: float) -> float:
    return (reference_s - candidate_s) / reference_s * 100


def md_cell(value: object) -> str:
    return str(value).replace("|", "\\|")


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return "_No data._"
    lines = [
        "| " + " | ".join(md_cell(header) for header in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md_cell(cell) for cell in row) + " |")
    return "\n".join(lines)


def metric_verdict(
    gil_value: float | None,
    ft_value: float | None,
    *,
    lower_is_better: bool,
) -> str:
    if gil_value is None or ft_value is None:
        return "n/a"
    if lower_is_better:
        return faster_label(
            gil_value,
            ft_value,
            left_name="gil",
            right_name="no-gil",
        )
    return better_scaling_label(
        gil_value,
        ft_value,
        left_name="gil",
        right_name="no-gil",
    )


def results_file_href(results_file: str, results_dir: Path) -> str:
    file_path = (results_dir / results_file).resolve()
    try:
        return file_path.relative_to(REPORT_ROOT.resolve()).as_posix()
    except ValueError:
        return file_path.as_posix()


def results_file_link(
    results_file: str,
    results_dir: Path,
    *,
    text: str,
) -> str:
    return f"[{text}]({results_file_href(results_file, results_dir)})"


def run_reference(run: RunAnalysis, results_dir: Path) -> str:
    return results_file_link(run.results_file, results_dir, text=run.run_id)


def gil_comparison_to_dict(comparison: GilComparison) -> dict:
    def run_summary(run: RunAnalysis | None) -> dict | None:
        if run is None:
            return None
        return analysis_to_dict(run)

    payload = {
        "stack_family": comparison.key.stack_family,
        "joblib_backend": comparison.key.joblib_backend,
        "gil": run_summary(comparison.gil_run),
        "freethreading": run_summary(comparison.freethreading_run),
    }

    gil = comparison.gil_run
    ft = comparison.freethreading_run
    if gil is not None and not gil.failed and ft is not None and not ft.failed:
        payload["deltas"] = {
            "baseline_duration_pct_no_gil_vs_gil": duration_delta_pct(
                gil.baseline_duration_s, ft.baseline_duration_s
            )
            if gil.baseline_duration_s and ft.baseline_duration_s
            else None,
            "best_duration_pct_no_gil_vs_gil": duration_delta_pct(
                gil.best_duration_s, ft.best_duration_s
            )
            if gil.best_duration_s and ft.best_duration_s
            else None,
            "peak_speedup_ratio_no_gil_vs_gil": (
                ft.peak_speedup / gil.peak_speedup
                if gil.peak_speedup and ft.peak_speedup
                else None
            ),
            "speedup_at_max_ratio_no_gil_vs_gil": (
                ft.speedup_at_max_n_jobs / gil.speedup_at_max_n_jobs
                if gil.speedup_at_max_n_jobs and ft.speedup_at_max_n_jobs
                else None
            ),
        }

    return payload


def gil_comparison_rows(
    comparison: GilComparison,
) -> tuple[list[list[str]], dict[str, int], dict[str, int]] | None:
    gil = comparison.gil_run
    ft = comparison.freethreading_run
    assert gil is not None and ft is not None

    gil_wins = {"baseline": 0, "best": 0, "peak_speedup": 0, "speedup_at_max": 0}
    ft_wins = dict(gil_wins)

    if gil.failed or ft.failed:
        if gil.failed and ft.failed:
            status = "both variants failed"
        else:
            gil_status = "failed" if gil.failed else "ok"
            ft_status = "failed" if ft.failed else "ok"
            status = f"incomplete pair (gil={gil_status}, no-gil={ft_status})"
        return (
            [[comparison.key.label(), status, "n/a", "n/a", "n/a"]],
            gil_wins,
            ft_wins,
        )

    metrics = [
        (
            "single-thread baseline",
            gil.baseline_duration_s,
            ft.baseline_duration_s,
            lambda value: fmt_seconds(value),
            True,
            "baseline",
        ),
        (
            "best duration",
            gil.best_duration_s,
            ft.best_duration_s,
            lambda value, run: fmt_duration_at_n_jobs(value, run.best_n_jobs),
            True,
            "best",
        ),
        (
            "peak speedup",
            gil.peak_speedup,
            ft.peak_speedup,
            lambda value, run: (
                f"{fmt_speedup(value)} "
                f"({fmt_duration_at_n_jobs(run.peak_duration_s, run.peak_speedup_n_jobs)})"
            ),
            False,
            "peak_speedup",
        ),
        (
            "speedup at max cores",
            gil.speedup_at_max_n_jobs,
            ft.speedup_at_max_n_jobs,
            lambda value, run: (
                f"{fmt_speedup(value)} "
                f"({fmt_duration_at_n_jobs(run.max_duration_s, run.max_n_jobs)})"
            ),
            False,
            "speedup_at_max",
        ),
    ]

    rows = []
    for label, gil_value, ft_value, fmt_fn, lower_is_better, win_key in metrics:
        if label == "single-thread baseline":
            gil_text = fmt_fn(gil_value) if gil_value is not None else "n/a"
            ft_text = fmt_fn(ft_value) if ft_value is not None else "n/a"
        else:
            gil_text = fmt_fn(gil_value, gil) if gil_value is not None else "n/a"
            ft_text = fmt_fn(ft_value, ft) if ft_value is not None else "n/a"
        verdict = metric_verdict(
            gil_value,
            ft_value,
            lower_is_better=lower_is_better,
        )
        rows.append([comparison.key.label(), label, gil_text, ft_text, verdict])

        if gil_value is None or ft_value is None:
            continue
        if lower_is_better:
            if gil_value < ft_value:
                gil_wins[win_key] += 1
            elif gil_value > ft_value:
                ft_wins[win_key] += 1
        elif gil_value > ft_value:
            gil_wins[win_key] += 1
        elif gil_value < ft_value:
            ft_wins[win_key] += 1

    return rows, gil_wins, ft_wins


def report_gil_comparisons(runs: list[RunAnalysis]) -> list[str]:
    comparisons = group_gil_comparisons(runs)
    paired = [
        comparison
        for comparison in comparisons
        if comparison.gil_run is not None and comparison.freethreading_run is not None
    ]
    partial = [
        comparison
        for comparison in comparisons
        if (comparison.gil_run is None) != (comparison.freethreading_run is None)
    ]

    if not comparisons:
        return []

    lines = ["### GIL vs free-threading comparisons", ""]
    if not paired:
        lines.append("No complete gil/no-gil pairs found for this hardware.")
        lines.append("")
    else:
        comparison_rows: list[list[str]] = []
        total_gil_wins = {"baseline": 0, "best": 0, "peak_speedup": 0, "speedup_at_max": 0}
        total_ft_wins = dict(total_gil_wins)

        for comparison in paired:
            result = gil_comparison_rows(comparison)
            assert result is not None
            rows, gil_wins, ft_wins = result
            comparison_rows.extend(rows)
            for key in total_gil_wins:
                total_gil_wins[key] += gil_wins[key]
                total_ft_wins[key] += ft_wins[key]

        lines.append(
            md_table(
                ["Stack / backend", "Metric", "GIL", "No-GIL", "Verdict"],
                comparison_rows,
            )
        )
        lines.append("")
        lines.append("#### Summary across paired stacks")
        lines.append("")
        lines.append(
            md_table(
                ["Metric", "GIL wins", "No-GIL wins"],
                [
                    ["single-thread baseline", str(total_gil_wins["baseline"]), str(total_ft_wins["baseline"])],
                    ["best duration", str(total_gil_wins["best"]), str(total_ft_wins["best"])],
                    ["peak speedup", str(total_gil_wins["peak_speedup"]), str(total_ft_wins["peak_speedup"])],
                    [
                        "speedup at max cores",
                        str(total_gil_wins["speedup_at_max"]),
                        str(total_ft_wins["speedup_at_max"]),
                    ],
                ],
            )
        )
        lines.append("")

    if partial:
        lines.append("#### Incomplete pairs (missing counterpart)")
        lines.append("")
        partial_rows = []
        for comparison in partial:
            missing = "no-gil" if comparison.freethreading_run is None else "gil"
            present = comparison.freethreading_run or comparison.gil_run
            assert present is not None
            status = "failed" if present.failed else "ok"
            partial_rows.append(
                [
                    comparison.key.label(),
                    missing,
                    present.setup.pixi_environment or "unknown",
                    status,
                ]
            )
        lines.append(
            md_table(
                ["Stack / backend", "Missing", "Present environment", "Status"],
                partial_rows,
            )
        )
        lines.append("")

    return lines


def report_full_results_table(
    runs: list[RunAnalysis],
    results_dir: Path,
) -> list[str]:
    rows: list[list[str]] = []
    for run in sorted(runs, key=lambda item: item.sort_key):
        if run.failed:
            continue
        rows.append(
            [
                *run_config_columns(run),
                fmt_blas(run.blas),
                fmt_seconds(run.baseline_duration_s),
                fmt_duration_at_n_jobs(run.best_duration_s, run.best_n_jobs),
                f"{fmt_speedup(run.peak_speedup)} "
                f"({fmt_duration_at_n_jobs(run.peak_duration_s, run.peak_speedup_n_jobs)})",
                f"{fmt_speedup(run.speedup_at_max_n_jobs)} "
                f"({fmt_duration_at_n_jobs(run.max_duration_s, run.max_n_jobs)})",
                fmt_ratio(run.parallel_efficiency_at_peak),
                fmt_ratio(run.parallel_efficiency_at_max),
                f"{fmt_ratio(run.slowdown_at_max)}x",
                run_reference(run, results_dir),
            ]
        )

    if not rows:
        return []

    return [
        "### All runs",
        "",
        md_table(
            [
                *RUN_CONFIG_HEADERS,
                "BLAS",
                "Baseline",
                "Best",
                "Peak speedup",
                "Speedup @ max",
                "Peak parallel efficiency",
                "Max-core parallel efficiency",
                "Slowdown @ max",
                "Run",
            ],
            rows,
        ),
        "",
    ]


def md_details(summary: str, body_lines: list[str]) -> list[str]:
    if not body_lines:
        return []
    return [
        "<details>",
        f"<summary>{summary}</summary>",
        "",
        *body_lines,
        "",
        "</details>",
        "",
    ]


TOP_N = 3


def top_runs(
    runs: list[RunAnalysis],
    key,
    *,
    reverse: bool = False,
    limit: int = TOP_N,
) -> list[RunAnalysis]:
    return sorted(runs, key=key, reverse=reverse)[:limit]


def absolute_speed_row(
    rank: int,
    run: RunAnalysis,
    results_dir: Path,
) -> list[str]:
    return [
        f"#{rank}",
        *run_config_columns(run),
        fmt_blas(run.blas),
        fmt_seconds(run.baseline_duration_s),
        fmt_duration_at_n_jobs(run.best_duration_s, run.best_n_jobs),
        run_reference(run, results_dir),
    ]


def scalability_row(
    rank: int,
    run: RunAnalysis,
    results_dir: Path,
) -> list[str]:
    return [
        f"#{rank}",
        *run_config_columns(run),
        fmt_blas(run.blas),
        fmt_speedup(run.peak_speedup),
        fmt_ratio(run.parallel_efficiency_at_peak),
        fmt_duration_at_n_jobs(run.peak_duration_s, run.peak_speedup_n_jobs),
        fmt_seconds(run.baseline_duration_s),
        fmt_duration_at_n_jobs(run.best_duration_s, run.best_n_jobs),
        run_reference(run, results_dir),
    ]


def problematic_row(rank: int, run: RunAnalysis, results_dir: Path) -> list[str]:
    return [
        f"#{rank}",
        *run_config_columns(run),
        fmt_blas(run.blas),
        fmt_seconds(run.baseline_duration_s),
        fmt_duration_at_n_jobs(run.best_duration_s, run.best_n_jobs),
        f"{fmt_speedup(run.peak_speedup)} "
        f"({fmt_duration_at_n_jobs(run.peak_duration_s, run.peak_speedup_n_jobs)})",
        f"{fmt_speedup(run.speedup_at_max_n_jobs)} "
        f"({fmt_duration_at_n_jobs(run.max_duration_s, run.max_n_jobs)})",
        f"{fmt_ratio(run.slowdown_at_max)}x",
        fmt_ratio(run.parallel_efficiency_at_max),
        run_reference(run, results_dir),
    ]


def problematic_sort_key(run: RunAnalysis) -> tuple:
    return (
        run.speedup_at_max_n_jobs if run.speedup_at_max_n_jobs is not None else 999,
        -(run.slowdown_at_max or 0),
        run.parallel_efficiency_at_max
        if run.parallel_efficiency_at_max is not None
        else 999,
    )


def report_hardware(
    hardware: HardwareKey,
    runs: list[RunAnalysis],
    *,
    results_dir: Path,
) -> list[str]:
    successful = [run for run in runs if not run.failed]
    failed = [run for run in runs if run.failed]

    lines = [
        f"## {hardware.label()}",
        "",
        f"Runs: {len(runs)} total, {len(successful)} successful, {len(failed)} failed",
        "",
    ]

    if not successful:
        lines.append("No successful runs for this hardware.")
        if failed:
            lines.extend(["", "### Failed setups", ""])
            lines.append(
                md_table(
                    [*RUN_CONFIG_HEADERS, "Results file"],
                    [[*run_config_columns(run), results_file_link(
                        run.results_file, results_dir, text=run.results_file
                    )] for run in failed],
                )
            )
        lines.append("")
        return lines

    absolute_rows = [
        absolute_speed_row(rank, run, results_dir)
        for rank, run in enumerate(
            top_runs(
                successful,
                lambda item: item.best_duration_s or float("inf"),
            ),
            start=1,
        )
    ]

    lines.extend(
        [
            "### Most efficient (absolute speed)",
            "",
            md_table(
                ["Rank", *RUN_CONFIG_HEADERS, "BLAS", "Baseline", "Best", "Run"],
                absolute_rows,
            ),
            "",
        ]
    )

    scalability_rows = [
        scalability_row(rank, run, results_dir)
        for rank, run in enumerate(
            top_runs(
                successful,
                lambda item: item.peak_speedup or float("-inf"),
                reverse=True,
            ),
            start=1,
        )
    ]

    lines.extend(
        [
            "### Most efficient (scalability)",
            "",
            md_table(
                [
                    "Rank",
                    *RUN_CONFIG_HEADERS,
                    "BLAS",
                    "Speedup",
                    "Parallel efficiency",
                    "Duration",
                    "Baseline",
                    "Best",
                    "Run",
                ],
                scalability_rows,
            ),
            "",
        ]
    )

    problematic_rows = [
        problematic_row(rank, run, results_dir)
        for rank, run in enumerate(
            sorted(successful, key=problematic_sort_key)[:TOP_N],
            start=1,
        )
    ]

    lines.append("### Most problematic (lack of scalability)")
    lines.append("")
    if problematic_rows:
        lines.append(
            md_table(
                [
                    "Rank",
                    *RUN_CONFIG_HEADERS,
                    "BLAS",
                    "Baseline",
                    "Best",
                    "Peak speedup",
                    "Speedup @ max",
                    "Slowdown @ max",
                    "Max-core efficiency",
                    "Run",
                ],
                problematic_rows,
            )
        )
    else:
        lines.append("No clearly problematic setups detected.")
    lines.append("")

    details_body = report_full_results_table(runs, results_dir)
    details_body.extend(report_gil_comparisons(runs))
    if details_body:
        lines.extend(
            md_details(
                "Full results and GIL vs free-threading comparisons",
                details_body,
            )
        )

    if failed:
        lines.extend(
            [
                "### Failed setups (excluded from rankings)",
                "",
                md_table(
                    [*RUN_CONFIG_HEADERS, "Results file"],
                    [[*run_config_columns(run), results_file_link(
                        run.results_file, results_dir, text=run.results_file
                    )] for run in failed],
                ),
                "",
            ]
        )

    return lines


def analysis_to_dict(analysis: RunAnalysis) -> dict:
    return {
        "run_id": analysis.run_id,
        "results_file": analysis.results_file,
        "hardware": {
            "model": analysis.hardware.model,
            "architecture": analysis.hardware.architecture,
            "logical_cores": analysis.hardware.logical_cores,
        },
        "setup": {
            "pixi_environment": analysis.setup.pixi_environment,
            "joblib_backend": analysis.setup.joblib_backend,
            "gil_enabled": analysis.setup.gil_enabled,
        },
        "distribution": analysis.distribution,
        "blas": {
            "implementation": analysis.blas.implementation,
            "openblas_coretype": analysis.blas.openblas_coretype,
            "openblas_threading_layer": analysis.blas.openblas_threading_layer,
            "label": analysis.blas.label(),
        },
        "baseline_duration_s": analysis.baseline_duration_s,
        "best_duration_s": analysis.best_duration_s,
        "best_n_jobs": analysis.best_n_jobs,
        "peak_duration_s": analysis.peak_duration_s,
        "peak_speedup": analysis.peak_speedup,
        "peak_speedup_n_jobs": analysis.peak_speedup_n_jobs,
        "max_n_jobs": analysis.max_n_jobs,
        "max_duration_s": analysis.max_duration_s,
        "speedup_at_max_n_jobs": analysis.speedup_at_max_n_jobs,
        "parallel_efficiency_at_peak": analysis.parallel_efficiency_at_peak,
        "parallel_efficiency_at_max": analysis.parallel_efficiency_at_max,
        "slowdown_at_max": analysis.slowdown_at_max,
        "failed": analysis.failed,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Analyze regression pipeline tuning results and rank runtime/hardware "
            "setups by absolute speed and scalability for each CPU."
        )
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=RESULTS_DIR,
        help=f"Directory containing benchmark JSON files (default: {RESULTS_DIR})",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of a markdown report.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the markdown report to this file instead of stdout.",
    )
    args = parser.parse_args(argv)

    if not args.results_dir.is_dir():
        print(f"Results directory not found: {args.results_dir}", file=sys.stderr)
        return 1

    records = load_results(args.results_dir)
    if not records:
        print(f"No JSON results found in {args.results_dir}", file=sys.stderr)
        return 1

    raw_count = len(records)
    records, duplicates_skipped = dedupe_records(records)

    analyses = [analyze_record(record) for record in records]
    grouped = group_by_hardware(analyses)

    if args.json:
        payload = {}
        for hardware, runs in sorted(grouped.items(), key=lambda item: item[0].label()):
            payload[hardware.label()] = {
                "runs": [
                    analysis_to_dict(analysis)
                    for analysis in sorted(runs, key=lambda run: run.sort_key)
                ],
                "gil_comparisons": [
                    gil_comparison_to_dict(comparison)
                    for comparison in group_gil_comparisons(runs)
                ],
            }
        json.dump(payload, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        return 0

    loaded_message = (
        f"Loaded {raw_count} result file(s) from `{args.results_dir}`"
        + (
            f", kept {len(records)} after deduplicating "
            f"{duplicates_skipped} older run(s) with the same hardware/setup."
            if duplicates_skipped
            else "."
        )
    )

    report_lines = [
        "# Regression pipeline tuning results",
        "",
        loaded_message,
        "",
    ]
    for hardware in sorted(grouped, key=lambda key: key.label()):
        report_lines.extend(
            report_hardware(hardware, grouped[hardware], results_dir=args.results_dir)
        )
    report = "\n".join(report_lines) + "\n"
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
