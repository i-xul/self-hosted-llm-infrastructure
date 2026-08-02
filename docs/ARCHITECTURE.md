# Architecture

This document describes the current and planned architecture of the self-hosted LLM infrastructure.

## Current Architecture

The current implementation uses a Windows 11 desktop computer as the local inference node.

```text
User
  │
  ▼
PowerShell / Ollama CLI
  │
  ▼
Ollama local API
  │
  ▼
Qwen3 8B
  │
  ▼
AMD Radeon RX 7800 XT
```

### Compute Node

The current compute node consists of:

* Windows 11
* AMD Ryzen 9 7900X
* 32 GB system memory
* AMD Radeon RX 7800 XT
* 16 GB VRAM
* Ollama as the inference engine
* Qwen3 8B as the initial test model

Model files are stored separately on the local HDD under:

```text
F:\AI\models
```

The model directory is configured through the Windows user environment variable:

```text
OLLAMA_MODELS=F:\AI\models
```

### Local Inference

Inference currently runs entirely on the Windows computer.

The initial Qwen3 8B test confirmed that the model was loaded with:

```text
100% GPU
```

This verifies that Ollama is using the AMD Radeon RX 7800 XT for model processing instead of relying entirely on CPU inference.

### Local API

Ollama provides a local HTTP API at:

```text
http://localhost:11434
```

At the current stage, the API is used only from the Windows host itself.

The API is not exposed to the public internet.

## Planned Architecture

The next major stage is to separate the inference layer from the user interface.

The Windows computer will remain the GPU-powered inference node, while a separate Linux system will host the web interface and supporting services.

```text
                     Private network
                LAN / Tailscale / Meshnet
                           │
                           ▼
              Ubuntu computer or Raspberry Pi 5
              ┌──────────────────────────────┐
              │ Open WebUI                   │
              │ Authentication               │
              │ Reverse proxy                │
              │ Monitoring                   │
              │ Future RAG services          │
              └──────────────┬───────────────┘
                             │
                             │ Restricted API access
                             ▼
              Windows 11 inference node
              ┌──────────────────────────────┐
              │ Ollama                       │
              │ Local LLM models             │
              │ AMD Radeon RX 7800 XT        │
              └──────────────────────────────┘
```

## Architectural Layers

The planned infrastructure is divided into separate layers.

### 1. Compute Layer

The compute layer performs model inference.

Current implementation:

* Windows 11
* Ollama
* AMD GPU acceleration
* Local language models

Future additions may include:

* llama.cpp
* Alternative inference engines
* Additional model formats
* Model-specific runtime configurations

### 2. Interface Layer

The interface layer provides access to the language models.

Planned components:

* Open WebUI
* Browser-based chat interface
* API clients
* Future integrations with local applications

The interface layer may run on an Ubuntu computer or Raspberry Pi 5.

### 3. Network Layer

The network layer connects clients and services without exposing the inference API directly to the public internet.

Planned access methods:

* Local area network
* Tailscale
* NordVPN Meshnet
* Restricted Windows Firewall rules

### 4. Data Layer

The data layer will contain local documents and metadata used by future AI services.

Possible components:

* Local document storage
* Embedding models
* Vector database
* Retrieval-Augmented Generation
* Homelab documentation
* Monitoring and inventory data

Private documents, prompts and generated data must remain outside the public Git repository.

### 5. Monitoring Layer

The monitoring layer will be added later to observe:

* Model status
* GPU utilization
* VRAM usage
* System memory usage
* Response latency
* Token generation speed
* API availability
* Error logs

## Security Boundaries

The architecture follows these initial security rules:

* Inference runs on local hardware.
* Models and prompts are not sent to external AI services.
* The Ollama API is not exposed directly to the public internet.
* Remote access must use a trusted private network path.
* Firewall access should be limited to explicitly approved hosts or networks.
* Secrets, private documents, model files and local logs must not be committed to Git.
* Administrative tools and model execution interfaces should remain separate where practical.

More detailed security decisions will be documented in `SECURITY.md`.

## Design Goals

The architecture is designed around the following goals:

* Local-first operation
* Privacy
* Clear separation of responsibilities
* Secure remote access
* Reproducibility
* Incremental development
* Hardware-efficient inference
* Support for multiple models and inference engines
* Future integration with existing homelab services

## Current Status

The current architecture has completed the first local inference milestone:

* Ollama installed on Windows 11
* Local model storage configured
* Qwen3 8B downloaded and tested
* Local API verified
* GPU acceleration verified
* Model successfully stopped and unloaded from GPU memory

The next architectural milestone is secure API access from a separate Linux system.
