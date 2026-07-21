# LL-NNNN — <short-slug>

- **ID**: LL-NNNN
- **Slug**: <short-slug>
- **Date observed**: YYYY-MM-DD
- **Module**: lab/NN-<name>
- **Status**: open | addressed by TECH-NNNN | won't address (reason)

## Symptom

A concrete, reproducible failure case. Include the exact prompt and the model's output.

```
Prompt: <paste the exact prompt>
Model: <model id, e.g. ollama/qwen2.5:7b-instruct>
Params: <temperature, top_p, num_predict, etc.>
Output:
<paste the model's output>
```

## Hypothesis

Why you think this happens. Prefer a mechanistic explanation (what is the model doing at the logits/attention/training-data level) over a behavioral one. It's fine to be wrong — write the hypothesis so an experiment can disprove it.

## Evidence

Anything you measured: probe outputs, logprobs, activation stats, counts across N runs. Raw data can live in `tools/python/llab/results/` and be referenced by path.

## Severity

- **Frequency**: how often (e.g. 8/10 runs)
- **Impact**: how bad (e.g. breaks the task entirely / degrades quality / cosmetic)
- **Scope**: which models/params it appears in

## Related

- Other LLs: LL-NNNN
- TECHs that address this: TECH-NNNN
- Module notes: lab/NN-<name>/notes.md
