# 04 — Evals

Build and use the lab's own eval harness (see `tools/python/llab/eval.py`).

## Objectives

- Define task vs metric vs judge and know which one you're touching.
- Build a small dataset (≥20 examples) for a behavior you care about.
- Implement exact-match, regex, and LLM-judge scorers.
- Measure variance across runs and learn paired comparison.

## Resources

- "Evaluating LLMs" — Hugging Face course chapter
- "LLM-as-a-Judge" paper (Zheng et al.)
- OpenAI Evals framework (for structure, not for copying)
- `tools/python/llab/eval.py` in this repo

## Exercises

- `exercises/01-task-metric-judge.md` — for one behavior, write a task spec, a metric, and a judge prompt.
- `exercises/02-build-dataset.md` — author 20+ JSONL examples with `{prompt, expected}` and run `llab eval` on them.
- `exercises/03-judge-scorer.md` — add an LLM-judge scorer using `LAB_JUDGE_MODEL`; compare its scores to exact-match.
- `exercises/04-variance.md` — run the same eval 5 times and report the score distribution; learn when differences are noise.

## Notes

See `notes.md`.
