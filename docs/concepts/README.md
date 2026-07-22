# Concept Notes

Polished writeups of concepts you have **mastered** through lab exercises. One file per concept, named `CONCEPT-<slug>.md` (e.g. `CONCEPT-tokenization.md`).

Running observations and in-progress learning live in `lab/NN-*/notes.md`. Concept notes are the durable, teachable artifact — written only after you pass the comprehension gate (see `.cursor/skills/learn/SKILL.md`).

## Depth ladder

A concept note should cover all six rungs when marked **mastered**:

| Rung | You can... | Usually captured in |
|------|-----------|---------------------|
| **Observe** | Point to surprising empirical facts | `notes.md` → "What I learned" |
| **Formalize** | State definitions, notation, key equations | `notes.md` derivation section |
| **Derive** | Reproduce the result from assumptions (paper work) | `notes.md` before code |
| **Predict** | State falsifiable expectations before running code | `notes.md` → "Predictions" |
| **Mechanize** | Trace information flow through your implementation | concept note → "Mechanism" |
| **Situate** | Cite 2–3 primary sources; name what's open | concept note → "Literature" |

## Promotion rules

| Status | When |
|--------|------|
| **draft** | Comprehension gate passed; note is being polished from `notes.md` |
| **mastered** | You can teach the concept back in ~5 minutes without notes; all six rungs covered |

Do **not** create a concept note until the comprehension gate passes. Do **not** mark **mastered** until you can derive and predict without hand-waving.

## How to add an entry

1. Complete the relevant lab exercise(s) and pass the comprehension gate.
2. Copy `CONCEPT-0000-template.md` to `CONCEPT-<slug>.md`.
3. Fill every section from your `notes.md` and exercise work. Write "unknown" rather than leaving fields blank.
4. Link the concept from the module `README.md` and any related `LL-` entries.
5. Update the index below when status changes.

## Rules

- One concept per file. Split if a topic grows beyond a single teachable unit.
- Cross-link prerequisites and related concepts.
- Verified or refuted literature claims belong in the concept note, not only in chat.

## Index

| Concept | Module | Status |
|---------|--------|--------|
| [Tokenization](CONCEPT-tokenization.md) | lab/01-foundations | mastered |
