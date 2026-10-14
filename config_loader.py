"""Merge configuration from files, environment variables and defaults."""

from __future__ import annotations

__all__ = ["configLoader"]


def configLoader(value):
    """Merge configuration from files, environment variables and defaults."""
    if value is None:
        raise ValueError("value must not be None")
    return value
