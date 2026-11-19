"""Stage 12 acceptance runs. Usage (from backend/): python scripts/run_stage12_experiments.py [--only L2-s50,L4]"""

from __future__ import annotations

import argparse

import httpx

from run_stage10_experiments import EPS_N, EPS_W, EPS_WIDE, RHO, c, request
from run_stage11_experiments import batch

GROUND = {"name": "infrared_emissivity_ground_facing", "lower": 0.05, "upper": 0.99}
CORE = [c("peak_core_temperature_c", "<=", 38)]
PHYSICAL = {"mean_radiant_temperature_method": "ground_energy_balance",
            "sky_temperature_method": "brutsaert_cloud"}

OPTIMIZATIONS = {
    **{
        f"L2-s{round(s * 100)}": request(
            f"S12-L2 Dubai Jul eps + eps_g, s={s}", "dubai", [7], [EPS_WIDE, GROUND],
            ("peak_core_temperature_c", "minimize"), [],
            map_axes=("infrared_emissivity", "infrared_emissivity_ground_facing"),
            assumptions={**PHYSICAL, "zone_view_separation": s},
        )
        for s in (0.0, 0.25, 0.5, 0.75)
    },
    "L3": request("S12-L3 Dubai Jul selective + eps_g", "dubai", [7], [RHO, EPS_W, EPS_N, GROUND],
                  ("skin_excess_degree_hours", "minimize"), CORE,
                  map_axes=("infrared_emissivity_window", "infrared_emissivity_ground_facing"),
                  assumptions=PHYSICAL),
    "L5": request("S12-L5 Guangzhou Aug eps + eps_g", "guangzhou", [8], [RHO, EPS_WIDE, GROUND],
                  ("skin_excess_degree_hours", "minimize"), CORE,
                  map_axes=("infrared_emissivity", "infrared_emissivity_ground_facing"),
                  assumptions=PHYSICAL),
}

# L4: omitting assumptions must now equal the explicit Stage 11 physical batch (K5-physical).
BATCHES = {"L4": batch("S12-L4 default env", {})}


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
                print(f"{key:8s} optimization {r.json()['id']}")
        for key, body in BATCHES.items():
            if keep(key):
                body = {k: v for k, v in body.items() if k != "environment_assumptions" or v}
                r = client.post("/api/v1/global-batches", json=body)
                r.raise_for_status()
                print(f"{key:8s} batch        {r.json()['id']}")


if __name__ == "__main__":
    main()