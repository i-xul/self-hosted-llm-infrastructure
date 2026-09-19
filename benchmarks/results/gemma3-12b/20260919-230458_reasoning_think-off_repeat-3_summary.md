# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `gemma3:12b` |
| Prompt | `reasoning.md` |
| Thinking | `off` |
| Runs | `3` |
| Cold runs | `1` |
| Warm runs | `2` |

## Environment

| Item | Value |
|---|---|
| Operating system | `Windows-11-10.0.26200-SP0` |
| Machine architecture | `AMD64` |
| Python version | `3.13.15` |
| Python implementation | `CPython` |
| Ollama version | `0.34.1` |
| Model format | `gguf` |
| Model family | `gemma3` |
| Model families | `gemma3` |
| Parameter size | `12.2B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 21.286 | 4.628 | 4.533 | 54.697 |
| Generated tokens | 249.0 | 249.0 | 249.0 | 249.0 |
| Generation speed (tokens/s) | 55.757 | 55.66 | 55.48 | 56.13 |

## Cold Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 25.237 | 25.237 | 25.237 | 25.237 |
| System RAM peak delta (GiB) | 7.292 | 7.292 | 7.292 | 7.292 |
| Inference GPU VRAM peak (GiB) | 12.424 | 12.424 | 12.424 | 12.424 |
| Inference GPU VRAM peak delta (GiB) | 9.144 | 9.144 | 9.144 | 9.144 |

## Warm Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 25.444 | 25.444 | 25.427 | 25.46 |
| System RAM peak delta (GiB) | 0.271 | 0.271 | 0.094 | 0.448 |
| Inference GPU VRAM peak (GiB) | 12.453 | 12.453 | 12.436 | 12.47 |
| Inference GPU VRAM peak delta (GiB) | 0.036 | 0.036 | 0.0 | 0.072 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | cold | 54.697 s | 50.025 s | 249 | 55.66 tok/s |
| 2 | warm | 4.628 s | 0.003 s | 249 | 55.48 tok/s |
| 3 | warm | 4.533 s | 0.003 s | 249 | 56.13 tok/s |
