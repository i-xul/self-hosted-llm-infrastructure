#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/lib/utils.py
# Created: 2026-08-05
# Version: v1.0.0
#
# Purpose:
# Defines shared benchmark filesystem paths and safe path helpers.
#
# Workflow:
# 1. Resolve benchmark, prompt, and result directories.
# 2. Convert model names into filesystem-safe directory names.
#
# ----------------------------------------------------------------------

"""Shared filesystem utilities and paths."""

from __future__ import annotations

import re
from pathlib import Path


# =============================================================================
# Benchmark filesystem paths
# =============================================================================

BENCHMARKS_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = BENCHMARKS_DIR / "prompts"
RESULTS_DIR = BENCHMARKS_DIR / "results"


# =============================================================================
# Filesystem-safe name conversion
# =============================================================================

def safe_path_component(value: str) -> str:
    """
    Convert an arbitrary value into a filesystem-safe path component.
    """

    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value)
    return cleaned.strip("-").lower() or "unknown"
