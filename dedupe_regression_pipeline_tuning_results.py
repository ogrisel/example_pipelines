#!/usr/bin/env python3
"""Remove duplicate benchmark JSON files, keeping the latest per hardware/setup."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from analyze_regression_pipeline_tuning_results import (
    RESULTS_DIR,
    dedupe_records,
    load_results,
    setup_hardware_key,
)


def find_duplicates(results_dir: Path) -> tuple[list[Path], list[Path]]:
    records = load_results(results_dir)
    if not records:
        return [], []

    kept_records, _ = dedupe_records(records)
    kept_files = {record["results_file"] for record in kept_records}

    to_keep: list[Path] = []
    to_delete: list[Path] = []
    for record in records:
        path = results_dir / record["results_file"]
        if record["results_file"] in kept_files:
            to_keep.append(path)
            kept_files.discard(record["results_file"])
        else:
            to_delete.append(path)

    return sorted(to_keep), sorted(to_delete)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Delete duplicate regression pipeline tuning result files, "
            "keeping the most recent file for each hardware/setup combination."
        )
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=RESULTS_DIR,
        help=f"Directory containing benchmark JSON files (default: {RESULTS_DIR})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print files that would be deleted without removing them.",
    )
    args = parser.parse_args(argv)

    if not args.results_dir.is_dir():
        print(f"Results directory not found: {args.results_dir}", file=sys.stderr)
        return 1

    to_keep, to_delete = find_duplicates(args.results_dir)
    if not to_delete:
        print(f"No duplicate result files found in {args.results_dir}.")
        print(f"Kept {len(to_keep)} file(s).")
        return 0

    print(
        f"Found {len(to_delete)} duplicate file(s) in {args.results_dir} "
        f"(keeping {len(to_keep)} latest per hardware/setup)."
    )
    for path in to_delete:
        record_key = path.name
        try:
            with path.open(encoding="utf-8") as file:
                record = json.load(file)
            key = setup_hardware_key(record)
            hardware = key[0].label()
            setup = key[1].label()
            timestamp = record.get("completed_at") or record.get("recorded_at") or "unknown"
            print(f"  delete {path.name}  ({hardware}; {setup}; {timestamp})")
        except (OSError, json.JSONDecodeError, KeyError):
            print(f"  delete {path.name}")

    if args.dry_run:
        print("\nDry run: no files were deleted.")
        return 0

    for path in to_delete:
        path.unlink()

    print(f"\nDeleted {len(to_delete)} duplicate file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
