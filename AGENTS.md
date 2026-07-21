# AGENTS.md — conventions for AI assistants working in ai-lab

This file gives any assistant (Cursor, pi, or other) a shared set of rules for working in this repo. Follow it before writing code or proposing changes.

## The three-loop model

Every contribution should advance at least one of:

1. **Learn** — a concept note in `docs/concepts/` or an exercise in `lab/`.
2. **Probe** — a logged weakness in `docs/limitations/LL-NNNN-*.md`.
3. **Ship** — a `TECH-NNNN` technique with an eval that measures the weakness it claims to address.

If a change doesn't advance any of these, push back and ask whether it belongs in this repo.

## Limitations → Techniques → Evals

- **No `TECH-` without a linked `LL-`.** A technique must address a specific logged weakness.
- **No `LL-` closed without a linked `TECH-`** or an explicit "won't address" reason in the LL file.
- **No claim that a technique works without an eval.** Run or extend `llab eval` and report baseline vs technique scores. "I think this is better" is not a result.
- Eval results go to `tools/python/llab/results/` (gitignored) and the summary is referenced from the `TECH-` file.

## File templates

Use the templates in:

- `docs/limitations/README.md` — `LL-NNNN` template.
- `research/experiments/README.md` — `EXP-NNNN` template.
- `research/techniques/README.md` — `TECH-NNNN` template.

Copy the template, fill the fields, don't improvise the structure.

## Module isolation

- `lab/NN-*` modules are self-contained. Module N may import from `tools/`, but **must not** import from module N-2 or earlier module code.
- Shared code lives in `tools/python/llab/` or `tools/ts/llab/`, not in `lab/`.

## Code style

- Python: type hints, `pydantic` for data, `pytest` for tests. Run `uv run ruff check` and `uv run ruff format` before committing.
- TypeScript: strict mode, `vitest` for tests. Run `pnpm build` before committing.

## Models

- Default local model: `LAB_MODEL` env var (Ollama).
- Judge model: `LAB_JUDGE_MODEL` (a stronger local model for LLM-judge evals).
- Closed APIs are optional — route via `llab.client.generate` using a model prefix (`ollama/...`, `openai/...`, `anthropic/...`).

## Don't

- Don't commit `.env`, model blobs, venvs, or eval result files.
- Don't write a technique before its weakness is logged.
- Don't claim improvement without an eval score.
- Don't let modules accumulate cross-dependencies.
