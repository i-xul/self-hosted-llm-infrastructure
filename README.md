# Self-Hosted LLM Infrastructure

A practical project documenting the design, deployment and evolution of a privacy-first, self-hosted Large Language Model (LLM) infrastructure.

The goal is to build a modular AI platform capable of running modern open-source language models entirely on local hardware while remaining secure, reproducible and easy to extend.

The objective is to build a modular AI platform where language models run entirely on local hardware while remaining secure, well-documented and easy to extend.

This repository focuses on the infrastructure surrounding local AI rather than a single language model or inference engine.

---

## Project Goals

* Build a fully self-hosted AI environment
* Keep all inference on local hardware
* Utilize GPU acceleration for efficient inference
* Compare multiple open-source language models
* Compare multiple inference engines
* Benchmark performance using repeatable test methods
* Document every major architectural decision
* Maintain strong security and privacy principles
* Support future Linux integration and remote access

---

## Current Status

**Current milestone:** Phase 1 – Local GPU Inference

Completed:

* ✔ Ollama installed on Windows 11
* ✔ Local model storage configured
* ✔ Local REST API verified
* ✔ First language model successfully deployed
* ✔ GPU acceleration verified
* ✔ Initial documentation completed

Current inference engine:

* Ollama

Current test model:

* Qwen3 8B

---

## Benchmarked Models

| Model | Parameters | GPU placement | Generation speed | Initial result |
|---|---:|---|---:|---|
| Qwen3 8B | 8.2B | 100% GPU | approximately 74–75 tok/s | Faster and more responsive |
| Gemma 3 12B | 12.2B | 100% GPU | approximately 46–48 tok/s | Stronger initial Finnish-language quality |

Detailed comparison:

- [Qwen3 8B vs. Gemma 3 12B](benchmarks/comparisons/qwen3-8b-vs-gemma3-12b.md)

---

## Current Architecture

```text
                 User
                   │
                   ▼
          Ollama Command Line
                   │
                   ▼
             Ollama Local API
                   │
                   ▼
               Qwen3 8B
                   │
                   ▼
        AMD Radeon RX 7800 XT
```

A more detailed architecture description is available in the project documentation.

---

## Documentation

| [`ARCHITECTURE.md`](docs/ARCHITECTURE.md) | System architecture and future design |
| [`PROJECT_PRINCIPLES.md`](docs/PROJECT_PRINCIPLES.md) | Design philosophy and development principles |
| [`ROADMAP.md`](docs/ROADMAP.md) | Planned project evolution |
| [`INSTALLATION.md`](docs/INSTALLATION.md) | Installation process and configuration |
| [`HARDWARE.md`](docs/HARDWARE.md) | Hardware platform |
| [`MODELS.md`](docs/MODELS.md) | Language model evaluations |
| [`BENCHMARKS.md`](docs/BENCHMARKS.md) | Benchmark methodology |
| [`SECURITY.md`](docs/SECURITY.md) | Security architecture and principles |
| [Model comparison](benchmarks/comparisons/qwen3-8b-vs-gemma3-12b.md) | First performance and response-quality comparison |

---

## Planned Development

The project is expected to evolve through the following stages:

1. Local GPU inference
2. Multi-model laboratory
3. Multiple inference engines
4. Secure remote access
5. Web-based interface
6. Monitoring
7. Retrieval-Augmented Generation (RAG)
8. Homelab integration
9. AI assistants and tool calling

Detailed planning is available in `docs/ROADMAP.md`.

---

## Repository Structure

```text
self-hosted-llm-infrastructure/
│
├── benchmarks/
│   ├── comparisons/
│   │   └── qwen3-8b-vs-gemma3-12b.md
|
├── docs/
│   ├── ARCHITECTURE.md
│   ├── BENCHMARKS.md
│   ├── HARDWARE.md
│   ├── INSTALLATION.md
│   ├── MODELS.md
│   ├── PROJECT_PRINCIPLES.md
│   ├── ROADMAP.md
│   └── SECURITY.md
│
├── screenshots/
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Design Philosophy

The project follows several core principles:

* Privacy first
* Local-first operation
* Security by default
* Modular architecture
* Reproducible deployment
* Benchmark before conclusions
* Incremental development
* Comprehensive documentation

The complete philosophy is documented in `docs/PROJECT_PRINCIPLES.md`.

---

## Project Status

This project is under active development.

Architectural decisions, benchmark methodologies and implementation details will continue to evolve as new models and inference technologies become available.

---

## Long-Term Vision

The long-term goal is to create a reusable reference implementation for building secure, privacy-focused AI infrastructure using consumer hardware.

Future versions may include:

* Multiple inference engines
* Local document search (RAG)
* Open WebUI
* AI-assisted homelab management
* Infrastructure monitoring
* Secure remote access
* Controlled tool calling
* Automation workflows

---

## License

This project is released under the MIT License.
