#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/lib/api.py
# Created: 2026-08-05
# Version: v1.0.0
#
# Purpose:
# Provides HTTP communication with the local Ollama API for model
# generation, process detection, version lookup, and model metadata.
#
# Workflow:
# 1. Build Ollama endpoint URLs.
# 2. Send JSON HTTP requests.
# 3. Detect whether a model is already loaded.
# 4. Request benchmark generation and model metadata.
#
# ----------------------------------------------------------------------

"""Ollama API communication helpers."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

# =============================================================================
# Default Ollama endpoint
# =============================================================================

DEFAULT_API_URL = "http://localhost:11434/api/generate"


# =============================================================================
# Generic JSON request helper
# =============================================================================

def _request_json(
    *,
    url: str,
    timeout: int,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Send an HTTP request and return the decoded JSON object.

    HTTP and connection errors are converted into readable RuntimeError
    exceptions for the command-line application.
    """

    data = None
    headers: dict[str, str] = {}

    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(
        url,
        data=data,
        headers=headers,
        method=method,
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            response_data = response.read().decode("utf-8")

    except urllib.error.HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")

        raise RuntimeError(
            f"Ollama returned HTTP {error.code}: {details}"
        ) from error

    except urllib.error.URLError as error:
        raise RuntimeError(
            f"Could not connect to Ollama at {url}."
        ) from error

    return json.loads(response_data)


# =============================================================================
# Ollama endpoint construction
# =============================================================================

def _build_api_url(generate_api_url: str, endpoint: str) -> str:
    """
    Build another Ollama API endpoint from the configured generate endpoint.
    """

    suffix = "/api/generate"

    if generate_api_url.endswith(suffix):
        base_url = generate_api_url[: -len(suffix)]
        return f"{base_url}/api/{endpoint}"

    return generate_api_url.rstrip("/") + f"/../{endpoint}"


def build_ps_url(generate_api_url: str) -> str:
    """
    Build the Ollama process-list endpoint.
    """

    return _build_api_url(generate_api_url, "ps")


# =============================================================================
# Ollama environment and model metadata
# =============================================================================

def get_ollama_version(
    *,
    generate_api_url: str,
    timeout: int,
) -> dict[str, Any]:
    """
    Return Ollama server version information.
    """

    return _request_json(
        url=_build_api_url(generate_api_url, "version"),
        timeout=timeout,
    )


def get_model_details(
    *,
    generate_api_url: str,
    model: str,
    timeout: int,
) -> dict[str, Any]:
    """
    Return detailed metadata for an installed Ollama model.
    """

    return _request_json(
        url=_build_api_url(generate_api_url, "show"),
        timeout=timeout,
        method="POST",
        payload={"model": model},
    )


# =============================================================================
# Cold and warm run detection
# =============================================================================

def detect_run_type(
    *,
    generate_api_url: str,
    model: str,
    timeout: int,
) -> str:
    """
    Return "warm" when the selected model is already loaded, otherwise "cold".
    """

    response = _request_json(
        url=build_ps_url(generate_api_url),
        timeout=timeout,
    )

    loaded_models = response.get("models", [])

    for loaded_model in loaded_models:
        loaded_name = loaded_model.get("name") or loaded_model.get("model")

        if loaded_name == model:
            return "warm"

    return "cold"


# =============================================================================
# Benchmark generation request
# =============================================================================

def call_ollama(
    *,
    api_url: str,
    model: str,
    prompt: str,
    think_enabled: bool,
    timeout: int,
) -> dict[str, Any]:
    """
    Send one non-streaming benchmark generation request to Ollama.
    """

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": think_enabled,
        "options": {
            "temperature": 0,
            "seed": 42,
            "num_ctx": 4096,
        },
    }

    result = _request_json(
        url=api_url,
        timeout=timeout,
        method="POST",
        payload=payload,
    )

    if not result.get("done", False):
        raise RuntimeError("Ollama did not return a completed response.")

    return result
