# 05 — Interpretability

Logits lens, activation patching, steering vectors, refusal directions.

## Objectives

- Explain a limitation mechanistically, not just behaviorally.
- Apply the logits lens to a small model at each layer for a chosen prompt.
- Capture activations on a contrast dataset and compute a steering vector.
- Test the steering vector: does adding it change behavior in the predicted direction?

## Resources

- "Logit Lens" — nostalgebraist blog
- "Inference-Time Intervention" paper (Li et al.) — refusal direction
- "Steering vectors" — Anthropic / Activation Addition work
- `tools/python/llab/probes.py` in this repo

## Exercises

- `exercises/01-logits-lens.md` — for a chosen prompt, project intermediate hidden states through the unembedding matrix and plot token probability by layer.
- `exercises/02-activation-capture.md` — capture residual-stream activations on a contrast dataset (e.g. harmful vs benign).
- `exercises/03-steering-vector.md` — compute the mean-difference steering vector and add it at inference on held-out prompts.
- `exercises/04-does-it-work.md` — measure the effect with `llab eval` (baseline vs steered); log any side effects as `LL-NNNN`.

## Notes

See `notes.md`.
