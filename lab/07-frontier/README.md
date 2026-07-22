# 07 — Frontier

Modern LLM stack: frontier architecture, post-training, test-time compute, research proposals.

## Objectives

- Map the modern LLM lifecycle (pretrain → post-training → inference-time) and locate where behavioral differences come from.
- Inspect frontier architecture choices in an open-weight model without hand-waving.
- Compare base vs instruct (and reasoning, if available) variants on a fixed prompt suite.
- Measure test-time compute strategies (CoT, best-of-N) with `llab eval`.
- Propose and evaluate one `TECH-` addressing a linked `LL-` — novelty not required; measurable improvement (or honest failure) is.

## Resources

- Qwen 2.5 or Llama 3 technical report — architecture and post-training sections
- DPO paper (Rafailov et al.)
- One test-time reasoning report (e.g. DeepSeek-R1 or similar) — methods section only
- Chinchilla or Kaplan scaling-laws paper (Hoffmann et al. or Kaplan et al.) — situate model sizing
- `tools/python/llab/eval.py`, `client.py`, `models.py` in this repo

## Exercises

- `exercises/01-modern-stack-map.md` — draw the modern pipeline; compare model variants on a shared prompt set.
- `exercises/02-architecture-in-the-wild.md` — inspect a model config; relate GQA/RoPE/context choices to cost and behavior.
- `exercises/03-post-training-compare.md` — base vs instruct comparison; log a reproducible weakness as `LL-NNNN`.
- `exercises/04-test-time-compute.md` — greedy vs CoT vs best-of-N on a ≥20-example eval; report variance.
- `exercises/05-research-proposal.md` — linked `LL-` → `TECH-` → `llab eval` capstone (Ship mode).

## Notes

See `notes.md`. Exercise 05 switches to Ship mode (`.cursor/skills/ship/SKILL.md`).

## Concepts

- `CONCEPT-frontier-architecture` — after Exercise 02
- `CONCEPT-post-training-stack` — after Exercise 03
- `CONCEPT-test-time-compute` — after Exercise 04

## Open frontiers (future modules)

Retrieval/grounding, long-context/memory, and multimodal are intentionally out of scope here. See `docs/learning-path.md` for the full path.
