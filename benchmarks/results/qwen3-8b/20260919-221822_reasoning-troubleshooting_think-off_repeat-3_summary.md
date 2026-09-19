# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `qwen3:8b` |
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
| Model family | `qwen3` |
| Model families | `qwen3` |
| Parameter size | `8.2B` |
| Quantization | `Q4_K_M` |
| Model context length | `40960` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 2.088 | 1.982 | 1.978 | 2.303 |
| Generated tokens | 174.667 | 169.0 | 169.0 | 186.0 |
| Generation speed (tokens/s) | 86.593 | 86.44 | 86.33 | 87.01 |

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
| System RAM peak (GiB) | 23.484 | 23.485 | 23.478 | 23.489 |
| System RAM peak delta (GiB) | 0.01 | 0.0 | 0.0 | 0.031 |
| Inference GPU VRAM peak (GiB) | 8.866 | 8.866 | 8.866 | 8.866 |
| Inference GPU VRAM peak delta (GiB) | 0.002 | 0.0 | 0.0 | 0.007 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 2.303 s | 0.003 s | 186 | 87.01 tok/s |
| 2 | warm | 1.982 s | 0.003 s | 169 | 86.33 tok/s |
| 3 | warm | 1.978 s | 0.003 s | 169 | 86.44 tok/s |
