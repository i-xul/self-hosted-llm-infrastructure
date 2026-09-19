# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
| Prompt | `reasoning-constraints.md` |
| Thinking | `off` |
| Runs | `3` |
| Cold runs | `0` |
| Warm runs | `3` |

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
| Total duration (s) | 3.227 | 3.213 | 3.179 | 3.288 |
| Generated tokens | 274.0 | 274.0 | 274.0 | 274.0 |
| Generation speed (tokens/s) | 86.573 | 86.51 | 86.38 | 86.83 |

## Cold Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | None | None | None | None |
| System RAM peak delta (GiB) | None | None | None | None |
| Inference GPU VRAM peak (GiB) | None | None | None | None |
| Inference GPU VRAM peak delta (GiB) | None | None | None | None |

## Warm Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 23.532 | 23.523 | 23.511 | 23.561 |
| System RAM peak delta (GiB) | 0.041 | 0.036 | 0.0 | 0.087 |
| Inference GPU VRAM peak (GiB) | 8.883 | 8.851 | 8.851 | 8.948 |
| Inference GPU VRAM peak delta (GiB) | 0.002 | 0.001 | 0.0 | 0.004 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 3.288 s | 0.003 s | 274 | 86.51 tok/s |
| 2 | warm | 3.213 s | 0.003 s | 274 | 86.38 tok/s |
| 3 | warm | 3.179 s | 0.003 s | 274 | 86.83 tok/s |
