# 03 — Training

Pretraining vs SFT vs RLHF/DPO. Run a tiny LoRA fine-tune to feel the loop.

## Objectives

- Describe what each training stage (pretraining, SFT, RLHF/DPO) does to model behavior, not just its weights.
- Run a tiny LoRA fine-tune on a small local model and observe a behavior change.
- Diagnose what changed, what didn't, and what broke after fine-tuning.

## Resources

- Karpathy's nanoGPT and "Let's reproduce GPT-2" video
- The original LoRA paper (Hu et al.)
- Hugging Face PEFT docs
- DPO paper (Rafailov et al.)

## Exercises

- `exercises/01-stages-on-paper.md` — write the objective function for each stage in your own words.
- `exercises/02-tiny-lora.md` — LoRA fine-tune Qwen2.5 0.5B on a 50-example custom dataset; save the adapter.
- `exercises/03-before-after-eval.md` — run `llab eval` on the base model and the fine-tuned model on a held-out set; compare.
- `exercises/04-what-broke.md` — find one capability that degraded after fine-tuning and log it as `LL-NNNN`.

## Notes

See `notes.md`.
