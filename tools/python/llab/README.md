# llab — Python harness

Shared Python harness for ai-lab: client, eval runner, models, probes.

## Setup

From the repo root:

```bash
uv sync
```

## Run

Eval against the default local Ollama model:

```bash
uv run python -m llab.eval --dataset tools/python/llab/sample.jsonl
```

Or via the entry point:

```bash
uv run llab eval --dataset tools/python/llab/sample.jsonl
uv run llab models
```

## Optional ML deps

For `lab/03-training` and `lab/05-interpretability`:

```bash
uv sync --extra ml
uv sync --extra notebooks
```

## Layout

- `client.py` — `generate(model, prompt, params)` routing to Ollama (and later OpenAI/Anthropic).
- `eval.py` — eval runner with exact-match / regex / LLM-judge scorers.
- `models.py` — list/inspect/pull local Ollama models.
- `probes.py` — interpretability helpers (skeleton).
- `cli.py` — `llab` entry point.
- `sample.jsonl` — tiny eval dataset.
- `results/` — eval output (gitignored).
