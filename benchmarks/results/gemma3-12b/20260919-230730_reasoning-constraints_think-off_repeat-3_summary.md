# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `gemma3:12b` |
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
| Model family | `gemma3` |
| Model families | `gemma3` |
| Parameter size | `12.2B` |
| Quantization | `Q4_K_M` |
| Model context length | `131072` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 5.519 | 5.538 | 5.478 | 5.541 |
| Generated tokens | 298.333 | 300.0 | 295.0 | 300.0 |
| Generation speed (tokens/s) | 55.927 | 55.95 | 55.82 | 56.01 |

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
| System RAM peak (GiB) | 25.909 | 25.877 | 25.585 | 26.264 |
| System RAM peak delta (GiB) | 0.213 | 0.303 | 0.028 | 0.307 |
| Inference GPU VRAM peak (GiB) | 12.555 | 12.554 | 12.531 | 12.58 |
| Inference GPU VRAM peak delta (GiB) | 0.017 | 0.008 | 0.0 | 0.042 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | warm | 5.478 s | 0.003 s | 295 | 56.01 tok/s |
| 2 | warm | 5.538 s | 0.003 s | 300 | 55.82 tok/s |
| 3 | warm | 5.541 s | 0.003 s | 300 | 55.95 tok/s |
