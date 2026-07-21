# @ai-lab/llab — TypeScript harness

Shared TypeScript harness for ai-lab, mirroring the Python `llab` package. Used for agent / Cursor SDK experiments in `lab/06-agents`.

## Setup

From the repo root:

```bash
pnpm install
```

## Build

```bash
pnpm build          # tsc → tools/ts/dist/
pnpm typecheck      # type-only check
```

## Run

Eval (uses the same JSONL datasets as the Python side):

```bash
pnpm eval --dataset tools/python/llab/sample.jsonl
# or directly:
tsx tools/ts/llab/cli.ts eval --dataset tools/python/llab/sample.jsonl
```

## Layout

- `index.ts` — public exports.
- `client.ts` — `generate(model, prompt, opts)` routing to Ollama (OpenAI/Anthropic are skeletons).
- `eval.ts` — eval runner with exact-match / regex / LLM-judge scorers.
- `agent.ts` — minimal tool-use loop with per-step recording.
- `cli.ts` — `llab` CLI entry point.
