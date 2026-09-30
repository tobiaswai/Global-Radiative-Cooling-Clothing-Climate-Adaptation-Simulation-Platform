"""Tests for duplicate API route registration."""

from collections import Counter

from fastapi.routing import APIRoute

from app.main import app


def test_method_and_path_pairs_are_unique() -> None:
    route_pairs: list[tuple[str, str]] = []

    for route in app.routes:
        if not isinstance(route, APIRoute):
            continue

        for method in route.methods or set():
            if method in {"HEAD", "OPTIONS"}:
                continue

            route_pairs.append((method, route.path))

    counts = Counter(route_pairs)

    duplicates = sorted(
        route_pair
        for route_pair, count in counts.items()
        if count > 1
    )

    assert not duplicates, (
        f"Duplicate route registrations were found: {duplicates}"
    )