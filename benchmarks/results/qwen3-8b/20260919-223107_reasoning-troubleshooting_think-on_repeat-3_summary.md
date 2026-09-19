# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
| Prompt | `reasoning-troubleshooting.md` |
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
| Total duration (s) | 365.618 | 513.556 | 69.325 | 513.973 |
| Generated tokens | 29189.0 | 40960.0 | 5647.0 | 40960.0 |
| Generation speed (tokens/s) | 80.397 | 79.8 | 79.74 | 81.65 |

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
| System RAM peak (GiB) | 25.174 | 25.31 | 24.815 | 25.396 |
| System RAM peak delta (GiB) | 0.332 | 0.343 | 0.048 | 0.605 |
| Inference GPU VRAM peak (GiB) | 8.878 | 8.845 | 8.831 | 8.959 |
| Inference GPU VRAM peak delta (GiB) | 0.045 | 0.007 | 0.0 | 0.129 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 69.325 s | 0.003 s | 5647 | 81.65 tok/s |
| 2 | warm | 513.973 s | 0.003 s | 40960 | 79.74 tok/s |
| 3 | warm | 513.556 s | 0.003 s | 40960 | 79.8 tok/s |
