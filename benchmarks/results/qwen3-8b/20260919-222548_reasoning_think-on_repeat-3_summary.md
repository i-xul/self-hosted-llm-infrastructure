# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
| Prompt | `reasoning.md` |
| Thinking | `on` |
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
| Total duration (s) | 21.532 | 11.609 | 11.591 | 41.395 |
| Generated tokens | 923.0 | 994.0 | 781.0 | 994.0 |
| Generation speed (tokens/s) | 86.16 | 86.14 | 86.04 | 86.3 |

## Cold Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 23.288 | 23.288 | 23.288 | 23.288 |
| System RAM peak delta (GiB) | 4.878 | 4.878 | 4.878 | 4.878 |
| Inference GPU VRAM peak (GiB) | 8.711 | 8.711 | 8.711 | 8.711 |
| Inference GPU VRAM peak delta (GiB) | 5.5 | 5.5 | 5.5 | 5.5 |

## Warm Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 23.491 | 23.491 | 23.433 | 23.549 |
| System RAM peak delta (GiB) | 0.134 | 0.134 | 0.121 | 0.146 |
| Inference GPU VRAM peak (GiB) | 8.711 | 8.711 | 8.711 | 8.711 |
| Inference GPU VRAM peak delta (GiB) | 0.0 | 0.0 | 0.0 | 0.0 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | cold | 41.395 s | 32.173 s | 781 | 86.3 tok/s |
| 2 | warm | 11.591 s | 0.003 s | 994 | 86.14 tok/s |
| 3 | warm | 11.609 s | 0.003 s | 994 | 86.04 tok/s |
