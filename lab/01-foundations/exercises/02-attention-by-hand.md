# Exercise 02 — Attention by Hand

Compute Q, K, V, softmax(QK^T / sqrt(d))V for a 4-token sequence on paper — no code yet.

## Prerequisites

- Exercise 01 (tokenization) complete.
- Read Vaswani et al., sections 3.1–3.2 (Scaled Dot-Product Attention).
- Optional: Jay Alammar, "The Illustrated Transformer" (attention section).

## Derive first

Before opening a REPL, work through the math on paper.

### Setup

4 tokens, embedding dimension d = 2 (small enough to compute by hand):

| Token | String |
|-------|--------|
| t1 | `"The"` |
| t2 | `" cat"` |
| t3 | `" sat"` |
| t4 | `"."` |

Assume you already have embedding vectors and learned projection matrices Wq, Wk, Wv. Each token i has:

- q_i = Wq · embed_i
- k_i = Wk · embed_i
- v_i = Wv · embed_i

### Tasks

1. **Write the attention formula** for a single head: scores, softmax, weighted sum of values. Include the sqrt(d) scaling factor and state why it exists.
2. **Pick concrete numbers** for Q, K, V (4×2 matrices). Use simple integers or fractions so dot products are tractable.
3. **Compute one full row** of the attention weight matrix — e.g. token 3 (`" sat"`) attending to all four tokens. Show every intermediate step: dot products, scaling, softmax, weighted V sum.
4. **Apply a causal mask** for decoder-style attention: recompute the same row with scores[i,j] = -∞ when j > i. Explain how the output changes.

**Done when:** you have a complete handwritten (or typed) derivation with no "then magic happens" steps.

## Predict

Write these in [`../notes.md`](../notes.md) **before** verifying with code in Exercise 03:

1. If q_3 · k_3 is much larger than q_3 · k_j for j ≠ 3, the output for token 3 will be dominated by v_3.
2. After applying the causal mask to row 3, the attention weights for j > 3 will be exactly zero (only j ∈ {1,2,3} contribute).
3. Removing the sqrt(d) scaling (d=2) will make softmax saturate toward one-hot weights when dot products exceed ~2–3.

## Tasks (implementation scope)

This exercise is **paper only**. No code required here.

1. Complete the derivation above.
2. Sanity-check: each row of the weight matrix sums to 1.0 (before and after masking).
3. Compare your masked row-3 output to what you expect token 3 to "see" — only prior context.

## Mastery criteria

Exercise completion requires more than finishing the arithmetic:

- **Done when** you can derive scaled dot-product attention from the definition without looking at notes.
- **Done when** you can explain why sqrt(d) scaling prevents softmax saturation as dimension grows.
- **Done when** you can predict how masking changes the output for a given row without recomputing.
- **Done when** you can connect this to tokenization: these four strings are the actual BPE tokens from Exercise 01's leading-space convention.

## Capture

Write observations in [`../notes.md`](../notes.md) using the session template. Carry forward open questions from Exercise 01 (embeddings, positional encoding).

## Next

Exercise 03 implements the same computation in numpy and verifies your hand calculation.
