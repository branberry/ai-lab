# Exercise 05 — Research Proposal

Capstone: link a logged weakness to a technique, run an eval, and record an honest result. **Ship mode** — follow `.cursor/skills/ship/SKILL.md`.

Novelty is not required. Applying best-of-N, a steering vector, a prompt template, or a decoding change systematically counts if the eval proves it.

## Prerequisites

- At least one `LL-NNNN` from module 03–07 with a reproducible trigger prompt.
- Exercises 01–04 complete (or strong progress on 03–04 with a logged LL).
- Familiarity with `research/techniques/TECH-0000-template.md` and `llab eval`.

## Tasks

### 1. Pick the weakness

Choose an `LL-` you logged (yours from Exercise 03, module 06, or earlier). Confirm it still reproduces with your current local model.

**Done when:** trigger prompt + failure documented in the LL file.

### 2. Draft the technique

Copy `research/techniques/TECH-0000-template.md` → `research/techniques/TECH-NNNN-<slug>.md`.

Fill every field. The technique must explicitly address the linked `LL-`. Examples (not exhaustive):

- Best-of-N with a task-specific judge
- CoT prefix for a failure class
- Decoding param change (temperature, min-p)
- Steering vector from module 05
- Prompt scaffold / system message

**Done when:** TECH file links to LL and describes a falsifiable intervention.

### 3. Build the eval

Author or reuse a JSONL dataset (≥20 examples) that includes:

- Cases that trigger the weakness
- Near-miss controls
- `{prompt, expected}` compatible with `llab eval`

Define baseline (no technique) and technique runs using the same model and judge.

**Done when:** both runs complete without manual cherry-picking.

### 4. Report results

Run:

```bash
cd /path/to/ai-lab
uv run llab eval --help   # use your harness flags
```

Record in the TECH file:

- Baseline score
- Technique score
- Variance if rerun
- Verdict: **failed / partial / improved**

Update the linked `LL-` status field.

**Done when:** numbers are in the TECH file and the verdict matches the data.

### 5. Write a finding

Add a short note in `research/findings/` (create if needed): what worked, what didn't, one next experiment.

**Done when:** finding links to TECH and LL ids.

## Capture

Ship artifacts live in `research/`, not `notes.md`. Optionally debrief in [`../notes.md`](../notes.md) under a dated heading.

## Module completion

You are done with module 07 when Exercise 05 has an eval-backed TECH verdict — including an honest **failed** result.
