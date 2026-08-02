# Hardware

This document describes the hardware used to build and evaluate the self-hosted LLM infrastructure.

Only components that have a direct impact on AI inference, benchmarking or system architecture are documented.

---

# Primary Compute Node

The current inference server is a Windows 11 workstation.

| Component        | Specification         |
| ---------------- | --------------------- |
| Operating System | Windows 11            |
| CPU              | AMD Ryzen 9 7900X     |
| System Memory    | 32 GB DDR5            |
| GPU              | AMD Radeon RX 7800 XT |
| Video Memory     | 16 GB VRAM            |

---

# Storage

The project separates operating system files from AI assets.

| Purpose          | Location           |
| ---------------- | ------------------ |
| Operating System | System drive       |
| AI Models        | `F:\AI\models`     |
| Documentation    | Git repository     |
| Future Datasets  | `F:\AI\datasets`   |
| Benchmarks       | `F:\AI\benchmarks` |

Large AI models are intentionally stored outside the Git repository.

---

# Compute Strategy

The Windows workstation acts as the dedicated AI inference node.

Current responsibilities include:

* Local model inference
* GPU acceleration
* Local REST API
* Language model benchmarking

Future versions of the project may separate the user interface from the compute node.

---

# GPU

The AMD Radeon RX 7800 XT is the primary accelerator for language model inference.

The initial Qwen3 8B test successfully verified:

* Full GPU inference
* Stable model loading
* Local execution
* Successful model unloading

Future benchmarks will compare GPU utilization across multiple models and inference engines.

---

# CPU

The Ryzen 9 7900X provides:

* Model loading
* Operating system tasks
* API handling
* Future supporting services

The long-term objective is to keep language model inference primarily on the GPU whenever supported.

---

# Memory

Current system memory:

```text id="70hmyr"
32 GB
```

Future benchmarks will monitor:

* System RAM usage
* VRAM usage
* Memory requirements for different models
* Effects of larger context windows

---

# Planned Secondary Systems

The current architecture focuses on a single Windows inference node.

Future development may introduce additional systems with separate responsibilities.

Possible additions include:

* Ubuntu workstation

  * Web interface
  * Monitoring
  * Reverse proxy
  * AI management services

* Raspberry Pi 5

  * Lightweight AI gateway
  * Monitoring
  * Remote management
  * Experimental deployments

These systems are intentionally kept separate from the primary compute node.

---

# Design Philosophy

The hardware architecture follows three main principles:

1. Keep inference on the most powerful hardware.
2. Separate compute resources from user-facing services whenever practical.
3. Allow future expansion without redesigning the infrastructure.

This approach keeps the project modular, scalable and suitable for long-term experimentation.
