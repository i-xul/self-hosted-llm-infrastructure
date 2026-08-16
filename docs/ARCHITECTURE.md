# Architecture

This document describes the current and planned architecture of the self-hosted LLM infrastructure.

## Current Architecture

The current implementation uses a Windows 11 desktop computer as the GPU-powered inference node and Docker Desktop with WSL 2 as the container platform for the browser-based interface.

```text
              Browser
                 │
                 ▼
             Open WebUI
        Docker Desktop / WSL 2
          localhost:3000
                 │
                 │ host.docker.internal:11434
                 ▼
               Ollama
          Windows 11 host
                 │
                 ▼
        Local language models
                 │
                 ▼
      AMD Radeon RX 7800 XT
            16 GB VRAM
```

### Compute Node

The current compute node consists of:

* Windows 11
* AMD Ryzen 9 7900X
* 32 GB system memory
* AMD Radeon RX 7800 XT
* 16 GB VRAM
* Ollama as the inference engine
* Multiple locally installed language models

Model files are stored separately on the local HDD under:

```text
F:\AI\models
```

The model directory is configured through the Windows user environment variable:

```text
OLLAMA_MODELS=F:\AI\models
```

### Local Inference

Inference runs directly on the Windows host through Ollama.

The currently benchmarked models are:

* Qwen3 8B
* Gemma 3 12B
* Llama 3.1 8B
* Phi-4 14B

GPU verification with `ollama ps` has confirmed:

```text
100% GPU
```

for tested model execution. Ollama therefore uses the AMD Radeon RX 7800 XT for model processing instead of relying entirely on CPU inference.

Ollama is intentionally kept on the Windows host rather than being moved into the Open WebUI container. This keeps the established GPU inference environment independent from the interface layer.

### Interface Layer

Open WebUI provides the current browser-based interface.

It runs as a Docker container using Docker Desktop with the WSL 2 backend.

The interface is currently published on the Windows host at:

```text
http://localhost:3000
```

The Open WebUI container uses persistent Docker storage for its application data.

Open WebUI is an interface layer only. Model inference continues to be performed by the Windows-hosted Ollama service.

### Ollama API Connection

Ollama provides its HTTP API on port `11434`.

From the Windows host, the service is available through:

```text
http://localhost:11434
```

From the Open WebUI container, the Windows host is reached through Docker's host gateway:

```text
http://host.docker.internal:11434
```

This connection has been verified by successfully discovering the locally installed Ollama models in Open WebUI and running browser-based inference.

The Ollama API is not intentionally exposed to the public internet.

## Planned Architecture

The current Docker-based Open WebUI deployment provides the first working interface layer on the Windows 11 host.

A future stage may move the interface and supporting services to a separate Linux system while keeping the Windows desktop as the dedicated GPU-powered inference node.

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

This architecture would separate the always-available interface and supporting services from the higher-power GPU inference system.

The current Windows-hosted Open WebUI deployment also provides a practical environment for developing and validating the interface layer before deciding whether it should be migrated to a separate Linux or Raspberry Pi system.

Remote access must use a trusted private network path rather than exposing Ollama or Open WebUI directly to the public internet.

## Architectural Layers

The infrastructure is divided into separate architectural layers.

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

The interface layer provides browser-based access to the language models.

Current implementation:

* Open WebUI
* Docker Desktop with WSL 2 backend
* Browser-based chat interface
* Persistent Docker volume for Open WebUI application data
* Connection to the Windows-hosted Ollama API through `host.docker.internal`

Future additions may include:

* API clients
* Integrations with local applications
* Additional authentication and access controls
* Reverse proxy
* Migration of Open WebUI to a separate Ubuntu or Raspberry Pi 5 system

The current interface layer runs on the Windows 11 host through Docker Desktop. A future deployment may move this layer to a separate low-power Linux system while keeping model inference on the Windows GPU node.

### 3. Network Layer

The network layer connects clients, the interface layer and the inference service without exposing the environment directly to the public internet.

Current implementation:

* Open WebUI is published by Docker on TCP port `3000`
* Open WebUI communicates with the Windows-hosted Ollama service through Docker's internal host gateway
* Ollama provides its API on TCP port `11434`
* Local browser access to Open WebUI has been verified
* Direct public internet exposure is not part of the architecture
* Open WebUI access from another device on the private LAN has been verified
* Windows Firewall allows inbound TCP port `3000` on the Private network profile

Current verified LAN path:

```text
LAN client
    │
    │ TCP 3000
    ▼
Windows 11 host
    │
    ▼
Open WebUI
Docker Desktop / WSL 2
    │
    │ host.docker.internal:11434
    ▼
Ollama
    │
    ▼
Qwen3 8B
    │
    ▼
AMD Radeon RX 7800 XT
100% GPU
```

The complete browser-to-GPU path has been verified from a separate LAN device.

Planned private access methods:

* Local area network
* Tailscale
* NordVPN Meshnet
* Restricted Windows Firewall rules

Remote access should use a trusted private network path such as Tailscale or NordVPN Meshnet rather than public port forwarding.

The network design should expose only the services required by clients. The Ollama API should remain restricted to trusted systems and does not need to be directly accessible to ordinary Open WebUI users.

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

The current architecture has completed the local inference and initial interface milestones:

* Ollama installed directly on Windows 11
* Dedicated local model storage configured
* AMD Radeon RX 7800 XT GPU acceleration verified
* Multiple local language models installed and benchmarked
* Repeatable benchmark and quality-evaluation framework implemented
* Local model registry implemented
* Docker Desktop with WSL 2 backend installed and verified
* Open WebUI deployed as a persistent Docker container
* Open WebUI connected to the Windows-hosted Ollama service
* Browser-based model discovery and inference verified
* 100% GPU model execution verified through the Open WebUI workflow

The current system therefore provides a complete local path from the browser interface to GPU-accelerated model inference:

```text
Browser
   │
   ▼
Open WebUI
   │
   ▼
Ollama
   │
   ▼
Local LLM
   │
   ▼
AMD Radeon RX 7800 XT
```

The next architectural milestones are secure private-network access from other devices and further development of the interface, data and monitoring layers.

A separate Linux or Raspberry Pi 5 interface node remains a possible future architecture rather than a requirement for the current deployment.
