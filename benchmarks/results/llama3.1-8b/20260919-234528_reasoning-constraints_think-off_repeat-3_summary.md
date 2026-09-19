# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `llama3.1:8b` |
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
| Model family | `llama` |
| Model families | `llama` |
| Parameter size | `8.0B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 2.338 | 2.274 | 2.272 | 2.468 |
| Generated tokens | 212.333 | 209.0 | 209.0 | 219.0 |
| Generation speed (tokens/s) | 93.573 | 93.55 | 93.52 | 93.65 |

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
| System RAM peak (GiB) | 22.347 | 22.349 | 22.299 | 22.392 |
| System RAM peak delta (GiB) | 0.047 | 0.055 | 0.025 | 0.06 |
| Inference GPU VRAM peak (GiB) | 8.572 | 8.572 | 8.572 | 8.572 |
| Inference GPU VRAM peak delta (GiB) | 0.0 | 0.0 | 0.0 | 0.001 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 2.468 s | 0.003 s | 219 | 93.55 tok/s |
| 2 | warm | 2.274 s | 0.003 s | 209 | 93.52 tok/s |
| 3 | warm | 2.272 s | 0.003 s | 209 | 93.65 tok/s |
