# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `phi4:14b` |
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
| Model family | `phi3` |
| Model families | `phi3` |
| Parameter size | `14.7B` |
| Quantization | `Q4_K_M` |
| Model context length | `16384` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 5.564 | 5.656 | 5.377 | 5.66 |
| Generated tokens | 300.667 | 310.0 | 282.0 | 310.0 |
| Generation speed (tokens/s) | 55.17 | 55.32 | 54.87 | 55.32 |

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
| System RAM peak (GiB) | 26.315 | 26.313 | 26.234 | 26.397 |
| System RAM peak delta (GiB) | 0.087 | 0.087 | 0.085 | 0.089 |
| Inference GPU VRAM peak (GiB) | 12.846 | 12.856 | 12.816 | 12.865 |
| Inference GPU VRAM peak delta (GiB) | 0.098 | 0.0 | 0.0 | 0.293 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 5.377 s | 0.002 s | 282 | 54.87 tok/s |
| 2 | warm | 5.656 s | 0.002 s | 310 | 55.32 tok/s |
| 3 | warm | 5.66 s | 0.003 s | 310 | 55.32 tok/s |
