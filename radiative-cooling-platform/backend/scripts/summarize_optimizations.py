"""Summarize completed optimization jobs (Markdown + JSON).

Usage (from backend/, API running):
    python scripts/summarize_optimizations.py --out docs/acceptance/stage-optimization
"""

from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path

import httpx

KEY_METRICS = ("peak_skin_temperature_c", "skin_exceedance_fraction",
               "peak_core_temperature_c", "mean_skin_cooling_c")
GROUP_EXCLUDE = {"name", "seed"}              # D: same setup, different seed
CURVE_EXCLUDE = GROUP_EXCLUDE | {"population_multiplier"}  # E


def fetch_details(client: httpx.Client) -> list[dict]:
    items, offset = [], 0
    while True:
        page = client.get("/api/v1/optimizations", params={"limit": 100, "offset": offset}).json()
        items += page["items"]
        offset += len(page["items"])
        if not page["items"] or offset >= page["total"]:
            break
    return [client.get(f"/api/v1/optimizations/{i['id']}").json()
            for i in items if i["status"] == "completed"]


def group_key(request: dict, exclude: set[str]) -> str:
    return json.dumps({k: v for k, v in request.items() if k not in exclude}, sort_keys=True)


def plateau_fraction(rmap: dict | None) -> float | None:
    """Share of map cells whose metric equals the minimum (flat objective)."""
    if not rmap:
        return None
    values = [c["metric_value"] for row in rmap["cells"] for c in row if c]
    if not values:
        return None
    low = min(values)
    return sum(abs(v - low) < 1e-6 for v in values) / len(values)


def summarize(detail: dict) -> dict:
    req, res = detail["request"], detail["result"]
    best, upper, rmap = res["best"], res["optical_upper_bound"], res["requirement_map"]
    lower = {v["name"]: v["lower"] for v in req["variables"]}

    row = {
        "name": detail["name"], "id": detail["id"][:8], "city": req["city_id"],
        "months": req["months"], "seed": req["seed"], "mult": req["population_multiplier"],
        "constraints": "; ".join(f'{c["metric"]} {c["operator"]} {c["threshold"]}' for c in req["constraints"]),
        "verdict": res["verdict"],
        "best": {k: round(v, 4) for k, v in best["parameters"].items()},
        "best_objective": best["objective_value"],
        "best_violation": best["constraint_violation"],
        "best_metrics": {k: best["metrics"][k] for k in KEY_METRICS} if best["metrics"] else None,
        "baseline_feasible": res["baseline"]["feasible"],
        "upper_feasible": upper["feasible"] if upper else None,
        "upper_violation": upper["constraint_violation"] if upper else None,
        "upper_peak_skin": upper["metrics"]["peak_skin_temperature_c"] if upper and upper["metrics"] else None,
        "evaluations": res["evaluation_count"], "generations": res["generations"],
        "seconds": res["elapsed_seconds"],
        "plateau_fraction": plateau_fraction(rmap),
    }
    if rmap:
        cells = [c for r in rmap["cells"] for c in r if c]
        row.update({
            "map": f'{rmap["x_variable"]} × {rmap["y_variable"]}',
            "min_x_at_max_y": rmap["minimum_x_at_max_y"],
            "min_y_at_max_x": rmap["minimum_y_at_max_x"],
            "feasible_cell_share": round(sum(c["feasible"] for c in cells) / len(cells), 3),
            # The searched lower bound is already feasible -> true requirement is below it.
            "x_lower_bound_binding": rmap["minimum_x_at_max_y"] == lower.get(rmap["x_variable"]),
            "frontier": rmap["frontier"],
        })
    return row


def stats(values: list[float]) -> str:
    if len(values) < 2:
        return f"{values[0]:.4f}" if values else "—"
    return f"{statistics.mean(values):.4f} ± {statistics.stdev(values):.4f}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    with httpx.Client(base_url=args.base_url, timeout=60) as client:
        details = fetch_details(client)
    rows = [summarize(d) for d in details]

    lines = ["| name | verdict | best | objective | violation | upper feasible (viol) | min x @ max y | min y @ max x | lower bound binding | plateau |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(
            f'| {r["name"]} | {r["verdict"]} | {r["best"]} | {r["best_objective"]} | {r["best_violation"]} '
            f'| {r["upper_feasible"]} ({r["upper_violation"]}) | {r.get("min_x_at_max_y")} | {r.get("min_y_at_max_x")} '
            f'| {r.get("x_lower_bound_binding")} | {r["plateau_fraction"]} |'
        )
        if r["plateau_fraction"] and r["plateau_fraction"] > 0.2:
            lines.append(f'|  ⚠ {r["name"]}: {r["plateau_fraction"]:.0%} of map cells share the minimum; '
                         'the reported optimum is arbitrary |||||||||')

    seeds = defaultdict(list)
    for d, r in zip(details, rows):
        seeds[group_key(d["request"], GROUP_EXCLUDE)].append(r)
    lines += ["", "## Seed groups", "", "| first name | n | ρ | ε | objective |", "|---|---|---|---|---|"]
    for group in seeds.values():
        if len(group) < 2:
            continue
        rho = [g["best"].get("solar_reflectance") for g in group if "solar_reflectance" in g["best"]]
        eps = [g["best"].get("infrared_emissivity") for g in group if "infrared_emissivity" in g["best"]]
        obj = [g["best_objective"] for g in group if g["best_objective"] is not None]
        lines.append(f'| {group[0]["name"]} | {len(group)} | {stats(rho)} | {stats(eps)} | {stats(obj)} |')

    curves = defaultdict(list)
    for d in details:
        curves[group_key(d["request"], CURVE_EXCLUDE)].append({
            "name": d["name"], "multiplier": d["request"]["population_multiplier"],
            "seed": d["request"]["seed"],
            "curve": [(h["evaluation_count"], h["penalised_objective"]) for h in d["history"]],
        })

    (args.out / "optimization-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (args.out / "optimization-summary.json").write_text(
        json.dumps({"runs": rows, "curves": list(curves.values())}, indent=2), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()