# Local LLM Performance and Quality Leaderboard

Performance and manually evaluated response quality are ranked separately because faster generation does not guarantee better answers.

## Performance Ranking

| Rank | Model | Parameters | Quantization | Average generation speed | Cold start | Benchmark date |
|---:|---|---:|---|---:|---:|---|
| 1 | Llama 3.1 8B | 8.0B | Q4_K_M | 78.22 tok/s | 35.19 s | 2026-08-05 |
| 2 | Qwen3 8B | 8.2B | Q4_K_M | 74.24 tok/s | 34.72 s | 2026-08-05 |
| 3 | Gemma 3 12B | 12.2B | Q4_K_M | 47.23 tok/s | 64.31 s | 2026-08-05 |

## Manual Quality Ranking

| Rank | Model | Finnish | Python | Summarization | Overall |
|---:|---|---:|---:|---:|---:|
| 1 | Gemma 3 12B | 8.5/10 | 7.5/10 | 8.0/10 | 8.0/10 |
| 2 | Qwen3 8B | 6.0/10 | 7.0/10 | 6.0/10 | 6.3/10 |
| 3 | Llama 3.1 8B | 4.0/10 | 6.0/10 | 3.0/10 | 4.3/10 |

Quality scale: 1.0–10.0, step 0.5.

**Evaluation scope:** Selected Finnish, Python and summarization benchmark responses

## Metadata Sources

| Model | Family | Metadata source |
|---|---|---|
| Llama 3.1 8B | llama | benchmark metadata |
| Qwen3 8B | qwen3 | compatibility override |
| Gemma 3 12B | gemma3 | benchmark metadata |

## Interpretation

- Performance values come from each model's latest all-prompts run.
- Cold start includes model loading from local storage.
- Overall quality is the arithmetic mean of available category scores.
- Manual scores are preliminary human evaluations, not objective facts.

## Quality Comparisons

- [Qwen3 8B vs. Gemma 3 12B](comparisons/qwen3-8b-vs-gemma3-12b.md)
