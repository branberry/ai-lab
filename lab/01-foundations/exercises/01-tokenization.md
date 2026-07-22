# Exercise 01 — Tokenization

Encode/decode text with BPE, inspect token splits, and build intuition for why tokenization matters.

## Prerequisites

```bash
cd /path/to/ai-lab
uv sync
```

## Tasks

### 1. Encode/decode loop

Use `tiktoken.get_encoding("cl100k_base")` to encode three sentences, print token ids, decode back, and confirm round-trip.

Suggested sentences:

- `"The quick brown fox jumps over the lazy dog."`
- `"Tokenization splits words like 'unhappiness' unpredictably."`
- `"  Leading spaces matter: ' hello' vs 'hello'."`

**Done when:** each sentence decodes to the original string.

### 2. Inspect splits

For each sentence, print `(token_id, token_string)` pairs. Find at least three surprising splits, such as:

- Leading-space tokens (`" The"` vs `"The"`)
- Punctuation glued to words (`" dog."`)
- Subword fragments (`" un"`, `"happiness"`)

**Done when:** you can explain each surprising split in plain language.

### 3. Compare encodings

Repeat the same sentences with a second encoding (`p50k_base` or `r50k_base`). Note where token counts or splits differ.

**Done when:** you have at least one concrete example where encodings disagree.

### 4. Length intuition

Count tokens for a ~100-word paragraph vs its character and word counts. Compute tokens-per-word ratio.

**Done when:** you have a rough rule of thumb (e.g. "~1.3 tokens per English word for cl100k_base").

### 5. Stretch — casing

Encode the same word in different casings: `"Python"`, `"python"`, `"PYTHON"`. Observe whether BPE treats them as related subwords or unrelated tokens.

## Run

```bash
uv run python lab/01-foundations/exercises/01_tokenization.py
```

## Capture

Write observations in [`../notes.md`](../notes.md) under a dated heading.
