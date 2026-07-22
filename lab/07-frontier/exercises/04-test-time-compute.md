# Exercise 04 — Test-Time Compute

Treat inference-time strategies as a capability lever and measure them with `llab eval`.

## Prerequisites

- Exercise 03 complete (at least one logged or draft `LL-` helps Exercise 05).
- `llab eval` working from module 04.
- `LAB_JUDGE_MODEL` set to a stronger local model for best-of-N scoring (optional but recommended).

## Derive first

In `notes.md`, before running anything:

1. Define test-time compute in one sentence.
2. Predict which task types benefit from CoT vs hurt from it.
3. Predict whether best-of-N helps your logged weakness from Exercise 03.

## Tasks

### 1. Build a dataset

Author ≥20 JSONL examples in `lab/07-frontier/exercises/data/test-time-compute.jsonl` (create `data/` if needed):

```json
{"prompt": "...", "expected": "...", "task_type": "math|factual|format|..."}
```

Mix at least three task types. Include 3–5 examples where you expect CoT to **hurt** (latency-sensitive or simple).

**Done when:** file validates and loads with `llab eval`.

### 2. Three strategies

On the same model and dataset, run:

| Strategy | Description |
|----------|-------------|
| **Greedy** | Default decode, no CoT instruction |
| **CoT** | Add a system or prefix that asks for step-by-step reasoning before the answer |
| **Best-of-N** | N=3 or N=5 samples; score with exact-match or LLM-judge; take the best |

Implement via scripts you write (Learn mode — user implements core loop). Route generation through `llab.client.generate`.

**Done when:** each strategy produces a scored run.

### 3. Measure and compare

Run `llab eval` for each strategy. Report:

- Mean score per strategy
- Score by `task_type` (which types flip?)
- Variance: rerun the winning strategy 3 times — is the gain stable?

**Done when:** table of baseline vs CoT vs best-of-N with variance noted.

### 4. Cost tradeoff

For your local setup, note approximate relative cost (tokens generated, wall time) for the best-performing strategy vs greedy.

**Done when:** one paragraph answers "when is the extra compute worth it here?"

## Capture

Write observations in [`../notes.md`](../notes.md). Pass the comprehension gate before drafting `docs/concepts/CONCEPT-test-time-compute.md`.

If best-of-N or CoT **fixes** your Exercise 03 weakness, note that — Exercise 05 may formalize it as a `TECH-`.
