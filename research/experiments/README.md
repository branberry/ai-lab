# Experiments

One file per structured experiment, named `EXP-NNNN-short-slug.md`.

An experiment is a controlled run that produces evidence for or against a hypothesis. It is **not** a technique — a technique (`TECH-NNNN`) is what you build on top of evidence; an experiment is how you get the evidence.

## Template

Copy `EXP-0000-template.md` to `EXP-NNNN-<slug>.md` and fill every field.

## Rules

- One experiment per file.
- Every experiment must have a hypothesis that can be falsified by its results.
- Raw results go to `tools/python/llab/results/` and are referenced by path, not pasted inline if large.
- Link the experiment to the `LL-` it probes and any `TECH-` it informs.

## Index

(Numbered entries will be listed here as they are added.)
