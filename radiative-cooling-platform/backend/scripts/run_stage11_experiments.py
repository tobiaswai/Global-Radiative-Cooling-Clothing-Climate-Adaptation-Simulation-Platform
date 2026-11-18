"""Stage 11 acceptance runs. Usage (from backend/): python scripts/run_stage11_experiments.py [--only G3,H3]"""

from __future__ import annotations

import argparse

import httpx

from run_stage10_experiments import CONTROL, EPS_N, EPS_W, EPS_WIDE, PERSON, RC, RHO, EPS, c, request

PHYSICAL = {"mean_radiant_temperature_method": "ground_energy_balance",
            "sky_temperature_method": "brutsaert_cloud"}
CORE = [c("peak_core_temperature_c", "<=", 38)]

OPTIMIZATIONS = {
    "G3": request("S11-G3 Dubai Jul gray eps, physical env", "dubai", [7], [EPS_WIDE],
                  ("peak_core_temperature_c", "minimize"), [], assumptions=PHYSICAL),
    **{
        f"G3-k{k}": request(f"S11-G3 Dubai Jul gray eps, physical env, K={k}", "dubai", [7], [EPS_WIDE],
                            ("peak_core_temperature_c", "minimize"), [],
                            assumptions={**PHYSICAL, "ground_soil_conductance_w_m2k": k})
        for k in (5, 40)
    },
    "H3": request("S11-H3 Dubai Jul selective, physical env", "dubai", [7], [RHO, EPS_W, EPS_N],
                  ("skin_excess_degree_hours", "minimize"), CORE,
                  map_axes=("infrared_emissivity_window", "infrared_emissivity_outside_window"),
                  assumptions=PHYSICAL),
    "F3": request("S11-F3 Guangzhou Aug degree-hours, physical env", "guangzhou", [8], [RHO, EPS],
                  ("skin_excess_degree_hours", "minimize"), CORE,
                  map_axes=("solar_reflectance", "infrared_emissivity"), assumptions=PHYSICAL),
}


def batch(name: str, assumptions: dict) -> dict:
    return {
        "name": name, "city_ids": ["dubai", "guangzhou", "lhasa"], "year": 2023,
        "start_month": 7, "end_month": 7, "analysis_resolution": "representative",
        "sample_days_per_month": 3, "local_start_hour": 12, "duration_minutes": 120,
        "output_interval_minutes": 10, "person": PERSON, "control_material": CONTROL,
        "rc_material": RC, "environment_assumptions": assumptions,
    }


BATCHES = {"K5-legacy": batch("S11-K5 legacy env", {}), "K5-physical": batch("S11-K5 physical env", PHYSICAL)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--only", default="")
    args = parser.parse_args()
    keep = lambda key: not args.only or key in args.only.split(",")  # noqa: E731

    with httpx.Client(base_url=args.base_url, timeout=60) as client:
        for key, body in OPTIMIZATIONS.items():
            if keep(key):
                r = client.post("/api/v1/optimizations", json=body)
                r.raise_for_status()
                print(f"{key:10s} optimization {r.json()['id']}")
        for key, body in BATCHES.items():
            if keep(key):
                r = client.post("/api/v1/global-batches", json=body)
                r.raise_for_status()
                print(f"{key:10s} batch        {r.json()['id']}")


if __name__ == "__main__":
    main()