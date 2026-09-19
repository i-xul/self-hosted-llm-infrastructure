# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `phi4:14b` |
| Prompt | `reasoning-troubleshooting.md` |
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
| Total duration (s) | 4.529 | 4.484 | 4.483 | 4.621 |
| Generated tokens | 243.333 | 245.0 | 240.0 | 245.0 |
| Generation speed (tokens/s) | 54.94 | 55.01 | 54.79 | 55.02 |

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
| System RAM peak (GiB) | 26.62 | 26.625 | 26.488 | 26.746 |
| System RAM peak delta (GiB) | 0.057 | 0.04 | 0.0 | 0.132 |
| Inference GPU VRAM peak (GiB) | 12.799 | 12.803 | 12.782 | 12.812 |
| Inference GPU VRAM peak delta (GiB) | 0.011 | 0.0 | 0.0 | 0.034 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 4.621 s | 0.003 s | 240 | 54.79 tok/s |
| 2 | warm | 4.483 s | 0.002 s | 245 | 55.02 tok/s |
| 3 | warm | 4.484 s | 0.003 s | 245 | 55.01 tok/s |
