# Local LLM Performance Leaderboard

This leaderboard is generated automatically from the latest all-prompts master summary for each tested model.

Models are currently ranked by average token generation speed. Response quality is evaluated separately in the comparison documents.

## Performance Ranking

| Rank | Model | Parameters | Quantization | Average generation speed | Cold start | Benchmark date |
|---:|---|---:|---|---:|---:|---|
| 1 | Qwen3 8B | 8.2B | Q4_K_M | 74.24 tok/s | 34.72 s | 2026-08-05 |
| 2 | Gemma 3 12B | 12.2B | Q4_K_M | 47.23 tok/s | 64.31 s | 2026-08-05 |

## Metadata Sources

| Model | Family | Metadata source |
|---|---|---|
| Qwen3 8B | qwen3 | compatibility override |
| Gemma 3 12B | gemma3 | benchmark metadata |

## Interpretation

- Average generation speed is calculated across the full all-prompts benchmark pass.
- Cold start includes loading the model from local storage.
- All current models use Q4_K_M quantization and were tested with GPU acceleration.
- A higher token rate does not automatically indicate better response quality.
- Manual quality comparisons are stored in `benchmarks/comparisons/`.

## Quality Comparisons

Performance metrics should be interpreted together with manual response-quality evaluations.

- [Qwen3 8B vs. Gemma 3 12B](comparisons/qwen3-8b-vs-gemma3-12b.md)