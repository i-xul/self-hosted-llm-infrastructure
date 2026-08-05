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
# Version: v0.2.0
#
# Purpose:
# Compare the version-controlled model registry with models
# currently installed in the local Ollama environment.
#
# Workflow:
# 1. Load and validate models.json.
# 2. Read installed models from ollama list.
# 3. Compare registered and installed model names.
# 4. Print a human-readable registry status report.
#
# ----------------------------------------------------------------------

"""Command-line entry point for the local LLM model registry."""

from registry.loader import load_registry
from registry.ollama import load_installed_models
from registry.output import print_registry_summary


# =============================================================================
# Main registry workflow
# =============================================================================

def main() -> int:
    """
    Load registry and Ollama data, then print their current relationship.

    Returns:
        int: Process exit code. Zero indicates success.
    """

    try:
        registry = load_registry()
        installed_models = load_installed_models()

        print_registry_summary(
            registry=registry,
            installed_models=installed_models,
        )

        return 0

    except (FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"Registry error: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
