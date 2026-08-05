# Qwen3 8B vs. Gemma 3 12B vs. Llama 3.1 8B

This document compares three local language models on the same Windows 11 workstation using Ollama, identical benchmark prompts and the same runtime configuration.

The comparison combines automatically collected performance metrics with preliminary manual evaluations of Finnish-language quality, Python programming and summarization.

## Test Environment

| Component | Value |
|---|---|
| Operating system | Windows 11 |
| CPU | AMD Ryzen 9 7900X |
| System memory | 32 GB |
| GPU | AMD Radeon RX 7800 XT |
| VRAM | 16 GB |
| Model storage | HDD |
| Inference engine | Ollama 0.32.5 |
| Python | 3.13.14 |
| Benchmark context size | 4096 |
| Temperature | 0 |
| Seed | 42 |

All three models were loaded entirely onto the GPU.

## Model Specifications

| Model | Parameters | Stored size | Quantization | Maximum context | GPU placement |
|---|---:|---:|---|---:|---|
| Qwen3 8B | 8.2B | 5.2 GB | Q4_K_M | 40,960 | 100% GPU |
| Gemma 3 12B | 12.2B | 8.1 GB | Q4_K_M | 131,072 | 100% GPU |
| Llama 3.1 8B | 8.0B | 4.9 GB | Q4_K_M | 131,072 | 100% GPU |

## Performance Ranking

| Rank | Model | Average generation speed | Cold start |
|---:|---|---:|---:|
| 1 | Llama 3.1 8B | 78.22 tok/s | 35.19 s |
| 2 | Qwen3 8B | 74.24 tok/s | 34.72 s |
| 3 | Gemma 3 12B | 47.23 tok/s | 64.31 s |

Llama 3.1 8B was the fastest model in raw token generation.

Qwen3 8B was only slightly slower and had the shortest measured cold start.

Gemma 3 12B was substantially slower and required the longest model-loading time from HDD.

## Manual Quality Ranking

| Rank | Model | Finnish | Python | Summarization | Overall |
|---:|---|---:|---:|---:|---:|
| 1 | Gemma 3 12B | 8.5/10 | 7.5/10 | 8.0/10 | 8.0/10 |
| 2 | Qwen3 8B | 6.0/10 | 7.0/10 | 6.0/10 | 6.3/10 |
| 3 | Llama 3.1 8B | 4.0/10 | 6.0/10 | 3.0/10 | 4.3/10 |

The scores are preliminary human evaluations based on selected benchmark responses. They are not objective or comprehensive model-quality measurements.

## Finnish-Language Quality

### Gemma 3 12B

Gemma produced the most natural and fluent Finnish of the three models. It followed the requested length more closely and organized the Raspberry Pi explanation clearly.

Its main weakness was an overly broad price claim stating that Raspberry Pi generally costs less than 50 euros.

### Qwen3 8B

Qwen produced understandable Finnish, but several expressions sounded translated or unnatural. Its answer was also substantially shorter than requested.

The response remained useful as a basic explanation, but it was less polished than Gemma's output.

### Llama 3.1 8B

Llama produced repetitive and unnatural Finnish. Its separate manual test also contained serious factual errors about Raspberry Pi hardware, including obsolete or incorrect CPU and memory specifications.

The formal benchmark response avoided the worst factual claims but remained brief, repetitive and linguistically weak.

### Finnish-language conclusion

Gemma 3 12B was clearly the strongest Finnish-language model in this comparison.

## Python Programming

### Gemma 3 12B

Gemma produced a detailed and mostly usable standard-library program with error handling, exit codes and usage instructions.

However, the timeout was configurable only inside the function and not through the command line as requested. The response was also unnecessarily verbose.

### Qwen3 8B

Qwen produced a more concise TCP-port checking solution with standard-library networking and command-line arguments.

Its response was less comprehensive than Gemma's, but it provided a reasonable balance between implementation detail and brevity.

### Llama 3.1 8B

Llama produced a readable basic program, but the timeout was fixed at one second rather than being configurable through command-line arguments.

It also failed to handle invalid port values cleanly, omitted port-range validation and included exception branches that were not fully consistent with the use of `connect_ex()`.

### Python conclusion

Gemma and Qwen both produced broadly usable solutions, but neither fully satisfied every requirement. Qwen was more concise, while Gemma was more comprehensive.

## Summarization

### Gemma 3 12B

Gemma preserved the main benefits, risks and pilot decision while staying within the five-sentence limit.

The summary was mostly natural Finnish, although it began with an unnecessary English introduction.

### Qwen3 8B

Qwen identified the main topic and conclusions, but its Finnish phrasing was less polished and natural than Gemma's.

### Llama 3.1 8B

Llama exceeded the five-sentence limit substantially and produced several awkward or incorrect expressions, including mistranslations related to web applications, non-critical services and operational requirements.

### Summarization conclusion

Gemma 3 12B was the strongest summarization model of the three. Llama 3.1 8B failed important structural and language requirements.

## Workload Recommendations

| Workload | Preliminary recommendation |
|---|---|
| Fastest raw generation | Llama 3.1 8B |
| Fast interactive technical chat | Qwen3 8B |
| Finnish-language explanations | Gemma 3 12B |
| Finnish summarization | Gemma 3 12B |
| Concise technical assistance | Qwen3 8B |
| Detailed technical guidance | Gemma 3 12B |
| Lowest storage requirement | Llama 3.1 8B |
| Best current speed-quality balance | Qwen3 8B |
| Long-context capability | Gemma 3 12B or Llama 3.1 8B |

## Overall Conclusion

Llama 3.1 8B achieved the highest token generation speed, but its Finnish-language and summarization quality were clearly the weakest.

Gemma 3 12B produced the strongest responses overall, especially in Finnish and summarization, but it was significantly slower and produced longer answers.

Qwen3 8B currently offers the strongest overall balance between speed, resource usage and response quality on this hardware.

## Limitations

This comparison is based on one complete benchmark pass per model and selected manual response evaluations.

Future testing should include:

- repeated all-prompts runs
- blind or multi-reviewer quality evaluation
- execution testing of generated Python programs
- longer-context workloads
- reasoning-mode comparisons
- additional benchmark categories
- additional model families

The current rankings and recommendations should therefore be treated as preliminary.