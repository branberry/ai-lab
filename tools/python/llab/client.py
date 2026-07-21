"""Unified generation client.

Routes to Ollama or a provider API based on a model prefix:
- `ollama/<name>`  → local Ollama (default)
- `openai/<name>`  → OpenAI API
- `anthropic/<name>` → Anthropic API

Returns a normalized `GenerateResult` regardless of backend so evals and
probes don't care which model they're hitting.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Any

import requests


@dataclass
class GenerateResult:
    text: str
    usage: dict[str, int] = field(default_factory=dict)
    logprobs: list[dict[str, Any]] | None = None
    raw: dict[str, Any] = field(default_factory=dict)
    model: str = ""
    backend: str = ""

    def __post_init__(self) -> None:
        if not self.model:
            self.model = ""
        if not self.backend:
            self.backend = ""


@dataclass
class GenerateParams:
    temperature: float = 0.0
    top_p: float = 1.0
    top_k: int | None = None
    min_p: float | None = None
    num_predict: int | None = None
    stop: list[str] | None = None
    seed: int | None = None
    extra: dict[str, Any] = field(default_factory=dict)

    def to_ollama_options(self) -> dict[str, Any]:
        opts: dict[str, Any] = {
            "temperature": self.temperature,
            "top_p": self.top_p,
        }
        if self.top_k is not None:
            opts["top_k"] = self.top_k
        if self.min_p is not None:
            opts["min_p"] = self.min_p
        if self.num_predict is not None:
            opts["num_predict"] = self.num_predict
        if self.stop:
            opts["stop"] = self.stop
        if self.seed is not None:
            opts["seed"] = self.seed
        opts.update(self.extra)
        return opts


def _load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for path in (".env", os.path.expanduser("~/.ai-lab.env")):
        if os.path.exists(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    env.setdefault(k.strip(), v.strip())
    return env


def _env(key: str, default: str | None = None) -> str | None:
    val = os.environ.get(key)
    if val is None:
        val = _load_env().get(key)
    return val if val is not None else default


def default_model() -> str:
    return _env("LAB_MODEL", "ollama/qwen2.5:7b-instruct") or "ollama/qwen2.5:7b-instruct"


def default_judge_model() -> str:
    return _env("LAB_JUDGE_MODEL", "ollama/qwen2.5:14b-instruct") or "ollama/qwen2.5:14b-instruct"


def split_backend(model: str) -> tuple[str, str]:
    """Split `backend/name` into (backend, name). Defaults to ollama."""
    if "/" in model:
        backend, name = model.split("/", 1)
        return backend, name
    return "ollama", model


def generate(
    model: str | None = None,
    prompt: str = "",
    *,
    system: str | None = None,
    params: GenerateParams | None = None,
    stream: bool = False,
) -> GenerateResult:
    """Generate a completion for `prompt` using `model`.

    `model` defaults to `LAB_MODEL`. Use a `backend/name` prefix to pick the
    backend. Currently only the `ollama` backend is implemented; `openai` and
    `anthropic` raise NotImplementedError (wire them up when you need them).
    """
    model = model or default_model()
    params = params or GenerateParams()
    backend, name = split_backend(model)

    full_prompt = f"{system}\n\n{prompt}" if system else prompt

    if backend == "ollama":
        return _generate_ollama(name, full_prompt, params, model, stream)
    if backend == "openai":
        raise NotImplementedError("openai backend — wire up when needed")
    if backend == "anthropic":
        raise NotImplementedError("anthropic backend — wire up when needed")
    raise ValueError(f"unknown backend: {backend!r}")


def _generate_ollama(
    name: str, prompt: str, params: GenerateParams, model: str, stream: bool
) -> GenerateResult:
    base_url = _env("OLLAMA_BASE_URL", "http://localhost:11434") or "http://localhost:11434"
    url = f"{base_url.rstrip('/')}/api/generate"
    payload: dict[str, Any] = {
        "model": name,
        "prompt": prompt,
        "stream": stream,
        "options": params.to_ollama_options(),
    }
    resp = requests.post(url, json=payload, timeout=600)
    resp.raise_for_status()
    data = resp.json()
    return GenerateResult(
        text=data.get("response", ""),
        usage={
            "prompt_eval_count": data.get("prompt_eval_count", 0),
            "eval_count": data.get("eval_count", 0),
        },
        logprobs=None,
        raw=data,
        model=model,
        backend="ollama",
    )


def generate_many(
    model: str | None,
    items: list[dict[str, Any]],
    *,
    params: GenerateParams | None = None,
    prompt_key: str = "prompt",
) -> list[GenerateResult]:
    """Convenience: generate for each item, using item[prompt_key] as the prompt."""
    out: list[GenerateResult] = []
    for it in items:
        out.append(generate(model, it[prompt_key], params=params))
    return out


def to_jsonl(results: list[GenerateResult], path: str) -> None:
    with open(path, "w") as f:
        for r in results:
            f.write(json.dumps({"text": r.text, "usage": r.usage, "model": r.model}) + "\n")
