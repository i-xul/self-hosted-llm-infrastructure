# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
| Prompt | `reasoning-logic.md` |
| Thinking | `on` |
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
| Total duration (s) | 45.319 | 45.114 | 44.924 | 45.919 |
| Generated tokens | 3743.0 | 3716.0 | 3716.0 | 3797.0 |
| Generation speed (tokens/s) | 82.88 | 82.91 | 82.77 | 82.96 |

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
| System RAM peak (GiB) | 24.081 | 24.089 | 23.569 | 24.586 |
| System RAM peak delta (GiB) | 0.392 | 0.53 | 0.035 | 0.612 |
| Inference GPU VRAM peak (GiB) | 8.81 | 8.81 | 8.81 | 8.811 |
| Inference GPU VRAM peak delta (GiB) | 0.033 | 0.001 | 0.0 | 0.098 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 45.919 s | 0.003 s | 3797 | 82.91 tok/s |
| 2 | warm | 44.924 s | 0.004 s | 3716 | 82.96 tok/s |
| 3 | warm | 45.114 s | 0.003 s | 3716 | 82.77 tok/s |
