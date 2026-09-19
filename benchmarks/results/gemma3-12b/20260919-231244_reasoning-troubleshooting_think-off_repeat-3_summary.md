# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `gemma3:12b` |
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
| Model family | `gemma3` |
| Model families | `gemma3` |
| Parameter size | `12.2B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 4.427 | 4.696 | 3.888 | 4.698 |
| Generated tokens | 235.667 | 253.0 | 201.0 | 253.0 |
| Generation speed (tokens/s) | 55.45 | 55.28 | 55.22 | 55.85 |

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
| System RAM peak (GiB) | 26.313 | 26.28 | 26.176 | 26.484 |
| System RAM peak delta (GiB) | 0.098 | 0.115 | 0.0 | 0.179 |
| Inference GPU VRAM peak (GiB) | 12.688 | 12.691 | 12.683 | 12.691 |
| Inference GPU VRAM peak delta (GiB) | 0.007 | 0.007 | 0.006 | 0.008 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 3.888 s | 0.003 s | 201 | 55.85 tok/s |
| 2 | warm | 4.696 s | 0.003 s | 253 | 55.22 tok/s |
| 3 | warm | 4.698 s | 0.003 s | 253 | 55.28 tok/s |
