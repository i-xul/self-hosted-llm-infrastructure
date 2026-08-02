# Installation

This document records the installation process and configuration used to build the current self-hosted LLM infrastructure.

It is not intended to be a generic Ollama installation guide. Instead, it documents the exact steps, configuration decisions and verification performed during this project.

---

# Host System

| Component        | Value                 |
| ---------------- | --------------------- |
| Operating System | Windows 11            |
| Inference Engine | Ollama                |
| Initial Model    | Qwen3 8B              |
| GPU              | AMD Radeon RX 7800 XT |
| CPU              | AMD Ryzen 9 7900X     |
| Memory           | 32 GB                 |

---

# Local AI Directory

A dedicated directory was created to keep AI-related data separate from the operating system.

```text
F:\AI\
├── benchmarks
├── datasets
├── docs
├── models
└── screenshots
```

Language models are intentionally stored outside the Git repository.

---

# Model Storage

The default Ollama model directory was overridden using the Windows user environment variable:

```text
OLLAMA_MODELS=F:\AI\models
```

This allows large model files to be stored on a dedicated drive instead of the system drive.

---

# Ollama Installation

Ollama was installed using the official Windows installer.

After installation, the following checks were performed.

## Version

```powershell
ollama --version
```

Result:

```text
0.32.3
```

---

## Verify Local API

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
```

The API responded successfully, confirming that the local inference service was running correctly.

---

# Initial Model

The first language model used in this project was:

```text
Qwen3 8B
```

Downloaded using:

```powershell
ollama run qwen3:8b
```

Ollama automatically downloaded the model, stored it in the configured model directory and started an interactive session.

---

# GPU Verification

GPU acceleration was verified using:

```powershell
ollama ps
```

Result:

```text
PROCESSOR
100% GPU
```

This confirmed that inference was performed entirely on the AMD Radeon RX 7800 XT.

---

# Stopping the Model

After testing, GPU memory was released using:

```powershell
ollama stop qwen3:8b
```

Verification:

```powershell
ollama ps
```

The command returned no active models, confirming that the model had been unloaded successfully.

---

# Current Status

The current environment provides:

* Local language model inference
* GPU acceleration
* Local REST API
* Dedicated model storage
* Documented installation process

The next development stage is to benchmark language models and expand the infrastructure beyond a single inference engine.
