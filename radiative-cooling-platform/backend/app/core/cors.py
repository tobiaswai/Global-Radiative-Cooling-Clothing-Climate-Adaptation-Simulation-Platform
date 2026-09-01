"""Central CORS middleware configuration."""

from __future__ import annotations

from collections.abc import Sequence

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def normalize_values(values: Sequence[str]) -> list[str]:
    """Remove blank and duplicate configuration values."""
    normalized: list[str] = []
    seen: set[str] = set()

    for value in values:
        item = value.strip()

        if not item or item in seen:
            continue

        normalized.append(item)
        seen.add(item)

    return normalized


def add_cors_middleware(
    application: FastAPI,
    *,
    origins: Sequence[str],
    methods: Sequence[str],
    headers: Sequence[str],
    expose_headers: Sequence[str],
    allow_credentials: bool,
) -> None:
    """Register CORS middleware exactly once."""
    already_registered = any(
        getattr(middleware, "cls", None) is CORSMiddleware
        for middleware in application.user_middleware
    )

    if already_registered:
        raise RuntimeError(
            "CORS middleware has already been registered."
        )

    normalized_origins = normalize_values(origins)
    normalized_methods = [
        method.upper()
        for method in normalize_values(methods)
    ]
    normalized_headers = normalize_values(headers)
    normalized_exposed_headers = normalize_values(expose_headers)

    if not normalized_origins:
        raise ValueError(
            "At least one CORS origin must be configured."
        )

    if not normalized_methods:
        raise ValueError(
            "At least one CORS method must be configured."
        )

    if allow_credentials:
        wildcard_fields = {
            "origins": normalized_origins,
            "methods": normalized_methods,
            "headers": normalized_headers,
        }

        for field_name, values in wildcard_fields.items():
            if "*" in values:
                raise ValueError(
                    "CORS wildcard values cannot be used for "
                    f"{field_name} when credentials are enabled."
                )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=normalized_origins,
        allow_credentials=allow_credentials,
        allow_methods=normalized_methods,
        allow_headers=normalized_headers,
        expose_headers=normalized_exposed_headers,
    )