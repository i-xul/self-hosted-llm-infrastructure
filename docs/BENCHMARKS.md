# Benchmarks

This document defines the benchmarking methodology used throughout the project.

The primary objective is consistency.

Every language model and inference engine should be evaluated using the same test methodology whenever practical.

This makes future comparisons meaningful and repeatable.

---

# Benchmark Goals

Each benchmark should answer the following questions:

* How fast is the model?
* How much memory does it require?
* Does it fully utilize the GPU?
* How well does it perform in Finnish?
* How well does it perform in technical tasks?
* Is the output accurate?
* Is the model suitable for everyday local use?

---

# Test Environment

Every benchmark should record:

| Item             | Value                 |
| ---------------- | --------------------- |
| Date             |                       |
| Operating System | Windows 11            |
| Inference Engine |                       |
| Model            |                       |
| Quantization     |                       |
| Context Size     |                       |
| GPU              | AMD Radeon RX 7800 XT |
| CPU              | AMD Ryzen 9 7900X     |
| System Memory    | 32 GB                 |

---

# Performance Measurements

Whenever possible, record:

* Time to first token
* Total response time
* Tokens per second
* GPU utilization
* VRAM usage
* System RAM usage
* CPU utilization
* Model loading time

---

# Functional Test Categories

Every tested model should complete the same categories.

## 1. Finnish Language

Example tasks:

* General conversation
* Technical explanations
* Grammar
* Natural wording

---

## 2. English Language

Example tasks:

* Technical writing
* Documentation
* General questions

---

## 3. Programming

Example tasks:

* Python
* Bash
* PowerShell
* SQL
* JavaScript

Evaluation should consider:

* Correctness
* Readability
* Practical usefulness

---

## 4. Linux Administration

Example topics:

* Docker
* systemd
* SSH
* Nginx
* Networking
* Shell scripting

---

## 5. Raspberry Pi

Example topics:

* Raspberry Pi OS
* Ubuntu
* GPIO
* Docker
* Self-hosting
* Performance tuning

---

## 6. Networking

Example topics:

* Routing
* DNS
* Firewalls
* Reverse proxies
* VPN
* TLS

---

## 7. Summarization

Test using long technical articles and news articles.

Evaluate:

* Accuracy
* Brevity
* Preservation of important information

---

## 8. Reasoning

Reasoning should be evaluated separately from factual correctness.

The reasoning benchmark uses multiple task types so that the comparison does not depend on a single style of problem:

* `reasoning.md` — arithmetic and capacity calculation
* `reasoning-logic.md` — dependency and scheduling logic
* `reasoning-constraints.md` — multi-constraint evaluation
* `reasoning-troubleshooting.md` — technical diagnosis and interpretation

Each model should be evaluated using the same deterministic benchmark configuration.

The evaluation should consider:

* correctness of the final answer
* correctness of intermediate reasoning
* constraint handling
* technical accuracy
* instruction following
* conciseness and practical usefulness
* consistency across repeated runs

When a model explicitly supports a reasoning or thinking mode, compare thinking-enabled and thinking-disabled execution separately.

Thinking mode should not automatically be considered superior. Record its effect on:

* response latency
* generated token count
* generation speed
* answer quality
* stability
* failure modes

Models without an explicit thinking capability should be evaluated using their normal generation mode rather than treating the absence of thinking mode as a disadvantage.

Reasoning scores are based on a deliberately small diagnostic test set and should not be interpreted as comprehensive measures of general reasoning ability.

---

# Comparison Criteria

Avoid subjective ratings whenever possible.

Instead of assigning stars or numerical scores, document observable behaviour.

Examples:

* Produced valid Python code without modification.
* Required manual corrections.
* Used natural Finnish.
* Produced unnecessarily long explanations.
* Failed to follow instructions.
* Hallucinated technical details.

These observations provide more value than arbitrary ratings.

---

# Benchmark Results

Detailed benchmark results will be added here as additional models and inference engines are tested.

The first benchmark will use:

* Ollama
* Qwen3 8B
* AMD Radeon RX 7800 XT

Future benchmarks will compare additional language models and inference engines using the same methodology.

---

## Cold and Warm Runs

Benchmark results distinguish between two execution modes:

- **Cold run:** The model is not loaded in GPU memory before the benchmark.
- **Warm run:** The model is already loaded in GPU memory before the benchmark.

Cold runs measure model loading and startup overhead.

Warm runs are used for comparing response generation speed and reasoning modes because they remove most storage-related loading time.

---

## Resource Monitoring

The benchmark runner automatically records system RAM and dedicated GPU VRAM usage during each benchmark run.

Resource monitoring records:

* resource usage before inference begins
* peak resource usage observed during the benchmark
* resource usage after inference completes
* the increase from the initial baseline to the observed peak

System RAM usage is measured from Windows physical-memory statistics.

Dedicated GPU VRAM usage is collected from the Windows `GPU Adapter Memory` performance counters. The benchmark runner tracks all reported GPU adapter instances and identifies the inference GPU based primarily on the largest increase in dedicated VRAM usage during the run.

For warm runs, where the model may already be resident in VRAM and therefore produce little or no additional allocation, the adapter with the highest absolute dedicated VRAM usage is used as a fallback.

Resource measurements are sampled periodically during benchmark execution. The current default sampling interval is 250 milliseconds.

Repeated benchmark summaries report RAM and inference-GPU VRAM statistics separately for cold and warm runs. This distinction is important because cold runs include model-loading memory allocation, while warm runs primarily measure resource usage with the model already resident in memory.

## Reasoning Benchmark Observations

The current reasoning comparison includes Qwen3 8B, Gemma 3 12B, Llama 3.1 8B and Phi-4 14B.

The four diagnostic reasoning tasks cover arithmetic, scheduling, constraint evaluation and technical troubleshooting.

Initial cross-model testing showed clear differences between models:

* Phi-4 14B produced the most consistently correct responses across the four reasoning task types.
* Qwen3 8B performed strongly with thinking disabled and correctly handled the technical Nginx troubleshooting scenario.
* Gemma 3 12B handled the simpler reasoning tasks successfully but made an important error in the Nginx troubleshooting scenario.
* Llama 3.1 8B handled basic arithmetic and scheduling but made errors in both constraint evaluation and technical troubleshooting.

Qwen3 8B was additionally tested with Ollama thinking mode enabled because it is the only model in the current four-model comparison that explicitly exposes a thinking capability.

Thinking mode did not improve the practical results in the tested tasks and substantially increased generated token counts and response latency.

The most significant failure occurred in the `reasoning-troubleshooting.md` benchmark. Two thinking-enabled warm runs generated 40,960 tokens and reached the model's configured context limit instead of producing an appropriately concise answer.

This result demonstrates that explicit thinking mode can introduce substantial computational and latency overhead and may also expose failure modes that are not present during normal non-thinking generation.

Thinking-mode results should therefore be treated as a separate model capability rather than being directly compared with models that do not expose an equivalent explicit reasoning mode.

Detailed per-model reasoning observations and preliminary manual scores are maintained in the benchmark comparison and quality-evaluation files.

---

# Long-Term Objective

The goal is to build a repeatable benchmark suite for self-hosted language models.

The benchmark process should remain stable over time so that new models can be compared against previous results under similar conditions.
