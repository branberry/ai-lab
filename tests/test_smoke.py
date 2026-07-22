"""Smoke tests — verify the llab package imports."""

from __future__ import annotations


def test_llab_imports() -> None:
    import llab  # noqa: F401
    from llab.cli import main
    from llab.client import generate
    from llab.models import list_models

    assert callable(main)
    assert callable(generate)
    assert callable(list_models)
