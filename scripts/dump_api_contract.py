#!/usr/bin/env python3
"""Write the ordered routes and OpenAPI schema to a JSON file."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
BACKEND_ROOT = (
    REPOSITORY_ROOT
    / "radiative-cooling-platform"
    / "backend"
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write the FastAPI contract to a JSON file.",
    )
    parser.add_argument(
        "output",
        type=Path,
        help="Output JSON file.",
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    output_path = arguments.output.resolve()

    os.chdir(BACKEND_ROOT)
    sys.path.insert(0, str(BACKEND_ROOT))

    from fastapi.routing import APIRoute
    from app.main import app

    ordered_routes: list[dict[str, object]] = []

    for route in app.routes:
        if not isinstance(route, APIRoute):
            continue

        methods = sorted(
            method
            for method in (route.methods or set())
            if method not in {"HEAD", "OPTIONS"}
        )

        ordered_routes.append(
            {
                "methods": methods,
                "name": route.name,
                "path": route.path,
            }
        )

    contract = {
        "ordered_routes": ordered_routes,
        "openapi": app.openapi(),
    }

    output_path.write_text(
        json.dumps(
            contract,
            ensure_ascii=True,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"API contract written to {output_path}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())