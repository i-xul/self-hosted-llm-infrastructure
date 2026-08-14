#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/registry/benchmarks.py
# Created: 2026-08-06
# Version: v0.4.0
#
# Purpose:
# Detect benchmarked models and read useful metadata from each model's
# latest all-prompts master summary.
#
# Workflow:
# 1. Scan benchmark result directories.
# 2. Read and validate master-summary JSON files.
# 3. Select the latest summary for each model.
# 4. Extract benchmark date, think mode, repeat count, and average speed.
# 5. Return benchmark status or detailed metadata to the registry.
#
# ----------------------------------------------------------------------

"""Read benchmark status and metadata from master-summary result files."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"


def find_master_summary_paths() -> list[Path]:
    """Return all all-prompts master-summary JSON files."""
    if not RESULTS_DIR.exists():
        return []
    return sorted(RESULTS_DIR.rglob("*_master-summary.json"))


def _read_summary(path: Path) -> dict[str, Any]:
    """Read and validate one benchmark master-summary JSON object."""
    try:
        data: Any = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid benchmark summary JSON: {path}") from error

    if not isinstance(data, dict):
        raise ValueError(f"Benchmark summary root must be an object: {path}")

    model_name = data.get("model")

    if not isinstance(model_name, str) or not model_name.strip():
        raise ValueError(f"Benchmark summary missing valid model name: {path}")

    return data


def _parse_summary_timestamp(data: dict[str, Any]) -> datetime:
    """Parse summary timestamp for latest-run comparison."""
    timestamp = data.get("summary_timestamp")

    if not isinstance(timestamp, str) or not timestamp.strip():
        return datetime.min

    try:
        return datetime.fromisoformat(timestamp)
    except ValueError:
        return datetime.min


def _extract_repeat_count(data: dict[str, Any]) -> int | None:
    """Infer the benchmark --repeat value from per-prompt run counts."""
    prompts = data.get("prompts")

    if not isinstance(prompts, list) or not prompts:
        return None

    run_counts = {
        prompt.get("run_count")
        for prompt in prompts
        if isinstance(prompt, dict)
        and isinstance(prompt.get("run_count"), int)
    }

    if len(run_counts) == 1:
        return run_counts.pop()

    return None


def _extract_benchmark_date(data: dict[str, Any]) -> str:
    """Return benchmark summary date in YYYY-MM-DD form."""
    timestamp = data.get("summary_timestamp")

    if not isinstance(timestamp, str) or not timestamp.strip():
        return "unknown"

    try:
        return datetime.fromisoformat(timestamp).date().isoformat()
    except ValueError:
        return "unknown"


def _build_benchmark_metadata(
    data: dict[str, Any],
    path: Path,
) -> dict[str, Any]:
    """Normalize registry-relevant metadata from one master summary."""
    statistics = data.get("statistics", {})
    if not isinstance(statistics, dict):
        statistics = {}

    speed_data = statistics.get("tokens_per_second", {})
    if not isinstance(speed_data, dict):
        speed_data = {}

    think_enabled = data.get("think_enabled")
    think_mode = (
        "on"
        if think_enabled is True
        else "off"
        if think_enabled is False
        else "unknown"
    )

    return {
        "model": data["model"].strip(),
        "latest_run": _extract_benchmark_date(data),
        "think": think_mode,
        "repeat": _extract_repeat_count(data),
        "average_tokens_per_second": speed_data.get("mean"),
        "source_path": str(path),
    }


def load_latest_benchmark_metadata() -> dict[str, dict[str, Any]]:
    """Return latest benchmark metadata indexed by model identifier."""
    latest: dict[str, tuple[datetime, dict[str, Any]]] = {}

    for path in find_master_summary_paths():
        data = _read_summary(path)
        model_name = data["model"].strip()
        timestamp = _parse_summary_timestamp(data)
        metadata = _build_benchmark_metadata(data, path)

        current = latest.get(model_name)

        if current is None or timestamp > current[0]:
            latest[model_name] = (timestamp, metadata)

    return {
        model_name: metadata
        for model_name, (_, metadata) in latest.items()
    }


def detect_benchmarked_models() -> set[str]:
    """Return model identifiers with at least one master summary."""
    return set(load_latest_benchmark_metadata())
