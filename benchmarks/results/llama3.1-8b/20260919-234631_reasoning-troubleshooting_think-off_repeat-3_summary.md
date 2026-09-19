# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `llama3.1:8b` |
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
| Model family | `llama` |
| Model families | `llama` |
| Parameter size | `8.0B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 3.984 | 3.513 | 3.494 | 4.944 |
| Generated tokens | 363.667 | 322.0 | 322.0 | 447.0 |
| Generation speed (tokens/s) | 93.12 | 93.11 | 92.97 | 93.28 |

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
| System RAM peak (GiB) | 22.404 | 22.399 | 22.392 | 22.422 |
| System RAM peak delta (GiB) | 0.056 | 0.032 | 0.024 | 0.112 |
| Inference GPU VRAM peak (GiB) | 8.578 | 8.573 | 8.571 | 8.589 |
| Inference GPU VRAM peak delta (GiB) | 0.006 | 0.0 | 0.0 | 0.018 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 4.944 s | 0.003 s | 447 | 93.11 tok/s |
| 2 | warm | 3.513 s | 0.002 s | 322 | 92.97 tok/s |
| 3 | warm | 3.494 s | 0.002 s | 322 | 93.28 tok/s |
