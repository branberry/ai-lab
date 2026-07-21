# 01 — Foundations

Tokenization, embeddings, the transformer block, attention by hand.

## Objectives

- Explain tokenization (BPE) and why it matters for model behavior.
- Implement a single self-attention head from scratch in numpy/torch.
- Trace a small transformer forward pass by hand and in code.
- Be able to explain attention to yourself without hand-waving.

## Resources

- "The Illustrated Transformer" — Jay Alammar
- "Attention Is All You Need" — Vaswani et al. (read sections 3–4)
- Karpathy's "Let's build GPT" video (nanoGPT)
- `tiktoken` for BPE encoding inspection

## Exercises

- `exercises/01-tokenization.md` — encode/decode a sentence, inspect token ids, find surprising splits.
- `exercises/02-attention-by-hand.md` — compute Q, K, V, softmax(QK^T / sqrt(d))V for a 4-token sequence by hand.
- `exercises/03-attention-in-code.md` — implement the same in numpy (no autograd) and verify it matches.
- `exercises/04-mini-transformer.md` — implement a 2-layer transformer forward pass and run it on a tiny vocab.

## Notes

See `notes.md` for your running notes. When you observe a model weakness worth attacking, log it in `docs/limitations/LL-NNNN-*.md`.
