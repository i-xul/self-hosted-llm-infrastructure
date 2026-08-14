#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/registry.py
# Created: 2026-08-06
# Version: v0.5.0
#
# Purpose:
# Compare persistent registry metadata, installed Ollama models,
# latest benchmark metadata, and manual quality scores.
#
# Workflow:
# 1. Load and validate models.json.
# 2. Read installed models from ollama list.
# 3. Load latest benchmark metadata for each model.
# 4. Load manual quality scores from quality_scores.json.
# 5. Print a combined registry status report.
#
# ----------------------------------------------------------------------

"""Command-line entry point for the local LLM model registry."""

from leaderboard.quality import load_quality_scores
from registry.benchmarks import load_latest_benchmark_metadata
from registry.loader import load_registry
from registry.ollama import load_installed_models
from registry.output import print_registry_summary


# =============================================================================
# Main registry workflow
# =============================================================================

def main() -> int:
    """Load registry, Ollama, benchmark, and quality metadata."""

    try:
        registry = load_registry()
        installed_models = load_installed_models()
        benchmark_metadata = load_latest_benchmark_metadata()
        quality_data = load_quality_scores()

        print_registry_summary(
            registry=registry,
            installed_models=installed_models,
            benchmark_metadata=benchmark_metadata,
            quality_data=quality_data,
        )

        return 0

    except (FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"Registry error: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
