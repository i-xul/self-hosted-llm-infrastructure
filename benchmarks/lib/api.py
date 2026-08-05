"""Ollama API communication."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

DEFAULT_API_URL = "http://localhost:11434/api/generate"


def _request_json(
    *,
    url: str,
    timeout: int,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Send an HTTP request and parse the JSON response."""
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
        raise RuntimeError(f"Could not connect to Ollama at {url}.") from error

    return json.loads(response_data)


def build_ps_url(generate_api_url: str) -> str:
    """Build the Ollama process-list endpoint from the generate endpoint."""
    suffix = "/api/generate"

    if generate_api_url.endswith(suffix):
        return generate_api_url[: -len(suffix)] + "/api/ps"

    return generate_api_url.rstrip("/") + "/../ps"


def detect_run_type(
    *,
    generate_api_url: str,
    model: str,
    timeout: int,
) -> str:
    """Return cold or warm depending on whether the model is loaded."""
    ps_url = build_ps_url(generate_api_url)
    response = _request_json(url=ps_url, timeout=timeout)
    loaded_models = response.get("models", [])

    for loaded_model in loaded_models:
        loaded_name = loaded_model.get("name") or loaded_model.get("model")
        if loaded_name == model:
            return "warm"

    return "cold"


def call_ollama(
    *,
    api_url: str,
    model: str,
    prompt: str,
    think_enabled: bool,
    timeout: int,
) -> dict[str, Any]:
    """Send a non-streaming generation request to the Ollama API."""
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
