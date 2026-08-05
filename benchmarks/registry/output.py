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
# Version: v0.3.0
#
# Purpose:
# Compare persistent registry entries, installed Ollama models,
# and automatically detected benchmark results.
#
# Workflow:
# 1. Index registry and installed models by name.
# 2. Calculate installed and benchmark status.
# 3. Identify missing and unregistered models.
# 4. Print a complete terminal report.
#
# ----------------------------------------------------------------------

"""Terminal output for the local LLM model registry."""

from __future__ import annotations

from typing import Any


# =============================================================================
# Shared output helpers
# =============================================================================

def _sort_by_name(
    models: list[dict[str, Any]],
    *,
    field: str,
) -> list[dict[str, Any]]:
    """
    Sort model records by a selected string field.
    """

    return sorted(
        models,
        key=lambda model: str(model[field]).casefold(),
    )


def _status_label(
    *,
    installed: bool,
    benchmarked: bool,
) -> str:
    """
    Build a concise installed and benchmark status label.
    """

    installation = "installed" if installed else "not installed"
    benchmark = "benchmarked" if benchmarked else "waiting for benchmark"

    return f"{installation}, {benchmark}"


def _print_registry_group(
    title: str,
    models: list[dict[str, Any]],
    *,
    installed_names: set[str],
    benchmarked_names: set[str],
    marker: str,
) -> None:
    """
    Print one group of persistent registry entries.
    """

    print(title)
    print("-" * len(title))

    if not models:
        print("None")
        print()
        return

    for model in _sort_by_name(models, field="display_name"):
        name = model["name"]

        print(
            f"{marker} {model['display_name']} "
            f"({name}, family={model['family']}, "
            f"{_status_label(installed=name in installed_names, benchmarked=name in benchmarked_names)})"
        )

    print()


def _print_installed_group(
    title: str,
    models: list[dict[str, Any]],
) -> None:
    """
    Print installed Ollama models missing from the persistent registry.
    """

    print(title)
    print("-" * len(title))

    if not models:
        print("None")
        print()
        return

    for model in _sort_by_name(models, field="name"):
        print(
            f"[?] {model['name']} "
            f"(id={model['id']}, size={model['size']})"
        )

    print()


# =============================================================================
# Complete registry comparison
# =============================================================================

def print_registry_summary(
    *,
    registry: dict[str, Any],
    installed_models: list[dict[str, Any]],
    benchmarked_models: set[str],
) -> None:
    """
    Print the complete registry, installation, and benchmark status report.
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

    registered_and_installed = [
        registered_by_name[name]
        for name in registered_names & installed_names
    ]

    registered_not_installed = [
        registered_by_name[name]
        for name in registered_names - installed_names
    ]

    installed_not_registered = [
        installed_by_name[name]
        for name in installed_names - registered_names
    ]

    benchmarked_registered = [
        registered_by_name[name]
        for name in registered_names & benchmarked_models
    ]

    waiting_for_benchmark = [
        registered_by_name[name]
        for name in registered_names - benchmarked_models
    ]

    print("Local LLM Model Registry")
    print("========================")
    print()
    print(f"Schema version: {registry['schema_version']}")
    print(f"Registered models: {len(registered_models)}")
    print(f"Installed Ollama models: {len(installed_models)}")
    print(f"Registered and installed: {len(registered_and_installed)}")
    print(f"Registered but not installed: {len(registered_not_installed)}")
    print(f"Installed but not registered: {len(installed_not_registered)}")
    print(f"Benchmarked registry entries: {len(benchmarked_registered)}")
    print(f"Waiting for benchmark: {len(waiting_for_benchmark)}")
    print()

    _print_registry_group(
        "Registered and installed",
        registered_and_installed,
        installed_names=installed_names,
        benchmarked_names=benchmarked_models,
        marker="[x]",
    )

    _print_registry_group(
        "Registered but not installed",
        registered_not_installed,
        installed_names=installed_names,
        benchmarked_names=benchmarked_models,
        marker="[!]",
    )

    _print_installed_group(
        "Installed but not registered",
        installed_not_registered,
    )

    _print_registry_group(
        "Waiting for benchmark",
        waiting_for_benchmark,
        installed_names=installed_names,
        benchmarked_names=benchmarked_models,
        marker="[ ]",
    )
