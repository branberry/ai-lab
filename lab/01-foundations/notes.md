# Module 01 — Running Notes

## 2026-07-22 — Exercise 01: Tokenization

### What I learned

- A **token** is an integer id pointing into a fixed vocabulary; the model never sees raw characters or words directly.
- **BPE** (byte-pair encoding) merges frequent byte pairs during training. Common fragments become single tokens; rare strings split into subwords.
- In `cl100k_base`, **leading spaces are part of the token** — e.g. `" quick"` not `"quick"`. Word boundaries are implicit in the merge table, not explicit whitespace tokens (except at sentence start).
- Round-trip encode/decode is lossless for these encodings — every string maps to ids and back exactly.
- Rough rule of thumb for English prose with `cl100k_base`: **~1.15 tokens per word** (124 tokens / 107 words on the sample paragraph).

### Surprising splits

1. **Leading-space convention** — `"The quick brown fox..."` tokenizes as `'The'` + `' quick'` + `' brown'` + … Every word after the first carries a leading space in its token string. `'The'` (id 791) vs `' the'` (id 279) are different tokens entirely.
2. **`unhappiness` fragments oddly** — `'un'` + `'h'` + `'appiness'` (3 tokens for the word inside quotes), not a clean prefix/suffix split. The `'h'` alone (id 71) is a single-byte merge artifact — BPE can produce very short pieces when that's what the merge table learned.
3. **Punctuation attaches to neighbors** — period is its own token (`'.'`, id 13), but in the third sentence `'hello'` and `"'."` are separate from the quote tokens. The string `"'."` (id 4527) glues quote + period into one token, while `'hello'` (id 15339) is a distinct token from `' hello'` (id 24748).
4. **Casing is not shared** — `'Python'`, `'python'`, `'PYTHON'` are three unrelated single-token ids (31380, 12958, 94240). No subword overlap across casings for this word.

### Encoding comparison

On `"Tokenization splits words like 'unhappiness' unpredictably."`, `cl100k_base`, `p50k_base`, and `r50k_base` all produced **identical** 13-token splits. Differences between encodings show up on other text (GPT-3 vs GPT-4 vocabularies diverge on rare tokens), but this sentence is identical across all three.

### Open questions (for Exercise 02)

- How do token embeddings turn these integer ids into vectors the attention mechanism can operate on?
- What does positional encoding add that token order alone doesn't capture?
- If `'The'` and `' the'` are different tokens, does the model learn separate representations for the same word in different positions?

---

## Preview — Exercise 02: Attention by hand

Setup: 4 tokens, embedding dim d=2 (tiny, for paper work).

Tokens: `t1="The"`, `t2=" cat"`, `t3=" sat"`, `t4="."`

After embedding + learned Wq/Wk/Wv projections, each token has Q, K, V vectors (2-dim each):

```
Q = [q1, q2, q3, q4]   shape (4, 2)
K = [k1, k2, k3, k4]   shape (4, 2)
V = [v1, v2, v3, v4]   shape (4, 2)
```

Attention scores for token i attending to all tokens j:

```
scores[i, j] = dot(qi, kj) / sqrt(d)
weights[i, :] = softmax(scores[i, :])
output[i] = sum_j weights[i, j] * vj
```

For a causal (decoder) mask, token i can only attend to tokens j ≤ i — set scores[i, j] = -inf when j > i before softmax.

**Next session:** pick concrete numbers for q/k/v, compute one row of the weight matrix by hand, verify with numpy in Exercise 03.
