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

When supported by the model, compare:

* Reasoning mode
* Non-reasoning mode

Record differences in:

* Response speed
* Output quality
* Practical usefulness

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

## Initial Qwen3 8B Observation

Initial testing showed approximately:

- 75 tokens per second in non-reasoning mode
- 75 tokens per second in reasoning mode
- significantly higher total token output in reasoning mode
- approximately 35 seconds for the first HDD-backed cold start
- approximately 2 seconds for a warm non-reasoning response

---

# Long-Term Objective

The goal is to build a repeatable benchmark suite for self-hosted language models.

The benchmark process should remain stable over time so that new models can be compared against previous results under similar conditions.
