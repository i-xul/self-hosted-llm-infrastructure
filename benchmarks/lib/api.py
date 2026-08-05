"""Ollama API communication."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

DEFAULT_API_URL = "http://localhost:11434/api/generate"


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

    request = urllib.request.Request(
        api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
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
            "Could not connect to Ollama. Confirm that Ollama is running at "
            f"{api_url}."
        ) from error

    result = json.loads(response_data)

    if not result.get("done", False):
        raise RuntimeError("Ollama did not return a completed response.")

    return result
