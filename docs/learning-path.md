# Learning Path

The curriculum is a sequence of self-contained modules in `lab/`. Each module has a `README.md` (objectives, resources, exercises), an `exercises/` folder, and a `notes.md` for your running notes.

The order below assumes an **intermediate user** moving toward model internals, working with **local open models via Ollama** and (optionally) closed APIs.

## Modules

### 01 — Foundations
Tokenization, embeddings, the transformer block, attention by hand.

**Goal**: explain attention to yourself without hand-waving.

- Implement tokenization (BPE) on a tiny corpus.
- Compute positional embeddings and a single self-attention head in numpy/torch from scratch.
- Trace a 2-layer transformer forward pass by hand on paper, then in code.

See `lab/01-foundations/`.

### 02 — Inference
Logits → probabilities, sampling (greedy / temperature / top-p / top-k / min-p), KV cache, quantization.

**Goal**: predict how a sampling change will affect output before running it.

- Expose Ollama params (`num_predict`, `temperature`, `top_k`, `top_p`, `min_p`) and compare outputs on a fixed prompt.
- Measure the effect of quantization (q4 vs q8 vs fp16) on a small model's perplexity and quality.
- Reproduce a known sampling pathology (e.g. degenerate repetition at low temperature).

See `lab/02-inference/`.

### 03 — Training
Pretraining vs SFT vs RLHF/DPO. Run a tiny LoRA fine-tune to feel the loop.

**Goal**: describe what each training stage does to the model's behavior, not just its weights.

- Run a tiny LoRA fine-tune on Qwen2.5 0.5B on a small custom dataset.
- Compare pre-fine-tune vs post-fine-tune outputs on held-out prompts.
- Write up: what changed, what didn't, what broke.

See `lab/03-training/`.

### 04 — Evals
Build the lab's own eval harness (see `tools/python/llab/eval.py`).

**Goal**: turn "I think this is better" into "this is measurably better."

- Define task vs metric vs judge.
- Build a small dataset (≥20 examples) for a behavior you care about.
- Implement exact-match, regex, and LLM-judge scorers.
- Measure variance across runs and learn paired comparison.

See `lab/04-evals/`.

### 05 — Interpretability
Logits lens, activation patching, steering vectors, refusal directions.

**Goal**: explain a limitation mechanistically, not just behaviorally.

- Apply the logits lens to a small model at each layer for a chosen prompt.
- Capture activations on a contrast dataset (e.g. harmful vs benign prompts) and compute a steering vector.
- Test the steering vector: does adding it change behavior in the predicted direction?

See `lab/05-interpretability/`.

### 06 — Agents
Tool use, planning, context limits, failure modes (loops, hallucinated tools, lost-in-the-middle).

**Goal**: enumerate the ways agents fail and tie each to a logged `LL-` weakness.

- Build a minimal tool-use loop with a provider SDK or the Cursor SDK.
- Probe context-length limits with a long-context task.
- Catalog at least 3 distinct agent failure modes as `LL-` entries.

See `lab/06-agents/`.

## How to use this path

1. Pick the lowest-numbered module you haven't finished.
2. Read its `README.md`, do the exercises, take notes in `notes.md`.
3. When you observe a model weakness worth attacking, log it in `docs/limitations/LL-NNNN-*.md`.
4. When you have an idea to address it, open `research/techniques/TECH-NNNN-*.md` and run an eval.
5. Write a finding in `research/findings/` and move to the next module.
