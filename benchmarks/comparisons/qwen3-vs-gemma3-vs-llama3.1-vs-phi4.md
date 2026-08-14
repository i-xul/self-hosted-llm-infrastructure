# Qwen3 8B vs. Gemma 3 12B vs. Llama 3.1 8B vs. Phi-4 14B

This document compares four local language models on the same Windows 11 workstation using Ollama, identical benchmark prompts and the same benchmark configuration.

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
| Inference engine | Ollama |
| Python | 3.13 |
| Benchmark context size | 4096 |
| Temperature | 0 |
| Seed | 42 |

All four models were loaded entirely onto the GPU.

The benchmark runs were not all performed with exactly the same Ollama and Python patch versions. The three earlier models were benchmarked on 2026-08-05, while Phi-4 14B was benchmarked on 2026-08-14. The benchmark configuration itself remained consistent.

## Model Specifications

| Model | Parameters | Stored size | Quantization | Maximum context | GPU placement |
|---|---:|---:|---|---:|---|
| Qwen3 8B | 8.2B | 5.2 GB | Q4_K_M | 40,960 | 100% GPU |
| Gemma 3 12B | 12.2B | 8.1 GB | Q4_K_M | 131,072 | 100% GPU |
| Llama 3.1 8B | 8.0B | 4.9 GB | Q4_K_M | 131,072 | 100% GPU |
| Phi-4 14B | 14.7B | 9.1 GB | Q4_K_M | 16,384 | 100% GPU |

## Performance Ranking

| Rank | Model | Average generation speed | Cold start |
|---:|---|---:|---:|
| 1 | Llama 3.1 8B | 78.22 tok/s | 35.19 s |
| 2 | Qwen3 8B | 74.24 tok/s | 34.72 s |
| 3 | Gemma 3 12B | 47.23 tok/s | 64.31 s |
| 4 | Phi-4 14B | 45.94 tok/s | 71.90 s |

Llama 3.1 8B remains the fastest model in raw token generation.

Qwen3 8B is only slightly slower and has the shortest measured cold start of the four models.

Gemma 3 12B and Phi-4 14B form a substantially slower group. Phi-4 is the slowest model in the current benchmark and also has the longest measured cold start.

The cold-start results should be interpreted partly as model-loading measurements because the models are stored on an HDD.

## Manual Quality Ranking

| Rank | Model | Finnish | Python | Summarization | Overall |
|---:|---|---:|---:|---:|---:|
| 1 | Gemma 3 12B | 8.5/10 | 7.5/10 | 8.0/10 | 8.0/10 |
| 2 | Qwen3 8B | 6.0/10 | 7.0/10 | 6.0/10 | 6.3/10 |
| 3 | Phi-4 14B | 7.0/10 | 6.5/10 | 4.5/10 | 6.0/10 |
| 4 | Llama 3.1 8B | 4.0/10 | 6.0/10 | 3.0/10 | 4.3/10 |

The scores are preliminary human evaluations based on selected benchmark responses. They are not objective or comprehensive model-quality measurements.

## Finnish-Language Quality

### Gemma 3 12B

Gemma produced the most natural and fluent Finnish of the four models. It followed the requested length reasonably well and organized the Raspberry Pi explanation clearly.

Its main weakness was an overly broad price claim stating that Raspberry Pi generally costs less than 50 euros.

### Phi-4 14B

Phi-4 produced generally understandable and reasonably fluent Finnish. Its formal benchmark response was substantially stronger than Llama 3.1 8B and somewhat more natural than Qwen3 8B in several places.

However, the response still contained awkward expressions and unnatural constructions.

A separate manual sanity check was significantly weaker and incorrectly described Raspberry Pi as a "computer emulator". It also contained additional technical wording problems, showing that apparently fluent output does not guarantee factual reliability.

### Qwen3 8B

Qwen produced understandable Finnish, but several expressions sounded translated or unnatural. Its answer was also substantially shorter than requested.

The response remained useful as a basic explanation, but it was less polished than Gemma's output.

### Llama 3.1 8B

Llama produced repetitive and unnatural Finnish.

Its separate manual test also contained serious factual errors about Raspberry Pi hardware, including obsolete or incorrect CPU and memory specifications.

The formal benchmark response avoided the worst factual claims but remained brief, repetitive and linguistically weak.

### Finnish-language conclusion

Gemma 3 12B remains clearly the strongest Finnish-language model in the current comparison.

Phi-4 14B ranks second in the manual Finnish score, but its separate sanity-check failure reduces confidence in using it for factual Finnish-language explanations without verification.

## Python Programming

### Gemma 3 12B

Gemma produced a detailed and mostly usable standard-library program with error handling, exit codes and usage instructions.

However, the timeout was configurable only inside the function and not through the command line as requested. The response was also unnecessarily verbose.

### Qwen3 8B

Qwen produced a concise TCP-port checking solution using the standard library and command-line arguments.

Its response was less comprehensive than Gemma's, but it provided a reasonable balance between implementation detail and brevity.

### Phi-4 14B

Phi-4 produced a clean and readable solution using `argparse`, the Python standard library and a command-line configurable timeout.

However, it contained an important behavioral flaw: `main()` ignored the boolean result returned by `check_port()`.

As a result, a closed or unreachable port could still allow the program to terminate with exit status 0, violating the requirement for an appropriate exit code.

This is a good example of code that looks polished during source review but still contains a meaningful functional defect.

### Llama 3.1 8B

Llama produced a readable basic program, but the timeout was fixed at one second rather than being configurable through command-line arguments.

It also failed to handle invalid port values cleanly, omitted port-range validation and included exception branches that were not fully consistent with the use of `connect_ex()`.

### Python conclusion

Gemma 3 12B and Qwen3 8B remain the strongest current Python responses.

Phi-4 14B generated structurally clean code, but its incorrect exit behavior is significant enough to place it below them in the current evaluation.

The results also reinforce the need for future automatic execution testing rather than relying only on visual code review.

## Summarization

### Gemma 3 12B

Gemma preserved the main benefits, risks and pilot decision while staying within the five-sentence limit.

The summary was mostly natural Finnish, although it began with an unnecessary English introduction.

### Qwen3 8B

Qwen identified the main topic and conclusions, but its Finnish phrasing was less polished and natural than Gemma's.

### Phi-4 14B

Phi-4 preserved the main benefits, risks and pilot decision reasonably well.

However, it substantially exceeded the requested five-sentence limit and contained several unnatural or grammatically incorrect Finnish expressions.

This significantly reduced its score despite reasonably good preservation of the source material.

### Llama 3.1 8B

Llama exceeded the five-sentence limit substantially and produced several awkward or incorrect expressions, including mistranslations related to web applications, non-critical services and operational requirements.

### Summarization conclusion

Gemma 3 12B remains the strongest summarization model in the current comparison.

Qwen3 8B is second. Phi-4 14B preserved the content reasonably well but failed an important structural instruction and showed weaker Finnish-language quality.

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
| Best current overall quality | Gemma 3 12B |
| Strong Finnish alternative for further testing | Phi-4 14B |
| Long-context capability | Gemma 3 12B or Llama 3.1 8B |

## Speed vs. Quality

The four-model comparison demonstrates why performance and quality should remain separate measurements.

Llama 3.1 8B produces the highest token rate but has the lowest manual quality score.

Gemma 3 12B is substantially slower but produces the highest-quality responses in the currently evaluated categories.

Qwen3 8B occupies the strongest middle position: its generation speed is close to Llama 3.1 8B while its evaluated response quality is considerably higher.

Phi-4 14B does not currently establish a clear speed-quality advantage. It is the slowest tested model and its overall manual quality score remains slightly below Qwen3 8B, although its Finnish-language score is stronger.

## Overall Conclusion

The addition of Phi-4 14B strengthens the main conclusion of the benchmark project: model size and raw generation speed alone are poor predictors of practical usefulness.

Llama 3.1 8B remains the fastest model but produces the weakest evaluated Finnish-language and summarization output.

Gemma 3 12B remains the strongest model for overall response quality, particularly for Finnish-language explanations and summarization, but its lower generation speed and longer cold start make it less responsive.

Phi-4 14B performs reasonably well in Finnish and generates polished-looking Python code, but it currently provides neither the best quality nor the best performance. Its functional Python error and weak instruction following in summarization also show why manual evaluation remains necessary.

Qwen3 8B therefore remains the strongest current speed-quality compromise on this hardware. It combines near-leading generation performance with substantially better evaluated quality than Llama 3.1 8B while requiring considerably fewer resources than the larger models.

## Limitations

This comparison is based on one complete benchmark pass per model and selected manual response evaluations.

The models were benchmarked on the same hardware and with the same benchmark configuration, but not all runs used exactly the same Ollama and Python patch versions.

The current manual quality evaluation covers only three categories:

- Finnish-language explanation
- Python programming
- summarization

The current results should therefore be treated as preliminary.

Future testing should include:

- repeated all-prompts runs
- blind or multi-reviewer quality evaluation
- automatic execution testing of generated Python programs
- longer-context workloads
- reasoning-mode comparisons
- additional benchmark categories
- factual-accuracy testing
- instruction-following measurements
- additional model families

As the number of tested models grows, workload-specific recommendations are likely to become more useful than selecting a single overall winner.