# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Model | `llama3.1:8b` |
| Prompt | `reasoning.md` |
| Thinking | `off` |
| Runs | `3` |
| Cold runs | `1` |
| Warm runs | `2` |

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
| Total duration (s) | 13.376 | 2.702 | 2.688 | 34.738 |
| Generated tokens | 250.0 | 250.0 | 250.0 | 250.0 |
| Generation speed (tokens/s) | 93.95 | 93.91 | 93.82 | 94.12 |

## Cold Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 22.39 | 22.39 | 22.39 | 22.39 |
| System RAM peak delta (GiB) | 4.737 | 4.737 | 4.737 | 4.737 |
| Inference GPU VRAM peak (GiB) | 8.417 | 8.417 | 8.417 | 8.417 |
| Inference GPU VRAM peak delta (GiB) | 5.159 | 5.159 | 5.159 | 5.159 |

## Warm Run Resource Statistics

| Resource metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| System RAM peak (GiB) | 22.36 | 22.36 | 22.349 | 22.371 |
| System RAM peak delta (GiB) | 0.041 | 0.041 | 0.007 | 0.074 |
| Inference GPU VRAM peak (GiB) | 8.417 | 8.417 | 8.417 | 8.417 |
| Inference GPU VRAM peak delta (GiB) | 0.0 | 0.0 | 0.0 | 0.0 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | cold | 34.738 s | 31.961 s | 250 | 94.12 tok/s |
| 2 | warm | 2.702 s | 0.002 s | 250 | 93.91 tok/s |
| 3 | warm | 2.688 s | 0.003 s | 250 | 93.82 tok/s |
