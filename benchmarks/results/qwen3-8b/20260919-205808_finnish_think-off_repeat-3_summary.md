# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
| Prompt | `finnish.md` |
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
| Total duration (s) | 12.727 | 1.77 | 1.769 | 34.643 |
| Generated tokens | 152.0 | 152.0 | 152.0 | 152.0 |
| Generation speed (tokens/s) | 87.283 | 87.06 | 86.92 | 87.87 |

## Cold Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 22.567 | 22.567 | 22.567 | 22.567 |
| System RAM peak delta (GiB) | 4.937 | 4.937 | 4.937 | 4.937 |
| Inference GPU VRAM peak (GiB) | 8.637 | 8.637 | 8.637 | 8.637 |
| Inference GPU VRAM peak delta (GiB) | 5.609 | 5.609 | 5.609 | 5.609 |

## Warm Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 22.63 | 22.63 | 22.627 | 22.633 |
| System RAM peak delta (GiB) | 0.009 | 0.009 | 0.0 | 0.017 |
| Inference GPU VRAM peak (GiB) | 8.564 | 8.564 | 8.493 | 8.636 |
| Inference GPU VRAM peak delta (GiB) | 0.011 | 0.011 | 0.0 | 0.023 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | cold | 34.643 s | 32.717 s | 152 | 86.92 tok/s |
| 2 | warm | 1.77 s | 0.003 s | 152 | 87.87 tok/s |
| 3 | warm | 1.769 s | 0.003 s | 152 | 87.06 tok/s |
