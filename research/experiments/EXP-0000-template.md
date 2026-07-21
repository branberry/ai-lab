# EXP-NNNN — <short-slug>

- **ID**: EXP-NNNN
- **Date**: YYYY-MM-DD
- **Probes**: LL-NNNN (the weakness this experiment is investigating)
- **Informs**: TECH-NNNN (the technique this evidence feeds, if any)

## Hypothesis

A single falsifiable statement. "If X is true, then under conditions Y we should observe Z."

## Setup

- **Model**: <e.g. ollama/qwen2.5:7b-instruct>
- **Params**: <temperature, top_p, num_predict, seed, ...>
- **Dataset**: <path or description, e.g. tools/python/llab/sample.jsonl>
- **N**: <number of runs or examples>
- **Seed**: <if set>

## Method

Step-by-step what you did. Enough that you (or someone else) could re-run it and get comparable numbers.

## Results

- **Raw**: `tools/python/llab/results/<file>.jsonl`
- **Summary scores**: <baseline = X, technique = Y, Δ = Z>
- **Notes**: <anything surprising, any caveats>

## Takeaways

- Did the hypothesis hold? Yes / No / Partially.
- What does this imply for the linked `TECH-` (if any)?
- What's the next experiment?

## Links

- LL: LL-NNNN
- TECH: TECH-NNNN
- Related EXPs: EXP-NNNN
