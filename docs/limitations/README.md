# Limitations Catalog

One file per observed model weakness, named `LL-NNNN-short-slug.md` (zero-padded, e.g. `LL-0001-repetition-at-low-temp.md`).

A weakness here is a **concrete, reproducible failure** of a model — not a vague complaint. If you can't write a prompt that triggers it, it isn't ready to log.

## Why this catalog exists

Every entry here is the input to the techniques loop (`research/techniques/TECH-NNNN`). A technique must address a specific `LL-`. If the weakness isn't logged, the technique can't be claimed to fix anything.

## How to add an entry

1. Copy `LL-0000-template.md` to `LL-NNNN-<slug>.md` (next free number).
2. Fill every field. Don't leave fields empty — write "unknown" or "not yet measured" rather than blank.
3. Link it from the relevant module's `notes.md`.
4. When a `TECH-` addresses it, update its **Status** field with the TECH id.

## Rules

- **No `TECH-` without a linked `LL-`.**
- **No `LL-` closed without a linked `TECH-`** or an explicit "won't address" reason in the LL file.
- One weakness per file. If a second weakness shows up while probing, open a second LL.

## Index

(Numbered entries will be listed here as they are added.)
