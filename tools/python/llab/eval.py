"""Minimal eval runner.

Takes a JSONL dataset of `{prompt, expected}` (exact-match / regex) or
`{prompt, judge}` (LLM-judge), runs `llab.client.generate` over it, scores,
prints a table, and writes results to `results/<eval-name>-<timestamp>.jsonl`.

This is the single most important file in the repo — it's how you turn
"I think this is better" into "this is measurably better."

Example:
    uv run python -m llab.eval --dataset tools/python/llab/sample.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from .client import GenerateParams, default_judge_model, default_model, generate


@dataclass
class Example:
    prompt: str
    expected: str | None = None
    judge: str | None = None
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass
class ScoredExample:
    example: Example
    output: str
    score: float
    scorer: str
    detail: str = ""


def load_dataset(path: str) -> list[Example]:
    examples: list[Example] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            examples.append(
                Example(
                    prompt=obj["prompt"],
                    expected=obj.get("expected"),
                    judge=obj.get("judge"),
                    meta={k: v for k, v in obj.items() if k not in {"prompt", "expected", "judge"}},
                )
            )
    return examples


def score_exact_match(output: str, expected: str) -> float:
    return 1.0 if output.strip() == expected.strip() else 0.0


def score_regex(output: str, expected: str) -> float:
    """`expected` is a regex. Score 1.0 if it matches anywhere in output."""
    return 1.0 if re.search(expected, output) else 0.0


def score_llm_judge(output: str, judge_prompt: str, judge_model: str) -> tuple[float, str]:
    """Ask the judge model to score the output 0.0–1.0 given judge_prompt.

    Returns (score, raw_judge_text). Parses the first float in the response.
    """
    full = (
        f"{judge_prompt}\n\n--- Output to judge ---\n{output}\n--- End output ---\n\n"
        "Respond with a single number between 0.0 and 1.0 only."
    )
    res = generate(judge_model, full, params=GenerateParams(temperature=0.0))
    text = res.text.strip()
    m = re.search(r"\d+(\.\d+)?", text)
    score = float(m.group(0)) if m else 0.0
    return max(0.0, min(1.0, score)), text


def score_one(ex: Example, output: str, judge_model: str | None) -> ScoredExample:
    if ex.expected is not None and ex.meta.get("scorer") == "regex":
        s = score_regex(output, ex.expected)
        return ScoredExample(ex, output, s, "regex")
    if ex.expected is not None:
        s = score_exact_match(output, ex.expected)
        return ScoredExample(ex, output, s, "exact_match")
    if ex.judge is not None and judge_model is not None:
        s, detail = score_llm_judge(output, ex.judge, judge_model)
        return ScoredExample(ex, output, s, "llm_judge", detail)
    return ScoredExample(ex, output, 0.0, "none")


def run_eval(
    dataset_path: str,
    model: str | None = None,
    judge_model: str | None = None,
    params: GenerateParams | None = None,
    results_dir: str = "tools/python/llab/results",
) -> list[ScoredExample]:
    model = model or default_model()
    judge_model = judge_model or default_judge_model()
    params = params or GenerateParams(temperature=0.0)

    examples = load_dataset(dataset_path)
    scored: list[ScoredExample] = []
    print(f"Eval: {len(examples)} examples | model={model} | judge={judge_model}")
    print("-" * 60)
    for i, ex in enumerate(examples, 1):
        res = generate(model, ex.prompt, params=params)
        s = score_one(ex, res.text, judge_model)
        scored.append(s)
        flag = "OK " if s.score >= 0.999 else "XX "
        print(
            f"{flag}[{i:2d}/{len(examples)}] score={s.score:.2f} ({s.scorer}) :: {res.text[:60]!r}"
        )

    print("-" * 60)
    mean = sum(s.score for s in scored) / max(1, len(scored))
    print(f"mean score: {mean:.3f} over {len(scored)} examples")

    Path(results_dir).mkdir(parents=True, exist_ok=True)
    stem = Path(dataset_path).stem
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = Path(results_dir) / f"{stem}-{ts}.jsonl"
    with open(out_path, "w") as f:
        for s in scored:
            f.write(
                json.dumps(
                    {
                        "prompt": s.example.prompt,
                        "expected": s.example.expected,
                        "output": s.output,
                        "score": s.score,
                        "scorer": s.scorer,
                        "detail": s.detail,
                        "model": model,
                    }
                )
                + "\n"
            )
    print(f"results: {out_path}")
    return scored


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="llab.eval", description="Run an eval over a JSONL dataset.")
    p.add_argument("--dataset", required=True, help="Path to JSONL dataset.")
    p.add_argument("--model", default=None, help="Model id (default: $LAB_MODEL).")
    p.add_argument("--judge", default=None, help="Judge model id (default: $LAB_JUDGE_MODEL).")
    p.add_argument("--temperature", type=float, default=0.0)
    p.add_argument("--top-p", type=float, default=1.0)
    p.add_argument("--num-predict", type=int, default=None)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--results-dir", default="tools/python/llab/results")
    args = p.parse_args(argv)

    params = GenerateParams(
        temperature=args.temperature,
        top_p=args.top_p,
        num_predict=args.num_predict,
        seed=args.seed,
    )
    t0 = time.time()
    run_eval(
        dataset_path=args.dataset,
        model=args.model,
        judge_model=args.judge,
        params=params,
        results_dir=args.results_dir,
    )
    print(f"elapsed: {time.time() - t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
