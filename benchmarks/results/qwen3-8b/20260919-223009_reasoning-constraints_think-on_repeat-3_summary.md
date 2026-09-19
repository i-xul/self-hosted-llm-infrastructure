# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
| Prompt | `reasoning-constraints.md` |
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
| Total duration (s) | 6.647 | 6.763 | 6.397 | 6.781 |
| Generated tokens | 568.667 | 581.0 | 544.0 | 581.0 |
| Generation speed (tokens/s) | 86.557 | 86.63 | 86.39 | 86.65 |

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
| System RAM peak (GiB) | 24.681 | 24.688 | 24.588 | 24.768 |
| System RAM peak delta (GiB) | 0.086 | 0.123 | 0.008 | 0.126 |
| Inference GPU VRAM peak (GiB) | 8.824 | 8.824 | 8.824 | 8.825 |
| Inference GPU VRAM peak delta (GiB) | 0.002 | 0.001 | 0.0 | 0.004 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 6.397 s | 0.003 s | 544 | 86.65 tok/s |
| 2 | warm | 6.781 s | 0.003 s | 581 | 86.39 tok/s |
| 3 | warm | 6.763 s | 0.003 s | 581 | 86.63 tok/s |
