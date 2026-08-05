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
# Version: v0.3.0
#
# Purpose:
# Detect which registered model names have completed benchmark
# master summaries in the local benchmark results directory.
#
# Workflow:
# 1. Scan benchmark result directories.
# 2. Read each master-summary JSON file.
# 3. Extract and normalize model names.
# 4. Return the set of benchmarked model identifiers.
#
# ----------------------------------------------------------------------

"""Detect benchmarked model names from result summary files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


# =============================================================================
# Benchmark result location
# =============================================================================

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"


# =============================================================================
# Master summary discovery
# =============================================================================

def find_master_summary_paths() -> list[Path]:
    """
    Return all all-prompts master-summary JSON files.
    """

    if not RESULTS_DIR.exists():
        return []

    return sorted(
        RESULTS_DIR.rglob("*_master-summary.json")
    )


def _read_summary_model(path: Path) -> str:
    """
    Read and validate the model identifier from one master summary.
    """

    try:
        data: Any = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid benchmark summary JSON: {path}"
        ) from error

    if not isinstance(data, dict):
        raise ValueError(
            f"Benchmark summary root must be an object: {path}"
        )

    model_name = data.get("model")

    if not isinstance(model_name, str) or not model_name.strip():
        raise ValueError(
            f"Benchmark summary missing valid model name: {path}"
        )

    return model_name.strip()


# =============================================================================
# Benchmarked model detection
# =============================================================================

def detect_benchmarked_models() -> set[str]:
    """
    Return model identifiers with at least one master summary.
    """

    return {
        _read_summary_model(path)
        for path in find_master_summary_paths()
    }
