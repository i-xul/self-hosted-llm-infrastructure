# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
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
| Model family | `qwen3` |
| Model families | `qwen3` |
| Parameter size | `8.2B` |
| Quantization | `Q4_K_M` |
| Model context length | `40960` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 20.044 | 3.518 | 3.515 | 53.099 |
| Generated tokens | 294.0 | 298.0 | 286.0 | 298.0 |
| Generation speed (tokens/s) | 85.96 | 85.97 | 85.87 | 86.04 |

## Cold Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 23.198 | 23.198 | 23.198 | 23.198 |
| System RAM peak delta (GiB) | 4.95 | 4.95 | 4.95 | 4.95 |
| Inference GPU VRAM peak (GiB) | 8.763 | 8.763 | 8.763 | 8.763 |
| Inference GPU VRAM peak delta (GiB) | 5.52 | 5.52 | 5.52 | 5.52 |

## Warm Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 23.276 | 23.276 | 23.243 | 23.31 |
| System RAM peak delta (GiB) | 0.048 | 0.048 | 0.036 | 0.06 |
| Inference GPU VRAM peak (GiB) | 8.799 | 8.799 | 8.775 | 8.822 |
| Inference GPU VRAM peak delta (GiB) | 0.028 | 0.028 | 0.008 | 0.048 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | cold | 53.099 s | 49.581 s | 286 | 86.04 tok/s |
| 2 | warm | 3.518 s | 0.003 s | 298 | 85.87 tok/s |
| 3 | warm | 3.515 s | 0.003 s | 298 | 85.97 tok/s |
