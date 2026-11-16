"""Submit the Stage 10 acceptance runs.

Usage (from backend/, API and an optimization worker running):
    python scripts/run_stage10_experiments.py
    python scripts/run_stage10_experiments.py --only F1,F2,H
Then: python scripts/summarize_optimizations.py --out docs/acceptance/stage-10-spectral
"""

from __future__ import annotations

import argparse

import httpx

PERSON = {"met": 2.6, "body_mass_kg": 70, "body_surface_area_m2": 1.8,
          "initial_core_temperature_c": 36.8, "initial_skin_temperature_c": 33.7, "position": "standing"}
CONTROL = {"name": "Conventional clothing", "clothing_insulation_clo": 0.5, "solar_reflectance": 0.3,
           "solar_transmittance": 0, "infrared_emissivity": 0.9, "projected_solar_area_factor": 0.25}
RC = {"name": "RC candidate", "clothing_insulation_clo": 0.4, "solar_reflectance": 0.9,
      "solar_transmittance": 0, "infrared_emissivity": 0.95, "projected_solar_area_factor": 0.25}

RHO = {"name": "solar_reflectance", "lower": 0.3, "upper": 0.98}
EPS = {"name": "infrared_emissivity", "lower": 0.5, "upper": 0.99}
EPS_WIDE = {"name": "infrared_emissivity", "lower": 0.05, "upper": 0.99}
EPS_W = {"name": "infrared_emissivity_window", "lower": 0.5, "upper": 0.99}
EPS_N = {"name": "infrared_emissivity_outside_window", "lower": 0.05, "upper": 0.99}
EQUAL_TO_AIR = {"mean_radiant_temperature_method": "equal_to_air"}


def c(metric, operator, threshold):
    return {"metric": metric, "operator": operator, "threshold": threshold}


def request(name, city, months, variables, objective, constraints, *,
            map_axes=None, seed=42, assumptions=None, tolerance=1e-4):
    return {
        "name": name, "city_id": city, "year": 2023, "months": months,
        "sample_days_per_month": 3, "local_start_hour": 12, "duration_minutes": 120,
        "output_interval_minutes": 5, "skin_threshold_c": 35, "core_threshold_c": 38,
        "person": PERSON, "control_material": CONTROL, "base_material": RC,
        "environment_assumptions": assumptions or {},
        "variables": variables,
        "objective": {"metric": objective[0], "sense": objective[1]},
        "constraints": constraints,
        "population_multiplier": 10, "max_generations": 30, "seed": seed,
        "secondary_demand_weight": 1e-3, "convergence_tolerance": tolerance,
        "requirement_map": (
            {"x_variable": map_axes[0], "y_variable": map_axes[1], "resolution": 11} if map_axes else None
        ),
    }


GZ_CONSTRAINTS = [c("skin_exceedance_fraction", "<=", 0.1), c("peak_core_temperature_c", "<=", 38)]
RHO_EPS_MAP = ("solar_reflectance", "infrared_emissivity")

EXPERIMENTS = {
    "F1": request("S10-F1 Guangzhou Aug exceedance (rerun Exp-B)", "guangzhou", [8], [RHO, EPS],
                  ("skin_exceedance_fraction", "minimize"), GZ_CONSTRAINTS, map_axes=RHO_EPS_MAP),
    "F2": request("S10-F2 Guangzhou Aug degree-hours", "guangzhou", [8], [RHO, EPS],
                  ("skin_excess_degree_hours", "minimize"), [c("peak_core_temperature_c", "<=", 38)],
                  map_axes=RHO_EPS_MAP),
    "G1": request("S10-G1 Dubai Jul gray eps, MRT air+solar", "dubai", [7], [EPS_WIDE],
                  ("peak_core_temperature_c", "minimize"), []),
    "G2": request("S10-G2 Dubai Jul gray eps, MRT = air", "dubai", [7], [EPS_WIDE],
                  ("peak_core_temperature_c", "minimize"), [], assumptions=EQUAL_TO_AIR),
    "H1": request("S10-H1 Dubai Jul selective, MRT air+solar", "dubai", [7], [RHO, EPS_W, EPS_N],
                  ("skin_excess_degree_hours", "minimize"), [c("peak_core_temperature_c", "<=", 38)],
                  map_axes=("infrared_emissivity_window", "infrared_emissivity_outside_window")),
    "H2": request("S10-H2 Dubai Jul selective, MRT = air", "dubai", [7], [RHO, EPS_W, EPS_N],
                  ("skin_excess_degree_hours", "minimize"), [c("peak_core_temperature_c", "<=", 38)],
                  map_axes=("infrared_emissivity_window", "infrared_emissivity_outside_window"),
                  assumptions=EQUAL_TO_AIR),
    **{
        f"I-s{seed}": request(f"S10-I Lhasa Jul material demand seed {seed}", "lhasa", [7], [RHO, EPS],
                              ("material_demand", "minimize"), GZ_CONSTRAINTS,
                              map_axes=RHO_EPS_MAP, seed=seed)
        for seed in (42, 1, 2, 3, 4, 5)
    },
    **{
        f"J-{tol:g}": request(f"S10-J Dubai Jul peak core, atol {tol:g}", "dubai", [7], [EPS_WIDE],
                              ("peak_core_temperature_c", "minimize"), [], tolerance=tol)
        for tol in (1e-3, 1e-4, 1e-5)
    },
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--only", default="")
    args = parser.parse_args()
    selected = [k for k in EXPERIMENTS if not args.only or k in args.only.split(",")]

    with httpx.Client(base_url=args.base_url, timeout=60) as client:
        for key in selected:
            response = client.post("/api/v1/optimizations", json=EXPERIMENTS[key])
            response.raise_for_status()
            print(f"{key:8s} {response.json()['id']}  {EXPERIMENTS[key]['name']}")


if __name__ == "__main__":
    main()