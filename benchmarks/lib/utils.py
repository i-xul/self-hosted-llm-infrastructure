"""Shared filesystem utilities and paths."""

from __future__ import annotations

import re
from pathlib import Path

BENCHMARKS_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = BENCHMARKS_DIR / "prompts"
RESULTS_DIR = BENCHMARKS_DIR / "results"


def safe_path_component(value: str) -> str:
    """Convert a value into a filesystem-safe path component."""
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value)
    return cleaned.strip("-").lower() or "unknown"
