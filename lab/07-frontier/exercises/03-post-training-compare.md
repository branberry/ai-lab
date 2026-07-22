# Exercise 03 — Post-Training Compare

Understand what post-training adds, what it breaks, and log a reproducible weakness.

## Prerequisites

- Exercises 01–02 complete.
- Base and instruct variants of the same model family (model-agnostic — record ids in `notes.md`).

## Derive first

Read Rafailov et al. (DPO) or the post-training section of your model's technical report. In `notes.md`, write:

1. The preference optimization objective in your own words (no copied equations required, but symbols must be defined if used).
2. What SFT alone cannot fix that preference optimization targets.
3. One prediction: an instruct model will be **worse** than base at ___.

## Tasks

### 1. Side-by-side eval

Reuse your Exercise 01 prompt suite. Add 5 prompts designed to stress post-training:

- Over-refusal (clearly benign)
- Format hacking (model ignores schema)
- Sycophancy bait ("You're absolutely right that…")
- Knowledge conflict (outdated fact in prompt)
- Verbosity (ask for one sentence)

Score qualitatively: base vs instruct on each (better / worse / different tradeoff).

**Done when:** every prompt has a scored comparison with a one-line rationale.

### 2. Failure catalog

Identify at least two reproducible weaknesses in the instruct (or base) model. For each:

- Trigger prompt (copy-paste ready)
- Expected vs actual behavior
- Likely stack stage (SFT vs preference opt vs inference)

**Done when:** both failures reproduce on 3/3 reruns with fixed decoding params.

### 3. Log one weakness

Copy `docs/limitations/LL-0000-template.md` → `docs/limitations/LL-NNNN-<slug>.md`. Fill every field. Link from this module's `notes.md`.

**Done when:** the LL file is complete and the trigger prompt is included.

### 4. Optional — your LoRA

If you completed module 03, compare your LoRA adapter to the official instruct model on 5 held-out prompts. What did official post-training fix that LoRA didn't?

## Capture

Write observations in [`../notes.md`](../notes.md). Pass the comprehension gate before drafting `docs/concepts/CONCEPT-post-training-stack.md`.
