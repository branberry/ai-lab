"""Interpretability probes (skeleton).

These helpers require the optional ML deps:
    uv sync --extra ml

Implemented later, when you reach `lab/05-interpretability`. The skeletons
below document the intended signatures so evals and notebooks can be written
against them before the bodies exist.

Planned:
- logits_lens(model, input_ids, layer) -> token probabilities at that layer
- activation_capture(model, input_ids, layer) -> residual-stream activations
- steering_vector_add(model, input_ids, vector, layer, coefficient) -> modified outputs
"""

from __future__ import annotations

from typing import Any


def logits_lens(model: Any, input_ids: Any, layer: int) -> dict[str, Any]:
    """Project a layer's residual stream through the unembedding matrix.

    Returns {layer, token_probs: list[float], top_tokens: list[(token, prob)]}.
    """
    raise NotImplementedError("implement in lab/05-interpretability")


def activation_capture(model: Any, input_ids: Any, layer: int) -> Any:
    """Capture residual-stream activations at `layer` for `input_ids`."""
    raise NotImplementedError("implement in lab/05-interpretability")


def steering_vector_add(
    model: Any, input_ids: Any, vector: Any, layer: int, coefficient: float = 1.0
) -> Any:
    """Add `coefficient * vector` to the residual stream at `layer` during forward pass."""
    raise NotImplementedError("implement in lab/05-interpretability")
