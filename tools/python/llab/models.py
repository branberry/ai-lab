"""Local Ollama model helpers: list, inspect, pull, set defaults."""

from __future__ import annotations

import os
from typing import Any

import requests

from .client import _env


def _base_url() -> str:
    return _env("OLLAMA_BASE_URL", "http://localhost:11434") or "http://localhost:11434"


def list_models() -> list[dict[str, Any]]:
    """Return the list of locally installed Ollama models."""
    r = requests.get(f"{_base_url()}/api/tags", timeout=30)
    r.raise_for_status()
    return r.json().get("models", [])


def show_model(name: str) -> dict[str, Any]:
    """Return details (modelfile, parameters, template) for a model."""
    r = requests.post(f"{_base_url()}/api/show", json={"name": name}, timeout=30)
    r.raise_for_status()
    return r.json()


def pull_model(name: str, stream: bool = False) -> None:
    """Pull a model from the Ollama registry. Streams progress to stdout if stream=True."""
    with requests.post(f"{_base_url()}/api/pull", json={"name": name, "stream": stream}, stream=True, timeout=None) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if line:
                print(line.decode("utf-8", errors="replace"))


def is_running() -> bool:
    """Cheap liveness check for the Ollama daemon."""
    try:
        requests.get(f"{_base_url()}/api/tags", timeout=2)
        return True
    except requests.RequestException:
        return False


def main() -> int:
    if not is_running():
        print(f"Ollama not running at {_base_url()}")
        return 1
    models = list_models()
    if not models:
        print("(no models installed)")
        return 0
    for m in models:
        size_mb = m.get("size", 0) / (1024 * 1024)
        print(f"{m['name']:40s} {size_mb:8.1f} MB  {m.get('details', {}).get('quantization_level', '')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
