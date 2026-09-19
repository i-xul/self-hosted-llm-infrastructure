# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `llama3.1:8b` |
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
| Model family | `llama` |
| Model families | `llama` |
| Parameter size | `8.0B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 1.363 | 1.421 | 1.244 | 1.424 |
| Generated tokens | 122.333 | 132.0 | 103.0 | 132.0 |
| Generation speed (tokens/s) | 94.55 | 94.37 | 94.14 | 95.14 |

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
| System RAM peak (GiB) | 22.289 | 22.294 | 22.272 | 22.3 |
| System RAM peak delta (GiB) | 0.021 | 0.022 | 0.014 | 0.028 |
| Inference GPU VRAM peak (GiB) | 8.572 | 8.572 | 8.572 | 8.572 |
| Inference GPU VRAM peak delta (GiB) | 0.052 | 0.0 | 0.0 | 0.155 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 1.244 s | 0.003 s | 103 | 95.14 tok/s |
| 2 | warm | 1.424 s | 0.003 s | 132 | 94.14 tok/s |
| 3 | warm | 1.421 s | 0.003 s | 132 | 94.37 tok/s |
