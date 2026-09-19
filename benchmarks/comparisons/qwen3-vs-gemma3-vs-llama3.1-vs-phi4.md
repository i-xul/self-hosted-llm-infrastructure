# Qwen3 8B vs. Gemma 3 12B vs. Llama 3.1 8B vs. Phi-4 14B

This document compares four local language models on the same Windows 11 workstation using Ollama, identical benchmark prompts and the same benchmark configuration.

The comparison combines automatically collected performance metrics with preliminary manual evaluations of Finnish-language quality, Python programming, summarization and reasoning.

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

| Rank | Model | Finnish | Python | Summarization | Reasoning | Overall |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Gemma 3 12B | 8.5/10 | 7.5/10 | 8.0/10 | 7.0/10 | 7.8/10 |
| 2 | Phi-4 14B | 7.0/10 | 6.5/10 | 4.5/10 | 9.0/10 | 6.8/10 |
| 3 | Qwen3 8B | 6.0/10 | 7.0/10 | 6.0/10 | 8.0/10 | 6.8/10 |
| 4 | Llama 3.1 8B | 4.0/10 | 6.0/10 | 3.0/10 | 5.5/10 | 4.6/10 |

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

## Reasoning

Reasoning quality was evaluated using four benchmark tasks covering arithmetic, scheduling, constraint evaluation and technical troubleshooting.

All four models were tested with the same deterministic benchmark configuration. Qwen3 8B was additionally tested with both thinking disabled and thinking enabled because it explicitly supports Ollama's thinking mode.

### Phi-4 14B

Phi-4 produced the most consistently reliable reasoning responses in the current test set.

It correctly handled the storage calculation, maintenance scheduling, server constraint evaluation and Nginx troubleshooting scenario.

The troubleshooting response correctly recognized that an application listening on `127.0.0.1:5000` remains reachable by Nginx running on the same host and therefore does not by itself prevent the proxied LAN request from working.

### Qwen3 8B

Qwen performed strongly with thinking disabled.

It correctly handled the arithmetic, scheduling and constraint tasks and correctly diagnosed the important distinction between direct LAN access to a loopback-bound backend and same-host access through Nginx.

Enabling thinking did not improve the practical result on these benchmark tasks.

The most significant regression occurred in the troubleshooting benchmark. Two thinking-enabled warm runs generated 40,960 tokens and reached the model's configured context limit instead of producing an appropriately concise response.

This demonstrates that explicit reasoning mode can substantially increase latency and token generation without necessarily improving answer quality.

### Gemma 3 12B

Gemma correctly handled the arithmetic and scheduling tasks and selected the correct server in the constraint-evaluation task.

Its main reasoning failure occurred in the Nginx troubleshooting benchmark.

The response incorrectly treated the application's `127.0.0.1:5000` bind address as preventing Nginx on the same server from reaching the backend. In reality, a same-host Nginx process can connect to a service listening on the loopback interface.

### Llama 3.1 8B

Llama handled the basic arithmetic and scheduling tasks correctly but showed significant errors in the more demanding tests.

In the constraint benchmark it repeatedly treated 25 GB of free disk space as satisfying a requirement for at least 40 GB.

In the troubleshooting benchmark it also incorrectly concluded that the loopback-bound backend prevents same-host Nginx proxying.

### Reasoning conclusion

The reasoning benchmarks show substantial differences that are not visible from raw generation speed alone.

Phi-4 14B produced the most consistently correct reasoning responses in the current test set.

Qwen3 8B also performed strongly with thinking disabled, while its explicit thinking mode introduced very large token and latency overhead and showed a severe failure mode in the troubleshooting benchmark.

Gemma 3 12B and Llama 3.1 8B both produced useful results on simpler reasoning tasks but made important technical reasoning errors in the troubleshooting scenario.

## Workload Recommendations

| Workload | Preliminary recommendation | Reason |
|---|---|---|
| Fast interactive responses | Llama 3.1 8B | Highest measured generation speed and low warm-response latency |
| Finnish-language interaction | Gemma 3 12B | Most natural and reliable Finnish in the current manual evaluation |
| Python programming | Gemma 3 12B / Qwen3 8B | Both produced useful solutions, with Gemma slightly stronger in the current manual evaluation |
| Summarization | Gemma 3 12B | Best combination of instruction following, content preservation and Finnish-language quality |
| General reasoning | Phi-4 14B | Most consistently correct across the current arithmetic, scheduling, constraint and troubleshooting tasks |
| Fast reasoning | Qwen3 8B with thinking disabled | Strong reasoning results combined with substantially higher generation speed than Phi-4 14B |
| Explicit thinking mode | Qwen3 8B, use selectively | Thinking mode increased token generation and latency substantially and showed a severe runaway-generation failure in the troubleshooting test |
| General local assistant | Gemma 3 12B or Qwen3 8B | Gemma emphasizes language quality; Qwen emphasizes speed and strong non-thinking reasoning |

## Speed vs. Quality

The benchmark results demonstrate that generation speed and response quality are separate characteristics.

Llama 3.1 8B was the fastest model in the measured performance benchmarks, but its manual quality scores were the weakest overall and it made important errors in both constraint evaluation and technical troubleshooting.

Qwen3 8B provides a strong balance between generation speed and response quality. Its non-thinking reasoning performance was particularly strong, while explicit thinking mode introduced substantial overhead without improving the tested answers.

Gemma 3 12B remains the strongest model for Finnish-language quality and summarization in the current comparison, although its technical troubleshooting result exposed an important reasoning weakness.

Phi-4 14B was slower than the 8B models and weaker in summarization, but it produced the most consistently correct reasoning responses in the current reasoning test set.

These results reinforce the need to evaluate local language models by workload rather than relying on model size or generation speed alone.

## Overall Conclusion

No single model dominated every measured workload.

Gemma 3 12B produced the strongest overall manual quality score and remains particularly strong for Finnish-language interaction and summarization.

Phi-4 14B produced the strongest reasoning results in the current reasoning benchmark set, correctly handling all four tested task types.

Qwen3 8B provided a strong combination of speed, programming capability and non-thinking reasoning quality. Its explicit thinking mode was considerably more expensive in generated tokens and latency and did not improve the tested reasoning results.

Llama 3.1 8B delivered the highest measured generation speed, but its lower manual quality scores and reasoning errors make the performance advantage workload-dependent.

The comparison therefore supports using different models for different local workloads rather than selecting a model based on a single aggregate metric.

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
- Reasoning scores are based on four deliberately small diagnostic tasks and should not be interpreted as comprehensive measures of general reasoning ability.
- Qwen3 8B was the only tested model with an explicit Ollama thinking capability, so thinking-mode results are not directly comparable across all four models.

As the number of tested models grows, workload-specific recommendations are likely to become more useful than selecting a single overall winner.
