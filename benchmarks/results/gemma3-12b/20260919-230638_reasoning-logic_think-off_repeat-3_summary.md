# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `gemma3:12b` |
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
| Model family | `gemma3` |
| Model families | `gemma3` |
| Parameter size | `12.2B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 5.067 | 5.036 | 5.008 | 5.158 |
| Generated tokens | 275.0 | 275.0 | 275.0 | 275.0 |
| Generation speed (tokens/s) | 56.187 | 56.22 | 56.05 | 56.29 |

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
| System RAM peak (GiB) | 25.531 | 25.582 | 25.424 | 25.587 |
| System RAM peak delta (GiB) | 0.07 | 0.022 | 0.022 | 0.167 |
| Inference GPU VRAM peak (GiB) | 12.543 | 12.538 | 12.538 | 12.554 |
| Inference GPU VRAM peak delta (GiB) | 0.054 | 0.016 | 0.0 | 0.145 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 5.158 s | 0.003 s | 275 | 56.22 tok/s |
| 2 | warm | 5.036 s | 0.002 s | 275 | 56.29 tok/s |
| 3 | warm | 5.008 s | 0.003 s | 275 | 56.05 tok/s |
