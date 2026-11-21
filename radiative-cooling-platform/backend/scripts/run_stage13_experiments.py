"""Stage 13 surrogate datasets and training.

Usage (from backend/):
    python scripts/run_stage13_experiments.py --only D3          # smoke test
    python scripts/run_stage13_experiments.py --only D1,D2
    python scripts/run_stage13_experiments.py --train <dataset_id> [--name M1]
"""

from __future__ import annotations

import argparse

import httpx

ALL_CITIES = ["dubai", "guangzhou", "lhasa", "singapore", "delhi", "riyadh", "cairo", "lagos",
              "nairobi", "phoenix", "houston", "mexico-city", "manaus", "sao-paulo", "darwin", "sydney"]
HOLDOUT_CITIES = ["dubai", "guangzhou", "lhasa", "singapore"]

PERSON = {"met": 2.8, "walking_speed_m_s": 1.11, "body_mass_kg": 70, "body_surface_area_m2": 1.8,
          "initial_core_temperature_c": 36.8, "initial_skin_temperature_c": 33.7, "position": "standing"}
CONTROL = {"name": "Conventional clothing", "clothing_insulation_clo": 0.5, "solar_reflectance": 0.3,
           "solar_transmittance": 0, "infrared_emissivity": 0.9, "projected_solar_area_factor": 0.25}
BASE = {"name": "RC candidate", "clothing_insulation_clo": 0.4, "solar_reflectance": 0.9,
        "solar_transmittance": 0, "infrared_emissivity": 0.95, "projected_solar_area_factor": 0.25}
VARIABLES = [
    {"name": "solar_reflectance", "lower": 0.3, "upper": 0.98},
    {"name": "infrared_emissivity", "lower": 0.05, "upper": 0.99},
    {"name": "infrared_emissivity_ground_facing", "lower": 0.05, "upper": 0.99},
    {"name": "clothing_insulation_clo", "lower": 0.2, "upper": 0.8},
]


def dataset(name, cities, year, months, days, materials, seed):
    return {"name": name, "city_ids": cities, "year": year, "months": months,
            "sample_days_per_month": days, "local_start_hour": 12, "duration_minutes": 120,
            "output_interval_minutes": 5, "skin_threshold_c": 35, "core_threshold_c": 38,
            "person": PERSON, "control_material": CONTROL, "base_material": BASE,
            "variables": VARIABLES, "material_count": materials, "seed": seed}


DATASETS = {
    "D1": dataset("S13-D1 training, 16 cities, 2023", ALL_CITIES, 2023, list(range(1, 13)), 3, 512, 0),
    "D2": dataset("S13-D2 temporal hold-out, 2022", HOLDOUT_CITIES, 2022, list(range(1, 13)), 1, 64, 7),
    "D3": dataset("S13-D3 smoke", ["dubai", "sydney"], 2023, [1, 7], 1, 32, 0),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--only", default="")
    parser.add_argument("--train", default="")
    parser.add_argument("--name", default="S13-M1")
    args = parser.parse_args()

    with httpx.Client(base_url=args.base_url, timeout=120) as client:
        if args.train:
            r = client.post("/api/v1/surrogate/models", json={"name": args.name, "dataset_id": args.train})
            r.raise_for_status()
            print(f"model {r.json()['id']} queued")
            return
        for key, body in DATASETS.items():
            if args.only and key not in args.only.split(","):
                continue
            estimate = client.post("/api/v1/surrogate/datasets/estimate", json=body)
            estimate.raise_for_status()
            r = client.post("/api/v1/surrogate/datasets", json=body)
            r.raise_for_status()
            e = estimate.json()
            print(f"{key} dataset {r.json()['id']}  chunks={e['chunk_count']}  "
                  f"materials={e['valid_material_count']}  simulations={e['thermal_simulation_count']:,}")


if __name__ == "__main__":
    main()