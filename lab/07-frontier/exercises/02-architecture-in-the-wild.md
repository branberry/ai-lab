# Exercise 02 — Architecture in the Wild

Inspect frontier architecture choices in a real open-weight model and connect them to cost and behavior.

## Prerequisites

- Exercise 01 complete.
- Access to a model config: Hugging Face `config.json`, model card, or Ollama `show` output for your chosen family.

## Derive first

Before opening the config, write down (in `notes.md`):

1. What GQA/MQA changes compared to standard multi-head attention.
2. What RoPE encodes and why it matters for context length.
3. One prediction: how doubling context length affects KV cache memory (qualitative — proportional to what?).

## Tasks

### 1. Config inspection

For one model you can run locally, record:

| Field | Value | Plain-language meaning |
|-------|-------|------------------------|
| Layers | | |
| Attention heads | | |
| KV heads (if GQA) | | |
| Hidden size | | |
| Context length | | |
| RoPE / position encoding | | |
| MoE (if any) | | |

**Done when:** the table is complete and every "meaning" cell is in your words.

### 2. Cost intuition

Given your config, estimate (order-of-magnitude is fine):

- KV cache bytes per token at fp16 (use layer count, kv heads, head dim).
- Whether GQA reduces cache vs full MHA for this model.

**Done when:** you show the formula and one numeric estimate.

### 3. Behavioral prediction

Pick one architecture fact (e.g. shorter context window, GQA, smaller hidden size). Predict one measurable effect on your prompt suite from Exercise 01 when comparing two models that differ on that axis.

Run the comparison.

**Done when:** you stated the prediction before running and recorded match or mismatch.

### 4. Stretch — MoE

If your chosen family includes a MoE variant, read how routing works in the technical report. Sketch what an "expert load imbalance" failure would look like at inference. Skip if no MoE model is available locally.

## Capture

Write observations in [`../notes.md`](../notes.md). Pass the comprehension gate before drafting `docs/concepts/CONCEPT-frontier-architecture.md`.
