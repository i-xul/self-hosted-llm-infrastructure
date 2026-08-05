# Qwen3 8B vs. Gemma 3 12B

This document compares Qwen3 8B and Gemma 3 12B using the same local hardware, inference engine, benchmark prompts and runtime configuration.

The comparison combines automatically collected performance metrics with manual observations of response quality.

## Test Environment

| Component | Value |
|---|---|
| Operating system | Windows 11 |
| CPU | AMD Ryzen 9 7900X |
| System memory | 32 GB |
| GPU | AMD Radeon RX 7800 XT |
| VRAM | 16 GB |
| Inference engine | Ollama 0.32.5 |
| Python | 3.13.14 |
| Quantization | Q4_K_M |
| Benchmark context size | 4096 |
| Temperature | 0 |
| Seed | 42 |

Both models were successfully loaded entirely onto the GPU.

## Model Specifications

| Model | Parameters | Stored size | Maximum context | GPU placement |
|---|---:|---:|---:|---|
| Qwen3 8B | 8.2B | 5.2 GB | 40,960 | 100% GPU |
| Gemma 3 12B | 12.2B | 8.1 GB | 131,072 | 100% GPU |

## Performance Overview

| Metric | Qwen3 8B | Gemma 3 12B |
|---|---:|---:|
| Cold start, Finnish prompt | 34.722 s | 64.307 s |
| Finnish generation speed | 75.13 tok/s | 48.11 tok/s |
| Linux generation speed | 73.92 tok/s | 46.39 tok/s |
| Networking generation speed | 73.78 tok/s | 46.49 tok/s |
| Python generation speed | 74.23 tok/s | 46.92 tok/s |
| Raspberry Pi generation speed | 73.80 tok/s | 46.38 tok/s |
| Reasoning generation speed | 74.64 tok/s | 48.35 tok/s |
| Summarization generation speed | 74.19 tok/s | 47.99 tok/s |

Qwen3 8B generated approximately 74–75 tokens per second, while Gemma 3 12B generated approximately 46–48 tokens per second.

Gemma required substantially more time to load from HDD and generated longer answers in several technical categories.

## Finnish Language

### Qwen3 8B

Observed strengths:

- Produced understandable Finnish.
- Followed the requested topic.
- Generated a concise answer.

Observed weaknesses:

- Used several unnatural expressions.
- Produced wording such as `Raspberry Pi -koulutusjärjestö`.
- The response was substantially shorter than the requested approximately 150 words.
- Grammar and sentence construction occasionally sounded translated.

### Gemma 3 12B

Observed strengths:

- Produced more natural and fluent Finnish.
- Organized the answer clearly.
- Followed the requested length more closely.
- Explained common Raspberry Pi use cases effectively.

Observed weaknesses:

- Claimed that the price is generally below 50 euros, which is too broad and may not remain accurate.
- Some expressions were repetitive, but the overall language quality was stronger than Qwen3 8B.

### Initial conclusion

Gemma 3 12B produced the stronger Finnish-language response, although Qwen3 8B was considerably faster.

## Python Programming

### Qwen3 8B

Observed strengths:

- Produced a functional standard-library TCP connection example.
- Used command-line arguments.
- Included basic error handling.
- Produced a relatively concise response.

Observed weaknesses:

- The initial manually tested response contained wording and argument-description issues.
- Further execution testing is required for the formal benchmark output.

### Gemma 3 12B

Observed strengths:

- Produced a complete and readable Python program.
- Used only the Python standard library.
- Handled invalid hostnames and connection errors.
- Returned meaningful exit codes.
- Included usage instructions.

Observed weaknesses:

- The timeout was configurable only as a function argument, not through the command line as requested.
- The response was considerably more verbose than necessary.
- Catching the general `Exception` class is broader than ideal.
- Port-range validation was missing.

### Initial conclusion

Gemma produced a comprehensive and mostly usable solution, but it did not fully satisfy every requirement. Qwen was more concise, while Gemma provided more explanation and defensive handling.

## Summarization

### Qwen3 8B

Observed strengths:

- Identified the main topic.
- Captured the general arguments.

Observed weaknesses:

- Earlier Finnish output contained unnatural wording.
- Additional direct comparison of the final benchmark response is still useful.

### Gemma 3 12B

Observed strengths:

- Stayed within the five-sentence limit.
- Preserved the main benefits, risks and pilot decision.
- Did not add major unsupported claims.
- Produced a clear and useful summary.

Observed weaknesses:

- Started with the English sentence `Here's a summary in Finnish`.
- Used `keskuspalvelin`, although the source referred more specifically to a virtualization host.
- The Finnish summary itself was otherwise natural.

### Initial conclusion

Gemma performed well in summarization and followed the structural constraints, but it failed to keep the entire response in Finnish.

## Resource and Usability Trade-offs

### Qwen3 8B

Advantages:

- Faster model loading.
- Approximately 55–60% higher token generation speed.
- Lower storage and VRAM requirements.
- Suitable for fast interactive use.

Disadvantages:

- Weaker Finnish wording in the initial tests.
- Less consistent instruction following.
- Shorter and sometimes less polished answers.

### Gemma 3 12B

Advantages:

- Better Finnish-language quality.
- More detailed technical responses.
- Larger maximum context length.
- Still fits entirely within 16 GB of VRAM.

Disadvantages:

- Significantly slower cold start from HDD.
- Lower token generation speed.
- Frequently produces unnecessarily long responses.
- Some instructions were only partially followed.

## Preliminary Recommendation

Qwen3 8B is currently the stronger option when speed, responsiveness and lower resource usage are priorities.

Gemma 3 12B is currently the stronger option when Finnish-language quality, detailed explanations and longer-context capability are more important.

Neither model can yet be declared universally better. The preferred model depends on the workload:

| Workload | Preliminary preference |
|---|---|
| Fast interactive chat | Qwen3 8B |
| Finnish-language explanations | Gemma 3 12B |
| Concise technical assistance | Qwen3 8B |
| Detailed technical guidance | Gemma 3 12B |
| Long-context workloads | Gemma 3 12B |
| Lower resource consumption | Qwen3 8B |

## Limitations

This comparison is based on one complete benchmark pass per model and selected manual observations.

Future testing should include:

- multiple repeated runs
- execution testing of generated code
- reasoning-mode comparisons
- longer context tests
- additional models
- more structured human evaluation

The conclusions in this document should therefore be treated as preliminary rather than final.