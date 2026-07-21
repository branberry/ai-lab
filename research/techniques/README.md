# Techniques

One file per proposed technique, named `TECH-NNNN-short-slug.md`.

A technique is a concrete idea for addressing a logged weakness (`LL-NNNN`). It must be paired with an eval that re-measures the weakness, so "this works" is a measured claim, not a feeling.

## Template

Copy `TECH-0000-template.md` to `TECH-NNNN-<slug>.md` and fill every field.

## Rules

- **No `TECH-` without a linked `LL-`.** A technique must address a specific logged weakness.
- **No claim a technique works without an eval.** Run `llab eval`, report baseline vs technique scores.
- Implementation lives in `tools/python/llab/`, `tools/ts/llab/`, or `research/techniques/NNNN/` — your choice, but reference it from the TECH file.
- Update the **Status** field as the technique moves: prototype → validated → abandoned (with reason).

## Index

(Numbered entries will be listed here as they are added.)
