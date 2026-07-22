# Exercise 01 — Modern Stack Map

Build a mental model of the 2024–2026 LLM pipeline and locate behavioral differences across model variants.

## Prerequisites

- Modules 01–03 conceptually (transformer, inference, training stages).
- `uv sync` and a working Ollama (or other) backend via `llab.client.generate`.
- Three model variants available locally: **base**, **instruct**, and optionally a **reasoning** or larger instruct model. Pick any open-weight family; record choices in `notes.md`.

## Derive first

On paper, draw the pipeline:

```
pretrain → [mid-training] → SFT → [preference optimization] → deployment → [inference-time techniques]
```

For each stage, fill in:

1. **What changes** — weights, data, objective, or nothing (inference-only)?
2. **What you can measure** — loss, benchmark score, format compliance, latency, cost?
3. **One failure mode** — something that can go wrong at this stage.

## Tasks

### 1. Stack map

Complete the diagram above in `notes.md`. Use your own words; do not copy a blog diagram blindly.

**Done when:** every box has all three fields filled.

### 2. Variant prompt suite

Author 8–10 prompts spanning:

- Factual QA (one-hop)
- Format constraint (e.g. JSON with two keys)
- Refusal edge case (benign but sensitive-sounding)
- Short reasoning (math or logic, no calculator)
- Creative (one paragraph)

Run the **same suite** on base and instruct variants via `llab.client.generate` (or Ollama CLI). Save outputs in `notes.md` or a local scratch file (not committed if large).

**Done when:** you have side-by-side outputs for every prompt on at least two variants.

### 3. Stage attribution

For each behavioral difference you observe, write which pipeline stage **most likely** caused it. Include at least one case where you're uncertain.

**Done when:** you have ≥5 attributions with at least one counterexample or misattribution you can explain.

### 4. Literature check

Read one primary source from the module README (technical report or DPO paper). Verify **one claim** from the paper against something you observed locally — even if your models are too small to reproduce numbers, say whether the *direction* matches.

**Done when:** one claim is cited with a local observation that supports or contradicts it.

## Capture

Write observations in [`../notes.md`](../notes.md) under a dated heading. Fill in the stack-stage cheat sheet and model-variant table.
