---
name: ship
description: >-
  Ship mode for ai-lab research — LL weaknesses, TECH techniques, evals,
  findings. Use when the user says /ship, works under research/, implements
  TECH-NNNN, fixes eval harness, or probes model failures.
---

# Ship Mode (ai-lab)

Optimize for **measurable improvement**. You may implement freely. Follow `AGENTS.md` rigor.

Learn mode (`.cursor/skills/learn/SKILL.md`) applies to `lab/` exercises and explicit `/learn` requests.

## Rules (from AGENTS.md)

- **No `TECH-` without a linked `LL-`.** A technique must address a specific logged weakness.
- **No `LL-` closed without a linked `TECH-`** or an explicit "won't address" reason.
- **No claim that a technique works without an eval.** Run or extend `llab eval` and report baseline vs technique scores.
- Eval results go to `tools/python/llab/results/` (gitignored); summarize in the `TECH-` file.

## Templates

- `docs/limitations/LL-0000-template.md` — log weaknesses
- `research/techniques/TECH-0000-template.md` — design techniques
- `research/experiments/EXP-0000-template.md` — experiments
- `research/findings/README.md` — writeups

## Workflow

```
Probe model → Log LL-NNNN → Design TECH-NNNN → Implement + llab eval
  → Eval improves? → Write finding → else redesign
```

## When Ship touches Learn

- If probing reveals a knowledge gap, suggest a lab exercise or concept note — do not teach inline during Ship.
- Link `TECH-` and `LL-` entries to relevant `docs/concepts/` when a technique depends on understood internals.

## Anti-patterns

- Do not write a technique before its weakness is logged.
- Do not claim improvement without eval scores.
- Do not skip the LL → TECH link.
