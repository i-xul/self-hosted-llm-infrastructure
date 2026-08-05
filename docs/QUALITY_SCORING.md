# Manual Quality Scoring

This document describes how manual response-quality scores are assigned in the local LLM benchmark project.

The goal is not to claim objective model quality. The scores provide a transparent and repeatable human evaluation of selected benchmark responses on the tested local hardware and runtime configuration.

## Scoring Scale

Scores use a scale from 1 to 10 in 0.5-point increments.

| Score | Interpretation |
|---:|---|
| 9.0–10.0 | Excellent response with only minor or no meaningful issues |
| 7.5–8.5 | Strong response with some identifiable weaknesses |
| 6.0–7.0 | Generally usable response with noticeable limitations |
| 4.0–5.5 | Weak response requiring substantial correction |
| 1.0–3.5 | Poor or unreliable response that fails important requirements |

## Evaluated Categories

### Finnish

The Finnish-language score evaluates:

- naturalness and fluency
- grammar and sentence structure
- vocabulary and terminology
- factual accuracy
- instruction following
- requested length and format
- absence of unnecessary language switching

### Python

The Python score evaluates:

- whether the program is complete and runnable
- use of the requested libraries and interfaces
- command-line argument handling
- error handling
- exit codes
- validation of user input
- instruction following
- clarity and maintainability
- unnecessary verbosity or complexity

The score is based primarily on source-code review. Generated programs should eventually also be execution-tested.

### Summarization

The summarization score evaluates:

- preservation of the main arguments and conclusions
- compliance with sentence or length limits
- absence of unsupported claims
- neutral tone
- natural Finnish
- correct terminology
- avoidance of unnecessary introductions or commentary

## Overall Score

The overall score is calculated automatically as the arithmetic mean of the available category scores.

For the current three categories:

```text
overall = (finnish + python + summarization) / 3
```

The overall score is not intended to replace category-specific analysis. A model may perform very differently across tasks.

## Evaluation Process

1. Run the same version-controlled benchmark prompts for every model.
2. Preserve the original model outputs without editing them.
3. Review selected response categories manually.
4. Record category scores and written observations in:

```text
benchmarks/quality/quality_scores.json
```

5. Generate the combined leaderboard:

```powershell
python .\benchmarks\leaderboard.py
```

6. Document broader conclusions in model comparison files under:

```text
benchmarks/comparisons/
```

## Evaluation Principles

Manual evaluation should follow these principles:

- Judge the generated response, not the reputation of the model family.
- Apply the same requirements to every model.
- Do not reward unnecessary length.
- Penalize factual errors even when the language is fluent.
- Penalize ignored formatting, language or length instructions.
- Distinguish minor wording issues from errors that affect practical usability.
- Record the reason for each score in the quality score notes.
- Treat all early scores as preliminary.

## Current Limitations

The current quality scores are based on selected responses reviewed by one evaluator.

They are therefore:

- subjective
- limited in sample size
- not blind evaluations
- not based on multiple reviewers
- not full measures of general model intelligence
- not substitutes for established academic benchmarks

Future improvements may include:

- repeated response sampling
- blind model comparison
- multiple human reviewers
- execution testing of generated programs
- weighted category scoring
- additional categories
- automated consistency checks
- separate factual-accuracy scoring

## Updating Scores

Scores may be updated when:

- a model is benchmarked with a newer version
- prompts are changed
- additional runs reveal inconsistent behavior
- generated code is execution-tested
- the evaluation methodology is expanded

Any meaningful score change should be documented in Git history and comparison notes.
