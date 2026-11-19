"""Summarize completed optimization jobs (Markdown + JSON).

Aligned with the current OptimizationJobDetail / OptimizationResult /
RequirementMapResult schemas (plateau_fraction on the map, best_corner,
simulation_count, multi-variable optical space, etc.).

Usage (from backend/, API running):
    python scripts/summarize_optimizations.py --out docs/acceptance/stage-optimization
"""

from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import httpx

KEY_METRICS = (
    "peak_skin_temperature_c",
    "skin_exceedance_fraction",
    "peak_core_temperature_c",
    "mean_skin_cooling_c",
)

# Grouping keys
GROUP_EXCLUDE = {"name", "seed"}  # same setup, different seed
CURVE_EXCLUDE = GROUP_EXCLUDE | {"population_multiplier"}

# Common optical / clothing variables that may appear in best.parameters
PARAM_KEYS_OF_INTEREST = (
    "solar_reflectance",
    "solar_transmittance",
    "infrared_emissivity",
    "infrared_emissivity_window",
    "infrared_emissivity_outside_window",
    "infrared_emissivity_ground_facing",
    "infrared_transmittance",
    "clothing_insulation_clo",
    "evaporative_resistance_m2pa_w",
)


def fetch_details(client: httpx.Client, max_workers: int = 8) -> list[dict]:
    """Paginate list endpoint, then fetch completed job details in parallel."""
    items: list[dict] = []
    offset = 0
    while True:
        page = client.get(
            "/api/v1/optimizations",
            params={"limit": 100, "offset": offset},
        ).json()
        batch = page.get("items") or []
        items.extend(batch)
        offset += len(batch)
        total = page.get("total", offset)
        if not batch or offset >= total:
            break

    completed_ids = [i["id"] for i in items if i.get("status") == "completed"]
    if not completed_ids:
        return []

    details: list[dict] = []

    def _get(job_id: str) -> dict:
        return client.get(f"/api/v1/optimizations/{job_id}").json()

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_get, jid): jid for jid in completed_ids}
        for fut in as_completed(futures):
            try:
                details.append(fut.result())
            except Exception as exc:  # noqa: BLE001
                print(f"warn: failed to fetch {futures[fut]}: {exc}")

    # Stable order by name then id for reproducible summaries
    details.sort(key=lambda d: (d.get("name") or "", d.get("id") or ""))
    return details


def group_key(request: dict, exclude: set[str]) -> str:
    return json.dumps(
        {k: v for k, v in request.items() if k not in exclude},
        sort_keys=True,
        default=str,
    )


def safe_get(d: dict | None, *keys: str, default: Any = None) -> Any:
    cur: Any = d
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
        if cur is None:
            return default
    return cur


def summarize(detail: dict) -> dict:
    req = detail.get("request") or {}
    res = detail.get("result") or {}
    best = res.get("best") or {}
    upper = res.get("optical_upper_bound")
    rmap = res.get("requirement_map")
    baseline = res.get("baseline") or {}
    best_corner = res.get("best_corner")

    variables = req.get("variables") or []
    lower = {v["name"]: v.get("lower") for v in variables if isinstance(v, dict)}

    constraints = req.get("constraints") or []
    constraint_str = "; ".join(
        f'{c.get("metric")} {c.get("operator")} {c.get("threshold")}'
        for c in constraints
        if isinstance(c, dict)
    )

    best_params = best.get("parameters") or {}
    best_metrics = best.get("metrics")

    row: dict[str, Any] = {
        "name": detail.get("name"),
        "id": (detail.get("id") or "")[:8],
        "city": req.get("city_id"),
        "months": req.get("months"),
        "seed": req.get("seed"),
        "mult": req.get("population_multiplier"),
        "constraints": constraint_str,
        "verdict": res.get("verdict"),
        "algorithm": res.get("algorithm"),
        "model_version": res.get("model_version"),
        "best": {k: round(v, 4) for k, v in best_params.items() if isinstance(v, (int, float))},
        "best_objective": best.get("objective_value"),
        "best_violation": best.get("constraint_violation"),
        "best_feasible": best.get("feasible"),
        "best_metrics": (
            {k: best_metrics[k] for k in KEY_METRICS if k in best_metrics}
            if isinstance(best_metrics, dict)
            else None
        ),
        "baseline_feasible": baseline.get("feasible"),
        "upper_feasible": upper.get("feasible") if upper else None,
        "upper_violation": upper.get("constraint_violation") if upper else None,
        "upper_peak_skin": safe_get(upper, "metrics", "peak_skin_temperature_c"),
        "best_corner_feasible": best_corner.get("feasible") if best_corner else None,
        "best_corner_params": (
            {k: round(v, 4) for k, v in (best_corner.get("parameters") or {}).items()
             if isinstance(v, (int, float))}
            if best_corner
            else None
        ),
        "evaluations": res.get("evaluation_count"),
        "simulations": res.get("simulation_count"),
        "sample_count": res.get("sample_count"),
        "generations": res.get("generations"),
        "seconds": res.get("elapsed_seconds"),
        "warnings": res.get("warnings") or [],
        "sensitivities": res.get("sensitivities") or [],
        "parameter_fingerprint": res.get("parameter_fingerprint"),
    }

    if rmap:
        # Prefer server-computed plateau_fraction; fall back only if absent
        plateau = rmap.get("plateau_fraction")
        if plateau is None:
            cells_flat = [c for r in (rmap.get("cells") or []) for c in r if c]
            values = [c["metric_value"] for c in cells_flat if "metric_value" in c]
            if values:
                low = min(values)
                plateau = sum(abs(v - low) < 1e-6 for v in values) / len(values)

        cells = [c for r in (rmap.get("cells") or []) for c in r if c]
        n_cells = len(cells) or 1
        x_var = rmap.get("x_variable")
        y_var = rmap.get("y_variable")

        row.update({
            "map": f"{x_var} × {y_var}" if x_var and y_var else None,
            "min_x_at_max_y": rmap.get("minimum_x_at_max_y"),
            "min_y_at_max_x": rmap.get("minimum_y_at_max_x"),
            "required_x_at_best_y": rmap.get("required_x_at_best_y"),
            "required_y_at_best_x": rmap.get("required_y_at_best_x"),
            "objective_trend": [
                rmap.get("objective_trend_x"),
                rmap.get("objective_trend_y"),
            ],
            "x_demand_direction": rmap.get("x_demand_direction"),
            "y_demand_direction": rmap.get("y_demand_direction"),
            "metric_min": rmap.get("metric_min"),
            "metric_max": rmap.get("metric_max"),
            "plateau_fraction": plateau,
            "feasible_cell_share": round(
                sum(1 for c in cells if c.get("feasible")) / n_cells, 3
            ),
            # Lower bound already feasible → true requirement lies below the searched range
            "x_lower_bound_binding": (
                rmap.get("minimum_x_at_max_y") == lower.get(x_var)
                if x_var and lower.get(x_var) is not None
                else None
            ),
            "y_lower_bound_binding": (
                rmap.get("minimum_y_at_max_x") == lower.get(y_var)
                if y_var and lower.get(y_var) is not None
                else None
            ),
            "frontier": rmap.get("frontier"),
            "fixed_parameters": rmap.get("fixed_parameters"),
        })
    else:
        row["plateau_fraction"] = None

    return row


def stats(values: list[float]) -> str:
    clean = [v for v in values if v is not None and isinstance(v, (int, float))]
    if not clean:
        return "—"
    if len(clean) < 2:
        return f"{clean[0]:.4f}"
    return f"{statistics.mean(clean):.4f} ± {statistics.stdev(clean):.4f}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize completed optimization jobs from the running API."
    )
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=8, help="Parallel detail fetches")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    with httpx.Client(base_url=args.base_url, timeout=120.0) as client:
        details = fetch_details(client, max_workers=args.workers)

    if not details:
        print("No completed optimization jobs found.")
        (args.out / "optimization-summary.md").write_text(
            "# No completed jobs\n", encoding="utf-8"
        )
        (args.out / "optimization-summary.json").write_text(
            json.dumps({"runs": [], "curves": []}, indent=2), encoding="utf-8"
        )
        return

    rows = [summarize(d) for d in details]

    # --- Markdown table ---
    header = (
        "| name | verdict | best | objective | violation | "
        "upper feasible (viol) | min x @ max y | min y @ max x | "
        "x lower binding | plateau |"
    )
    sep = "|---|---|---|---|---|---|---|---|---|---|"
    lines: list[str] = [header, sep]

    for r in rows:
        lines.append(
            f'| {r["name"]} | {r["verdict"]} | {r["best"]} | {r["best_objective"]} | '
            f'{r["best_violation"]} | {r["upper_feasible"]} ({r["upper_violation"]}) | '
            f'{r.get("min_x_at_max_y")} | {r.get("min_y_at_max_x")} | '
            f'{r.get("x_lower_bound_binding")} | {r["plateau_fraction"]} |'
        )
        pf = r.get("plateau_fraction")
        if pf is not None and pf > 0.2:
            lines.append(
                f'|  ⚠ {r["name"]}: {pf:.0%} of map cells share the minimum; '
                f"the reported optimum is arbitrary |||||||||"
            )

    # --- Seed groups (generalised over any parameters present) ---
    seeds: dict[str, list[dict]] = defaultdict(list)
    for d, r in zip(details, rows):
        seeds[group_key(d.get("request") or {}, GROUP_EXCLUDE)].append(r)

    lines += ["", "## Seed groups", ""]
    # Dynamic columns from parameters that actually appear
    param_cols = [
        k for k in PARAM_KEYS_OF_INTEREST
        if any(k in (g.get("best") or {}) for group in seeds.values() for g in group)
    ]
    seed_header = "| first name | n | " + " | ".join(param_cols) + " | objective |"
    seed_sep = "|---|" + "---|" * (len(param_cols) + 2)
    lines += [seed_header, seed_sep]

    for group in seeds.values():
        if len(group) < 2:
            continue
        cells = [group[0]["name"], str(len(group))]
        for pk in param_cols:
            vals = [g["best"].get(pk) for g in group if pk in (g.get("best") or {})]
            cells.append(stats(vals))  # type: ignore[arg-type]
        objs = [g["best_objective"] for g in group if g.get("best_objective") is not None]
        cells.append(stats(objs))  # type: ignore[arg-type]
        lines.append("| " + " | ".join(cells) + " |")

    # --- Convergence curves ---
    curves: dict[str, list[dict]] = defaultdict(list)
    for d in details:
        hist = d.get("history") or []
        curves[group_key(d.get("request") or {}, CURVE_EXCLUDE)].append({
            "name": d.get("name"),
            "multiplier": (d.get("request") or {}).get("population_multiplier"),
            "seed": (d.get("request") or {}).get("seed"),
            "curve": [
                (h.get("evaluation_count"), h.get("penalised_objective"))
                for h in hist
                if isinstance(h, dict)
            ],
        })

    md_path = args.out / "optimization-summary.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    json_path = args.out / "optimization-summary.json"
    json_path.write_text(
        json.dumps({"runs": rows, "curves": list(curves.values())}, indent=2, default=str),
        encoding="utf-8",
    )

    print("\n".join(lines))
    print(f"\nWrote {md_path} and {json_path} ({len(rows)} runs)")


if __name__ == "__main__":
    main()