"""Compare annual city metrics of two global batches (Stage 12 L4).

Usage: python scripts/compare_batches.py <batch_a> <batch_b> [--tolerance 1e-4]
Exit code 1 if any metric differs by more than the tolerance.
"""

from __future__ import annotations

import argparse
import sys

import httpx

FIELDS = (
    "annual_average_skin_improvement_c",
    "annual_average_core_improvement_c",
    "climate_adaptation_rate_percent",
    "exposure_coverage_percent",
)


def load(client: httpx.Client, batch_id: str) -> dict[str, dict]:
    r = client.get(f"/api/v1/global-batches/{batch_id}")
    r.raise_for_status()
    return {c["city_id"]: c for c in r.json()["city_results"] if c["status"] == "completed"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("a")
    parser.add_argument("b")
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--tolerance", type=float, default=1e-4)
    args = parser.parse_args()

    with httpx.Client(base_url=args.base_url, timeout=60) as client:
        a, b = load(client, args.a), load(client, args.b)

    worst = 0.0
    for city in sorted(set(a) | set(b)):
        if city not in a or city not in b:
            print(f"{city:12s} only in {'A' if city in a else 'B'}")
            worst = float("inf")
            continue
        for field in FIELDS:
            va, vb = a[city][field], b[city][field]
            if va is None or vb is None:
                same = va == vb
                diff = 0.0 if same else float("inf")
            else:
                diff = abs(va - vb)
            worst = max(worst, diff)
            print(f"{city:12s} {field:36s} {va!s:>10} {vb!s:>10} diff {diff:.2e}")

    print(f"max diff {worst:.2e} (tolerance {args.tolerance:g})")
    sys.exit(0 if worst <= args.tolerance else 1)


if __name__ == "__main__":
    main()