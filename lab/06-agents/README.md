# 06 — Agents

Tool use, planning, context limits, failure modes (loops, hallucinated tools, lost-in-the-middle).

## Objectives

- Build a minimal tool-use loop with a provider SDK or the Cursor SDK.
- Probe context-length limits with a long-context task.
- Enumerate the ways agents fail and tie each to a logged `LL-` weakness.
- Catalog at least 3 distinct agent failure modes.

## Resources

- ReAct paper (Yao et al.)
- "Lost in the Middle" paper (Liu et al.)
- Provider SDK tool-use docs (Anthropic, OpenAI)
- Cursor SDK docs (if using `tools/ts/llab/agent.ts`)
- `tools/ts/llab/agent.ts` in this repo

## Exercises

- `exercises/01-minimal-tool-loop.md` — build a 1-tool agent (e.g. a calculator) and trace its loop.
- `exercises/02-context-limit.md` — construct a prompt that places a key fact at the start, middle, and end of a long context; measure retrieval accuracy.
- `exercises/03-failure-modes.md` — induce at least 3 distinct failures (infinite loop, hallucinated tool name, lost-in-the-middle) and log each as `LL-NNNN`.
- `exercises/04-technique-sketch.md` — for one of the logged failures, sketch a `TECH-NNNN` idea and run an eval.

## Notes

See `notes.md`.
