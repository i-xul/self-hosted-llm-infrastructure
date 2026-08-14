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
# Version: v0.5.0
#
# Purpose:
# Compare registry entries, installed Ollama models, latest benchmark
# metadata, and manual quality scores in one terminal report.
#
# Workflow:
# 1. Index registry and installed models by name.
# 2. Calculate installation and benchmark status.
# 3. Attach latest benchmark metadata.
# 4. Attach manual overall quality scores.
# 5. Print model groups and detailed metadata.
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
    """Sort model records by a selected string field."""

    return sorted(
        models,
        key=lambda model: str(model[field]).casefold(),
    )


def _format_speed(value: Any) -> str:
    """Format an optional average generation speed."""

    if not isinstance(value, (int, float)):
        return "unknown"

    return f"{float(value):.2f} tok/s"


def _format_repeat(value: Any) -> str:
    """Format an optional repeat count."""

    return str(value) if isinstance(value, int) else "unknown"


def _format_quality(value: Any) -> str:
    """Format an optional manual overall quality score."""

    if not isinstance(value, (int, float)):
        return "not rated"

    return f"{float(value):.1f}/10"


def _print_benchmark_details(
    metadata: dict[str, Any] | None,
    quality_model: dict[str, Any] | None,
) -> None:
    """Print benchmark and quality metadata for one model."""

    if metadata is not None:
        print(f"    latest run : {metadata.get('latest_run', 'unknown')}")
        print(f"    think      : {metadata.get('think', 'unknown')}")
        print(f"    repeats    : {_format_repeat(metadata.get('repeat'))}")
        print(
            "    avg speed  : "
            f"{_format_speed(metadata.get('average_tokens_per_second'))}"
        )

    quality_score = None

    if quality_model is not None:
        quality_score = quality_model.get("overall_score")

    print(f"    quality    : {_format_quality(quality_score)}")


def _status_label(
    *,
    installed: bool,
    benchmarked: bool,
) -> str:
    """Build a concise installed and benchmark status label."""

    installation = "installed" if installed else "not installed"
    benchmark = "benchmarked" if benchmarked else "waiting for benchmark"

    return f"{installation}, {benchmark}"


def _print_registry_group(
    title: str,
    models: list[dict[str, Any]],
    *,
    installed_names: set[str],
    benchmark_metadata: dict[str, dict[str, Any]],
    quality_models: dict[str, dict[str, Any]],
    marker: str,
) -> None:
    """Print one group of persistent registry entries."""

    print(title)
    print("-" * len(title))

    if not models:
        print("None")
        print()
        return

    benchmarked_names = set(benchmark_metadata)

    for model in _sort_by_name(models, field="display_name"):
        name = model["name"]

        print(
            f"{marker} {model['display_name']} "
            f"({name}, family={model['family']}, "
            f"{_status_label(installed=name in installed_names, benchmarked=name in benchmarked_names)})"
        )

        _print_benchmark_details(
            benchmark_metadata.get(name),
            quality_models.get(name),
        )

    print()


def _print_installed_group(
    title: str,
    models: list[dict[str, Any]],
) -> None:
    """Print installed Ollama models missing from the persistent registry."""

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
    benchmark_metadata: dict[str, dict[str, Any]],
    quality_data: dict[str, Any],
) -> None:
    """Print the complete registry, benchmark, and quality status report."""

    registered_models = registry["models"]
    quality_models = quality_data.get("models", {})

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
    benchmarked_names = set(benchmark_metadata)

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
        for name in registered_names & benchmarked_names
    ]

    waiting_for_benchmark = [
        registered_by_name[name]
        for name in registered_names - benchmarked_names
    ]

    quality_rated = [
        name
        for name in registered_names
        if quality_models.get(name, {}).get("overall_score") is not None
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
    print(f"Quality-rated registry entries: {len(quality_rated)}")
    print(f"Waiting for benchmark: {len(waiting_for_benchmark)}")
    print()

    _print_registry_group(
        "Registered and installed",
        registered_and_installed,
        installed_names=installed_names,
        benchmark_metadata=benchmark_metadata,
        quality_models=quality_models,
        marker="[x]",
    )

    _print_registry_group(
        "Registered but not installed",
        registered_not_installed,
        installed_names=installed_names,
        benchmark_metadata=benchmark_metadata,
        quality_models=quality_models,
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
        benchmark_metadata=benchmark_metadata,
        quality_models=quality_models,
        marker="[ ]",
    )
