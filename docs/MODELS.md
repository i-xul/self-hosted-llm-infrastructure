# Models

This document tracks every language model evaluated during this project.

The objective is not to identify a single "best" model, but to understand the strengths, limitations and resource requirements of different open-source models running entirely on local hardware.

## Tested Models

| Model | Parameters | Quantization | GPU placement | Status | Comparison |
|---|---:|---|---|---|---|
| Qwen3 8B | 8.2B | Q4_K_M | 100% GPU | Benchmarked | [Qwen3 8B vs. Gemma 3 12B](../benchmarks/comparisons/qwen3-8b-vs-gemma3-12b.md) |
| Gemma 3 12B | 12.2B | Q4_K_M | 100% GPU | Benchmarked | [Qwen3 8B vs. Gemma 3 12B](../benchmarks/comparisons/qwen3-8b-vs-gemma3-12b.md) |

## Performance Leaderboard

The automatically generated performance leaderboard is available here:

- [Local LLM Performance Leaderboard](../benchmarks/LEADERBOARD.md)

The leaderboard currently ranks models by average token generation speed. Manual response-quality evaluations are documented separately.

## Initial Performance Summary

| Model | Stored size | Approximate generation speed | Initial observation |
|---|---:|---:|---|
| Qwen3 8B | 5.2 GB | 74–75 tokens/s | Faster and more responsive, but Finnish wording was occasionally unnatural |
| Gemma 3 12B | 8.1 GB | 46–48 tokens/s | Slower, but generally produced more natural Finnish and more detailed responses |

Both models fit entirely in the 16 GB VRAM of the AMD Radeon RX 7800 XT.

---

# Evaluation Method

Each model will be evaluated using the same repeatable methodology whenever practical.

Areas of evaluation include:

* Installation experience
* GPU compatibility
* Memory requirements
* Response latency
* Generation speed
* Finnish language quality
* English language quality
* Programming capability
* Technical explanations
* Text summarization
* General reasoning
* Stability

The same benchmark prompts should be reused whenever possible to make comparisons meaningful.

---

# Current Model

## Qwen3 8B

### Status

Current primary test model.

### Installation

Installed using:

```powershell
ollama run qwen3:8b
```

### Initial Observations

**Strengths**

* Successfully runs entirely on the AMD Radeon RX 7800 XT.
* Produces fluent Finnish responses.
* Generates functional Python code.
* Good overall first impression.
* Simple installation through Ollama.

**Weaknesses**

* Reasoning mode produces long internal reasoning before the final answer.
* Some Finnish wording can occasionally sound unnatural.
* Additional benchmarking is required before drawing conclusions.

### Initial Test Results

| Category          | Result |
| ----------------- | ------ |
| Local inference   | ✅      |
| GPU acceleration  | ✅      |
| Finnish language  | ✅      |
| Programming       | ✅      |
| Summarization     | ✅      |
| API compatibility | ✅      |

### Future Evaluation

The following topics remain to be evaluated:

* Non-reasoning mode
* Larger context windows
* Memory consumption
* Response speed
* Long conversations
* Programming accuracy
* Linux administration
* Docker knowledge
* Networking
* Nginx
* Raspberry Pi
* Security-related tasks

---

# Future Models

The following models are candidates for future evaluation.

## Llama family

Status:

Not yet tested.

Evaluation goals:

* Compare against Qwen
* Programming
* General reasoning
* Resource usage

---

## Gemma family

Evaluation goals:

* Speed
* Small-model performance
* General assistant quality

---

## Mistral family

Status:

Not yet tested.

Evaluation goals:

* Reasoning
* Technical writing
* Response quality

---

## Planned Models

- Llama family
- Mistral family
- Phi family
- Larger Qwen variants
- Additional models that fit fully or partially within the available 16 GB VRAM

---

# Future Comparison Matrix

A comparison table will be added as additional models are tested.

| Model    | GPU | Finnish | Programming |  Speed  | Reasoning | Notes            |
| -------- | :-: | :-----: | :---------: | :-----: | :-------: | ---------------- |
| Qwen3 8B |  ✅  |    ✅    |      ✅      | Pending |  Pending  | Current baseline |

---

# Long-Term Goal

The project aims to build a well-documented collection of repeatable local LLM evaluations.

Rather than searching for a universally "best" model, the objective is to understand which models perform best for different workloads while remaining fully self-hosted.
