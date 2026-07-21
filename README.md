# ai-lab

A personal lab for pushing the boundary of my understanding of LLMs and AI tools — and for developing techniques that address their limitations.

The lab runs **three loops at once**:

1. **Learn** — work through a concept (transformers, attention, sampling, training, evals, interpretability, agents).
2. **Probe** — run a model and observe a concrete failure.
3. **Ship** — design a technique that addresses the failure, implement it, and measure it with an eval.

Each loop feeds the next. A documented weakness (`docs/limitations/LL-NNNN`) becomes the seed for a technique (`research/techniques/TECH-NNNN`), and the technique is judged by an eval that re-measures that weakness.

## Layout

```
docs/        curriculum: learning path, concept notes, limitations catalog
lab/         numbered learning modules (01..06), each self-contained
research/    experiments, techniques, findings — the boundary-pushing loop
tools/       shared harness
  python/llab/   client, eval runner, probes, models  (uv)
  ts/llab/       client, eval, agent                  (pnpm)
notebooks/   free-form exploration
```

## Quickstart

### Python (uv)

```bash
uv sync
uv run python -m llab.eval --dataset tools/python/llab/sample.jsonl
```

### TypeScript (pnpm)

```bash
pnpm install
pnpm build
```

### Models

Default local model is configured via `.env` (copy from `.env.example`):

```
OLLAMA_BASE_URL=http://localhost:11434
LAB_MODEL=qwen2.5:7b-instruct
LAB_JUDGE_MODEL=qwen2.5:14b-instruct
```

Pull with `ollama pull qwen2.5:7b-instruct`.

## The three loops

```
Learn a concept → Probe a model → Log a weakness (LL-NNNN)
  → Design a technique (TECH-NNNN) → Implement + eval → Eval improves?
      yes → Write finding → next concept
      no  → redesign technique
```

## Conventions

See `AGENTS.md` for the rules any assistant (Cursor, pi, etc.) must follow when working in this repo. The short version:

- No `TECH-` without a linked `LL-`.
- No `LL-` closed without a linked `TECH-` or an explicit "won't address" reason.
- Run or extend `llab eval` before claiming a technique works.
- Keep modules self-contained; module N must not depend on module N-2's code.
