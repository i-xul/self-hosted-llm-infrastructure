# Roadmap

This document outlines the planned evolution of the self-hosted LLM infrastructure.

The roadmap is intentionally incremental. Each phase should result in a stable, fully working system before moving to the next.

---

# Phase 1 — Local GPU Inference

## Objective

Build a fully functional local inference environment on a Windows 11 workstation.

### Completed

* [x] Install Ollama
* [x] Configure local model storage
* [x] Download and run the first language model
* [x] Verify local REST API
* [x] Verify GPU acceleration on AMD Radeon RX 7800 XT
* [x] Create the initial GitHub repository
* [x] Create the documentation structure
* [x] Create repeatable benchmark prompts
* [x] Compare reasoning vs. non-reasoning modes
* [x] Evaluate additional language models
* [x] Measure response latency
* [x] Measure generation speed
* [x] Measure GPU memory usage
* [x] Measure system memory usage

---

# Phase 2 — Multi-Model Laboratory

## Objective

Transform the project from a single-model setup into a reusable local AI laboratory.

### Completed

* [x] Test additional open-source models
* [x] Compare different model sizes
* [x] Compare Finnish language quality
* [x] Compare programming capabilities
* [x] Compare summarization quality
* [x] Document strengths and weaknesses of each model

### Planned

* [ ] Compare reasoning quality across models

---

# Phase 3 — Multiple Inference Engines

## Objective

Compare different local inference engines.

### Planned

* [ ] Evaluate llama.cpp
* [ ] Compare Ollama and llama.cpp
* [ ] Compare performance
* [ ] Compare memory usage
* [ ] Compare supported features
* [ ] Document architectural differences

---

# Phase 4 — Remote Access

## Objective

Provide secure network access to the local AI interface while keeping inference services protected from unnecessary network exposure.

### Planned

* [ ] Allow secure API access from Ubuntu
* [x] Configure Windows Firewall for Open WebUI LAN access
* [x] Restrict Open WebUI LAN access with Windows Firewall
* [x] Restrict Open WebUI access to the trusted `192.168.1.0/24` subnet
* [x] Test LAN connectivity from another device
* [x] Verify browser-to-GPU inference over the private LAN
* [ ] Evaluate a suitable encrypted VPN or private-network solution for external remote access
* [ ] Test external remote access after a suitable solution has been selected

---

# Phase 5 — Web Interface

## Objective

Provide a dedicated browser-based interface.

### Completed

* [x] Deploy Open WebUI
* [x] Connect to the Windows inference node
* [x] Configure Open WebUI authentication

### Planned

* [ ] Add HTTPS
* [ ] Support multiple users (if needed)

---

# Phase 6 — Monitoring

## Objective

Monitor the local AI infrastructure.

### Planned

* [ ] GPU monitoring
* [ ] VRAM monitoring
* [ ] RAM monitoring
* [ ] CPU monitoring
* [ ] API availability
* [ ] Model status
* [ ] Performance history

---

# Phase 7 — Retrieval-Augmented Generation (RAG)

## Objective

Allow language models to answer questions using locally stored documentation.

### Planned

* [ ] Evaluate embedding models
* [ ] Evaluate vector databases
* [ ] Import local Markdown documentation
* [ ] Import PDF documents
* [ ] Test semantic search
* [ ] Document RAG architecture

---

# Phase 8 — Homelab Integration

## Objective

Integrate the AI platform with existing homelab services.

Possible future integrations include:

* Homelab Hub
* Infrastructure documentation
* Inventory data
* Monitoring data
* Log analysis
* Raspberry Pi projects

---

# Phase 9 — AI Assistants

## Objective

Allow the local language model to perform controlled actions.

Possible future capabilities:

* Tool calling
* Local automation
* Service diagnostics
* Configuration assistance
* Log interpretation
* Infrastructure troubleshooting

Administrative actions should always remain explicitly authorized by the user.

---

# Long-Term Vision

The long-term goal is to build a modular, privacy-first AI platform where:

* inference remains local
* multiple models can coexist
* different inference engines can be compared
* Linux and Windows systems cooperate
* documentation remains comprehensive
* future components can be added without redesigning the entire architecture

The project should evolve into a reusable reference implementation for building secure, self-hosted AI infrastructure.
