# Tokenization (BPE)

- **Module**: lab/01-foundations
- **Status**: draft
- **Prerequisites**: basic Unicode / string encoding
- **Exercises**: lab/01-foundations/exercises/01-tokenization.md

## One-paragraph intuition

Language models never see raw text. A tokenizer maps every string to a sequence of integer ids from a fixed vocabulary. Byte-pair encoding (BPE) builds that vocabulary by repeatedly merging the most frequent byte pairs in a training corpus, so common fragments become single tokens while rare strings split into subword pieces. The merge table is frozen at training time — token boundaries are empirical facts about the corpus, not linguistic rules. This affects context window usage, cost, and model behavior on punctuation, casing, and rare words.

## Formal definition

Given a training corpus as a byte sequence, BPE iteratively:

1. Count all adjacent byte pairs.
2. Merge the most frequent pair into a new symbol.
3. Repeat until vocabulary size reaches target N.

**Encoding** greedily applies the learned merge table to split input text into tokens. **Decoding** maps token ids back to byte sequences and concatenates. For byte-level BPE (GPT family), the process is lossless: every Unicode string round-trips exactly.

A **token** is an integer id `t ∈ {0, …, V-1}`. The model's embedding layer maps `t` to a vector; the tokenizer itself is not learned during pretraining (vocabulary is fixed).

## Derivation / algorithm

BPE merge order is determined entirely by corpus statistics at tokenizer training time — not by morphology or syntax. Therefore:

- Frequent byte sequences become single tokens early in training.
- Rare sequences decompose into shorter pieces, which may be single bytes (e.g. `'h'`, id 71).
- Word boundaries are **not** explicit tokens; they emerge because leading-space variants (`"The"` vs `" the"`) are distinct frequent patterns in web text.

Greedy encoding scans left-to-right, applying the longest matching merge at each step (implementation detail in `tiktoken`; principle holds for all BPE variants).

## Mechanism (what actually happens in the model)

1. Input string → tokenizer → `List[int]` token ids.
2. Embedding lookup: each id → `d`-dim vector from a learned matrix `E ∈ R^{V×d}`.
3. Positional information is added separately (sinusoidal or learned); token ids carry no order information on their own.
4. Downstream layers (attention, FFN) operate on these vectors.

Because `'The'` (id 791) and `' the'` (id 279) are different ids, they get **different rows** of E — the model must learn separate representations for the same word in different positions. Casing variants (`'Python'`, `'python'`, `'PYTHON'`) are likewise independent tokens with no guaranteed subword overlap.

## Worked example (from your lab code)

On `"The quick brown fox jumps over the lazy dog."` with `cl100k_base`:

- `'The'` (791) — no leading space (sentence-initial).
- `' quick'` (4184), `' brown'` (…), etc. — every subsequent word includes a leading space in the token string.
- `'unhappiness'` in context splits as `'un'` + `'h'` + `'appiness'` — not a clean morphological split; `'h'` is a single-byte merge artifact.

Tokens-per-word on the sample paragraph: **~1.15** (124 tokens / 107 words).

Encoding comparison: `cl100k_base`, `p50k_base`, `r50k_base` produced **identical** 13-token splits on the test sentence — divergence appears on rarer tokens, not common English prose.

## Common misconceptions

| Misconception | Reality |
|---------------|---------|
| Tokens are words | Tokens are merge-table artifacts; words often span multiple tokens |
| BPE respects word boundaries | Leading spaces are part of tokens; boundaries are implicit |
| Same word, different case shares subwords | Often no overlap — each casing can be a wholly separate token |
| Tokenizer learns during pretraining | Vocabulary is fixed; only embeddings and downstream weights learn |
| Longer words always mean more tokens | Merge frequency matters, not length — `'unhappiness'` can split oddly |

## Literature (2–5 primary refs)

- Sennrich et al., *Neural Machine Translation of Rare Words with Subword Units* — introduces BPE for NMT; subword units handle rare words via compositional splits. **Verified in lab**: rare strings split into subword fragments.
- Radford et al., *Language Models are Unsupervised Multitask Learners* (GPT-2) — byte-level BPE for Unicode coverage. **Verified in lab**: round-trip encode/decode is lossless.
- Brown et al., *Language Models are Few-Shot Learners* (GPT-3) — documents `p50k_base` / `r50k_base` vocabularies. **Verified in lab**: common sentence identical across encodings; divergence expected on rare tokens (not observed on test sentence).
- Vaswani et al., *Attention Is All You Need* — models operate on token embeddings, not raw text. **Connects to**: Exercise 02 open questions.

## Open questions / research frontier

- How do token embeddings turn integer ids into vectors the attention mechanism can operate on? → Exercise 02
- What does positional encoding add that token order alone doesn't capture? → Exercise 02+
- Do models learn semantically related representations for `'The'` vs `' the'`, or treat them as unrelated? → interpretability module
- Optimal vocabulary size trade-offs (compression vs generalization) remain an active design choice

## Connections

- Related concepts: CONCEPT-attention (Exercise 02), CONCEPT-embeddings (upcoming)
- Limitations this explains: token-boundary effects on context length, casing sensitivity, subword fragmentation on rare terms

## Teach-back

A tokenizer is a fixed lookup table built before training by merging frequent byte pairs. Text becomes a list of integers; the model's embedding layer turns those integers into vectors. BPE doesn't know about words — it knows about byte frequency. That's why you see `" quick"` with a leading space, why `unhappiness` can split at a single `h`, and why Python/python/PYTHON are three unrelated tokens. Every downstream behavior — context cost, punctuation handling, rare word generalization — starts here.
