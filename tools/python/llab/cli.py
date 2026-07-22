"""Command-line entry point for the llab harness.

uv run llab eval --dataset tools/python/llab/sample.jsonl
uv run llab models
"""

from __future__ import annotations

import sys


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: llab <command> [args...]")
        print("commands: eval, models")
        return 1
    cmd = sys.argv[1]
    rest = sys.argv[2:]
    if cmd == "eval":
        from .eval import main as eval_main

        return eval_main(rest)
    if cmd == "models":
        from .models import main as models_main

        return models_main()
    print(f"unknown command: {cmd}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
