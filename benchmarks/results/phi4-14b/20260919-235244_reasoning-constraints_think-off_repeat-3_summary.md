# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `phi4:14b` |
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
| Model family | `phi3` |
| Model families | `phi3` |
| Parameter size | `14.7B` |
| Quantization | `Q4_K_M` |
| Model context length | `16384` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 7.337 | 7.356 | 7.297 | 7.359 |
| Generated tokens | 398.667 | 402.0 | 392.0 | 402.0 |
| Generation speed (tokens/s) | 55.13 | 55.13 | 55.13 | 55.13 |

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
| System RAM peak (GiB) | 26.448 | 26.46 | 26.325 | 26.56 |
| System RAM peak delta (GiB) | 0.086 | 0.122 | 0.0 | 0.136 |
| Inference GPU VRAM peak (GiB) | 12.767 | 12.767 | 12.767 | 12.767 |
| Inference GPU VRAM peak delta (GiB) | 0.002 | 0.0 | 0.0 | 0.006 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 7.297 s | 0.003 s | 392 | 55.13 tok/s |
| 2 | warm | 7.356 s | 0.002 s | 402 | 55.13 tok/s |
| 3 | warm | 7.359 s | 0.002 s | 402 | 55.13 tok/s |
