#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/lib/resources.py
# Created: 2026-09-19
# Version: v1.0.0
#
# Purpose:
# Collects runtime system-memory and GPU-memory usage for benchmark runs.
#
# Workflow:
# 1. Query Windows performance counters through PowerShell.
# 2. Calculate used physical system memory.
# 3. Collect dedicated GPU-memory usage for available GPU adapters.
# 4. Normalize resource values into GiB for benchmark integration.
#
# ----------------------------------------------------------------------

"""Runtime resource monitoring for local LLM benchmarks."""

from __future__ import annotations

import json
import subprocess
import threading
import time
from typing import Any


# =============================================================================
# Constants
# =============================================================================

BYTES_PER_GIB = 1024**3


# =============================================================================
# Shared helpers
# =============================================================================

def bytes_to_gib(value: int | float) -> float:
    """
    Convert a byte value to gibibytes.
    """

    return round(float(value) / BYTES_PER_GIB, 3)


def _run_powershell_json(command: str) -> Any:
    """
    Run a PowerShell command and parse its JSON output.

    Raises RuntimeError when PowerShell execution or JSON parsing fails.
    """

    completed = subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-NonInteractive",
            "-Command",
            command,
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    if completed.returncode != 0:
        error_message = completed.stderr.strip() or "Unknown PowerShell error."
        raise RuntimeError(
            f"Resource monitoring PowerShell command failed: {error_message}"
        )

    output = completed.stdout.strip()

    if not output:
        raise RuntimeError(
            "Resource monitoring PowerShell command returned no output."
        )

    try:
        return json.loads(output)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            "Resource monitoring PowerShell output was not valid JSON."
        ) from error


# =============================================================================
# System memory
# =============================================================================

def get_system_memory_usage() -> dict[str, float]:
    """
    Return total, available, and used physical system memory in GiB.
    """

    command = (
        "$os = Get-CimInstance Win32_OperatingSystem; "
        "[PSCustomObject]@{"
        "TotalBytes = [int64]$os.TotalVisibleMemorySize * 1KB; "
        "AvailableBytes = [int64]$os.FreePhysicalMemory * 1KB"
        "} | ConvertTo-Json -Compress"
    )

    data = _run_powershell_json(command)

    total_bytes = int(data["TotalBytes"])
    available_bytes = int(data["AvailableBytes"])
    used_bytes = total_bytes - available_bytes

    return {
        "total_gib": bytes_to_gib(total_bytes),
        "available_gib": bytes_to_gib(available_bytes),
        "used_gib": bytes_to_gib(used_bytes),
    }


# =============================================================================
# GPU memory
# =============================================================================

def get_gpu_memory_usage() -> list[dict[str, Any]]:
    """
    Return dedicated GPU-memory usage for every Windows GPU adapter instance.
    """

    command = (
        "$samples = "
        "(Get-Counter '\\GPU Adapter Memory(*)\\Dedicated Usage').CounterSamples; "
        "@($samples | ForEach-Object { "
        "[PSCustomObject]@{"
        "InstanceName = $_.InstanceName; "
        "DedicatedBytes = [int64]$_.CookedValue"
        "}"
        "}) | ConvertTo-Json -Compress"
    )

    data = _run_powershell_json(command)

    if isinstance(data, dict):
        data = [data]

    return [
        {
            "instance_name": item["InstanceName"],
            "dedicated_gib": bytes_to_gib(item["DedicatedBytes"]),
        }
        for item in data
    ]


# =============================================================================
# Combined snapshot
# =============================================================================

def collect_resource_snapshot() -> dict[str, Any]:
    """
    Collect one normalized system-memory and GPU-memory snapshot.
    """

    return {
        "system_memory": get_system_memory_usage(),
        "gpu_adapters": get_gpu_memory_usage(),
    }

# =============================================================================
# Runtime resource sampler
# =============================================================================


class ResourceSampler:
    """
    Sample system RAM and dedicated GPU memory during a benchmark run.

    The sampler records a baseline snapshot before the benchmark starts,
    periodically samples resource usage in a background thread, and records
    a final snapshot when the benchmark finishes.

    Peak values represent the highest observed usage during the sampling
    window. GPU peak usage is tracked independently for every adapter.
    """

    def __init__(self, interval_seconds: float = 0.25) -> None:
        """
        Initialize the resource sampler.

        Args:
            interval_seconds:
                Delay between background samples. The default 250 ms interval
                provides useful peak detection without excessive overhead.
        """

        if interval_seconds <= 0:
            raise ValueError("Sampling interval must be greater than zero.")

        self.interval_seconds = interval_seconds

        self.before: dict[str, Any] | None = None
        self.after: dict[str, Any] | None = None

        self.peak_system_memory_gib: float | None = None
        self.peak_gpu_memory_gib: dict[str, float] = {}

        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None
        self._error: str | None = None

    def _update_peaks(self, snapshot: dict[str, Any]) -> None:
        """
        Update peak RAM and GPU-memory values from one snapshot.
        """

        system_used_gib = snapshot["system_memory"]["used_gib"]

        if (
            self.peak_system_memory_gib is None
            or system_used_gib > self.peak_system_memory_gib
        ):
            self.peak_system_memory_gib = system_used_gib

        for adapter in snapshot["gpu_adapters"]:
            instance_name = adapter["instance_name"]
            dedicated_gib = adapter["dedicated_gib"]

            previous_peak = self.peak_gpu_memory_gib.get(instance_name, 0.0)

            if dedicated_gib > previous_peak:
                self.peak_gpu_memory_gib[instance_name] = dedicated_gib

    def _sampling_loop(self) -> None:
        """
        Collect resource snapshots until the sampler is stopped.
        """

        while not self._stop_event.wait(self.interval_seconds):
            try:
                snapshot = collect_resource_snapshot()
                self._update_peaks(snapshot)
            except Exception as error:
                self._error = str(error)
                return

    def start(self) -> None:
        """
        Capture the baseline snapshot and start background sampling.
        """

        if self._thread is not None and self._thread.is_alive():
            raise RuntimeError("Resource sampler is already running.")

        self._stop_event.clear()
        self._error = None

        self.before = collect_resource_snapshot()
        self.after = None

        self.peak_system_memory_gib = None
        self.peak_gpu_memory_gib = {}

        self._update_peaks(self.before)

        self._thread = threading.Thread(
            target=self._sampling_loop,
            name="benchmark-resource-sampler",
            daemon=True,
        )
        self._thread.start()

    def stop(self) -> dict[str, Any]:
        """
        Stop background sampling and return the complete resource summary.
        """

        if self.before is None:
            raise RuntimeError("Resource sampler has not been started.")

        self._stop_event.set()

        if self._thread is not None:
            self._thread.join()

        self.after = collect_resource_snapshot()
        self._update_peaks(self.after)

        return self.get_summary()

    def get_summary(self) -> dict[str, Any]:
        """
        Build a normalized summary of the collected resource measurements.
        """

        if self.before is None or self.after is None:
            raise RuntimeError(
                "Resource sampler summary is unavailable before stop()."
            )

        before_system = self.before["system_memory"]["used_gib"]
        after_system = self.after["system_memory"]["used_gib"]

        system_peak = self.peak_system_memory_gib
        system_peak_delta = (
            round(system_peak - before_system, 3)
            if system_peak is not None
            else None
        )

        before_gpu = {
            adapter["instance_name"]: adapter["dedicated_gib"]
            for adapter in self.before["gpu_adapters"]
        }

        after_gpu = {
            adapter["instance_name"]: adapter["dedicated_gib"]
            for adapter in self.after["gpu_adapters"]
        }

        gpu_adapters: list[dict[str, Any]] = []

        adapter_names = sorted(
            set(before_gpu)
            | set(after_gpu)
            | set(self.peak_gpu_memory_gib)
        )

        for instance_name in adapter_names:
            before_gib = before_gpu.get(instance_name, 0.0)
            after_gib = after_gpu.get(instance_name, 0.0)
            peak_gib = self.peak_gpu_memory_gib.get(
                instance_name,
                max(before_gib, after_gib),
            )

            gpu_adapters.append(
                {
                    "instance_name": instance_name,
                    "before_gib": before_gib,
                    "peak_gib": peak_gib,
                    "after_gib": after_gib,
                    "peak_delta_gib": round(
                        peak_gib - before_gib,
                        3,
                    ),
                }
            )

        # Prefer the adapter whose dedicated VRAM usage increased most during
        # the run. During warm runs the model may already be fully resident in
        # VRAM, producing no measurable delta; in that case, fall back to the
        # adapter with the highest absolute dedicated-memory usage.

        inference_gpu = None

        if gpu_adapters:
            largest_delta_adapter = max(
                gpu_adapters,
                key=lambda adapter: adapter["peak_delta_gib"],
            )

            if largest_delta_adapter["peak_delta_gib"] > 0:
                inference_gpu = largest_delta_adapter
            else:
                largest_usage_adapter = max(
                    gpu_adapters,
                    key=lambda adapter: adapter["peak_gib"],
                )

                if largest_usage_adapter["peak_gib"] > 0:
                    inference_gpu = largest_usage_adapter

        return {
            "sampling_interval_seconds": self.interval_seconds,
            "system_memory": {
                "before_gib": before_system,
                "peak_gib": system_peak,
                "after_gib": after_system,
                "peak_delta_gib": system_peak_delta,
            },
            "inference_gpu": inference_gpu,
            "gpu_adapters": gpu_adapters,
            "sampling_error": self._error,
        }
