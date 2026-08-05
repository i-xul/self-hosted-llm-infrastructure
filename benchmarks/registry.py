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
# Version: v0.3.0
#
# Purpose:
# Compare the model registry, installed Ollama models, and
# automatically detected benchmark result status.
#
# Workflow:
# 1. Load and validate models.json.
# 2. Read installed models from ollama list.
# 3. Detect benchmarked models from result summaries.
# 4. Print a combined registry status report.
#
# ----------------------------------------------------------------------

"""Command-line entry point for the local LLM model registry."""

from registry.benchmarks import detect_benchmarked_models
from registry.loader import load_registry
from registry.ollama import load_installed_models
from registry.output import print_registry_summary


# =============================================================================
# Main registry workflow
# =============================================================================

def main() -> int:
    """
    Load registry, Ollama, and benchmark result data.

    Returns:
        int: Process exit code. Zero indicates success.
    """

    try:
        registry = load_registry()
        installed_models = load_installed_models()
        benchmarked_models = detect_benchmarked_models()

        print_registry_summary(
            registry=registry,
            installed_models=installed_models,
            benchmarked_models=benchmarked_models,
        )

        return 0

    except (FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"Registry error: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
