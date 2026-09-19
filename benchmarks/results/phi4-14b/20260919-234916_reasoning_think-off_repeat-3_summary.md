# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `phi4:14b` |
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
| Model family | `phi3` |
| Model families | `phi3` |
| Parameter size | `14.7B` |
| Quantization | `Q4_K_M` |
| Model context length | `16384` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 26.929 | 8.727 | 8.697 | 63.364 |
| Generated tokens | 463.0 | 471.0 | 447.0 | 471.0 |
| Generation speed (tokens/s) | 54.51 | 54.57 | 54.34 | 54.62 |

## Cold Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 26.131 | 26.131 | 26.131 | 26.131 |
| System RAM peak delta (GiB) | 8.494 | 8.494 | 8.494 | 8.494 |
| Inference GPU VRAM peak (GiB) | 12.543 | 12.543 | 12.543 | 12.543 |
| Inference GPU VRAM peak delta (GiB) | 9.405 | 9.405 | 9.405 | 9.405 |

## Warm Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 26.254 | 26.254 | 26.178 | 26.329 |
| System RAM peak delta (GiB) | 0.116 | 0.116 | 0.084 | 0.148 |
| Inference GPU VRAM peak (GiB) | 12.588 | 12.588 | 12.571 | 12.605 |
| Inference GPU VRAM peak delta (GiB) | 0.028 | 0.028 | 0.026 | 0.029 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | cold | 63.364 s | 55.006 s | 447 | 54.62 tok/s |
| 2 | warm | 8.727 s | 0.003 s | 471 | 54.34 tok/s |
| 3 | warm | 8.697 s | 0.003 s | 471 | 54.57 tok/s |
