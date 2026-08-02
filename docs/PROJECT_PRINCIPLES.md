# Project Principles

This document defines the long-term principles that guide the design and development of this project.

The goal is not simply to run a local language model, but to build a secure, maintainable and well-documented self-hosted AI infrastructure.

## 1. Privacy First

All language model inference should run on hardware that I control.

Prompts, responses and local documents should remain on local systems whenever practical.

External AI services should never be required for normal operation.

---

## 2. Local-First Architecture

The project should continue functioning without internet access after the required software and models have been installed.

Internet connectivity may be required only for:

* downloading software updates
* downloading new language models
* optional future integrations

Normal inference should not depend on cloud services.

---

## 3. Security by Default

Security should be considered before convenience.

Examples include:

* restricted API access
* private networking
* firewall rules
* least-privilege configuration
* secure authentication
* separation of services

No language model service should ever be exposed directly to the public internet.

---

## 4. Separation of Responsibilities

Whenever practical, different responsibilities should remain separate.

Typical examples:

* inference
* user interface
* monitoring
* document storage
* authentication
* reverse proxy

This makes the infrastructure easier to maintain and extend.

---

## 5. Reproducibility

The complete environment should be reproducible from documentation.

Another technically experienced user should be able to recreate the same infrastructure by following the documented steps.

Important configuration decisions should always be documented.

---

## 6. Documentation Matters

Documentation is considered part of the project, not an afterthought.

Major architectural decisions, benchmarks, installation steps and design choices should be recorded throughout the project's lifetime.

---

## 7. Benchmark Before Conclusions

Language models should not be judged based on first impressions.

Whenever possible, models should be compared using repeatable benchmark tasks covering areas such as:

* programming
* Linux administration
* networking
* summarization
* Finnish language quality
* English language quality
* reasoning
* response speed
* GPU and memory usage

Measurements should be documented before drawing conclusions.

---

## 8. Incremental Development

The project should evolve through small, verifiable improvements.

Each completed milestone should leave the system in a working state before new functionality is added.

---

## 9. Technology Independence

Whenever practical, the project should avoid becoming dependent on a single language model or inference engine.

Current technologies may include:

* Ollama
* llama.cpp

Future alternatives should be evaluated as the ecosystem evolves.

---

## 10. Open Learning

This repository documents both successful implementations and lessons learned.

Design changes, unexpected behavior and performance observations are valuable parts of the project and should be documented whenever they help explain technical decisions.

---

# Project Vision

The long-term vision is to build a fully self-hosted AI platform capable of serving multiple devices securely within a private network while remaining independent of commercial cloud AI providers.

The platform should provide practical AI capabilities without sacrificing privacy, security or maintainability.
