# Repeated Benchmark Summary

## Configuration

| Item | Value |
|---|---|
| Summary timestamp | `2026-08-05T19:40:30.494774+03:00` |
| Batch timestamp | `20260805-193938` |
| Model | `qwen3:8b` |
| Prompt | `finnish.md` |
| Thinking | `off` |
| Context size | `4096` |
| Temperature | `0` |
| Seed | `42` |
| Runs | `3` |
| Cold runs | `1` |
| Warm runs | `2` |

## Aggregate Statistics

| Metric | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Total duration (s) | 13.21 | 2.241 | 2.228 | 35.162 |
| Model load duration (s) | 10.996 | 0.137 | 0.125 | 32.725 |
| Generated tokens | 160.0 | 156.0 | 156.0 | 168.0 |
| Generation duration (s) | 2.125 | 2.068 | 2.066 | 2.241 |
| Generation speed (tokens/s) | 75.313 | 75.45 | 74.98 | 75.51 |

## Individual Runs

| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |
|---:|---|---:|---:|---:|---:|
| 1 | cold | 35.162 s | 32.725 s | 168 | 74.98 tok/s |
| 2 | warm | 2.241 s | 0.137 s | 156 | 75.51 tok/s |
| 3 | warm | 2.228 s | 0.125 s | 156 | 75.45 tok/s |
