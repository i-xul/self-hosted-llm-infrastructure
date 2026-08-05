#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/registry/output.py
# Created: 2026-08-06
# Version: v0.2.0
#
# Purpose:
# Compare registered and installed model records and print a
# human-readable terminal status report.
#
# Workflow:
# 1. Index registered and installed models by name.
# 2. Identify matched, missing, and unregistered models.
# 3. Print counts and detailed model groups.
#
# ----------------------------------------------------------------------

"""Terminal output formatting for the local LLM model registry."""

from __future__ import annotations

from typing import Any


# =============================================================================
# Shared sorting and formatting
# =============================================================================

def _sort_by_name(
    models: list[dict[str, Any]],
    *,
    field: str = "name",
) -> list[dict[str, Any]]:
    """
    Sort model records by a selected string field.
    """

    return sorted(
        models,
        key=lambda model: str(model[field]).casefold(),
    )


def _print_registered_group(
    title: str,
    models: list[dict[str, Any]],
    *,
    marker: str,
) -> None:
    """
    Print one group of version-controlled registry entries.
    """

    print(title)
    print("-" * len(title))

    if not models:
        print("None")
        print()
        return

    for model in _sort_by_name(models, field="display_name"):
        benchmark_status = (
            "benchmarked"
            if model["benchmarked"]
            else "waiting for benchmark"
        )

        print(
            f"{marker} {model['display_name']} "
            f"({model['name']}, family={model['family']}, "
            f"{benchmark_status})"
        )

    print()


def _print_installed_group(
    title: str,
    models: list[dict[str, Any]],
    *,
    marker: str,
) -> None:
    """
    Print one group of installed Ollama model records.
    """

    print(title)
    print("-" * len(title))

    if not models:
        print("None")
        print()
        return

    for model in _sort_by_name(models):
        print(
            f"{marker} {model['name']} "
            f"(id={model['id']}, size={model['size']})"
        )

    print()


# =============================================================================
# Registry and installed-model comparison
# =============================================================================

def print_registry_summary(
    *,
    registry: dict[str, Any],
    installed_models: list[dict[str, Any]],
) -> None:
    """
    Compare registry and Ollama data, then print the complete status report.
    """

    registered_models = registry["models"]

    registered_by_name = {
        model["name"]: model
        for model in registered_models
    }

    installed_by_name = {
        model["name"]: model
        for model in installed_models
    }

    registered_names = set(registered_by_name)
    installed_names = set(installed_by_name)

    matched = [
        registered_by_name[name]
        for name in registered_names & installed_names
    ]

    missing_from_ollama = [
        registered_by_name[name]
        for name in registered_names - installed_names
    ]

    unregistered_installed = [
        installed_by_name[name]
        for name in installed_names - registered_names
    ]

    benchmarked = [
        model
        for model in registered_models
        if model["benchmarked"]
    ]

    pending = [
        model
        for model in registered_models
        if not model["benchmarked"]
    ]

    print("Local LLM Model Registry")
    print("========================")
    print()
    print(f"Schema version: {registry['schema_version']}")
    print(f"Registered models: {len(registered_models)}")
    print(f"Installed Ollama models: {len(installed_models)}")
    print(f"Registered and installed: {len(matched)}")
    print(f"Registered but not installed: {len(missing_from_ollama)}")
    print(f"Installed but not registered: {len(unregistered_installed)}")
    print(f"Benchmarked registry entries: {len(benchmarked)}")
    print(f"Waiting for benchmark: {len(pending)}")
    print()

    _print_registered_group(
        "Registered and installed",
        matched,
        marker="[x]",
    )

    _print_registered_group(
        "Registered but not installed",
        missing_from_ollama,
        marker="[!]",
    )

    _print_installed_group(
        "Installed but not registered",
        unregistered_installed,
        marker="[?]",
    )

    _print_registered_group(
        "Waiting for benchmark",
        pending,
        marker="[ ]",
    )
