# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
| Prompt | `reasoning-logic.md` |
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
| Total duration (s) | 5.024 | 4.728 | 4.587 | 5.758 |
| Generated tokens | 414.0 | 383.0 | 383.0 | 476.0 |
| Generation speed (tokens/s) | 83.62 | 84.44 | 81.91 | 84.51 |

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
| System RAM peak (GiB) | 23.475 | 23.491 | 23.342 | 23.592 |
| System RAM peak delta (GiB) | 0.086 | 0.126 | 0.0 | 0.133 |
| Inference GPU VRAM peak (GiB) | 8.856 | 8.834 | 8.802 | 8.931 |
| Inference GPU VRAM peak delta (GiB) | 0.093 | 0.094 | 0.059 | 0.127 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 5.758 s | 0.003 s | 476 | 84.44 tok/s |
| 2 | warm | 4.587 s | 0.003 s | 383 | 84.51 tok/s |
| 3 | warm | 4.728 s | 0.003 s | 383 | 81.91 tok/s |
