# 02 — Inference

Logits → probabilities, sampling (greedy / temperature / top-p / top-k / min-p), KV cache, quantization.

## Objectives

- Predict how a sampling change will affect output before running it.
- Explain the KV cache and why it changes the cost profile of generation.
- Measure the effect of quantization on perplexity and quality.
- Reproduce a known sampling pathology.

## Resources

- "How to generate text" — Hugging Face blog (decoding strategies)
- The min-p paper / blog post
- Ollama API docs — `num_predict`, `temperature`, `top_k`, `top_p`, `min_p`, `repeat_penalty`
- llama.cpp quantization primer

## Exercises

- `exercises/01-sampling-sweep.md` — fix a prompt, sweep `temperature` ∈ {0, 0.3, 0.7, 1.0, 1.5}, log outputs.
- `exercises/02-top-p-vs-top-k.md` — compare top-p and top-k on a prompt that exposes the difference.
- `exercises/03-quantization-quality.md` — run the same prompt on q4_K_M vs q8_0 vs fp16 of the same model; measure quality on a small eval.
- `exercises/04-repetition-pathology.md` — trigger degenerate repetition at low temperature and characterize when it appears.

## Notes

See `notes.md`.
