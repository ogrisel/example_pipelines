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


@dataclass
class RunAnalysis:
    run_id: str
    results_file: str
    hardware: HardwareKey
    setup: SetupKey
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

    if not timings:
        return RunAnalysis(
            run_id=record.get("run_id", ""),
            results_file=record.get("results_file", ""),
            hardware=hardware,
            setup=setup,
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


def group_by_hardware(analyses: list[RunAnalysis]) -> dict[HardwareKey, list[RunAnalysis]]:
    grouped: dict[HardwareKey, list[RunAnalysis]] = {}
    for analysis in analyses:
        grouped.setdefault(analysis.hardware, []).append(analysis)
    return grouped


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


def fmt_run_timings(
    run: RunAnalysis,
    *,
    include_baseline: bool = True,
    include_best: bool = True,
    include_peak: bool = False,
    include_max: bool = False,
) -> str:
    parts: list[str] = []
    if include_baseline:
        parts.append(f"baseline {fmt_seconds(run.baseline_duration_s)}")
    if include_best:
        parts.append(
            f"best {fmt_duration_at_n_jobs(run.best_duration_s, run.best_n_jobs)}"
        )
    if include_peak:
        parts.append(
            f"peak {fmt_duration_at_n_jobs(run.peak_duration_s, run.peak_speedup_n_jobs)}"
        )
    if include_max:
        parts.append(
            f"max {fmt_duration_at_n_jobs(run.max_duration_s, run.max_n_jobs)}"
        )
    return "; ".join(parts)


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


def print_metric_comparison(
    label: str,
    *,
    gil_value: float | None,
    gil_suffix: str,
    ft_value: float | None,
    ft_suffix: str,
    lower_is_better: bool,
) -> None:
    gil_text = "n/a" if gil_value is None else f"{gil_value:.2f}{gil_suffix}"
    ft_text = "n/a" if ft_value is None else f"{ft_value:.2f}{ft_suffix}"
    print(f"  {label:<24} gil {gil_text:<16} no-gil {ft_text}")

    if gil_value is None or ft_value is None:
        return
    if lower_is_better:
        verdict = faster_label(
            gil_value,
            ft_value,
            left_name="gil",
            right_name="no-gil",
        )
    else:
        verdict = better_scaling_label(
            gil_value,
            ft_value,
            left_name="gil",
            right_name="no-gil",
        )
    print(f"    -> {verdict}")


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


def report_gil_comparisons(runs: list[RunAnalysis]) -> None:
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
        return

    print("GIL vs free-threading comparisons")
    if not paired:
        print("  No complete gil/no-gil pairs found for this hardware.")
    else:
        gil_wins = {"baseline": 0, "best": 0, "peak_speedup": 0, "speedup_at_max": 0}
        ft_wins = dict(gil_wins)

        for comparison in paired:
            gil = comparison.gil_run
            ft = comparison.freethreading_run
            assert gil is not None and ft is not None

            print(f"\n  {comparison.key.label()}")
            if gil.failed or ft.failed:
                if gil.failed and ft.failed:
                    print("    both variants failed")
                else:
                    gil_status = "failed" if gil.failed else "ok"
                    ft_status = "failed" if ft.failed else "ok"
                    print(f"    incomplete pair (gil={gil_status}, no-gil={ft_status})")
                continue

            print_metric_comparison(
                "single-thread baseline",
                gil_value=gil.baseline_duration_s,
                gil_suffix="s",
                ft_value=ft.baseline_duration_s,
                ft_suffix="s",
                lower_is_better=True,
            )
            print_metric_comparison(
                "best duration",
                gil_value=gil.best_duration_s,
                gil_suffix=f"s @ n_jobs={gil.best_n_jobs}",
                ft_value=ft.best_duration_s,
                ft_suffix=f"s @ n_jobs={ft.best_n_jobs}",
                lower_is_better=True,
            )
            print_metric_comparison(
                "peak speedup",
                gil_value=gil.peak_speedup,
                gil_suffix=(
                    f"x ({fmt_duration_at_n_jobs(gil.peak_duration_s, gil.peak_speedup_n_jobs)})"
                ),
                ft_value=ft.peak_speedup,
                ft_suffix=(
                    f"x ({fmt_duration_at_n_jobs(ft.peak_duration_s, ft.peak_speedup_n_jobs)})"
                ),
                lower_is_better=False,
            )
            print_metric_comparison(
                "speedup at max cores",
                gil_value=gil.speedup_at_max_n_jobs,
                gil_suffix=(
                    f"x ({fmt_duration_at_n_jobs(gil.max_duration_s, gil.max_n_jobs)})"
                ),
                ft_value=ft.speedup_at_max_n_jobs,
                ft_suffix=(
                    f"x ({fmt_duration_at_n_jobs(ft.max_duration_s, ft.max_n_jobs)})"
                ),
                lower_is_better=False,
            )

            if gil.baseline_duration_s and ft.baseline_duration_s:
                winner = "gil" if gil.baseline_duration_s < ft.baseline_duration_s else "no-gil"
                if gil.baseline_duration_s == ft.baseline_duration_s:
                    pass
                elif winner == "gil":
                    gil_wins["baseline"] += 1
                else:
                    ft_wins["baseline"] += 1
            if gil.best_duration_s and ft.best_duration_s:
                if gil.best_duration_s < ft.best_duration_s:
                    gil_wins["best"] += 1
                elif gil.best_duration_s > ft.best_duration_s:
                    ft_wins["best"] += 1
            if gil.peak_speedup and ft.peak_speedup:
                if gil.peak_speedup > ft.peak_speedup:
                    gil_wins["peak_speedup"] += 1
                elif gil.peak_speedup < ft.peak_speedup:
                    ft_wins["peak_speedup"] += 1
            if gil.speedup_at_max_n_jobs and ft.speedup_at_max_n_jobs:
                if gil.speedup_at_max_n_jobs > ft.speedup_at_max_n_jobs:
                    gil_wins["speedup_at_max"] += 1
                elif gil.speedup_at_max_n_jobs < ft.speedup_at_max_n_jobs:
                    ft_wins["speedup_at_max"] += 1

        print("\n  Summary across paired stacks")
        print(
            f"    single-thread baseline: gil {gil_wins['baseline']} wins, "
            f"no-gil {ft_wins['baseline']} wins"
        )
        print(
            f"    best duration:          gil {gil_wins['best']} wins, "
            f"no-gil {ft_wins['best']} wins"
        )
        print(
            f"    peak speedup:           gil {gil_wins['peak_speedup']} wins, "
            f"no-gil {ft_wins['peak_speedup']} wins"
        )
        print(
            f"    speedup at max cores:   gil {gil_wins['speedup_at_max']} wins, "
            f"no-gil {ft_wins['speedup_at_max']} wins"
        )

    if partial:
        print("\n  Incomplete pairs (missing counterpart)")
        for comparison in partial:
            missing = "no-gil" if comparison.freethreading_run is None else "gil"
            present = comparison.freethreading_run or comparison.gil_run
            assert present is not None
            status = "failed" if present.failed else "ok"
            print(
                f"    {comparison.key.label()}: only {missing} missing "
                f"(have {present.setup.pixi_environment}, status={status})"
            )

    print()


def print_run_line(analysis: RunAnalysis, *, detail: str) -> None:
    print(
        f"  - {analysis.setup_label}\n"
        f"    {detail}\n"
        f"    run_id={analysis.run_id}, file={analysis.results_file}"
    )


def report_hardware(hardware: HardwareKey, runs: list[RunAnalysis]) -> None:
    successful = [run for run in runs if not run.failed]
    failed = [run for run in runs if run.failed]

    print("=" * 80)
    print(hardware.label())
    print(f"Runs: {len(runs)} total, {len(successful)} successful, {len(failed)} failed")
    print()

    if not successful:
        print("No successful runs for this hardware.")
        if failed:
            print("\nFailed setups:")
            for run in failed:
                print(f"  - {run.setup_label} ({run.results_file})")
        print()
        return

    fastest = min(successful, key=lambda run: run.best_duration_s or float("inf"))
    fastest_baseline = min(
        successful, key=lambda run: run.baseline_duration_s or float("inf")
    )
    best_peak_speedup = max(
        successful, key=lambda run: run.peak_speedup or float("-inf")
    )
    scalable = [
        run
        for run in successful
        if (run.peak_speedup or 0) > 1.05 and (run.peak_speedup_n_jobs or 0) > 1
    ]
    scalable_at_max = [
        run
        for run in successful
        if (run.speedup_at_max_n_jobs or 0) > 1.05 and (run.max_n_jobs or 0) > 1
    ]

    print("Most efficient (absolute speed)")
    print_run_line(
        fastest,
        detail=fmt_run_timings(fastest, include_peak=False, include_max=False),
    )
    if fastest.run_id != fastest_baseline.run_id:
        print_run_line(
            fastest_baseline,
            detail=(
                f"fastest single-thread baseline "
                f"{fmt_seconds(fastest_baseline.baseline_duration_s)}; "
                f"best {fmt_duration_at_n_jobs(fastest_baseline.best_duration_s, fastest_baseline.best_n_jobs)}"
            ),
        )
    print()

    print("Most efficient (scalability)")
    print_run_line(
        best_peak_speedup,
        detail=(
            f"peak speedup {fmt_speedup(best_peak_speedup.peak_speedup)} "
            f"({fmt_duration_at_n_jobs(best_peak_speedup.peak_duration_s, best_peak_speedup.peak_speedup_n_jobs)}); "
            f"{fmt_run_timings(best_peak_speedup, include_peak=False, include_max=False)}"
        ),
    )
    if scalable:
        best_peak_efficiency = max(
            scalable,
            key=lambda run: run.parallel_efficiency_at_peak or float("-inf"),
        )
        print_run_line(
            best_peak_efficiency,
            detail=(
                f"best peak parallel efficiency "
                f"{fmt_ratio(best_peak_efficiency.parallel_efficiency_at_peak)} "
                f"(speedup {fmt_speedup(best_peak_efficiency.peak_speedup)} "
                f"at {fmt_duration_at_n_jobs(best_peak_efficiency.peak_duration_s, best_peak_efficiency.peak_speedup_n_jobs)}); "
                f"{fmt_run_timings(best_peak_efficiency, include_peak=False, include_max=False)}"
            ),
        )
    if scalable_at_max:
        best_max_efficiency = max(
            scalable_at_max,
            key=lambda run: run.parallel_efficiency_at_max or float("-inf"),
        )
        print_run_line(
            best_max_efficiency,
            detail=(
                f"best max-core parallel efficiency "
                f"{fmt_ratio(best_max_efficiency.parallel_efficiency_at_max)} "
                f"(speedup {fmt_speedup(best_max_efficiency.speedup_at_max_n_jobs)} "
                f"at {fmt_duration_at_n_jobs(best_max_efficiency.max_duration_s, best_max_efficiency.max_n_jobs)}); "
                f"{fmt_run_timings(best_max_efficiency, include_peak=False, include_max=False)}"
            ),
        )
    print()

    print("Most problematic (lack of scalability)")
    problematic = sorted(
        successful,
        key=lambda run: (
            run.speedup_at_max_n_jobs if run.speedup_at_max_n_jobs is not None else 999,
            -(run.slowdown_at_max or 0),
            run.parallel_efficiency_at_max
            if run.parallel_efficiency_at_max is not None
            else 999,
        ),
    )

    shown = 0
    for run in problematic:
        if shown >= 5:
            break
        peak = run.peak_speedup or 0
        at_max = run.speedup_at_max_n_jobs or 0
        slowdown = run.slowdown_at_max or 1
        low_max_core_efficiency = (
            run.parallel_efficiency_at_max is not None
            and run.parallel_efficiency_at_max < 0.15
        )
        is_problematic = (
            at_max < 1.0
            or low_max_core_efficiency
            or slowdown >= 1.25
            or (peak > 1.05 and at_max < 0.75 * peak)
        )
        if not is_problematic and shown >= 3:
            continue
        shown += 1
        print_run_line(
            run,
            detail=(
                f"speedup at max n_jobs={run.max_n_jobs}: "
                f"{fmt_speedup(run.speedup_at_max_n_jobs)} "
                f"({fmt_duration_at_n_jobs(run.max_duration_s, run.max_n_jobs)}); "
                f"peak {fmt_speedup(run.peak_speedup)} "
                f"({fmt_duration_at_n_jobs(run.peak_duration_s, run.peak_speedup_n_jobs)}); "
                f"baseline {fmt_seconds(run.baseline_duration_s)}; "
                f"best {fmt_duration_at_n_jobs(run.best_duration_s, run.best_n_jobs)}; "
                f"slowdown at max {fmt_ratio(run.slowdown_at_max)}x baseline; "
                f"max-core efficiency {fmt_ratio(run.parallel_efficiency_at_max)}"
            ),
        )

    if shown == 0:
        print("  No clearly problematic setups detected.")
    print()

    report_gil_comparisons(runs)

    if failed:
        print("Failed setups (excluded from rankings)")
        for run in failed:
            print(f"  - {run.setup_label} ({run.results_file})")
        print()


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
        help="Emit machine-readable JSON instead of a text report.",
    )
    args = parser.parse_args(argv)

    if not args.results_dir.is_dir():
        print(f"Results directory not found: {args.results_dir}", file=sys.stderr)
        return 1

    records = load_results(args.results_dir)
    if not records:
        print(f"No JSON results found in {args.results_dir}", file=sys.stderr)
        return 1

    analyses = [analyze_record(record) for record in records]
    grouped = group_by_hardware(analyses)

    if args.json:
        payload = {}
        for hardware, runs in sorted(grouped.items(), key=lambda item: item[0].label()):
            payload[hardware.label()] = {
                "runs": [
                    analysis_to_dict(analysis)
                    for analysis in sorted(runs, key=lambda run: run.setup_label)
                ],
                "gil_comparisons": [
                    gil_comparison_to_dict(comparison)
                    for comparison in group_gil_comparisons(runs)
                ],
            }
        json.dump(payload, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        return 0

    print(f"Loaded {len(records)} result file(s) from {args.results_dir}\n")
    for hardware in sorted(grouped, key=lambda key: key.label()):
        report_hardware(hardware, grouped[hardware])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
