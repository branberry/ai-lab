# TECH-NNNN — <short-slug>

- **ID**: TECH-NNNN
- **Addresses**: LL-NNNN
- **Date proposed**: YYYY-MM-DD
- **Status**: prototype | validated | abandoned (reason)

## Idea

The technique in one paragraph. What you do, when you do it, what changes.

## Mechanism

Why it should work, mechanistically. Tie it to a model-level claim (attention, logits, KV cache, training distribution, prompt structure, agent loop) — not just "it helps the model think better."

## Implementation

Pointer to code:

- `tools/python/llab/<file>.py` (or `tools/ts/llab/<file>.ts`)
- or `research/techniques/NNNN/<file>`

Brief description of the entry point and how to invoke it.

## Eval

- **Dataset**: <path, e.g. tools/python/llab/sample.jsonl or a custom dataset>
- **Scorer**: <exact-match | regex | llm-judge>
- **Baseline**: <score>
- **Technique**: <score>
- **Δ**: <technique - baseline>
- **Variance**: <across N runs>
- **Raw**: `tools/python/llab/results/<file>.jsonl`

## Status notes

What's the current state? If validated, what's the supporting evidence? If abandoned, why?

## Links

- LL: LL-NNNN
- EXPs: EXP-NNNN
- Related TECHs: TECH-NNNN
