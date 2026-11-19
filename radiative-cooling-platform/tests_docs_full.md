# Tests & Docs Source (`backend/tests/`, `backend/docs/`)

## Directory Structure
```text
backend/docs/acceptance/legacy-stage-3-two-node-prototype/energy-residual.txt
backend/docs/acceptance/legacy-stage-3-two-node-prototype/pytest-all.txt
backend/docs/acceptance/stage-10-spectral/golden-refresh.md
backend/docs/acceptance/stage-10-spectral/optimization-summary.json
backend/docs/acceptance/stage-10-spectral/optimization-summary.md
backend/docs/acceptance/stage-11-radiant/optimization-summary.json
backend/docs/acceptance/stage-11-radiant/optimization-summary.md
backend/docs/acceptance/stage-2/golden-refresh.md
backend/docs/acceptance/stage-3-reference-comparison/golden-refresh.md
backend/docs/acceptance/stage-3-reference-comparison/pytest-all.txt
backend/docs/acceptance/stage-4-material-library/pytest-all.txt
backend/docs/acceptance/stage-5-solar-surface/golden-refresh.md
backend/docs/acceptance/stage-5-solar-surface/pytest-all.txt
backend/docs/acceptance/stage-6-consistency/golden-refresh.md
backend/docs/acceptance/stage-8-observability/README.md
backend/docs/acceptance/stage-8-observability/resume-benchmark.json
backend/docs/acceptance/stage-9-reliability/drills.md
backend/docs/acceptance/stage-optimization/optimization-summary.md
backend/docs/decisions/0001-body-surface-area.md
backend/docs/decisions/0002-gagge-controllers.md
backend/docs/decisions/0003-clothing-surface-balance.md
backend/docs/decisions/0004-material-library-provenance.md
backend/docs/decisions/0005-solar-on-clothing-surface.md
backend/docs/decisions/0006-shortwave-geometry-and-posture.md
backend/docs/decisions/0007-two-band-longwave-and-requirement-search.md
backend/docs/decisions/0008-physical-radiant-environment.md
backend/docs/decisions/0009-physical-environment-default.md
backend/docs/decisions/0010-two-zone-garment-longwave.md
backend/docs/environment-assumptions.md
backend/docs/model-parameters.md
backend/tests/__init__.py
backend/tests/conftest.py
backend/tests/core/test_numba_cache_integration.py
backend/tests/core/test_runtime.py
backend/tests/fixtures/dubai_2h/expected_results.json
backend/tests/fixtures/dubai_2h/open_meteo_payload.json
backend/tests/fixtures/dubai_2h/open_meteo_payload.sha256
backend/tests/fixtures/dubai_2h/request.json
backend/tests/fixtures/dubai_2h/request_params.json
backend/tests/helpers/__init__.py
backend/tests/helpers/environment.py
backend/tests/test_api.py
backend/tests/test_batch_single_consistency.py
backend/tests/test_body.py
backend/tests/test_cities.py
backend/tests/test_climate_adaptation.py
backend/tests/test_climate_scenarios.py
backend/tests/test_clothing.py
backend/tests/test_cors.py
backend/tests/test_daily_maximum.py
backend/tests/test_environment_model.py
backend/tests/test_exposure_statistics.py
backend/tests/test_frontend_mirrors.py
backend/tests/test_gagge_benchmark.py
backend/tests/test_gagge_reference.py
backend/tests/test_global_batch_geojson.py
backend/tests/test_global_batches_api.py
backend/tests/test_golden_dubai_2h.py
backend/tests/test_job_service.py
backend/tests/test_longwave.py
backend/tests/test_material_fields.py
backend/tests/test_material_resolution.py
backend/tests/test_materials_api.py
backend/tests/test_materials_update_delete.py
backend/tests/test_model_parameters.py
backend/tests/test_optimization.py
backend/tests/test_optimization_stage10.py
backend/tests/test_parameter_participation.py
backend/tests/test_physics.py
backend/tests/test_planck.py
backend/tests/test_radiant_environment.py
backend/tests/test_radiation_convention.py
backend/tests/test_result_export.py
backend/tests/test_result_storage.py
backend/tests/test_route_registration.py
backend/tests/test_scenario_summary.py
backend/tests/test_solar.py
backend/tests/test_spectral_summary.py
backend/tests/test_spectrum_parser.py
backend/tests/test_stage12_defaults.py
backend/tests/test_stage_4_2_export.py
backend/tests/test_stage_4_2_exposure.py
backend/tests/test_stage_4_2_sampling.py
backend/tests/test_stage_4_3_estimate.py
backend/tests/test_stage_4_3_sampling.py
backend/tests/test_stage_4_3_weather_slice.py
backend/tests/test_stage_4_4_analytics.py
backend/tests/test_stage_4_4_checkpoint.py
backend/tests/test_stage_8_observability.py
backend/tests/test_stage_8_resume_benchmark.py
backend/tests/test_stage_9_leases_and_provenance.py
backend/tests/test_two_node.py
backend/tests/test_weather_api.py
backend/tests/test_weather_extras.py
backend/tests/test_weather_interpolation.py
backend/tests/test_weather_quality.py
backend/tests/test_weather_service.py
backend/tests/test_weather_simulation.py
backend/tests/test_weather_timeline_stage6.py
backend/tests/test_worker_tasks.py
backend/tests/test_zoned_longwave.py
```

---

## Source Code Files

### File: `backend/docs/acceptance/legacy-stage-3-two-node-prototype/energy-residual.txt`
```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
plugins: anyio-4.14.2, cov-7.1.0
collecting ... collected 1 item

tests/test_two_node.py::test_energy_balance_residual_is_small PASSED

============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 1 passed, 1 warning in 0.02s =========================

```

### File: `backend/docs/acceptance/legacy-stage-3-two-node-prototype/pytest-all.txt`
```text
Python:
C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
Numba cache:
C:/nc
pythermalcomfort:
C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Lib\site-packages\pythermalcomfort\__init__.py
開始執行測試...
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.14.2, cov-7.1.0
collecting ... collected 27 items

tests/test_api.py::test_health_endpoint PASSED                           [  3%]
tests/test_api.py::test_simulation_endpoint PASSED                       [  7%]
tests/test_api.py::test_invalid_material_is_rejected PASSED              [ 11%]
tests/test_api.py::test_identical_material_api_improvement_is_zero PASSED [ 14%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_dry-42.0-20.0-2.0-900.0] PASSED [ 18%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_humid-34.0-85.0-1.0-700.0] PASSED [ 22%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[high_altitude_solar-24.0-25.0-2.5-1000.0] PASSED [ 25%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[night-30.0-60.0-0.5-0.0] PASSED [ 29%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_returns_finite_values PASSED [ 33%]
tests/test_gagge_benchmark.py::test_gagge_output_is_in_broad_range PASSED [ 37%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_api PASSED           [ 40%]
tests/test_physics.py::test_saturation_pressure_increases_with_temperature PASSED [ 44%]
tests/test_physics.py::test_saturation_pressure_near_reference_value PASSED [ 48%]
tests/test_physics.py::test_invalid_optical_sum_is_rejected PASSED       [ 51%]
tests/test_physics.py::test_higher_reflectance_reduces_solar_absorption PASSED [ 55%]
tests/test_physics.py::test_flux_calculation_is_finite[0.0] PASSED       [ 59%]
tests/test_physics.py::test_flux_calculation_is_finite[0.1] PASSED       [ 62%]
tests/test_physics.py::test_flux_calculation_is_finite[1.0] PASSED       [ 66%]
tests/test_physics.py::test_flux_calculation_is_finite[3.0] PASSED       [ 70%]
tests/test_physics.py::test_flux_calculation_is_finite[8.0] PASSED       [ 74%]
tests/test_two_node.py::test_simulation_returns_expected_number_of_points PASSED [ 77%]
tests/test_two_node.py::test_initial_temperatures_are_preserved PASSED   [ 81%]
tests/test_two_node.py::test_all_temperatures_are_finite PASSED          [ 85%]
tests/test_two_node.py::test_temperature_stays_in_broad_physiological_range PASSED [ 88%]
tests/test_two_node.py::test_energy_balance_residual_is_small PASSED     [ 92%]
tests/test_two_node.py::test_rc_material_reduces_skin_temperature PASSED [ 96%]
tests/test_two_node.py::test_identical_materials_produce_identical_results PASSED [100%]

============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 27 passed, 1 warning in 0.31s ========================

```

### File: `backend/docs/acceptance/stage-10-spectral/golden-refresh.md`
```markdown
# Stage 10 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes: four registry constants added (second_radiation_constant,
atmospheric_window_lower/upper_um, emissivity_reference_temperature);
MODEL_VERSION 0.7.0 -> 0.8.0. Both fixture garments are gray, so the selective
path is not exercised.

| metric | before (0.7.0) | after (0.8.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 2.1232 | <fill> | must be 0 |
| final_core_temperature_improvement_c | 1.9117 | <fill> | must be 0 |
| average_skin_temperature_improvement_c | 1.2876 | <fill> | must be 0 |

model_parameter_set_sha256: cab48ac8... -> <fill>
parameter_fingerprint: 10003d40... -> <fill>
```

### File: `backend/docs/acceptance/stage-10-spectral/optimization-summary.json`
```json
{
  "runs": [
    {
      "name": "J-tol-1e-4-b",
      "id": "e1db6442",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.439081,
      "best_violation": 4.098262,
      "best_metrics": {
        "peak_skin_temperature_c": 37.0226,
        "skin_exceedance_fraction": 0.939092,
        "peak_core_temperature_c": 38.2201,
        "mean_skin_cooling_c": 1.37305
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 4.098262,
      "upper_peak_skin": 37.0226,
      "evaluations": 122,
      "generations": 11,
      "seconds": 15.858,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "skin_excess_degree_hours <= 0.5: violated by 1.939, but the whole search range moves skin_excess_degree_hours by only about 0.08524 (linearised at the optimum); the target is out of reach of the selected variables",
        "peak_core_temperature_c <= 38: violated by 0.2201, but the whole search range moves peak_core_temperature_c by only about 0.058 (linearised at the optimum); the target is out of reach of the selected variables"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0242,
            "mean_skin_cooling_c": 0.0432,
            "mean_skin_temperature_c": -0.0432,
            "peak_core_temperature_c": -0.058,
            "peak_skin_temperature_c": -0.07,
            "core_exceedance_fraction": -0.0151,
            "core_excess_degree_hours": -0.00906,
            "skin_exceedance_fraction": -0.001,
            "skin_excess_degree_hours": -0.08524
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "J-tol-1e-5",
      "id": "d5c68053",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.439081,
      "best_violation": 4.098262,
      "best_metrics": {
        "peak_skin_temperature_c": 37.0226,
        "skin_exceedance_fraction": 0.939092,
        "peak_core_temperature_c": 38.2201,
        "mean_skin_cooling_c": 1.37305
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 4.098262,
      "upper_peak_skin": 37.0226,
      "evaluations": 151,
      "generations": 14,
      "seconds": 19.536,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "skin_excess_degree_hours <= 0.5: violated by 1.939, but the whole search range moves skin_excess_degree_hours by only about 0.08524 (linearised at the optimum); the target is out of reach of the selected variables",
        "peak_core_temperature_c <= 38: violated by 0.2201, but the whole search range moves peak_core_temperature_c by only about 0.058 (linearised at the optimum); the target is out of reach of the selected variables"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0242,
            "mean_skin_cooling_c": 0.0432,
            "mean_skin_temperature_c": -0.0432,
            "peak_core_temperature_c": -0.058,
            "peak_skin_temperature_c": -0.07,
            "core_exceedance_fraction": -0.0151,
            "core_excess_degree_hours": -0.00906,
            "skin_exceedance_fraction": -0.001,
            "skin_excess_degree_hours": -0.08524
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "J-tol-1e-4",
      "id": "fc14744e",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.4582,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0794,
        "mean_skin_cooling_c": 1.54682
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 34.1105,
      "evaluations": 115,
      "generations": 13,
      "seconds": 15.392,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.5245,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0176,
            "mean_skin_cooling_c": 0.4606,
            "mean_skin_temperature_c": -0.4606,
            "peak_core_temperature_c": -0.044,
            "peak_skin_temperature_c": -0.366,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": 0.0,
            "skin_excess_degree_hours": 0.0
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-6",
      "id": "5792f168",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 6,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13281778211284515,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640023,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23334
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 745,
      "generations": 30,
      "seconds": 98.687,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446585,
          "probe_high": 0.514585,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.63,
            "mean_skin_temperature_c": -1.63,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.628,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19147,
            "skin_excess_degree_hours": -2.10386
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524534,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059517,
            "mean_skin_cooling_c": 0.364694,
            "mean_skin_temperature_c": -0.364894,
            "peak_core_temperature_c": -0.087878,
            "peak_skin_temperature_c": -0.315562,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.260399,
            "skin_excess_degree_hours": -0.438132
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-5",
      "id": "f2dc6007",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 5,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13278593937575026,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640091,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23329
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 741,
      "generations": 30,
      "seconds": 96.962,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446575,
          "probe_high": 0.514575,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.6298,
            "mean_skin_temperature_c": -1.6299,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.627,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.191,
            "skin_excess_degree_hours": -2.10381
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.52451,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059376,
            "mean_skin_cooling_c": 0.364851,
            "mean_skin_temperature_c": -0.364851,
            "peak_core_temperature_c": -0.087964,
            "peak_skin_temperature_c": -0.313872,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.259994,
            "skin_excess_degree_hours": -0.438201
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-4",
      "id": "bf4a830c",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 4,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.1327957833133253,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640071,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23332
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 743,
      "generations": 30,
      "seconds": 94.39,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446587,
          "probe_high": 0.514587,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.63,
            "mean_skin_temperature_c": -1.63,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.628,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19152,
            "skin_excess_degree_hours": -2.10391
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524511,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059373,
            "mean_skin_cooling_c": 0.364836,
            "mean_skin_temperature_c": -0.364836,
            "peak_core_temperature_c": -0.087961,
            "peak_skin_temperature_c": -0.315858,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.260303,
            "skin_excess_degree_hours": -0.438103
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-3",
      "id": "17bea257",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 3,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13277891656662663,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640091,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23328
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 738,
      "generations": 30,
      "seconds": 95.516,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446571,
          "probe_high": 0.514571,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.6298,
            "mean_skin_temperature_c": -1.6299,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.627,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19092,
            "skin_excess_degree_hours": -2.10384
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524506,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059385,
            "mean_skin_cooling_c": 0.364711,
            "mean_skin_temperature_c": -0.364711,
            "peak_core_temperature_c": -0.087978,
            "peak_skin_temperature_c": -0.313923,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.259916,
            "skin_excess_degree_hours": -0.438013
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-2",
      "id": "3f44794e",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 2,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13278631452581038,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640071,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23331
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 742,
      "generations": 30,
      "seconds": 94.727,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446588,
          "probe_high": 0.514588,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.6299,
            "mean_skin_temperature_c": -1.63,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.627,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19155,
            "skin_excess_degree_hours": -2.10388
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524501,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059398,
            "mean_skin_cooling_c": 0.364785,
            "mean_skin_temperature_c": -0.364785,
            "peak_core_temperature_c": -0.087996,
            "peak_skin_temperature_c": -0.315987,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.260409,
            "skin_excess_degree_hours": -0.438162
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-1",
      "id": "7575e16b",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 1,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13279345738295323,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640071,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23332
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 740,
      "generations": 30,
      "seconds": 100.325,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446588,
          "probe_high": 0.514588,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.63,
            "mean_skin_temperature_c": -1.63,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.628,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19152,
            "skin_excess_degree_hours": -2.10391
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524508,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059381,
            "mean_skin_cooling_c": 0.364881,
            "mean_skin_temperature_c": -0.364881,
            "peak_core_temperature_c": -0.087971,
            "peak_skin_temperature_c": -0.315897,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.260335,
            "skin_excess_degree_hours": -0.438157
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "H2 - Jul",
      "id": "565fe333",
      "city": "dubai",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity_window": 0.99,
        "infrared_emissivity_outside_window": 0.05
      },
      "best_objective": 3.601119,
      "best_violation": 7.196338,
      "best_metrics": {
        "peak_skin_temperature_c": 37.8585,
        "skin_exceedance_fraction": 0.970815,
        "peak_core_temperature_c": 38.9941,
        "mean_skin_cooling_c": 1.83442
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 7.196338,
      "upper_peak_skin": 37.8585,
      "evaluations": 1057,
      "generations": 30,
      "seconds": 390.447,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity_window sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "best infrared_emissivity_outside_window sits at its lower search bound (0.05); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 1.17,
            "mean_skin_cooling_c": 1.6002,
            "mean_skin_temperature_c": -1.6002,
            "peak_core_temperature_c": -2.128,
            "peak_skin_temperature_c": -2.358,
            "core_exceedance_fraction": -1.3186,
            "core_excess_degree_hours": -1.61602,
            "skin_exceedance_fraction": -0.01734,
            "skin_excess_degree_hours": -3.17794
          }
        },
        {
          "name": "infrared_emissivity_window",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0706,
            "mean_skin_cooling_c": 0.0966,
            "mean_skin_temperature_c": -0.0966,
            "peak_core_temperature_c": -0.132,
            "peak_skin_temperature_c": -0.148,
            "core_exceedance_fraction": -0.08828,
            "core_excess_degree_hours": -0.09152,
            "skin_exceedance_fraction": -0.00102,
            "skin_excess_degree_hours": -0.19194
          }
        },
        {
          "name": "infrared_emissivity_outside_window",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0792,
            "mean_skin_cooling_c": -0.1088,
            "mean_skin_temperature_c": 0.109,
            "peak_core_temperature_c": 0.148,
            "peak_skin_temperature_c": 0.164,
            "core_exceedance_fraction": 0.10078,
            "core_excess_degree_hours": 0.1036,
            "skin_exceedance_fraction": 0.00136,
            "skin_excess_degree_hours": 0.21608
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "infrared_emissivity_window \u00d7 infrared_emissivity_outside_window",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "H1 -  Aug",
      "id": "75b42686",
      "city": "dubai",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity_window": 0.99,
        "infrared_emissivity_outside_window": 0.05
      },
      "best_objective": 3.81147,
      "best_violation": 7.75924,
      "best_metrics": {
        "peak_skin_temperature_c": 38.0157,
        "skin_exceedance_fraction": 0.971934,
        "peak_core_temperature_c": 39.1363,
        "mean_skin_cooling_c": 1.9489
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 7.75924,
      "upper_peak_skin": 38.0157,
      "evaluations": 1059,
      "generations": 30,
      "seconds": 398.358,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity_window sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "best infrared_emissivity_outside_window sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "low infrared_emissivity_outside_window is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 1.2016,
            "mean_skin_cooling_c": 1.6318,
            "mean_skin_temperature_c": -1.6318,
            "peak_core_temperature_c": -2.132,
            "peak_skin_temperature_c": -2.36,
            "core_exceedance_fraction": -0.98534,
            "core_excess_degree_hours": -1.88278,
            "skin_exceedance_fraction": -0.01594,
            "skin_excess_degree_hours": -3.24296
          }
        },
        {
          "name": "infrared_emissivity_window",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0392,
            "mean_skin_cooling_c": 0.0536,
            "mean_skin_temperature_c": -0.0536,
            "peak_core_temperature_c": -0.072,
            "peak_skin_temperature_c": -0.08,
            "core_exceedance_fraction": -0.03626,
            "core_excess_degree_hours": -0.05958,
            "skin_exceedance_fraction": -0.0005,
            "skin_excess_degree_hours": -0.1065
          }
        },
        {
          "name": "infrared_emissivity_outside_window",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.189,
            "mean_skin_cooling_c": -0.2574,
            "mean_skin_temperature_c": 0.2574,
            "peak_core_temperature_c": 0.344,
            "peak_skin_temperature_c": 0.38,
            "core_exceedance_fraction": 0.17052,
            "core_excess_degree_hours": 0.28852,
            "skin_exceedance_fraction": 0.0027,
            "skin_excess_degree_hours": 0.51134
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "infrared_emissivity_window \u00d7 infrared_emissivity_outside_window",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "G2 - Equal to air (shaded)",
      "id": "b0738e64",
      "city": "guangzhou",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.375719,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 36.8985,
        "skin_exceedance_fraction": 0.933548,
        "peak_core_temperature_c": 38.1176,
        "mean_skin_cooling_c": 1.45854
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 36.8985,
      "evaluations": 142,
      "generations": 13,
      "seconds": 17.643,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.943,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.1172,
            "mean_skin_cooling_c": 0.1942,
            "mean_skin_temperature_c": -0.1944,
            "peak_core_temperature_c": -0.258,
            "peak_skin_temperature_c": -0.286,
            "core_exceedance_fraction": -0.09108,
            "core_excess_degree_hours": -0.0269,
            "skin_exceedance_fraction": -0.00878,
            "skin_excess_degree_hours": -0.37704
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "G1 - Air + linear solar gain",
      "id": "9524b52a",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 4.399347,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4243,
        "skin_exceedance_fraction": 0.971222,
        "peak_core_temperature_c": 39.4968,
        "mean_skin_cooling_c": 1.55468
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.5257,
      "evaluations": 72,
      "generations": 7,
      "seconds": 9.55,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0556,
            "mean_skin_cooling_c": -0.0738,
            "mean_skin_temperature_c": 0.0738,
            "peak_core_temperature_c": 0.114,
            "peak_skin_temperature_c": 0.12,
            "core_exceedance_fraction": 0.01758,
            "core_excess_degree_hours": 0.09776,
            "skin_exceedance_fraction": 0.00108,
            "skin_excess_degree_hours": 0.14612
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "F2-degree-hours-gradient",
      "id": "53682159",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.126385,
      "best_violation": 3.25277,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7782,
        "skin_exceedance_fraction": 0.931436,
        "peak_core_temperature_c": 37.9969,
        "mean_skin_cooling_c": 1.53443
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 3.25277,
      "upper_peak_skin": 36.7782,
      "evaluations": 442,
      "generations": 15,
      "seconds": 57.356,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 0.701,
            "mean_skin_cooling_c": 1.3778,
            "mean_skin_temperature_c": -1.3778,
            "peak_core_temperature_c": -1.886,
            "peak_skin_temperature_c": -2.068,
            "core_exceedance_fraction": -0.87962,
            "core_excess_degree_hours": -0.08126,
            "skin_exceedance_fraction": -0.0664,
            "skin_excess_degree_hours": -2.66524
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0144,
            "mean_skin_cooling_c": 0.0336,
            "mean_skin_temperature_c": -0.0336,
            "peak_core_temperature_c": -0.036,
            "peak_skin_temperature_c": -0.046,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.00058,
            "skin_excess_degree_hours": -0.06666
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "F1-infeasible-out-of-reach",
      "id": "4a13bad4",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.0; peak_core_temperature_c <= 38.0; peak_skin_temperature_c <= 32.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.126385,
      "best_violation": 9.03097,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7782,
        "skin_exceedance_fraction": 0.931436,
        "peak_core_temperature_c": 37.9969,
        "mean_skin_cooling_c": 1.53443
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 9.03097,
      "upper_peak_skin": 36.7782,
      "evaluations": 739,
      "generations": 30,
      "seconds": 94.374,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "peak_skin_temperature_c <= 32: violated by 4.778, but the whole search range moves peak_skin_temperature_c by only about 2.114 (linearised at the optimum); the target is out of reach of the selected variables"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 0.701,
            "mean_skin_cooling_c": 1.3778,
            "mean_skin_temperature_c": -1.3778,
            "peak_core_temperature_c": -1.886,
            "peak_skin_temperature_c": -2.068,
            "core_exceedance_fraction": -0.87962,
            "core_excess_degree_hours": -0.08126,
            "skin_exceedance_fraction": -0.0664,
            "skin_excess_degree_hours": -2.66524
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0144,
            "mean_skin_cooling_c": 0.0336,
            "mean_skin_temperature_c": -0.0336,
            "peak_core_temperature_c": -0.036,
            "peak_skin_temperature_c": -0.046,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.00058,
            "skin_excess_degree_hours": -0.06666
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "L-W \u62c9\u85a9\u6b0a\u91cd 2:1 / 1:2",
      "id": "8ba7a747",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7243,
      "evaluations": 242,
      "generations": 5,
      "seconds": 31.655,
      "plateau_fraction": 0.2727272727272727,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.614,
      "min_y_at_max_x": 0.1,
      "feasible_cell_share": 0.355,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.1,
          "minimum_x": 0.802,
          "required_x": null
        },
        {
          "y": 0.188,
          "minimum_x": 0.802,
          "required_x": null
        },
        {
          "y": 0.276,
          "minimum_x": 0.802,
          "required_x": null
        },
        {
          "y": 0.364,
          "minimum_x": 0.802,
          "required_x": null
        },
        {
          "y": 0.452,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.54,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.628,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.716,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.804,
          "minimum_x": 0.614,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.614,
          "required_x": null
        },
        {
          "y": 0.98,
          "minimum_x": 0.614,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 5",
      "id": "caffdcbc",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 5,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 202,
      "generations": 3,
      "seconds": 27.078,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 4",
      "id": "3d83bbf7",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 4,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 222,
      "generations": 4,
      "seconds": 29.775,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 3",
      "id": "3ebaa2be",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 3,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 222,
      "generations": 4,
      "seconds": 29.239,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 2",
      "id": "f0897399",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 2,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 222,
      "generations": 4,
      "seconds": 28.744,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 1",
      "id": "dd922952",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 1,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 281,
      "generations": 7,
      "seconds": 36.664,
      "plateau_fraction": 0.3305785123966942,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.628,
      "min_y_at_max_x": 0.55,
      "feasible_cell_share": 0.413,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.55,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.594,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.638,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.682,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.726,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.77,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.814,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.858,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.902,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.946,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.628,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09",
      "id": "d72418b5",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 242,
      "generations": 5,
      "seconds": 31.319,
      "plateau_fraction": 0.2809917355371901,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.628,
      "min_y_at_max_x": 0.05,
      "feasible_cell_share": 0.355,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": 0.804,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": 0.804,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": 0.804,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": 0.804,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.628,
          "required_x": null
        }
      ]
    },
    {
      "name": "H Dubai peak_core min, \u03b5 [0.05,0.99]",
      "id": "d93fc6a6",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.4968,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4243,
        "skin_exceedance_fraction": 0.971222,
        "peak_core_temperature_c": 39.4968,
        "mean_skin_cooling_c": 1.55468
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.5257,
      "evaluations": 23,
      "generations": 1,
      "seconds": 3.075,
      "plateau_fraction": null,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "Exp-E Guangzhou mult=20",
      "id": "e73cb312",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 20,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9885
      },
      "best_objective": 0.93144,
      "best_violation": 0.8314400000000001,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7784,
        "skin_exceedance_fraction": 0.93144,
        "peak_core_temperature_c": 37.997,
        "mean_skin_cooling_c": 1.5343
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 1042,
      "generations": 22,
      "seconds": 142.371,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-E Guangzhou mult=10",
      "id": "54d8da07",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9876
      },
      "best_objective": 0.931447,
      "best_violation": 0.831447,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7787,
        "skin_exceedance_fraction": 0.931447,
        "peak_core_temperature_c": 37.9972,
        "mean_skin_cooling_c": 1.53411
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 519,
      "generations": 19,
      "seconds": 72.705,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-E Guangzhou mult=5",
      "id": "66f1f154",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 5,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9524
      },
      "best_objective": 0.931483,
      "best_violation": 0.831483,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7819,
        "skin_exceedance_fraction": 0.931483,
        "peak_core_temperature_c": 37.9998,
        "mean_skin_cooling_c": 1.53179
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 340,
      "generations": 21,
      "seconds": 45.3,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=5",
      "id": "98519f18",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 5,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9894
      },
      "best_objective": 0.93144,
      "best_violation": 0.8314400000000001,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7784,
        "skin_exceedance_fraction": 0.93144,
        "peak_core_temperature_c": 37.997,
        "mean_skin_cooling_c": 1.53431
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 501,
      "generations": 18,
      "seconds": 71.1,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=4",
      "id": "e5877c0f",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 4,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9873
      },
      "best_objective": 0.931442,
      "best_violation": 0.831442,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7785,
        "skin_exceedance_fraction": 0.931442,
        "peak_core_temperature_c": 37.9971,
        "mean_skin_cooling_c": 1.53421
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 519,
      "generations": 19,
      "seconds": 72.227,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=3",
      "id": "9f03fcea",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 3,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9899
      },
      "best_objective": 0.931444,
      "best_violation": 0.8314440000000001,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7784,
        "skin_exceedance_fraction": 0.931444,
        "peak_core_temperature_c": 37.997,
        "mean_skin_cooling_c": 1.53428
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 520,
      "generations": 19,
      "seconds": 73.434,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=2",
      "id": "d8f0070d",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 2,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9853
      },
      "best_objective": 0.931443,
      "best_violation": 0.831443,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7787,
        "skin_exceedance_fraction": 0.931443,
        "peak_core_temperature_c": 37.9973,
        "mean_skin_cooling_c": 1.53408
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 522,
      "generations": 19,
      "seconds": 70.077,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=1",
      "id": "c1f10bd8",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 1,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9842
      },
      "best_objective": 0.93145,
      "best_violation": 0.83145,
      "best_metrics": {
        "peak_skin_temperature_c": 36.779,
        "skin_exceedance_fraction": 0.93145,
        "peak_core_temperature_c": 37.9975,
        "mean_skin_cooling_c": 1.53389
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 462,
      "generations": 16,
      "seconds": 64.497,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-C Lhasa July skin_exceedance \u2264 0.1 + peak_core \u2264 38",
      "id": "455d0022",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.827,
        "infrared_emissivity": 0.7751
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.5537,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0906,
        "mean_skin_cooling_c": 1.49506
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 200,
      "generations": 3,
      "seconds": 27.69,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-C Dubai July skin_exceedance \u2264 0.1 + peak_core \u2264 38",
      "id": "f99754dc",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.5004
      },
      "best_objective": 0.969569,
      "best_violation": 2.150069000000004,
      "best_metrics": {
        "peak_skin_temperature_c": 38.188,
        "skin_exceedance_fraction": 0.969569,
        "peak_core_temperature_c": 39.2805,
        "mean_skin_cooling_c": 1.70892
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 2.2187320000000015,
      "upper_peak_skin": 38.2597,
      "evaluations": 621,
      "generations": 24,
      "seconds": 89.03,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-B Guangzhou skin_exceedance \u2264 0.1 + peak_core \u2264 38",
      "id": "b25a5038",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9876
      },
      "best_objective": 0.931447,
      "best_violation": 0.831447,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7787,
        "skin_exceedance_fraction": 0.931447,
        "peak_core_temperature_c": 37.9972,
        "mean_skin_cooling_c": 1.53411
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 519,
      "generations": 19,
      "seconds": 72.203,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-A Guangzhou peak_skin \u2264 33",
      "id": "314795f8",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "mean_skin_temperature_c <= 33.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9798,
        "infrared_emissivity": 0.9886
      },
      "best_objective": 0.931456,
      "best_violation": 3.0220899999999986,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7789,
        "skin_exceedance_fraction": 0.931456,
        "peak_core_temperature_c": 37.9975,
        "mean_skin_cooling_c": 1.53397
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 3.021630000000002,
      "upper_peak_skin": 36.7782,
      "evaluations": 500,
      "generations": 18,
      "seconds": 68.218,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Guangzhou August requirement search",
      "id": "d2d9cca2",
      "city": "guangzhou",
      "months": [
        9
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9866
      },
      "best_objective": 0.803111,
      "best_violation": 0.703111,
      "best_metrics": {
        "peak_skin_temperature_c": 36.6638,
        "skin_exceedance_fraction": 0.803111,
        "peak_core_temperature_c": 37.9028,
        "mean_skin_cooling_c": 1.54986
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.702697,
      "upper_peak_skin": 36.6635,
      "evaluations": 481,
      "generations": 17,
      "seconds": 64.969,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Guangzhou August requirement search",
      "id": "6300b97f",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9876
      },
      "best_objective": 0.931447,
      "best_violation": 0.831447,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7787,
        "skin_exceedance_fraction": 0.931447,
        "peak_core_temperature_c": 37.9972,
        "mean_skin_cooling_c": 1.53411
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 519,
      "generations": 19,
      "seconds": 67.048,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    }
  ],
  "curves": [
    [
      {
        "name": "J-tol-1e-4-b",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            1004.099012
          ],
          [
            31,
            1004.099012
          ],
          [
            41,
            1004.099012
          ],
          [
            50,
            1004.099012
          ],
          [
            60,
            1004.099006
          ],
          [
            70,
            1004.098788
          ],
          [
            80,
            1004.098602
          ],
          [
            90,
            1004.098386
          ],
          [
            100,
            1004.098274
          ],
          [
            109,
            1004.098274
          ],
          [
            119,
            1004.098268
          ]
        ]
      }
    ],
    [
      {
        "name": "J-tol-1e-5",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            1004.099012
          ],
          [
            31,
            1004.099012
          ],
          [
            41,
            1004.099012
          ],
          [
            50,
            1004.099012
          ],
          [
            60,
            1004.099006
          ],
          [
            70,
            1004.098788
          ],
          [
            80,
            1004.098602
          ],
          [
            90,
            1004.098386
          ],
          [
            100,
            1004.098274
          ],
          [
            109,
            1004.098274
          ],
          [
            119,
            1004.098268
          ],
          [
            129,
            1004.098268
          ],
          [
            138,
            1004.098268
          ],
          [
            148,
            1004.098268
          ]
        ]
      }
    ],
    [
      {
        "name": "J-tol-1e-4",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            0.12419886329825881
          ],
          [
            31,
            0.12419886329825881
          ],
          [
            41,
            0.02650373477167746
          ],
          [
            48,
            0.003126385869926268
          ],
          [
            55,
            0.003126385869926268
          ],
          [
            62,
            0.0019088905598226096
          ],
          [
            69,
            1.4294289389337618e-05
          ],
          [
            79,
            1.4294289389337618e-05
          ],
          [
            87,
            1.4294289389337618e-05
          ],
          [
            95,
            1.4294289389337618e-05
          ],
          [
            100,
            1.4294289389337618e-05
          ],
          [
            106,
            1.4294289389337618e-05
          ],
          [
            112,
            1.3417167359001636e-05
          ]
        ]
      }
    ],
    [
      {
        "name": "I-Lhasa-min-demand-seed-6",
        "multiplier": 10,
        "seed": 6,
        "curve": [
          [
            41,
            2.725480144698141
          ],
          [
            61,
            1.598835370531701
          ],
          [
            81,
            1.5478510981423146
          ],
          [
            101,
            1.5478510981423146
          ],
          [
            121,
            1.5478510981423146
          ],
          [
            140,
            1.5369202950974914
          ],
          [
            160,
            1.465948708721182
          ],
          [
            180,
            1.3675561438005515
          ],
          [
            200,
            1.3634688732763527
          ],
          [
            220,
            1.3634688732763527
          ],
          [
            240,
            1.3634688732763527
          ],
          [
            260,
            1.3634688732763527
          ],
          [
            280,
            1.3634688732763527
          ],
          [
            300,
            1.339794197141067
          ],
          [
            320,
            1.339794197141067
          ],
          [
            340,
            1.3306093445884033
          ],
          [
            360,
            1.3306093445884033
          ],
          [
            380,
            1.3306093445884033
          ],
          [
            400,
            1.3306093445884033
          ],
          [
            420,
            1.3306093445884033
          ],
          [
            440,
            1.3297571142457987
          ],
          [
            460,
            1.3291632894734318
          ],
          [
            480,
            1.3291632894734318
          ],
          [
            500,
            1.3287215096567502
          ],
          [
            520,
            1.3287215096567502
          ],
          [
            540,
            1.3287215096567502
          ],
          [
            560,
            1.3287215096567502
          ],
          [
            580,
            1.3284476752662768
          ],
          [
            600,
            1.3281794657026815
          ],
          [
            620,
            1.3281794657026815
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-5",
        "multiplier": 10,
        "seed": 5,
        "curve": [
          [
            41,
            1.5292830036810803
          ],
          [
            61,
            1.5292830036810803
          ],
          [
            81,
            1.5292830036810803
          ],
          [
            101,
            1.5292830036810803
          ],
          [
            121,
            1.4607648156879218
          ],
          [
            141,
            1.4607648156879218
          ],
          [
            161,
            1.4607648156879218
          ],
          [
            181,
            1.4171332085650026
          ],
          [
            201,
            1.4171332085650026
          ],
          [
            221,
            1.3728744617458266
          ],
          [
            240,
            1.3728744617458266
          ],
          [
            260,
            1.361810141718447
          ],
          [
            279,
            1.3536817243271273
          ],
          [
            299,
            1.3468589721727313
          ],
          [
            319,
            1.3386054717959472
          ],
          [
            339,
            1.3386054717959472
          ],
          [
            358,
            1.3343128841499385
          ],
          [
            378,
            1.3307640871083941
          ],
          [
            397,
            1.3307640871083941
          ],
          [
            416,
            1.3307640871083941
          ],
          [
            436,
            1.3307640871083941
          ],
          [
            456,
            1.3307640871083941
          ],
          [
            476,
            1.3303804838488786
          ],
          [
            496,
            1.3299043303075035
          ],
          [
            516,
            1.3299043303075035
          ],
          [
            536,
            1.3295923702657089
          ],
          [
            556,
            1.328056453426605
          ],
          [
            576,
            1.328056453426605
          ],
          [
            596,
            1.3278584691055884
          ],
          [
            616,
            1.3278584691055884
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-4",
        "multiplier": 10,
        "seed": 4,
        "curve": [
          [
            41,
            1.729880422247806
          ],
          [
            61,
            1.6799872040850212
          ],
          [
            81,
            1.6799872040850212
          ],
          [
            101,
            1.6547900846508197
          ],
          [
            121,
            1.6437144237757906
          ],
          [
            141,
            1.623616521621123
          ],
          [
            161,
            1.623616521621123
          ],
          [
            181,
            1.5641344168798426
          ],
          [
            201,
            1.3559318642132812
          ],
          [
            221,
            1.3559318642132812
          ],
          [
            241,
            1.3559318642132812
          ],
          [
            261,
            1.3419121720792855
          ],
          [
            281,
            1.3419121720792855
          ],
          [
            301,
            1.3320194322777945
          ],
          [
            321,
            1.3320194322777945
          ],
          [
            341,
            1.3320194322777945
          ],
          [
            361,
            1.3320194322777945
          ],
          [
            381,
            1.3320194322777945
          ],
          [
            401,
            1.3300724140689446
          ],
          [
            421,
            1.3290957659648432
          ],
          [
            441,
            1.3289414245448143
          ],
          [
            461,
            1.3289414245448143
          ],
          [
            481,
            1.3282399626102788
          ],
          [
            501,
            1.3280759133480309
          ],
          [
            520,
            1.3280759133480309
          ],
          [
            540,
            1.3280143179772
          ],
          [
            560,
            1.3280143179772
          ],
          [
            578,
            1.3280143179772
          ],
          [
            598,
            1.327990757817316
          ],
          [
            618,
            1.3279587323065796
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-3",
        "multiplier": 10,
        "seed": 3,
        "curve": [
          [
            41,
            1.8527381509754774
          ],
          [
            60,
            1.8527381509754774
          ],
          [
            80,
            1.4154372964864161
          ],
          [
            99,
            1.4154372964864161
          ],
          [
            118,
            1.3691064459319628
          ],
          [
            138,
            1.3691064459319628
          ],
          [
            158,
            1.3691064459319628
          ],
          [
            177,
            1.3691064459319628
          ],
          [
            197,
            1.3691064459319628
          ],
          [
            217,
            1.345921601140767
          ],
          [
            237,
            1.345921601140767
          ],
          [
            256,
            1.3330455565885628
          ],
          [
            276,
            1.3293164099520034
          ],
          [
            296,
            1.3293164099520034
          ],
          [
            316,
            1.3293164099520034
          ],
          [
            336,
            1.3293164099520034
          ],
          [
            356,
            1.3293164099520034
          ],
          [
            376,
            1.3293164099520034
          ],
          [
            396,
            1.3281384448367912
          ],
          [
            416,
            1.3281384448367912
          ],
          [
            436,
            1.3281384448367912
          ],
          [
            456,
            1.3281384448367912
          ],
          [
            476,
            1.3281384448367912
          ],
          [
            496,
            1.327807766946713
          ],
          [
            516,
            1.327807766946713
          ],
          [
            536,
            1.327807766946713
          ],
          [
            555,
            1.327787456200275
          ],
          [
            574,
            1.327787456200275
          ],
          [
            594,
            1.327787456200275
          ],
          [
            613,
            1.327787456200275
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-2",
        "multiplier": 10,
        "seed": 2,
        "curve": [
          [
            41,
            1.5664646926005046
          ],
          [
            61,
            1.5664646926005046
          ],
          [
            81,
            1.5664646926005046
          ],
          [
            101,
            1.5664646926005046
          ],
          [
            121,
            1.5664646926005046
          ],
          [
            141,
            1.4719367335876792
          ],
          [
            161,
            1.3822842548434382
          ],
          [
            181,
            1.3822842548434382
          ],
          [
            201,
            1.3822842548434382
          ],
          [
            220,
            1.3822842548434382
          ],
          [
            240,
            1.3822842548434382
          ],
          [
            260,
            1.3781904250433226
          ],
          [
            280,
            1.3680592186835276
          ],
          [
            300,
            1.351534187048356
          ],
          [
            320,
            1.3350660871380085
          ],
          [
            340,
            1.3350660871380085
          ],
          [
            360,
            1.3348799081452878
          ],
          [
            379,
            1.3348799081452878
          ],
          [
            399,
            1.330306471618344
          ],
          [
            419,
            1.330306471618344
          ],
          [
            439,
            1.3283548384395156
          ],
          [
            459,
            1.3283548384395156
          ],
          [
            479,
            1.327928722651613
          ],
          [
            498,
            1.327928722651613
          ],
          [
            518,
            1.327928722651613
          ],
          [
            538,
            1.327928722651613
          ],
          [
            558,
            1.327928722651613
          ],
          [
            577,
            1.327928722651613
          ],
          [
            597,
            1.3278826544129452
          ],
          [
            617,
            1.3278582904823035
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-1",
        "multiplier": 10,
        "seed": 1,
        "curve": [
          [
            41,
            1.8118347063681985
          ],
          [
            61,
            1.7758508943555684
          ],
          [
            81,
            1.5007268420767232
          ],
          [
            100,
            1.5007268420767232
          ],
          [
            120,
            1.4122775078159184
          ],
          [
            140,
            1.4122775078159184
          ],
          [
            160,
            1.4122775078159184
          ],
          [
            180,
            1.3817195153238748
          ],
          [
            200,
            1.3817195153238748
          ],
          [
            220,
            1.3817195153238748
          ],
          [
            240,
            1.3577050714747463
          ],
          [
            260,
            1.3577050714747463
          ],
          [
            280,
            1.3577050714747463
          ],
          [
            300,
            1.3577050714747463
          ],
          [
            319,
            1.3577050714747463
          ],
          [
            339,
            1.3577050714747463
          ],
          [
            359,
            1.3577050714747463
          ],
          [
            378,
            1.3485231072777852
          ],
          [
            397,
            1.3397171477488845
          ],
          [
            416,
            1.3397171477488845
          ],
          [
            436,
            1.3373984308259703
          ],
          [
            456,
            1.3324943879126787
          ],
          [
            476,
            1.3324943879126787
          ],
          [
            496,
            1.3317163027859131
          ],
          [
            516,
            1.3294027261203512
          ],
          [
            536,
            1.3294027261203512
          ],
          [
            556,
            1.3294027261203512
          ],
          [
            576,
            1.3284983396148815
          ],
          [
            595,
            1.3284983396148815
          ],
          [
            615,
            1.3279349382132637
          ]
        ]
      }
    ],
    [
      {
        "name": "H2 - Jul",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            61,
            1007.756422
          ],
          [
            91,
            1007.562784
          ],
          [
            120,
            1007.51585
          ],
          [
            150,
            1007.51585
          ],
          [
            180,
            1007.432442
          ],
          [
            210,
            1007.307522
          ],
          [
            240,
            1007.307522
          ],
          [
            270,
            1007.307522
          ],
          [
            300,
            1007.295212
          ],
          [
            330,
            1007.286162
          ],
          [
            360,
            1007.260034
          ],
          [
            390,
            1007.258342
          ],
          [
            420,
            1007.247392
          ],
          [
            450,
            1007.218202
          ],
          [
            480,
            1007.212878
          ],
          [
            510,
            1007.212878
          ],
          [
            539,
            1007.2096
          ],
          [
            569,
            1007.2096
          ],
          [
            599,
            1007.201024
          ],
          [
            629,
            1007.201024
          ],
          [
            659,
            1007.201024
          ],
          [
            689,
            1007.198248
          ],
          [
            719,
            1007.198248
          ],
          [
            749,
            1007.197504
          ],
          [
            779,
            1007.197504
          ],
          [
            809,
            1007.197504
          ],
          [
            839,
            1007.197504
          ],
          [
            869,
            1007.197504
          ],
          [
            899,
            1007.197504
          ],
          [
            929,
            1007.197504
          ]
        ]
      }
    ],
    [
      {
        "name": "H1 -  Aug",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            61,
            1007.962926
          ],
          [
            91,
            1007.962926
          ],
          [
            121,
            1007.86505
          ],
          [
            151,
            1007.86505
          ],
          [
            181,
            1007.86505
          ],
          [
            211,
            1007.805542
          ],
          [
            241,
            1007.805542
          ],
          [
            271,
            1007.805542
          ],
          [
            301,
            1007.805542
          ],
          [
            331,
            1007.805542
          ],
          [
            361,
            1007.805542
          ],
          [
            391,
            1007.805542
          ],
          [
            421,
            1007.805542
          ],
          [
            451,
            1007.805542
          ],
          [
            481,
            1007.80406
          ],
          [
            511,
            1007.795122
          ],
          [
            541,
            1007.793032
          ],
          [
            571,
            1007.781754
          ],
          [
            601,
            1007.777556
          ],
          [
            631,
            1007.777556
          ],
          [
            661,
            1007.775496
          ],
          [
            691,
            1007.77518
          ],
          [
            721,
            1007.76721
          ],
          [
            751,
            1007.766408
          ],
          [
            781,
            1007.766408
          ],
          [
            811,
            1007.766398
          ],
          [
            841,
            1007.762224
          ],
          [
            871,
            1007.762224
          ],
          [
            901,
            1007.762206
          ],
          [
            931,
            1007.762206
          ]
        ]
      }
    ],
    [
      {
        "name": "G2 - Equal to air (shaded)",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.028599277494516084
          ],
          [
            31,
            -0.028599277494516084
          ],
          [
            41,
            -0.028599277494516084
          ],
          [
            50,
            -0.028599277494516084
          ],
          [
            60,
            -0.02864318981492294
          ],
          [
            70,
            -0.029294336729074406
          ],
          [
            80,
            -0.029917516249253807
          ],
          [
            90,
            -0.030502763497541354
          ],
          [
            100,
            -0.030984115447982748
          ],
          [
            110,
            -0.03098411712512213
          ],
          [
            120,
            -0.030994095917564895
          ],
          [
            130,
            -0.031022045106164593
          ],
          [
            139,
            -0.03102205148363758
          ]
        ]
      }
    ],
    [
      {
        "name": "G1 - Air + linear solar gain",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.23980558011366981
          ],
          [
            31,
            -0.23980558011366981
          ],
          [
            41,
            -0.24271134962652227
          ],
          [
            48,
            -0.24336568736141298
          ],
          [
            55,
            -0.24336568736141298
          ],
          [
            62,
            -0.24340580911094425
          ],
          [
            69,
            -0.24346999857057136
          ]
        ]
      }
    ],
    [
      {
        "name": "F2-degree-hours-gradient",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            1003.568282
          ],
          [
            61,
            1003.36176
          ],
          [
            80,
            1003.36176
          ],
          [
            100,
            1003.276918
          ],
          [
            119,
            1003.276918
          ],
          [
            139,
            1003.276918
          ],
          [
            159,
            1003.276918
          ],
          [
            179,
            1003.276918
          ],
          [
            199,
            1003.276918
          ],
          [
            219,
            1003.276918
          ],
          [
            239,
            1003.275298
          ],
          [
            259,
            1003.26127
          ],
          [
            279,
            1003.26127
          ],
          [
            299,
            1003.26127
          ],
          [
            319,
            1003.26127
          ]
        ]
      }
    ],
    [
      {
        "name": "F1-infeasible-out-of-reach",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            1009.437382
          ],
          [
            61,
            1009.17116
          ],
          [
            80,
            1009.17116
          ],
          [
            100,
            1009.062618
          ],
          [
            119,
            1009.062618
          ],
          [
            139,
            1009.062618
          ],
          [
            159,
            1009.062618
          ],
          [
            179,
            1009.062618
          ],
          [
            199,
            1009.062618
          ],
          [
            219,
            1009.062618
          ],
          [
            239,
            1009.060598
          ],
          [
            259,
            1009.04257
          ],
          [
            279,
            1009.04257
          ],
          [
            299,
            1009.04257
          ],
          [
            319,
            1009.04257
          ],
          [
            339,
            1009.041766
          ],
          [
            359,
            1009.033464
          ],
          [
            379,
            1009.033464
          ],
          [
            399,
            1009.031698
          ],
          [
            419,
            1009.031698
          ],
          [
            439,
            1009.031698
          ],
          [
            458,
            1009.031698
          ],
          [
            478,
            1009.031698
          ],
          [
            497,
            1009.031698
          ],
          [
            516,
            1009.031698
          ],
          [
            536,
            1009.031698
          ],
          [
            556,
            1009.031698
          ],
          [
            576,
            1009.031698
          ],
          [
            596,
            1009.031698
          ],
          [
            616,
            1009.031564
          ]
        ]
      }
    ],
    [
      {
        "name": "L-W \u62c9\u85a9\u6b0a\u91cd 2:1 / 1:2",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ],
          [
            121,
            0.0
          ]
        ]
      }
    ],
    [
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 5",
        "multiplier": 10,
        "seed": 5,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ]
        ]
      },
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 4",
        "multiplier": 10,
        "seed": 4,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ]
        ]
      },
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 3",
        "multiplier": 10,
        "seed": 3,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ]
        ]
      },
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 2",
        "multiplier": 10,
        "seed": 2,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ]
        ]
      },
      {
        "name": "Exp-C Lhasa July skin_exceedance \u2264 0.1 + peak_core \u2264 38",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            40,
            0.0
          ],
          [
            59,
            0.0
          ],
          [
            79,
            0.0
          ]
        ]
      }
    ],
    [
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 1",
        "multiplier": 10,
        "seed": 1,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            100,
            0.0
          ],
          [
            120,
            0.0
          ],
          [
            140,
            0.0
          ],
          [
            160,
            0.0
          ]
        ]
      }
    ],
    [
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ],
          [
            121,
            0.0
          ]
        ]
      }
    ],
    [
      {
        "name": "H Dubai peak_core min, \u03b5 [0.05,0.99]",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            39.4982
          ]
        ]
      }
    ],
    [
      {
        "name": "Exp-E Guangzhou mult=20",
        "multiplier": 20,
        "seed": 42,
        "curve": [
          [
            81,
            856.0663339999966
          ],
          [
            121,
            856.0663339999966
          ],
          [
            161,
            851.7379060000022
          ],
          [
            201,
            851.7379060000022
          ],
          [
            241,
            835.100569000001
          ],
          [
            281,
            834.3505189999992
          ],
          [
            321,
            834.3505189999992
          ],
          [
            361,
            832.4575259999999
          ],
          [
            401,
            832.4575259999999
          ],
          [
            441,
            832.4575259999999
          ],
          [
            481,
            832.4575259999999
          ],
          [
            521,
            832.3944630000001
          ],
          [
            561,
            832.3944630000001
          ],
          [
            601,
            832.3944630000001
          ],
          [
            641,
            832.3854540000001
          ],
          [
            681,
            832.37144
          ],
          [
            721,
            832.37144
          ],
          [
            761,
            832.37144
          ],
          [
            801,
            832.37144
          ],
          [
            841,
            832.37144
          ],
          [
            881,
            832.37144
          ],
          [
            921,
            832.37144
          ]
        ]
      },
      {
        "name": "Exp-E Guangzhou mult=10",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            913.8961620000011
          ],
          [
            61,
            856.4090770000024
          ],
          [
            80,
            856.4090770000024
          ],
          [
            100,
            835.4835520000001
          ],
          [
            119,
            835.4835520000001
          ],
          [
            139,
            835.4835520000001
          ],
          [
            159,
            835.4835520000001
          ],
          [
            179,
            835.4835520000001
          ],
          [
            199,
            835.4835520000001
          ],
          [
            219,
            835.4835520000001
          ],
          [
            239,
            835.4835520000001
          ],
          [
            259,
            832.395464
          ],
          [
            279,
            832.395464
          ],
          [
            299,
            832.395464
          ],
          [
            318,
            832.387456
          ],
          [
            338,
            832.387456
          ],
          [
            358,
            832.387456
          ],
          [
            378,
            832.380449
          ],
          [
            398,
            832.378447
          ]
        ]
      },
      {
        "name": "Exp-E Guangzhou mult=5",
        "multiplier": 5,
        "seed": 42,
        "curve": [
          [
            21,
            889.8420090000011
          ],
          [
            31,
            877.0468140000022
          ],
          [
            40,
            877.0468140000022
          ],
          [
            50,
            877.0468140000022
          ],
          [
            60,
            877.0468140000022
          ],
          [
            70,
            877.0468140000022
          ],
          [
            80,
            877.0468140000022
          ],
          [
            90,
            834.9655339999978
          ],
          [
            100,
            834.9655339999978
          ],
          [
            110,
            833.3325010000016
          ],
          [
            120,
            833.3325010000016
          ],
          [
            130,
            833.3325010000016
          ],
          [
            140,
            833.3325010000016
          ],
          [
            150,
            833.3325010000016
          ],
          [
            159,
            833.3325010000016
          ],
          [
            169,
            833.3325010000016
          ],
          [
            179,
            833.3325010000016
          ],
          [
            189,
            832.419488
          ],
          [
            199,
            832.4144829999999
          ],
          [
            209,
            832.4144829999999
          ],
          [
            219,
            832.4144829999999
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=5",
        "multiplier": 10,
        "seed": 5,
        "curve": [
          [
            40,
            896.7895560000005
          ],
          [
            60,
            847.1709389999987
          ],
          [
            80,
            846.0388070000012
          ],
          [
            100,
            845.3557240000024
          ],
          [
            120,
            832.465534
          ],
          [
            140,
            832.465534
          ],
          [
            160,
            832.465534
          ],
          [
            180,
            832.413482
          ],
          [
            200,
            832.413482
          ],
          [
            220,
            832.3854540000001
          ],
          [
            240,
            832.3854540000001
          ],
          [
            260,
            832.3854540000001
          ],
          [
            280,
            832.376445
          ],
          [
            300,
            832.37144
          ],
          [
            320,
            832.37144
          ],
          [
            340,
            832.37144
          ],
          [
            360,
            832.37144
          ],
          [
            380,
            832.37144
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=4",
        "multiplier": 10,
        "seed": 4,
        "curve": [
          [
            41,
            880.2294969999975
          ],
          [
            61,
            880.2294969999975
          ],
          [
            81,
            880.2294969999975
          ],
          [
            101,
            837.4636319999993
          ],
          [
            121,
            837.4376059999993
          ],
          [
            141,
            837.4376059999993
          ],
          [
            161,
            837.4376059999993
          ],
          [
            181,
            834.4175859999992
          ],
          [
            201,
            833.0965649999986
          ],
          [
            221,
            832.5725410000033
          ],
          [
            240,
            832.387456
          ],
          [
            259,
            832.387456
          ],
          [
            279,
            832.387456
          ],
          [
            298,
            832.387456
          ],
          [
            318,
            832.387456
          ],
          [
            338,
            832.387456
          ],
          [
            358,
            832.3854540000001
          ],
          [
            378,
            832.3814500000001
          ],
          [
            398,
            832.373442
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=3",
        "multiplier": 10,
        "seed": 3,
        "curve": [
          [
            41,
            847.444713000001
          ],
          [
            61,
            847.444713000001
          ],
          [
            81,
            847.444713000001
          ],
          [
            101,
            836.2016699999988
          ],
          [
            121,
            836.2016699999988
          ],
          [
            141,
            836.2016699999988
          ],
          [
            161,
            836.2016699999988
          ],
          [
            181,
            834.713582000002
          ],
          [
            201,
            834.713582000002
          ],
          [
            221,
            834.713582000002
          ],
          [
            241,
            832.4254940000001
          ],
          [
            261,
            832.4254940000001
          ],
          [
            281,
            832.413482
          ],
          [
            301,
            832.413482
          ],
          [
            321,
            832.404473
          ],
          [
            341,
            832.397466
          ],
          [
            361,
            832.3894580000001
          ],
          [
            380,
            832.3754440000001
          ],
          [
            399,
            832.3754440000001
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=2",
        "multiplier": 10,
        "seed": 2,
        "curve": [
          [
            41,
            885.0625300000006
          ],
          [
            61,
            866.7189869999995
          ],
          [
            81,
            855.6209890000005
          ],
          [
            101,
            855.6209890000005
          ],
          [
            121,
            855.6209890000005
          ],
          [
            141,
            855.6209890000005
          ],
          [
            161,
            855.6209890000005
          ],
          [
            181,
            843.3087769999967
          ],
          [
            201,
            839.2487169999989
          ],
          [
            221,
            839.0046729999993
          ],
          [
            241,
            832.387456
          ],
          [
            261,
            832.387456
          ],
          [
            281,
            832.387456
          ],
          [
            301,
            832.387456
          ],
          [
            321,
            832.387456
          ],
          [
            341,
            832.387456
          ],
          [
            361,
            832.387456
          ],
          [
            381,
            832.3854540000001
          ],
          [
            401,
            832.374443
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=1",
        "multiplier": 10,
        "seed": 1,
        "curve": [
          [
            41,
            885.1262929999987
          ],
          [
            61,
            855.9562239999967
          ],
          [
            81,
            851.8961639999987
          ],
          [
            101,
            845.8408090000015
          ],
          [
            121,
            843.4737420000032
          ],
          [
            141,
            837.6216900000026
          ],
          [
            161,
            837.6216900000026
          ],
          [
            181,
            832.3944630000001
          ],
          [
            201,
            832.3944630000001
          ],
          [
            221,
            832.3944630000001
          ],
          [
            241,
            832.3944630000001
          ],
          [
            261,
            832.3944630000001
          ],
          [
            281,
            832.3944630000001
          ],
          [
            301,
            832.387456
          ],
          [
            321,
            832.3814500000001
          ],
          [
            341,
            832.3814500000001
          ]
        ]
      },
      {
        "name": "Exp-B Guangzhou skin_exceedance \u2264 0.1 + peak_core \u2264 38",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            913.8961620000011
          ],
          [
            61,
            856.4090770000024
          ],
          [
            80,
            856.4090770000024
          ],
          [
            100,
            835.4835520000001
          ],
          [
            119,
            835.4835520000001
          ],
          [
            139,
            835.4835520000001
          ],
          [
            159,
            835.4835520000001
          ],
          [
            179,
            835.4835520000001
          ],
          [
            199,
            835.4835520000001
          ],
          [
            219,
            835.4835520000001
          ],
          [
            239,
            835.4835520000001
          ],
          [
            259,
            832.395464
          ],
          [
            279,
            832.395464
          ],
          [
            299,
            832.395464
          ],
          [
            318,
            832.387456
          ],
          [
            338,
            832.387456
          ],
          [
            358,
            832.387456
          ],
          [
            378,
            832.380449
          ],
          [
            398,
            832.378447
          ]
        ]
      },
      {
        "name": "Guangzhou August requirement search",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            913.8961620000011
          ],
          [
            61,
            856.4090770000024
          ],
          [
            80,
            856.4090770000024
          ],
          [
            100,
            835.4835520000001
          ],
          [
            119,
            835.4835520000001
          ],
          [
            139,
            835.4835520000001
          ],
          [
            159,
            835.4835520000001
          ],
          [
            179,
            835.4835520000001
          ],
          [
            199,
            835.4835520000001
          ],
          [
            219,
            835.4835520000001
          ],
          [
            239,
            835.4835520000001
          ],
          [
            259,
            832.395464
          ],
          [
            279,
            832.395464
          ],
          [
            299,
            832.395464
          ],
          [
            318,
            832.387456
          ],
          [
            338,
            832.387456
          ],
          [
            358,
            832.387456
          ],
          [
            378,
            832.380449
          ],
          [
            398,
            832.378447
          ]
        ]
      }
    ],
    [
      {
        "name": "Exp-C Dubai July skin_exceedance \u2264 0.1 + peak_core \u2264 38",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            2208.255085000003
          ],
          [
            61,
            2208.255085000003
          ],
          [
            81,
            2178.0948249999983
          ],
          [
            101,
            2161.7336640000003
          ],
          [
            121,
            2161.7336640000003
          ],
          [
            141,
            2161.7336640000003
          ],
          [
            161,
            2158.2036339999977
          ],
          [
            181,
            2157.297628000003
          ],
          [
            201,
            2154.674605000002
          ],
          [
            221,
            2154.572602999999
          ],
          [
            241,
            2154.572602999999
          ],
          [
            261,
            2154.572602999999
          ],
          [
            281,
            2152.5525829999965
          ],
          [
            300,
            2152.5525829999965
          ],
          [
            320,
            2152.2495800000006
          ],
          [
            340,
            2152.2495800000006
          ],
          [
            360,
            2152.2495800000006
          ],
          [
            380,
            2151.9475779999984
          ],
          [
            400,
            2151.8465770000016
          ],
          [
            420,
            2151.3405709999993
          ],
          [
            440,
            2151.3405709999993
          ],
          [
            460,
            2151.3405709999993
          ],
          [
            480,
            2151.140571
          ],
          [
            500,
            2151.0385690000035
          ]
        ]
      }
    ],
    [
      {
        "name": "Exp-A Guangzhou peak_skin \u2264 33",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            3083.594161999997
          ],
          [
            61,
            3044.3620770000007
          ],
          [
            80,
            3044.3620770000007
          ],
          [
            100,
            3027.921551999998
          ],
          [
            119,
            3027.921551999998
          ],
          [
            139,
            3027.921551999998
          ],
          [
            159,
            3027.921551999998
          ],
          [
            179,
            3027.921551999998
          ],
          [
            199,
            3027.921551999998
          ],
          [
            219,
            3027.921551999998
          ],
          [
            239,
            3027.5515950000013
          ],
          [
            259,
            3024.7315060000014
          ],
          [
            279,
            3024.7315060000014
          ],
          [
            299,
            3024.7315060000014
          ],
          [
            319,
            3024.7315060000014
          ],
          [
            339,
            3024.5815050000033
          ],
          [
            359,
            3023.0214559999986
          ],
          [
            379,
            3023.0214559999986
          ]
        ]
      }
    ],
    [
      {
        "name": "Guangzhou August requirement search",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            734.067234
          ],
          [
            61,
            728.749922
          ],
          [
            81,
            720.40959
          ],
          [
            101,
            706.588783
          ],
          [
            121,
            706.588783
          ],
          [
            141,
            706.588783
          ],
          [
            161,
            706.588783
          ],
          [
            181,
            706.588783
          ],
          [
            200,
            706.588783
          ],
          [
            220,
            704.742939
          ],
          [
            240,
            704.742939
          ],
          [
            260,
            704.4246210000001
          ],
          [
            280,
            704.4246210000001
          ],
          [
            300,
            704.312509
          ],
          [
            320,
            704.214411
          ],
          [
            340,
            704.151348
          ],
          [
            360,
            703.9141109999999
          ]
        ]
      }
    ]
  ]
}
```

### File: `backend/docs/acceptance/stage-10-spectral/optimization-summary.md`
```markdown
| name | verdict | best | objective | violation | upper feasible (viol) | min x @ max y | min y @ max x | lower bound binding | plateau |
|---|---|---|---|---|---|---|---|---|---|
| J-tol-1e-4-b | infeasible | {'infrared_emissivity': 0.99} | 2.439081 | 4.098262 | False (4.098262) | None | None | None | None |
| J-tol-1e-5 | infeasible | {'infrared_emissivity': 0.99} | 2.439081 | 4.098262 | False (4.098262) | None | None | None | None |
| J-tol-1e-4 | feasible | {'infrared_emissivity': 0.5} | 0.0 | 0.0 | True (0.0) | None | None | None | None |
| I-Lhasa-min-demand-seed-6 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13281778211284515 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-6: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-5 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13278593937575026 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-5: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-4 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.1327957833133253 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-4: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-3 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13277891656662663 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-3: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-2 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13278631452581038 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-2: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-1 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13279345738295323 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-1: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| H2 - Jul | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.601119 | 7.196338 | False (7.196338) | None | None | False | 0.008264462809917356 |
| H1 -  Aug | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.81147 | 7.75924 | False (7.75924) | None | None | False | 0.008264462809917356 |
| G2 - Equal to air (shaded) | unconstrained | {'infrared_emissivity': 0.99} | 2.375719 | 0.0 | True (0.0) | None | None | None | None |
| G1 - Air + linear solar gain | unconstrained | {'infrared_emissivity': 0.05} | 4.399347 | 0.0 | True (0.0) | None | None | None | None |
| F2-degree-hours-gradient | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 2.126385 | 3.25277 | False (3.25277) | None | None | False | 0.008264462809917356 |
| F1-infeasible-out-of-reach | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 2.126385 | 9.03097 | False (9.03097) | None | None | False | 0.008264462809917356 |
| L-W 拉薩權重 2:1 / 1:2 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.614 | 0.1 | False | 0.2727272727272727 |
|  ⚠ L-W 拉薩權重 2:1 / 1:2: 27% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.628 | 0.55 | False | 0.3305785123966942 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1: 33% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1） | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.628 | 0.05 | False | 0.2809917355371901 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）: 28% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| H Dubai peak_core min, ε [0.05,0.99] | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| Exp-E Guangzhou mult=20 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9885} | 0.93144 | 0.8314400000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-E Guangzhou mult=10 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-E Guangzhou mult=5 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9524} | 0.931483 | 0.831483 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=5 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9894} | 0.93144 | 0.8314400000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=4 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9873} | 0.931442 | 0.831442 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=3 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9899} | 0.931444 | 0.8314440000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=2 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9853} | 0.931443 | 0.831443 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=1 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9842} | 0.93145 | 0.83145 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | feasible | {'solar_reflectance': 0.827, 'infrared_emissivity': 0.7751} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| Exp-C Dubai July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.5004} | 0.969569 | 2.150069000000004 | False (2.2187320000000015) | None | None | False | 0.008264462809917356 |
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-A Guangzhou peak_skin ≤ 33 | infeasible | {'solar_reflectance': 0.9798, 'infrared_emissivity': 0.9886} | 0.931456 | 3.0220899999999986 | False (3.021630000000002) | None | None | False | 0.008264462809917356 |
| Guangzhou August requirement search | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9866} | 0.803111 | 0.703111 | False (0.702697) | None | None | False | 0.008264462809917356 |
| Guangzhou August requirement search | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |

## Seed groups

| first name | n | ρ | ε | objective |
|---|---|---|---|---|
| I-Lhasa-min-demand-seed-6 | 6 | 0.4806 ± 0.0000 | 0.5000 ± 0.0000 | 0.1328 ± 0.0000 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | 5 | 0.8854 ± 0.0326 | 0.9150 ± 0.0782 | 0.0000 ± 0.0000 |
| Exp-E Guangzhou mult=10 | 8 | 0.9799 ± 0.0001 | 0.9874 ± 0.0019 | 0.9314 ± 0.0000 |

```

### File: `backend/docs/acceptance/stage-11-radiant/optimization-summary.json`
```json
{
  "runs": [
    {
      "name": "S11-F3 Guangzhou Aug degree-hours, physical env",
      "id": "a87648bc",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.5
      },
      "best_objective": 2.599091,
      "best_violation": 0.3354,
      "best_metrics": {
        "peak_skin_temperature_c": 37.1554,
        "skin_exceedance_fraction": 0.941723,
        "peak_core_temperature_c": 38.3354,
        "mean_skin_cooling_c": 1.60354
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.5342,
      "upper_peak_skin": 37.3659,
      "evaluations": 742,
      "generations": 30,
      "seconds": 130.677,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)",
        "performance worsens as infrared_emissivity becomes more demanding; its demand_direction is probably inverted for this scenario"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 0.9052,
            "mean_skin_cooling_c": 1.3912,
            "mean_skin_temperature_c": -1.3912,
            "peak_core_temperature_c": -2.126,
            "peak_skin_temperature_c": -2.318,
            "core_exceedance_fraction": -1.1637,
            "core_excess_degree_hours": -0.542,
            "skin_exceedance_fraction": -0.06534,
            "skin_excess_degree_hours": -2.70808
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.5245,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0918,
            "mean_skin_cooling_c": -0.1436,
            "mean_skin_temperature_c": 0.1436,
            "peak_core_temperature_c": 0.218,
            "peak_skin_temperature_c": 0.23,
            "core_exceedance_fraction": 0.12934,
            "core_excess_degree_hours": 0.04756,
            "skin_exceedance_fraction": 0.00772,
            "skin_excess_degree_hours": 0.27796
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "worsens"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "S11-H3 Dubai Jul selective, physical env",
      "id": "683ee690",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity_window": 0.5,
        "infrared_emissivity_outside_window": 0.05
      },
      "best_objective": 4.038676,
      "best_violation": 1.2582,
      "best_metrics": {
        "peak_skin_temperature_c": 38.1659,
        "skin_exceedance_fraction": 0.969219,
        "peak_core_temperature_c": 39.2582,
        "mean_skin_cooling_c": 1.9629
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 1.2845,
      "upper_peak_skin": 38.1942,
      "evaluations": 1059,
      "generations": 30,
      "seconds": 321.111,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity_window sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "best infrared_emissivity_outside_window sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)",
        "map metric is non-monotone along infrared_emissivity_window; requirement readings are least-demanding feasible values, not thresholds"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 1.2342,
            "mean_skin_cooling_c": 1.668,
            "mean_skin_temperature_c": -1.668,
            "peak_core_temperature_c": -2.39,
            "peak_skin_temperature_c": -2.59,
            "core_exceedance_fraction": -0.5562,
            "core_excess_degree_hours": -2.07684,
            "skin_exceedance_fraction": -0.02022,
            "skin_excess_degree_hours": -3.30976
          }
        },
        {
          "name": "infrared_emissivity_window",
          "probe_low": 0.5,
          "probe_high": 0.5245,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0042,
            "mean_skin_cooling_c": -0.0054,
            "mean_skin_temperature_c": 0.0056,
            "peak_core_temperature_c": 0.026,
            "peak_skin_temperature_c": 0.03,
            "core_exceedance_fraction": 0.00372,
            "core_excess_degree_hours": 0.00532,
            "skin_exceedance_fraction": 0.0002,
            "skin_excess_degree_hours": 0.01074
          }
        },
        {
          "name": "infrared_emissivity_outside_window",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.2732,
            "mean_skin_cooling_c": -0.3708,
            "mean_skin_temperature_c": 0.3708,
            "peak_core_temperature_c": 0.572,
            "peak_skin_temperature_c": 0.62,
            "core_exceedance_fraction": 0.13248,
            "core_excess_degree_hours": 0.4536,
            "skin_exceedance_fraction": 0.00486,
            "skin_excess_degree_hours": 0.73544
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "mixed",
        "improves"
      ],
      "map": "infrared_emissivity_window \u00d7 infrared_emissivity_outside_window",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "S11-G3 Dubai Jul gray eps, physical env, K=40",
      "id": "ff17a793",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.5111,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4405,
        "skin_exceedance_fraction": 0.971302,
        "peak_core_temperature_c": 39.5111,
        "mean_skin_cooling_c": 1.65911
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.7957,
      "evaluations": 72,
      "generations": 7,
      "seconds": 8.967,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.1606,
            "mean_skin_cooling_c": -0.2164,
            "mean_skin_temperature_c": 0.2164,
            "peak_core_temperature_c": 0.376,
            "peak_skin_temperature_c": 0.416,
            "core_exceedance_fraction": 0.05414,
            "core_excess_degree_hours": 0.28108,
            "skin_exceedance_fraction": 0.00252,
            "skin_excess_degree_hours": 0.42948
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "S11-G3 Dubai Jul gray eps, physical env, K=5",
      "id": "271e6073",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.5341,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4644,
        "skin_exceedance_fraction": 0.971487,
        "peak_core_temperature_c": 39.5341,
        "mean_skin_cooling_c": 1.86663
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 39.1941,
      "evaluations": 72,
      "generations": 7,
      "seconds": 7.714,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.373,
            "mean_skin_cooling_c": -0.4974,
            "mean_skin_temperature_c": 0.4972,
            "peak_core_temperature_c": 0.804,
            "peak_skin_temperature_c": 0.86,
            "core_exceedance_fraction": 0.1266,
            "core_excess_degree_hours": 0.65124,
            "skin_exceedance_fraction": 0.00584,
            "skin_excess_degree_hours": 0.9869
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "S11-G3 Dubai Jul gray eps, physical env",
      "id": "1c8ca1ae",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.5228,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4527,
        "skin_exceedance_fraction": 0.971396,
        "peak_core_temperature_c": 39.5228,
        "mean_skin_cooling_c": 1.76575
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.9997,
      "evaluations": 72,
      "generations": 7,
      "seconds": 7.484,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.2694,
            "mean_skin_cooling_c": -0.3604,
            "mean_skin_temperature_c": 0.3604,
            "peak_core_temperature_c": 0.596,
            "peak_skin_temperature_c": 0.644,
            "core_exceedance_fraction": 0.0914,
            "core_excess_degree_hours": 0.47054,
            "skin_exceedance_fraction": 0.0042,
            "skin_excess_degree_hours": 0.71536
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "S10-J Dubai Jul peak core, atol 1e-05",
      "id": "7a55bcc4",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.4968,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4243,
        "skin_exceedance_fraction": 0.971222,
        "peak_core_temperature_c": 39.4968,
        "mean_skin_cooling_c": 1.55468
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.5257,
      "evaluations": 72,
      "generations": 7,
      "seconds": 5.041,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0556,
            "mean_skin_cooling_c": -0.0738,
            "mean_skin_temperature_c": 0.0738,
            "peak_core_temperature_c": 0.114,
            "peak_skin_temperature_c": 0.12,
            "core_exceedance_fraction": 0.01758,
            "core_excess_degree_hours": 0.09776,
            "skin_exceedance_fraction": 0.00108,
            "skin_excess_degree_hours": 0.14612
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "S10-J Dubai Jul peak core, atol 0.0001",
      "id": "8641043d",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.4968,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4243,
        "skin_exceedance_fraction": 0.971222,
        "peak_core_temperature_c": 39.4968,
        "mean_skin_cooling_c": 1.55468
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.5257,
      "evaluations": 72,
      "generations": 7,
      "seconds": 5.244,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0556,
            "mean_skin_cooling_c": -0.0738,
            "mean_skin_temperature_c": 0.0738,
            "peak_core_temperature_c": 0.114,
            "peak_skin_temperature_c": 0.12,
            "core_exceedance_fraction": 0.01758,
            "core_excess_degree_hours": 0.09776,
            "skin_exceedance_fraction": 0.00108,
            "skin_excess_degree_hours": 0.14612
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "S10-J Dubai Jul peak core, atol 0.001",
      "id": "31b5a6fb",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.4968,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4243,
        "skin_exceedance_fraction": 0.971222,
        "peak_core_temperature_c": 39.4968,
        "mean_skin_cooling_c": 1.55468
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.5257,
      "evaluations": 58,
      "generations": 5,
      "seconds": 4.144,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0556,
            "mean_skin_cooling_c": -0.0738,
            "mean_skin_temperature_c": 0.0738,
            "peak_core_temperature_c": 0.114,
            "peak_skin_temperature_c": 0.12,
            "core_exceedance_fraction": 0.01758,
            "core_excess_degree_hours": 0.09776,
            "skin_exceedance_fraction": 0.00108,
            "skin_excess_degree_hours": 0.14612
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "S10-I Lhasa Jul material demand seed 5",
      "id": "2e6315fc",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 5,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.6821,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.28099027611044414,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.2484,
        "skin_exceedance_fraction": 0.099278,
        "peak_core_temperature_c": 37.2008,
        "mean_skin_cooling_c": 0.77464
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 740,
      "generations": 30,
      "seconds": 53.865,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.648144,
          "probe_high": 0.716144,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2353,
            "mean_skin_cooling_c": 2.0528,
            "mean_skin_temperature_c": -2.0529,
            "peak_core_temperature_c": -0.41,
            "peak_skin_temperature_c": -2.109,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -2.86147,
            "skin_excess_degree_hours": -0.65523
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524502,
          "full_range_effects": {
            "mean_core_cooling_c": 0.042397,
            "mean_skin_cooling_c": 0.397168,
            "mean_skin_temperature_c": -0.397168,
            "peak_core_temperature_c": -0.067994,
            "peak_skin_temperature_c": -0.341972,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.219762,
            "skin_excess_degree_hours": -0.065375
          }
        }
      ],
      "required_x_at_best_y": 0.572,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": 0.572
        }
      ]
    },
    {
      "name": "S10-I Lhasa Jul material demand seed 4",
      "id": "b7748a52",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 4,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.6822,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.28102028811524615,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.2483,
        "skin_exceedance_fraction": 0.099096,
        "peak_core_temperature_c": 37.2008,
        "mean_skin_cooling_c": 0.77472
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 745,
      "generations": 30,
      "seconds": 66.244,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.648164,
          "probe_high": 0.716164,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2352,
            "mean_skin_cooling_c": 2.053,
            "mean_skin_temperature_c": -2.0531,
            "peak_core_temperature_c": -0.409,
            "peak_skin_temperature_c": -2.109,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -2.86093,
            "skin_excess_degree_hours": -0.65486
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524517,
          "full_range_effects": {
            "mean_core_cooling_c": 0.042371,
            "mean_skin_cooling_c": 0.397524,
            "mean_skin_temperature_c": -0.397324,
            "peak_core_temperature_c": -0.067953,
            "peak_skin_temperature_c": -0.341763,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.21677,
            "skin_excess_degree_hours": -0.065415
          }
        }
      ],
      "required_x_at_best_y": 0.572,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": 0.572
        }
      ]
    },
    {
      "name": "S10-I Lhasa Jul material demand seed 3",
      "id": "b4adb273",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 3,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.6823,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.2811007352941177,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.2479,
        "skin_exceedance_fraction": 0.094872,
        "peak_core_temperature_c": 37.2007,
        "mean_skin_cooling_c": 0.7751
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 741,
      "generations": 30,
      "seconds": 60.952,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.648297,
          "probe_high": 0.716297,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2353,
            "mean_skin_cooling_c": 2.0534,
            "mean_skin_temperature_c": -2.0535,
            "peak_core_temperature_c": -0.41,
            "peak_skin_temperature_c": -2.109,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -2.85519,
            "skin_excess_degree_hours": -0.6528
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.5245,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0424,
            "mean_skin_cooling_c": 0.3974,
            "mean_skin_temperature_c": -0.3972,
            "peak_core_temperature_c": -0.068,
            "peak_skin_temperature_c": -0.342,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.13488,
            "skin_excess_degree_hours": -0.06524
          }
        }
      ],
      "required_x_at_best_y": 0.572,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": 0.572
        }
      ]
    },
    {
      "name": "S10-I Lhasa Jul material demand seed 2",
      "id": "10b038e3",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 2,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.6821,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.2810093337334935,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.2484,
        "skin_exceedance_fraction": 0.099278,
        "peak_core_temperature_c": 37.2008,
        "mean_skin_cooling_c": 0.77464
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 744,
      "generations": 30,
      "seconds": 56.856,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.648138,
          "probe_high": 0.716138,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2353,
            "mean_skin_cooling_c": 2.0528,
            "mean_skin_temperature_c": -2.0529,
            "peak_core_temperature_c": -0.41,
            "peak_skin_temperature_c": -2.109,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -2.86147,
            "skin_excess_degree_hours": -0.65523
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524525,
          "full_range_effects": {
            "mean_core_cooling_c": 0.042357,
            "mean_skin_cooling_c": 0.397195,
            "mean_skin_temperature_c": -0.397195,
            "peak_core_temperature_c": -0.067931,
            "peak_skin_temperature_c": -0.341651,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.237038,
            "skin_excess_degree_hours": -0.065333
          }
        }
      ],
      "required_x_at_best_y": 0.572,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": 0.572
        }
      ]
    },
    {
      "name": "S10-I Lhasa Jul material demand seed 1",
      "id": "4921de23",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 1,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.6821,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.28101970288115247,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.2483,
        "skin_exceedance_fraction": 0.09921,
        "peak_core_temperature_c": 37.2008,
        "mean_skin_cooling_c": 0.77465
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 742,
      "generations": 30,
      "seconds": 63.392,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.648141,
          "probe_high": 0.716141,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2353,
            "mean_skin_cooling_c": 2.0529,
            "mean_skin_temperature_c": -2.0529,
            "peak_core_temperature_c": -0.41,
            "peak_skin_temperature_c": -2.109,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -2.86129,
            "skin_excess_degree_hours": -0.65522
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524533,
          "full_range_effects": {
            "mean_core_cooling_c": 0.042343,
            "mean_skin_cooling_c": 0.397265,
            "mean_skin_temperature_c": -0.397465,
            "peak_core_temperature_c": -0.067909,
            "peak_skin_temperature_c": -0.34154,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.23726,
            "skin_excess_degree_hours": -0.065412
          }
        }
      ],
      "required_x_at_best_y": 0.572,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": 0.572
        }
      ]
    },
    {
      "name": "S10-I Lhasa Jul material demand seed 42",
      "id": "04d5daf6",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.6822,
        "infrared_emissivity": 0.5002
      },
      "best_objective": 0.28116919267707086,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.2482,
        "skin_exceedance_fraction": 0.097058,
        "peak_core_temperature_c": 37.2007,
        "mean_skin_cooling_c": 0.77485
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 745,
      "generations": 30,
      "seconds": 59.941,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.648175,
          "probe_high": 0.716175,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2353,
            "mean_skin_cooling_c": 2.053,
            "mean_skin_temperature_c": -2.0529,
            "peak_core_temperature_c": -0.409,
            "peak_skin_temperature_c": -2.109,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -2.85859,
            "skin_excess_degree_hours": -0.65408
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524655,
          "full_range_effects": {
            "mean_core_cooling_c": 0.042133,
            "mean_skin_cooling_c": 0.397287,
            "mean_skin_temperature_c": -0.397287,
            "peak_core_temperature_c": -0.067573,
            "peak_skin_temperature_c": -0.341837,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.216212,
            "skin_excess_degree_hours": -0.065347
          }
        }
      ],
      "required_x_at_best_y": 0.572,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": 0.708
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": 0.64
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": 0.572
        }
      ]
    },
    {
      "name": "S10-H2 Dubai Jul selective, MRT = air",
      "id": "bddb5ea5",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity_window": 0.99,
        "infrared_emissivity_outside_window": 0.05
      },
      "best_objective": 3.579197,
      "best_violation": 0.9026,
      "best_metrics": {
        "peak_skin_temperature_c": 37.7778,
        "skin_exceedance_fraction": 0.965799,
        "peak_core_temperature_c": 38.9026,
        "mean_skin_cooling_c": 1.76056
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.9026,
      "upper_peak_skin": 37.7778,
      "evaluations": 1059,
      "generations": 30,
      "seconds": 247.742,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity_window sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "best infrared_emissivity_outside_window sits at its lower search bound (0.05); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 1.1596,
            "mean_skin_cooling_c": 1.5974,
            "mean_skin_temperature_c": -1.5976,
            "peak_core_temperature_c": -2.306,
            "peak_skin_temperature_c": -2.502,
            "core_exceedance_fraction": -1.04236,
            "core_excess_degree_hours": -1.67444,
            "skin_exceedance_fraction": -0.0285,
            "skin_excess_degree_hours": -3.16302
          }
        },
        {
          "name": "infrared_emissivity_window",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0696,
            "mean_skin_cooling_c": 0.0962,
            "mean_skin_temperature_c": -0.0964,
            "peak_core_temperature_c": -0.14,
            "peak_skin_temperature_c": -0.15,
            "core_exceedance_fraction": -0.07094,
            "core_excess_degree_hours": -0.09718,
            "skin_exceedance_fraction": -0.002,
            "skin_excess_degree_hours": -0.19062
          }
        },
        {
          "name": "infrared_emissivity_outside_window",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0528,
            "mean_skin_cooling_c": -0.0726,
            "mean_skin_temperature_c": 0.0726,
            "peak_core_temperature_c": 0.118,
            "peak_skin_temperature_c": 0.126,
            "core_exceedance_fraction": 0.0443,
            "core_excess_degree_hours": 0.07838,
            "skin_exceedance_fraction": 0.0017,
            "skin_excess_degree_hours": 0.1435
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "infrared_emissivity_window \u00d7 infrared_emissivity_outside_window",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "S10-H1 Dubai Jul selective, MRT air+solar",
      "id": "a35ed126",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity_window": 0.99,
        "infrared_emissivity_outside_window": 0.05
      },
      "best_objective": 3.786867,
      "best_violation": 1.0543,
      "best_metrics": {
        "peak_skin_temperature_c": 37.9421,
        "skin_exceedance_fraction": 0.967561,
        "peak_core_temperature_c": 39.0543,
        "mean_skin_cooling_c": 1.8633
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 1.0543,
      "upper_peak_skin": 37.9421,
      "evaluations": 1059,
      "generations": 30,
      "seconds": 218.873,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity_window sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "best infrared_emissivity_outside_window sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "low infrared_emissivity_outside_window is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 1.178,
            "mean_skin_cooling_c": 1.6076,
            "mean_skin_temperature_c": -1.6074,
            "peak_core_temperature_c": -2.308,
            "peak_skin_temperature_c": -2.504,
            "core_exceedance_fraction": -0.74958,
            "core_excess_degree_hours": -1.8592,
            "skin_exceedance_fraction": -0.02214,
            "skin_excess_degree_hours": -3.18626
          }
        },
        {
          "name": "infrared_emissivity_window",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.038,
            "mean_skin_cooling_c": 0.052,
            "mean_skin_temperature_c": -0.052,
            "peak_core_temperature_c": -0.074,
            "peak_skin_temperature_c": -0.082,
            "core_exceedance_fraction": -0.02664,
            "core_excess_degree_hours": -0.05896,
            "skin_exceedance_fraction": -0.00064,
            "skin_excess_degree_hours": -0.10308
          }
        },
        {
          "name": "infrared_emissivity_outside_window",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.1582,
            "mean_skin_cooling_c": -0.2164,
            "mean_skin_temperature_c": 0.2162,
            "peak_core_temperature_c": 0.322,
            "peak_skin_temperature_c": 0.348,
            "core_exceedance_fraction": 0.10502,
            "core_excess_degree_hours": 0.24818,
            "skin_exceedance_fraction": 0.00316,
            "skin_excess_degree_hours": 0.42852
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "infrared_emissivity_window \u00d7 infrared_emissivity_outside_window",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "S10-G2 Dubai Jul gray eps, MRT = air",
      "id": "6711d887",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.9898
      },
      "best_objective": 39.2552,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.1595,
        "skin_exceedance_fraction": 0.969499,
        "peak_core_temperature_c": 39.2552,
        "mean_skin_cooling_c": 1.52149
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.1594,
      "evaluations": 133,
      "generations": 12,
      "seconds": 9.882,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.942759,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.101878,
            "mean_skin_cooling_c": 0.138092,
            "mean_skin_temperature_c": -0.138092,
            "peak_core_temperature_c": -0.189031,
            "peak_skin_temperature_c": -0.208929,
            "core_exceedance_fraction": -0.054083,
            "core_excess_degree_hours": -0.167441,
            "skin_exceedance_fraction": -0.001453,
            "skin_excess_degree_hours": -0.274114
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "S10-G1 Dubai Jul gray eps, MRT air+solar",
      "id": "3a65ab74",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.4968,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4243,
        "skin_exceedance_fraction": 0.971222,
        "peak_core_temperature_c": 39.4968,
        "mean_skin_cooling_c": 1.55468
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.5257,
      "evaluations": 72,
      "generations": 7,
      "seconds": 5.406,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0556,
            "mean_skin_cooling_c": -0.0738,
            "mean_skin_temperature_c": 0.0738,
            "peak_core_temperature_c": 0.114,
            "peak_skin_temperature_c": 0.12,
            "core_exceedance_fraction": 0.01758,
            "core_excess_degree_hours": 0.09776,
            "skin_exceedance_fraction": 0.00108,
            "skin_excess_degree_hours": 0.14612
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "S10-F2 Guangzhou Aug degree-hours",
      "id": "e809dfd1",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.126385,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7782,
        "skin_exceedance_fraction": 0.931436,
        "peak_core_temperature_c": 37.9969,
        "mean_skin_cooling_c": 1.53443
      },
      "baseline_feasible": false,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 36.7782,
      "evaluations": 741,
      "generations": 30,
      "seconds": 61.16,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 0.701,
            "mean_skin_cooling_c": 1.3778,
            "mean_skin_temperature_c": -1.3778,
            "peak_core_temperature_c": -1.886,
            "peak_skin_temperature_c": -2.068,
            "core_exceedance_fraction": -0.87962,
            "core_excess_degree_hours": -0.08126,
            "skin_exceedance_fraction": -0.0664,
            "skin_excess_degree_hours": -2.66524
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0144,
            "mean_skin_cooling_c": 0.0336,
            "mean_skin_temperature_c": -0.0336,
            "peak_core_temperature_c": -0.036,
            "peak_skin_temperature_c": -0.046,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.00058,
            "skin_excess_degree_hours": -0.06666
          }
        }
      ],
      "required_x_at_best_y": 0.98,
      "required_y_at_best_x": 0.99,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.98,
      "min_y_at_max_x": 0.99,
      "feasible_cell_share": 0.008,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.98,
          "required_x": 0.98
        }
      ]
    },
    {
      "name": "S10-F1 Guangzhou Aug exceedance (rerun Exp-B)",
      "id": "f3396795",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.99
      },
      "best_objective": 0.931436,
      "best_violation": 8.31436,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7782,
        "skin_exceedance_fraction": 0.931436,
        "peak_core_temperature_c": 37.9969,
        "mean_skin_cooling_c": 1.53443
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 8.31436,
      "upper_peak_skin": 36.7782,
      "evaluations": 661,
      "generations": 26,
      "seconds": 49.062,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "skin_exceedance_fraction <= 0.1: violated by 0.8314, but the whole search range moves skin_exceedance_fraction by only about 0.06698 (linearised at the optimum); the target is out of reach of the selected variables",
        "skin_exceedance_fraction is saturated: the threshold is crossed in almost the whole design space, so the metric has no usable gradient. Use skin_excess_degree_hours, which keeps one."
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 0.701,
            "mean_skin_cooling_c": 1.3778,
            "mean_skin_temperature_c": -1.3778,
            "peak_core_temperature_c": -1.886,
            "peak_skin_temperature_c": -2.068,
            "core_exceedance_fraction": -0.87962,
            "core_excess_degree_hours": -0.08126,
            "skin_exceedance_fraction": -0.0664,
            "skin_excess_degree_hours": -2.66524
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0144,
            "mean_skin_cooling_c": 0.0336,
            "mean_skin_temperature_c": -0.0336,
            "peak_core_temperature_c": -0.036,
            "peak_skin_temperature_c": -0.046,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.00058,
            "skin_excess_degree_hours": -0.06666
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "J-tol-1e-4-b",
      "id": "e1db6442",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.439081,
      "best_violation": 4.098262,
      "best_metrics": {
        "peak_skin_temperature_c": 37.0226,
        "skin_exceedance_fraction": 0.939092,
        "peak_core_temperature_c": 38.2201,
        "mean_skin_cooling_c": 1.37305
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 4.098262,
      "upper_peak_skin": 37.0226,
      "evaluations": 122,
      "generations": 11,
      "seconds": 15.858,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "skin_excess_degree_hours <= 0.5: violated by 1.939, but the whole search range moves skin_excess_degree_hours by only about 0.08524 (linearised at the optimum); the target is out of reach of the selected variables",
        "peak_core_temperature_c <= 38: violated by 0.2201, but the whole search range moves peak_core_temperature_c by only about 0.058 (linearised at the optimum); the target is out of reach of the selected variables"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0242,
            "mean_skin_cooling_c": 0.0432,
            "mean_skin_temperature_c": -0.0432,
            "peak_core_temperature_c": -0.058,
            "peak_skin_temperature_c": -0.07,
            "core_exceedance_fraction": -0.0151,
            "core_excess_degree_hours": -0.00906,
            "skin_exceedance_fraction": -0.001,
            "skin_excess_degree_hours": -0.08524
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "J-tol-1e-5",
      "id": "d5c68053",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.439081,
      "best_violation": 4.098262,
      "best_metrics": {
        "peak_skin_temperature_c": 37.0226,
        "skin_exceedance_fraction": 0.939092,
        "peak_core_temperature_c": 38.2201,
        "mean_skin_cooling_c": 1.37305
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 4.098262,
      "upper_peak_skin": 37.0226,
      "evaluations": 151,
      "generations": 14,
      "seconds": 19.536,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "skin_excess_degree_hours <= 0.5: violated by 1.939, but the whole search range moves skin_excess_degree_hours by only about 0.08524 (linearised at the optimum); the target is out of reach of the selected variables",
        "peak_core_temperature_c <= 38: violated by 0.2201, but the whole search range moves peak_core_temperature_c by only about 0.058 (linearised at the optimum); the target is out of reach of the selected variables"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0242,
            "mean_skin_cooling_c": 0.0432,
            "mean_skin_temperature_c": -0.0432,
            "peak_core_temperature_c": -0.058,
            "peak_skin_temperature_c": -0.07,
            "core_exceedance_fraction": -0.0151,
            "core_excess_degree_hours": -0.00906,
            "skin_exceedance_fraction": -0.001,
            "skin_excess_degree_hours": -0.08524
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "J-tol-1e-4",
      "id": "fc14744e",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.4582,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0794,
        "mean_skin_cooling_c": 1.54682
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 34.1105,
      "evaluations": 115,
      "generations": 13,
      "seconds": 15.392,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.5245,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0176,
            "mean_skin_cooling_c": 0.4606,
            "mean_skin_temperature_c": -0.4606,
            "peak_core_temperature_c": -0.044,
            "peak_skin_temperature_c": -0.366,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": 0.0,
            "skin_excess_degree_hours": 0.0
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-6",
      "id": "5792f168",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 6,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13281778211284515,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640023,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23334
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 745,
      "generations": 30,
      "seconds": 98.687,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446585,
          "probe_high": 0.514585,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.63,
            "mean_skin_temperature_c": -1.63,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.628,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19147,
            "skin_excess_degree_hours": -2.10386
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524534,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059517,
            "mean_skin_cooling_c": 0.364694,
            "mean_skin_temperature_c": -0.364894,
            "peak_core_temperature_c": -0.087878,
            "peak_skin_temperature_c": -0.315562,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.260399,
            "skin_excess_degree_hours": -0.438132
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-5",
      "id": "f2dc6007",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 5,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13278593937575026,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640091,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23329
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 741,
      "generations": 30,
      "seconds": 96.962,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446575,
          "probe_high": 0.514575,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.6298,
            "mean_skin_temperature_c": -1.6299,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.627,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.191,
            "skin_excess_degree_hours": -2.10381
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.52451,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059376,
            "mean_skin_cooling_c": 0.364851,
            "mean_skin_temperature_c": -0.364851,
            "peak_core_temperature_c": -0.087964,
            "peak_skin_temperature_c": -0.313872,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.259994,
            "skin_excess_degree_hours": -0.438201
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-4",
      "id": "bf4a830c",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 4,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.1327957833133253,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640071,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23332
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 743,
      "generations": 30,
      "seconds": 94.39,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446587,
          "probe_high": 0.514587,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.63,
            "mean_skin_temperature_c": -1.63,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.628,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19152,
            "skin_excess_degree_hours": -2.10391
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524511,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059373,
            "mean_skin_cooling_c": 0.364836,
            "mean_skin_temperature_c": -0.364836,
            "peak_core_temperature_c": -0.087961,
            "peak_skin_temperature_c": -0.315858,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.260303,
            "skin_excess_degree_hours": -0.438103
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-3",
      "id": "17bea257",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 3,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13277891656662663,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640091,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23328
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 738,
      "generations": 30,
      "seconds": 95.516,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446571,
          "probe_high": 0.514571,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.6298,
            "mean_skin_temperature_c": -1.6299,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.627,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19092,
            "skin_excess_degree_hours": -2.10384
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524506,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059385,
            "mean_skin_cooling_c": 0.364711,
            "mean_skin_temperature_c": -0.364711,
            "peak_core_temperature_c": -0.087978,
            "peak_skin_temperature_c": -0.313923,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.259916,
            "skin_excess_degree_hours": -0.438013
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-2",
      "id": "3f44794e",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 2,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13278631452581038,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640071,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23331
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 742,
      "generations": 30,
      "seconds": 94.727,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446588,
          "probe_high": 0.514588,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.6299,
            "mean_skin_temperature_c": -1.63,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.627,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19155,
            "skin_excess_degree_hours": -2.10388
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524501,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059398,
            "mean_skin_cooling_c": 0.364785,
            "mean_skin_temperature_c": -0.364785,
            "peak_core_temperature_c": -0.087996,
            "peak_skin_temperature_c": -0.315987,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.260409,
            "skin_excess_degree_hours": -0.438162
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "I-Lhasa-min-demand-seed-1",
      "id": "7575e16b",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 1,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.4806,
        "infrared_emissivity": 0.5
      },
      "best_objective": 0.13279345738295323,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 35.7972,
        "skin_exceedance_fraction": 0.640071,
        "peak_core_temperature_c": 37.3287,
        "mean_skin_cooling_c": 0.23332
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 740,
      "generations": 30,
      "seconds": 100.325,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.5); the optimum may lie outside the searched range",
        "infrared_emissivity requirement reads at its least demanding bound (0.5): the true requirement lies beyond the searched range",
        "41% of map cells share the minimum; ties are resolved towards the least demanding design",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.446588,
          "probe_high": 0.514588,
          "full_range_effects": {
            "mean_core_cooling_c": 0.2778,
            "mean_skin_cooling_c": 1.63,
            "mean_skin_temperature_c": -1.63,
            "peak_core_temperature_c": -0.451,
            "peak_skin_temperature_c": -1.628,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -1.19152,
            "skin_excess_degree_hours": -2.10391
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.5,
          "probe_high": 0.524508,
          "full_range_effects": {
            "mean_core_cooling_c": 0.059381,
            "mean_skin_cooling_c": 0.364881,
            "mean_skin_temperature_c": -0.364881,
            "peak_core_temperature_c": -0.087971,
            "peak_skin_temperature_c": -0.315897,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.260335,
            "skin_excess_degree_hours": -0.438157
          }
        }
      ],
      "required_x_at_best_y": 0.368,
      "required_y_at_best_x": 0.5,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.368,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.81,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.549,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.598,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.647,
          "minimum_x": 0.504,
          "required_x": 0.504
        },
        {
          "y": 0.696,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.745,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.794,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.843,
          "minimum_x": 0.436,
          "required_x": 0.436
        },
        {
          "y": 0.892,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.941,
          "minimum_x": 0.368,
          "required_x": 0.368
        },
        {
          "y": 0.99,
          "minimum_x": 0.368,
          "required_x": 0.368
        }
      ]
    },
    {
      "name": "H2 - Jul",
      "id": "565fe333",
      "city": "dubai",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity_window": 0.99,
        "infrared_emissivity_outside_window": 0.05
      },
      "best_objective": 3.601119,
      "best_violation": 7.196338,
      "best_metrics": {
        "peak_skin_temperature_c": 37.8585,
        "skin_exceedance_fraction": 0.970815,
        "peak_core_temperature_c": 38.9941,
        "mean_skin_cooling_c": 1.83442
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 7.196338,
      "upper_peak_skin": 37.8585,
      "evaluations": 1057,
      "generations": 30,
      "seconds": 390.447,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity_window sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "best infrared_emissivity_outside_window sits at its lower search bound (0.05); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 1.17,
            "mean_skin_cooling_c": 1.6002,
            "mean_skin_temperature_c": -1.6002,
            "peak_core_temperature_c": -2.128,
            "peak_skin_temperature_c": -2.358,
            "core_exceedance_fraction": -1.3186,
            "core_excess_degree_hours": -1.61602,
            "skin_exceedance_fraction": -0.01734,
            "skin_excess_degree_hours": -3.17794
          }
        },
        {
          "name": "infrared_emissivity_window",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0706,
            "mean_skin_cooling_c": 0.0966,
            "mean_skin_temperature_c": -0.0966,
            "peak_core_temperature_c": -0.132,
            "peak_skin_temperature_c": -0.148,
            "core_exceedance_fraction": -0.08828,
            "core_excess_degree_hours": -0.09152,
            "skin_exceedance_fraction": -0.00102,
            "skin_excess_degree_hours": -0.19194
          }
        },
        {
          "name": "infrared_emissivity_outside_window",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0792,
            "mean_skin_cooling_c": -0.1088,
            "mean_skin_temperature_c": 0.109,
            "peak_core_temperature_c": 0.148,
            "peak_skin_temperature_c": 0.164,
            "core_exceedance_fraction": 0.10078,
            "core_excess_degree_hours": 0.1036,
            "skin_exceedance_fraction": 0.00136,
            "skin_excess_degree_hours": 0.21608
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "infrared_emissivity_window \u00d7 infrared_emissivity_outside_window",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "H1 -  Aug",
      "id": "75b42686",
      "city": "dubai",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity_window": 0.99,
        "infrared_emissivity_outside_window": 0.05
      },
      "best_objective": 3.81147,
      "best_violation": 7.75924,
      "best_metrics": {
        "peak_skin_temperature_c": 38.0157,
        "skin_exceedance_fraction": 0.971934,
        "peak_core_temperature_c": 39.1363,
        "mean_skin_cooling_c": 1.9489
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 7.75924,
      "upper_peak_skin": 38.0157,
      "evaluations": 1059,
      "generations": 30,
      "seconds": 398.358,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity_window sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "best infrared_emissivity_outside_window sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "low infrared_emissivity_outside_window is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 1.2016,
            "mean_skin_cooling_c": 1.6318,
            "mean_skin_temperature_c": -1.6318,
            "peak_core_temperature_c": -2.132,
            "peak_skin_temperature_c": -2.36,
            "core_exceedance_fraction": -0.98534,
            "core_excess_degree_hours": -1.88278,
            "skin_exceedance_fraction": -0.01594,
            "skin_excess_degree_hours": -3.24296
          }
        },
        {
          "name": "infrared_emissivity_window",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0392,
            "mean_skin_cooling_c": 0.0536,
            "mean_skin_temperature_c": -0.0536,
            "peak_core_temperature_c": -0.072,
            "peak_skin_temperature_c": -0.08,
            "core_exceedance_fraction": -0.03626,
            "core_excess_degree_hours": -0.05958,
            "skin_exceedance_fraction": -0.0005,
            "skin_excess_degree_hours": -0.1065
          }
        },
        {
          "name": "infrared_emissivity_outside_window",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.189,
            "mean_skin_cooling_c": -0.2574,
            "mean_skin_temperature_c": 0.2574,
            "peak_core_temperature_c": 0.344,
            "peak_skin_temperature_c": 0.38,
            "core_exceedance_fraction": 0.17052,
            "core_excess_degree_hours": 0.28852,
            "skin_exceedance_fraction": 0.0027,
            "skin_excess_degree_hours": 0.51134
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "infrared_emissivity_window \u00d7 infrared_emissivity_outside_window",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "G2 - Equal to air (shaded)",
      "id": "b0738e64",
      "city": "guangzhou",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.375719,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 36.8985,
        "skin_exceedance_fraction": 0.933548,
        "peak_core_temperature_c": 38.1176,
        "mean_skin_cooling_c": 1.45854
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 36.8985,
      "evaluations": 142,
      "generations": 13,
      "seconds": 17.643,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.943,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.1172,
            "mean_skin_cooling_c": 0.1942,
            "mean_skin_temperature_c": -0.1944,
            "peak_core_temperature_c": -0.258,
            "peak_skin_temperature_c": -0.286,
            "core_exceedance_fraction": -0.09108,
            "core_excess_degree_hours": -0.0269,
            "skin_exceedance_fraction": -0.00878,
            "skin_excess_degree_hours": -0.37704
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "G1 - Air + linear solar gain",
      "id": "9524b52a",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 4.399347,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4243,
        "skin_exceedance_fraction": 0.971222,
        "peak_core_temperature_c": 39.4968,
        "mean_skin_cooling_c": 1.55468
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.5257,
      "evaluations": 72,
      "generations": 7,
      "seconds": 9.55,
      "plateau_fraction": null,
      "warnings": [
        "best infrared_emissivity sits at its lower search bound (0.05); the optimum may lie outside the searched range",
        "best beats the most demanding design: performance is non-monotone in at least one variable (check demand directions and the trends below)",
        "low infrared_emissivity is favoured because T_mrt = T_air + solar gain places the non-sky hemisphere above the clothing surface; repeat with mean_radiant_temperature_method = equal_to_air before reporting this"
      ],
      "sensitivities": [
        {
          "name": "infrared_emissivity",
          "probe_low": 0.05,
          "probe_high": 0.097,
          "full_range_effects": {
            "mean_core_cooling_c": -0.0556,
            "mean_skin_cooling_c": -0.0738,
            "mean_skin_temperature_c": 0.0738,
            "peak_core_temperature_c": 0.114,
            "peak_skin_temperature_c": 0.12,
            "core_exceedance_fraction": 0.01758,
            "core_excess_degree_hours": 0.09776,
            "skin_exceedance_fraction": 0.00108,
            "skin_excess_degree_hours": 0.14612
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "F2-degree-hours-gradient",
      "id": "53682159",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.5; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.126385,
      "best_violation": 3.25277,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7782,
        "skin_exceedance_fraction": 0.931436,
        "peak_core_temperature_c": 37.9969,
        "mean_skin_cooling_c": 1.53443
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 3.25277,
      "upper_peak_skin": 36.7782,
      "evaluations": 442,
      "generations": 15,
      "seconds": 57.356,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 0.701,
            "mean_skin_cooling_c": 1.3778,
            "mean_skin_temperature_c": -1.3778,
            "peak_core_temperature_c": -1.886,
            "peak_skin_temperature_c": -2.068,
            "core_exceedance_fraction": -0.87962,
            "core_excess_degree_hours": -0.08126,
            "skin_exceedance_fraction": -0.0664,
            "skin_excess_degree_hours": -2.66524
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0144,
            "mean_skin_cooling_c": 0.0336,
            "mean_skin_temperature_c": -0.0336,
            "peak_core_temperature_c": -0.036,
            "peak_skin_temperature_c": -0.046,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.00058,
            "skin_excess_degree_hours": -0.06666
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "F1-infeasible-out-of-reach",
      "id": "4a13bad4",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_excess_degree_hours <= 0.0; peak_core_temperature_c <= 38.0; peak_skin_temperature_c <= 32.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.99
      },
      "best_objective": 2.126385,
      "best_violation": 9.03097,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7782,
        "skin_exceedance_fraction": 0.931436,
        "peak_core_temperature_c": 37.9969,
        "mean_skin_cooling_c": 1.53443
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 9.03097,
      "upper_peak_skin": 36.7782,
      "evaluations": 739,
      "generations": 30,
      "seconds": 94.374,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [
        "best solar_reflectance sits at its upper search bound (0.98); the optimum may lie outside the searched range",
        "best infrared_emissivity sits at its upper search bound (0.99); the optimum may lie outside the searched range",
        "peak_skin_temperature_c <= 32: violated by 4.778, but the whole search range moves peak_skin_temperature_c by only about 2.114 (linearised at the optimum); the target is out of reach of the selected variables"
      ],
      "sensitivities": [
        {
          "name": "solar_reflectance",
          "probe_low": 0.946,
          "probe_high": 0.98,
          "full_range_effects": {
            "mean_core_cooling_c": 0.701,
            "mean_skin_cooling_c": 1.3778,
            "mean_skin_temperature_c": -1.3778,
            "peak_core_temperature_c": -1.886,
            "peak_skin_temperature_c": -2.068,
            "core_exceedance_fraction": -0.87962,
            "core_excess_degree_hours": -0.08126,
            "skin_exceedance_fraction": -0.0664,
            "skin_excess_degree_hours": -2.66524
          }
        },
        {
          "name": "infrared_emissivity",
          "probe_low": 0.9655,
          "probe_high": 0.99,
          "full_range_effects": {
            "mean_core_cooling_c": 0.0144,
            "mean_skin_cooling_c": 0.0336,
            "mean_skin_temperature_c": -0.0336,
            "peak_core_temperature_c": -0.036,
            "peak_skin_temperature_c": -0.046,
            "core_exceedance_fraction": 0.0,
            "core_excess_degree_hours": 0.0,
            "skin_exceedance_fraction": -0.00058,
            "skin_excess_degree_hours": -0.06666
          }
        }
      ],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        "improves",
        "improves"
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "L-W \u62c9\u85a9\u6b0a\u91cd 2:1 / 1:2",
      "id": "8ba7a747",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7243,
      "evaluations": 242,
      "generations": 5,
      "seconds": 31.655,
      "plateau_fraction": 0.2727272727272727,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.614,
      "min_y_at_max_x": 0.1,
      "feasible_cell_share": 0.355,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.1,
          "minimum_x": 0.802,
          "required_x": null
        },
        {
          "y": 0.188,
          "minimum_x": 0.802,
          "required_x": null
        },
        {
          "y": 0.276,
          "minimum_x": 0.802,
          "required_x": null
        },
        {
          "y": 0.364,
          "minimum_x": 0.802,
          "required_x": null
        },
        {
          "y": 0.452,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.54,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.628,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.716,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.804,
          "minimum_x": 0.614,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.614,
          "required_x": null
        },
        {
          "y": 0.98,
          "minimum_x": 0.614,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 5",
      "id": "caffdcbc",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 5,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 202,
      "generations": 3,
      "seconds": 27.078,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 4",
      "id": "3d83bbf7",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 4,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 222,
      "generations": 4,
      "seconds": 29.775,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 3",
      "id": "3ebaa2be",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 3,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 222,
      "generations": 4,
      "seconds": 29.239,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 2",
      "id": "f0897399",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 2,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 222,
      "generations": 4,
      "seconds": 28.744,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 1",
      "id": "dd922952",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 1,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 281,
      "generations": 7,
      "seconds": 36.664,
      "plateau_fraction": 0.3305785123966942,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.628,
      "min_y_at_max_x": 0.55,
      "feasible_cell_share": 0.413,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.55,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.594,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.638,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.682,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.726,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.77,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.814,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.858,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.902,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.946,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.628,
          "required_x": null
        }
      ]
    },
    {
      "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09",
      "id": "d72418b5",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.9,
        "infrared_emissivity": 0.95
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.1375,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0433,
        "mean_skin_cooling_c": 1.96577
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 242,
      "generations": 5,
      "seconds": 31.319,
      "plateau_fraction": 0.2809917355371901,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.628,
      "min_y_at_max_x": 0.05,
      "feasible_cell_share": 0.355,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.05,
          "minimum_x": 0.804,
          "required_x": null
        },
        {
          "y": 0.144,
          "minimum_x": 0.804,
          "required_x": null
        },
        {
          "y": 0.238,
          "minimum_x": 0.804,
          "required_x": null
        },
        {
          "y": 0.332,
          "minimum_x": 0.804,
          "required_x": null
        },
        {
          "y": 0.426,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.52,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.614,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.708,
          "minimum_x": 0.716,
          "required_x": null
        },
        {
          "y": 0.802,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.896,
          "minimum_x": 0.628,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.628,
          "required_x": null
        }
      ]
    },
    {
      "name": "H Dubai peak_core min, \u03b5 [0.05,0.99]",
      "id": "d93fc6a6",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "",
      "verdict": "unconstrained",
      "best": {
        "infrared_emissivity": 0.05
      },
      "best_objective": 39.4968,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 38.4243,
        "skin_exceedance_fraction": 0.971222,
        "peak_core_temperature_c": 39.4968,
        "mean_skin_cooling_c": 1.55468
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 38.5257,
      "evaluations": 23,
      "generations": 1,
      "seconds": 3.075,
      "plateau_fraction": null,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ]
    },
    {
      "name": "Exp-E Guangzhou mult=20",
      "id": "e73cb312",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 20,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9885
      },
      "best_objective": 0.93144,
      "best_violation": 0.8314400000000001,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7784,
        "skin_exceedance_fraction": 0.93144,
        "peak_core_temperature_c": 37.997,
        "mean_skin_cooling_c": 1.5343
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 1042,
      "generations": 22,
      "seconds": 142.371,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-E Guangzhou mult=10",
      "id": "54d8da07",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9876
      },
      "best_objective": 0.931447,
      "best_violation": 0.831447,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7787,
        "skin_exceedance_fraction": 0.931447,
        "peak_core_temperature_c": 37.9972,
        "mean_skin_cooling_c": 1.53411
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 519,
      "generations": 19,
      "seconds": 72.705,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-E Guangzhou mult=5",
      "id": "66f1f154",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 5,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9524
      },
      "best_objective": 0.931483,
      "best_violation": 0.831483,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7819,
        "skin_exceedance_fraction": 0.931483,
        "peak_core_temperature_c": 37.9998,
        "mean_skin_cooling_c": 1.53179
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 340,
      "generations": 21,
      "seconds": 45.3,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=5",
      "id": "98519f18",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 5,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9894
      },
      "best_objective": 0.93144,
      "best_violation": 0.8314400000000001,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7784,
        "skin_exceedance_fraction": 0.93144,
        "peak_core_temperature_c": 37.997,
        "mean_skin_cooling_c": 1.53431
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 501,
      "generations": 18,
      "seconds": 71.1,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=4",
      "id": "e5877c0f",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 4,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9873
      },
      "best_objective": 0.931442,
      "best_violation": 0.831442,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7785,
        "skin_exceedance_fraction": 0.931442,
        "peak_core_temperature_c": 37.9971,
        "mean_skin_cooling_c": 1.53421
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 519,
      "generations": 19,
      "seconds": 72.227,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=3",
      "id": "9f03fcea",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 3,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9899
      },
      "best_objective": 0.931444,
      "best_violation": 0.8314440000000001,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7784,
        "skin_exceedance_fraction": 0.931444,
        "peak_core_temperature_c": 37.997,
        "mean_skin_cooling_c": 1.53428
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 520,
      "generations": 19,
      "seconds": 73.434,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=2",
      "id": "d8f0070d",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 2,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9853
      },
      "best_objective": 0.931443,
      "best_violation": 0.831443,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7787,
        "skin_exceedance_fraction": 0.931443,
        "peak_core_temperature_c": 37.9973,
        "mean_skin_cooling_c": 1.53408
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 522,
      "generations": 19,
      "seconds": 70.077,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-D Guangzhou seed=1",
      "id": "c1f10bd8",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 1,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9842
      },
      "best_objective": 0.93145,
      "best_violation": 0.83145,
      "best_metrics": {
        "peak_skin_temperature_c": 36.779,
        "skin_exceedance_fraction": 0.93145,
        "peak_core_temperature_c": 37.9975,
        "mean_skin_cooling_c": 1.53389
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 462,
      "generations": 16,
      "seconds": 64.497,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-C Lhasa July skin_exceedance \u2264 0.1 + peak_core \u2264 38",
      "id": "455d0022",
      "city": "lhasa",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "feasible",
      "best": {
        "solar_reflectance": 0.827,
        "infrared_emissivity": 0.7751
      },
      "best_objective": 0.0,
      "best_violation": 0.0,
      "best_metrics": {
        "peak_skin_temperature_c": 34.5537,
        "skin_exceedance_fraction": 0.0,
        "peak_core_temperature_c": 37.0906,
        "mean_skin_cooling_c": 1.49506
      },
      "baseline_feasible": true,
      "upper_feasible": true,
      "upper_violation": 0.0,
      "upper_peak_skin": 33.7608,
      "evaluations": 200,
      "generations": 3,
      "seconds": 27.69,
      "plateau_fraction": 0.4132231404958678,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": 0.572,
      "min_y_at_max_x": 0.5,
      "feasible_cell_share": 0.521,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": 0.708,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": 0.64,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": 0.572,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-C Dubai July skin_exceedance \u2264 0.1 + peak_core \u2264 38",
      "id": "f99754dc",
      "city": "dubai",
      "months": [
        7
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.5004
      },
      "best_objective": 0.969569,
      "best_violation": 2.150069000000004,
      "best_metrics": {
        "peak_skin_temperature_c": 38.188,
        "skin_exceedance_fraction": 0.969569,
        "peak_core_temperature_c": 39.2805,
        "mean_skin_cooling_c": 1.70892
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 2.2187320000000015,
      "upper_peak_skin": 38.2597,
      "evaluations": 621,
      "generations": 24,
      "seconds": 89.03,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-B Guangzhou skin_exceedance \u2264 0.1 + peak_core \u2264 38",
      "id": "b25a5038",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9876
      },
      "best_objective": 0.931447,
      "best_violation": 0.831447,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7787,
        "skin_exceedance_fraction": 0.931447,
        "peak_core_temperature_c": 37.9972,
        "mean_skin_cooling_c": 1.53411
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 519,
      "generations": 19,
      "seconds": 72.203,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Exp-A Guangzhou peak_skin \u2264 33",
      "id": "314795f8",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "mean_skin_temperature_c <= 33.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9798,
        "infrared_emissivity": 0.9886
      },
      "best_objective": 0.931456,
      "best_violation": 3.0220899999999986,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7789,
        "skin_exceedance_fraction": 0.931456,
        "peak_core_temperature_c": 37.9975,
        "mean_skin_cooling_c": 1.53397
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 3.021630000000002,
      "upper_peak_skin": 36.7782,
      "evaluations": 500,
      "generations": 18,
      "seconds": 68.218,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Guangzhou August requirement search",
      "id": "d2d9cca2",
      "city": "guangzhou",
      "months": [
        9
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.98,
        "infrared_emissivity": 0.9866
      },
      "best_objective": 0.803111,
      "best_violation": 0.703111,
      "best_metrics": {
        "peak_skin_temperature_c": 36.6638,
        "skin_exceedance_fraction": 0.803111,
        "peak_core_temperature_c": 37.9028,
        "mean_skin_cooling_c": 1.54986
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.702697,
      "upper_peak_skin": 36.6635,
      "evaluations": 481,
      "generations": 17,
      "seconds": 64.969,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    },
    {
      "name": "Guangzhou August requirement search",
      "id": "6300b97f",
      "city": "guangzhou",
      "months": [
        8
      ],
      "seed": 42,
      "mult": 10,
      "constraints": "skin_exceedance_fraction <= 0.1; peak_core_temperature_c <= 38.0",
      "verdict": "infeasible",
      "best": {
        "solar_reflectance": 0.9799,
        "infrared_emissivity": 0.9876
      },
      "best_objective": 0.931447,
      "best_violation": 0.831447,
      "best_metrics": {
        "peak_skin_temperature_c": 36.7787,
        "skin_exceedance_fraction": 0.931447,
        "peak_core_temperature_c": 37.9972,
        "mean_skin_cooling_c": 1.53411
      },
      "baseline_feasible": false,
      "upper_feasible": false,
      "upper_violation": 0.8314360000000001,
      "upper_peak_skin": 36.7782,
      "evaluations": 519,
      "generations": 19,
      "seconds": 67.048,
      "plateau_fraction": 0.008264462809917356,
      "warnings": [],
      "sensitivities": [],
      "required_x_at_best_y": null,
      "required_y_at_best_x": null,
      "objective_trend": [
        null,
        null
      ],
      "map": "solar_reflectance \u00d7 infrared_emissivity",
      "min_x_at_max_y": null,
      "min_y_at_max_x": null,
      "feasible_cell_share": 0.0,
      "x_lower_bound_binding": false,
      "frontier": [
        {
          "y": 0.5,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.549,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.598,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.647,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.696,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.745,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.794,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.843,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.892,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.941,
          "minimum_x": null,
          "required_x": null
        },
        {
          "y": 0.99,
          "minimum_x": null,
          "required_x": null
        }
      ]
    }
  ],
  "curves": [
    [
      {
        "name": "S11-F3 Guangzhou Aug degree-hours, physical env",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            1000.4408
          ],
          [
            61,
            1000.4408
          ],
          [
            81,
            1000.3953
          ],
          [
            101,
            1000.3801
          ],
          [
            121,
            1000.3532
          ],
          [
            141,
            1000.3532
          ],
          [
            161,
            1000.3532
          ],
          [
            181,
            1000.3532
          ],
          [
            200,
            1000.3532
          ],
          [
            220,
            1000.3503
          ],
          [
            240,
            1000.3433
          ],
          [
            260,
            1000.3366
          ],
          [
            280,
            1000.3366
          ],
          [
            300,
            1000.3366
          ],
          [
            320,
            1000.3366
          ],
          [
            340,
            1000.3366
          ],
          [
            360,
            1000.3366
          ],
          [
            380,
            1000.3366
          ],
          [
            400,
            1000.3364
          ],
          [
            420,
            1000.3364
          ],
          [
            440,
            1000.3362
          ],
          [
            460,
            1000.3362
          ],
          [
            480,
            1000.3357
          ],
          [
            500,
            1000.3357
          ],
          [
            519,
            1000.3355
          ],
          [
            539,
            1000.3355
          ],
          [
            559,
            1000.3355
          ],
          [
            579,
            1000.3355
          ],
          [
            599,
            1000.3355
          ],
          [
            619,
            1000.3355
          ]
        ]
      }
    ],
    [
      {
        "name": "S11-H3 Dubai Jul selective, physical env",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            61,
            1001.3258
          ],
          [
            91,
            1001.3258
          ],
          [
            121,
            1001.3033
          ],
          [
            151,
            1001.3033
          ],
          [
            181,
            1001.2845
          ],
          [
            211,
            1001.2845
          ],
          [
            241,
            1001.2726
          ],
          [
            271,
            1001.2726
          ],
          [
            301,
            1001.2726
          ],
          [
            331,
            1001.2726
          ],
          [
            361,
            1001.2666
          ],
          [
            391,
            1001.2666
          ],
          [
            421,
            1001.2666
          ],
          [
            451,
            1001.2641
          ],
          [
            481,
            1001.2641
          ],
          [
            511,
            1001.2641
          ],
          [
            541,
            1001.2641
          ],
          [
            571,
            1001.2641
          ],
          [
            601,
            1001.2629
          ],
          [
            631,
            1001.2619
          ],
          [
            661,
            1001.26
          ],
          [
            691,
            1001.26
          ],
          [
            721,
            1001.2599
          ],
          [
            751,
            1001.2599
          ],
          [
            781,
            1001.2592
          ],
          [
            811,
            1001.2588
          ],
          [
            841,
            1001.2588
          ],
          [
            871,
            1001.2588
          ],
          [
            901,
            1001.2588
          ],
          [
            931,
            1001.2588
          ]
        ]
      }
    ],
    [
      {
        "name": "S11-G3 Dubai Jul gray eps, physical env, K=40",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.30588758011367134
          ],
          [
            31,
            -0.30588758011367134
          ],
          [
            41,
            -0.309597349626526
          ],
          [
            48,
            -0.31049968736141054
          ],
          [
            55,
            -0.31049968736141054
          ],
          [
            62,
            -0.31059980911094487
          ],
          [
            69,
            -0.3105999985705719
          ]
        ]
      }
    ],
    [
      {
        "name": "S11-G3 Dubai Jul gray eps, physical env, K=5",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.6498875801136725
          ],
          [
            31,
            -0.6498875801136725
          ],
          [
            41,
            -0.6577973496265246
          ],
          [
            48,
            -0.6596996873614138
          ],
          [
            55,
            -0.6596996873614138
          ],
          [
            62,
            -0.659799809110941
          ],
          [
            69,
            -0.6599999985705677
          ]
        ]
      }
    ],
    [
      {
        "name": "S11-G3 Dubai Jul gray eps, physical env",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.4814875801136742
          ],
          [
            31,
            -0.4814875801136742
          ],
          [
            41,
            -0.48739734962652376
          ],
          [
            48,
            -0.48879968736141066
          ],
          [
            55,
            -0.48879968736141066
          ],
          [
            62,
            -0.488899809110945
          ],
          [
            69,
            -0.48899999857057536
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-J Dubai Jul peak core, atol 1e-05",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.09278758011367416
          ],
          [
            31,
            -0.09278758011367416
          ],
          [
            41,
            -0.0938973496265207
          ],
          [
            48,
            -0.09419968736141374
          ],
          [
            55,
            -0.09419968736141374
          ],
          [
            62,
            -0.09419980911094475
          ],
          [
            69,
            -0.09419999857057179
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-J Dubai Jul peak core, atol 0.0001",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.09278758011367416
          ],
          [
            31,
            -0.09278758011367416
          ],
          [
            41,
            -0.0938973496265207
          ],
          [
            48,
            -0.09419968736141374
          ],
          [
            55,
            -0.09419968736141374
          ],
          [
            62,
            -0.09419980911094475
          ],
          [
            69,
            -0.09419999857057179
          ]
        ]
      },
      {
        "name": "S10-G1 Dubai Jul gray eps, MRT air+solar",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.09278758011367416
          ],
          [
            31,
            -0.09278758011367416
          ],
          [
            41,
            -0.0938973496265207
          ],
          [
            48,
            -0.09419968736141374
          ],
          [
            55,
            -0.09419968736141374
          ],
          [
            62,
            -0.09419980911094475
          ],
          [
            69,
            -0.09419999857057179
          ]
        ]
      },
      {
        "name": "H Dubai peak_core min, \u03b5 [0.05,0.99]",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            39.4982
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-J Dubai Jul peak core, atol 0.001",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.09278758011367416
          ],
          [
            31,
            -0.09278758011367416
          ],
          [
            41,
            -0.0938973496265207
          ],
          [
            48,
            -0.09419968736141374
          ],
          [
            55,
            -0.09419968736141374
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-I Lhasa Jul material demand seed 5",
        "multiplier": 10,
        "seed": 5,
        "curve": [
          [
            41,
            3.6653589139606555
          ],
          [
            61,
            3.4199656532811797
          ],
          [
            81,
            2.9414455669467836
          ],
          [
            101,
            2.9414455669467836
          ],
          [
            121,
            2.9414455669467836
          ],
          [
            141,
            2.9414455669467836
          ],
          [
            161,
            2.9414455669467836
          ],
          [
            180,
            2.9414455669467836
          ],
          [
            200,
            2.8795337866376847
          ],
          [
            220,
            2.8644898713114877
          ],
          [
            240,
            2.8644898713114877
          ],
          [
            260,
            2.849701745678628
          ],
          [
            279,
            2.849701745678628
          ],
          [
            299,
            2.8404467289653343
          ],
          [
            319,
            2.8190808087408294
          ],
          [
            339,
            2.8190808087408294
          ],
          [
            358,
            2.8190808087408294
          ],
          [
            378,
            2.8190808087408294
          ],
          [
            397,
            2.8190808087408294
          ],
          [
            415,
            2.8190808087408294
          ],
          [
            435,
            2.815350993908771
          ],
          [
            455,
            2.812602264753319
          ],
          [
            475,
            2.812602264753319
          ],
          [
            495,
            2.811780356579539
          ],
          [
            515,
            2.811780356579539
          ],
          [
            535,
            2.811780356579539
          ],
          [
            555,
            2.810245307298861
          ],
          [
            575,
            2.810245307298861
          ],
          [
            595,
            2.809904752543535
          ],
          [
            615,
            2.809904752543535
          ]
        ]
      },
      {
        "name": "S10-I Lhasa Jul material demand seed 4",
        "multiplier": 10,
        "seed": 4,
        "curve": [
          [
            41,
            4.167440719884437
          ],
          [
            61,
            3.3276060310085462
          ],
          [
            81,
            3.3276060310085462
          ],
          [
            101,
            3.3276060310085462
          ],
          [
            121,
            3.1343351819145524
          ],
          [
            141,
            3.1343351819145524
          ],
          [
            161,
            2.8506096746178935
          ],
          [
            181,
            2.8506096746178935
          ],
          [
            201,
            2.818945970924694
          ],
          [
            221,
            2.818945970924694
          ],
          [
            241,
            2.818945970924694
          ],
          [
            261,
            2.818945970924694
          ],
          [
            280,
            2.818945970924694
          ],
          [
            300,
            2.818945970924694
          ],
          [
            320,
            2.818155942043432
          ],
          [
            340,
            2.8174647361770067
          ],
          [
            360,
            2.8137867474522853
          ],
          [
            380,
            2.8137867474522853
          ],
          [
            400,
            2.8137867474522853
          ],
          [
            420,
            2.8129160608943353
          ],
          [
            440,
            2.8129160608943353
          ],
          [
            460,
            2.8129160608943353
          ],
          [
            480,
            2.8129160608943353
          ],
          [
            500,
            2.8129160608943353
          ],
          [
            520,
            2.8108666358444214
          ],
          [
            540,
            2.8108666358444214
          ],
          [
            560,
            2.8108666358444214
          ],
          [
            580,
            2.8104522577836946
          ],
          [
            600,
            2.8101970814156427
          ],
          [
            620,
            2.8101970814156427
          ]
        ]
      },
      {
        "name": "S10-I Lhasa Jul material demand seed 3",
        "multiplier": 10,
        "seed": 3,
        "curve": [
          [
            41,
            3.1457771119366464
          ],
          [
            61,
            3.1457771119366464
          ],
          [
            80,
            3.1457771119366464
          ],
          [
            100,
            3.1457771119366464
          ],
          [
            119,
            2.902297824842083
          ],
          [
            139,
            2.902297824842083
          ],
          [
            159,
            2.8723465927469842
          ],
          [
            179,
            2.850199569573795
          ],
          [
            198,
            2.850199569573795
          ],
          [
            218,
            2.850199569573795
          ],
          [
            238,
            2.850199569573795
          ],
          [
            258,
            2.8499661654932256
          ],
          [
            278,
            2.834182681749017
          ],
          [
            298,
            2.834182681749017
          ],
          [
            318,
            2.834182681749017
          ],
          [
            338,
            2.834182681749017
          ],
          [
            358,
            2.834182681749017
          ],
          [
            378,
            2.8308040203882467
          ],
          [
            397,
            2.8308040203882467
          ],
          [
            417,
            2.828673831947568
          ],
          [
            437,
            2.8225439064199254
          ],
          [
            457,
            2.8225439064199254
          ],
          [
            477,
            2.8171947996837496
          ],
          [
            497,
            2.8139162787841996
          ],
          [
            517,
            2.8139162787841996
          ],
          [
            537,
            2.8123514777801932
          ],
          [
            557,
            2.8123514777801932
          ],
          [
            577,
            2.8123514777801932
          ],
          [
            597,
            2.811359107330563
          ],
          [
            617,
            2.8110130229618937
          ]
        ]
      },
      {
        "name": "S10-I Lhasa Jul material demand seed 2",
        "multiplier": 10,
        "seed": 2,
        "curve": [
          [
            41,
            3.409564303255324
          ],
          [
            61,
            3.1232841545810186
          ],
          [
            81,
            2.9284955406835227
          ],
          [
            101,
            2.9284955406835227
          ],
          [
            121,
            2.9284955406835227
          ],
          [
            141,
            2.9284955406835227
          ],
          [
            161,
            2.8664069385067656
          ],
          [
            181,
            2.8334306045948123
          ],
          [
            201,
            2.8334306045948123
          ],
          [
            221,
            2.8334306045948123
          ],
          [
            241,
            2.832155231167287
          ],
          [
            261,
            2.832155231167287
          ],
          [
            281,
            2.832155231167287
          ],
          [
            301,
            2.8301280751798057
          ],
          [
            321,
            2.8225751790086715
          ],
          [
            341,
            2.8225751790086715
          ],
          [
            361,
            2.8140284615126125
          ],
          [
            381,
            2.8140284615126125
          ],
          [
            401,
            2.8140284615126125
          ],
          [
            421,
            2.813083218700646
          ],
          [
            441,
            2.813083218700646
          ],
          [
            461,
            2.8114070172606165
          ],
          [
            481,
            2.8114070172606165
          ],
          [
            501,
            2.81139333218027
          ],
          [
            521,
            2.811378073955975
          ],
          [
            541,
            2.811378073955975
          ],
          [
            561,
            2.8111593650095106
          ],
          [
            580,
            2.81112847557509
          ],
          [
            599,
            2.8103549765273326
          ],
          [
            619,
            2.810098850318873
          ]
        ]
      },
      {
        "name": "S10-I Lhasa Jul material demand seed 1",
        "multiplier": 10,
        "seed": 1,
        "curve": [
          [
            41,
            3.16508068644475
          ],
          [
            61,
            3.16508068644475
          ],
          [
            81,
            2.916888182648968
          ],
          [
            101,
            2.916888182648968
          ],
          [
            120,
            2.916888182648968
          ],
          [
            140,
            2.9064306996749876
          ],
          [
            160,
            2.9064306996749876
          ],
          [
            180,
            2.9064306996749876
          ],
          [
            200,
            2.8995139370649894
          ],
          [
            220,
            2.8905580704631273
          ],
          [
            240,
            2.858017238371102
          ],
          [
            260,
            2.838681827361903
          ],
          [
            280,
            2.838681827361903
          ],
          [
            300,
            2.829073929466268
          ],
          [
            320,
            2.823808161103473
          ],
          [
            340,
            2.8218731556872427
          ],
          [
            360,
            2.8155494671225947
          ],
          [
            380,
            2.815467677253977
          ],
          [
            400,
            2.815467677253977
          ],
          [
            420,
            2.815467677253977
          ],
          [
            440,
            2.815467677253977
          ],
          [
            460,
            2.8119842485464472
          ],
          [
            480,
            2.8118813708365717
          ],
          [
            499,
            2.8108334648779874
          ],
          [
            519,
            2.8108334648779874
          ],
          [
            539,
            2.8104361473324877
          ],
          [
            559,
            2.810342513542326
          ],
          [
            578,
            2.8101958023424314
          ],
          [
            597,
            2.8101958023424314
          ],
          [
            617,
            2.8101958023424314
          ]
        ]
      },
      {
        "name": "S10-I Lhasa Jul material demand seed 42",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            3.476399860869772
          ],
          [
            61,
            3.391572008203582
          ],
          [
            81,
            3.0036016311399805
          ],
          [
            101,
            3.0036016311399805
          ],
          [
            121,
            3.0036016311399805
          ],
          [
            141,
            3.0036016311399805
          ],
          [
            161,
            3.0036016311399805
          ],
          [
            181,
            3.0036016311399805
          ],
          [
            200,
            3.0036016311399805
          ],
          [
            220,
            3.0036016311399805
          ],
          [
            240,
            3.0036016311399805
          ],
          [
            260,
            2.978553131420508
          ],
          [
            280,
            2.978553131420508
          ],
          [
            300,
            2.9154370856229597
          ],
          [
            320,
            2.8597633934291213
          ],
          [
            340,
            2.858188104178963
          ],
          [
            360,
            2.8255393497314367
          ],
          [
            380,
            2.8255393497314367
          ],
          [
            400,
            2.8255393497314367
          ],
          [
            420,
            2.8238872009941556
          ],
          [
            440,
            2.8208313974973787
          ],
          [
            460,
            2.8161741791825956
          ],
          [
            480,
            2.8161741791825956
          ],
          [
            500,
            2.813328151957793
          ],
          [
            520,
            2.8116910994534283
          ],
          [
            540,
            2.8116910994534283
          ],
          [
            560,
            2.8116910994534283
          ],
          [
            580,
            2.8116910994534283
          ],
          [
            600,
            2.8116910994534283
          ],
          [
            620,
            2.8116910994534283
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-H2 Dubai Jul selective, MRT = air",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            61,
            1001.0325
          ],
          [
            91,
            1001.0105
          ],
          [
            121,
            1000.9834
          ],
          [
            151,
            1000.9539
          ],
          [
            181,
            1000.9539
          ],
          [
            211,
            1000.9539
          ],
          [
            241,
            1000.9297
          ],
          [
            271,
            1000.9297
          ],
          [
            301,
            1000.9297
          ],
          [
            331,
            1000.9297
          ],
          [
            361,
            1000.9145
          ],
          [
            391,
            1000.9094
          ],
          [
            421,
            1000.9094
          ],
          [
            451,
            1000.9094
          ],
          [
            481,
            1000.9076
          ],
          [
            511,
            1000.9076
          ],
          [
            541,
            1000.9076
          ],
          [
            571,
            1000.9048
          ],
          [
            601,
            1000.9048
          ],
          [
            631,
            1000.9048
          ],
          [
            661,
            1000.9048
          ],
          [
            691,
            1000.9048
          ],
          [
            721,
            1000.9046
          ],
          [
            751,
            1000.9046
          ],
          [
            781,
            1000.9032
          ],
          [
            811,
            1000.9032
          ],
          [
            841,
            1000.9032
          ],
          [
            871,
            1000.9032
          ],
          [
            901,
            1000.9032
          ],
          [
            931,
            1000.9032
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-H1 Dubai Jul selective, MRT air+solar",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            61,
            1001.1078
          ],
          [
            91,
            1001.1078
          ],
          [
            121,
            1001.0816
          ],
          [
            151,
            1001.0816
          ],
          [
            181,
            1001.0816
          ],
          [
            211,
            1001.0665
          ],
          [
            241,
            1001.0665
          ],
          [
            271,
            1001.0665
          ],
          [
            301,
            1001.0665
          ],
          [
            331,
            1001.0665
          ],
          [
            361,
            1001.0665
          ],
          [
            391,
            1001.0665
          ],
          [
            421,
            1001.0665
          ],
          [
            451,
            1001.0621
          ],
          [
            481,
            1001.0621
          ],
          [
            511,
            1001.0621
          ],
          [
            541,
            1001.0621
          ],
          [
            571,
            1001.0615
          ],
          [
            601,
            1001.0599
          ],
          [
            631,
            1001.0577
          ],
          [
            661,
            1001.0577
          ],
          [
            691,
            1001.0577
          ],
          [
            721,
            1001.0561
          ],
          [
            751,
            1001.0553
          ],
          [
            781,
            1001.0553
          ],
          [
            811,
            1001.0553
          ],
          [
            841,
            1001.0553
          ],
          [
            871,
            1001.0548
          ],
          [
            901,
            1001.0547
          ],
          [
            931,
            1001.0546
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-G2 Dubai Jul gray eps, MRT = air",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.006403277494512426
          ],
          [
            31,
            -0.006403277494512426
          ],
          [
            41,
            -0.006403277494512426
          ],
          [
            50,
            -0.00640341976569752
          ],
          [
            60,
            -0.007000141199377919
          ],
          [
            70,
            -0.007000141199377919
          ],
          [
            80,
            -0.007000141199377919
          ],
          [
            90,
            -0.007000220847948639
          ],
          [
            100,
            -0.007000220847948639
          ],
          [
            110,
            -0.007000220847948639
          ],
          [
            120,
            -0.007000220847948639
          ],
          [
            130,
            -0.007000255878689288
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-F2 Guangzhou Aug degree-hours",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            1000.0788
          ],
          [
            61,
            1000.0234
          ],
          [
            80,
            1000.0234
          ],
          [
            100,
            1000.003
          ],
          [
            119,
            1000.003
          ],
          [
            139,
            1000.003
          ],
          [
            159,
            1000.003
          ],
          [
            179,
            1000.003
          ],
          [
            199,
            1000.003
          ],
          [
            219,
            1000.003
          ],
          [
            239,
            1000.003
          ],
          [
            259,
            -0.6345921643162162
          ],
          [
            279,
            -0.6345921643162162
          ],
          [
            299,
            -0.6345921643162162
          ],
          [
            318,
            -0.636103547256715
          ],
          [
            338,
            -0.636103547256715
          ],
          [
            358,
            -0.636103547256715
          ],
          [
            378,
            -0.6370462244620663
          ],
          [
            398,
            -0.6370462244620663
          ],
          [
            418,
            -0.6370462244620663
          ],
          [
            438,
            -0.6381841199483019
          ],
          [
            458,
            -0.6381920543707787
          ],
          [
            478,
            -0.6381920543707787
          ],
          [
            498,
            -0.6382000090259227
          ],
          [
            518,
            -0.6382000090259227
          ],
          [
            538,
            -0.6382000090259227
          ],
          [
            558,
            -0.6382000090259227
          ],
          [
            578,
            -0.6382000090259227
          ],
          [
            598,
            -0.6382000090259227
          ],
          [
            618,
            -0.6382740139242866
          ]
        ]
      }
    ],
    [
      {
        "name": "S10-F1 Guangzhou Aug exceedance (rerun Exp-B)",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            1008.42042
          ],
          [
            61,
            1008.34417
          ],
          [
            80,
            1008.34417
          ],
          [
            100,
            1008.31852
          ],
          [
            119,
            1008.31852
          ],
          [
            139,
            1008.31852
          ],
          [
            159,
            1008.31852
          ],
          [
            179,
            1008.31852
          ],
          [
            199,
            1008.31852
          ],
          [
            219,
            1008.31852
          ],
          [
            239,
            1008.31852
          ],
          [
            259,
            1008.31464
          ],
          [
            279,
            1008.31464
          ],
          [
            299,
            1008.31464
          ],
          [
            318,
            1008.31456
          ],
          [
            338,
            1008.31456
          ],
          [
            358,
            1008.31456
          ],
          [
            378,
            1008.31449
          ],
          [
            398,
            1008.31447
          ],
          [
            418,
            1008.31443
          ],
          [
            438,
            1008.3144
          ],
          [
            458,
            1008.3144
          ],
          [
            478,
            1008.3144
          ],
          [
            498,
            1008.3144
          ],
          [
            518,
            1008.31439
          ],
          [
            538,
            1008.31437
          ]
        ]
      },
      {
        "name": "Exp-E Guangzhou mult=20",
        "multiplier": 20,
        "seed": 42,
        "curve": [
          [
            81,
            856.0663339999966
          ],
          [
            121,
            856.0663339999966
          ],
          [
            161,
            851.7379060000022
          ],
          [
            201,
            851.7379060000022
          ],
          [
            241,
            835.100569000001
          ],
          [
            281,
            834.3505189999992
          ],
          [
            321,
            834.3505189999992
          ],
          [
            361,
            832.4575259999999
          ],
          [
            401,
            832.4575259999999
          ],
          [
            441,
            832.4575259999999
          ],
          [
            481,
            832.4575259999999
          ],
          [
            521,
            832.3944630000001
          ],
          [
            561,
            832.3944630000001
          ],
          [
            601,
            832.3944630000001
          ],
          [
            641,
            832.3854540000001
          ],
          [
            681,
            832.37144
          ],
          [
            721,
            832.37144
          ],
          [
            761,
            832.37144
          ],
          [
            801,
            832.37144
          ],
          [
            841,
            832.37144
          ],
          [
            881,
            832.37144
          ],
          [
            921,
            832.37144
          ]
        ]
      },
      {
        "name": "Exp-E Guangzhou mult=10",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            913.8961620000011
          ],
          [
            61,
            856.4090770000024
          ],
          [
            80,
            856.4090770000024
          ],
          [
            100,
            835.4835520000001
          ],
          [
            119,
            835.4835520000001
          ],
          [
            139,
            835.4835520000001
          ],
          [
            159,
            835.4835520000001
          ],
          [
            179,
            835.4835520000001
          ],
          [
            199,
            835.4835520000001
          ],
          [
            219,
            835.4835520000001
          ],
          [
            239,
            835.4835520000001
          ],
          [
            259,
            832.395464
          ],
          [
            279,
            832.395464
          ],
          [
            299,
            832.395464
          ],
          [
            318,
            832.387456
          ],
          [
            338,
            832.387456
          ],
          [
            358,
            832.387456
          ],
          [
            378,
            832.380449
          ],
          [
            398,
            832.378447
          ]
        ]
      },
      {
        "name": "Exp-E Guangzhou mult=5",
        "multiplier": 5,
        "seed": 42,
        "curve": [
          [
            21,
            889.8420090000011
          ],
          [
            31,
            877.0468140000022
          ],
          [
            40,
            877.0468140000022
          ],
          [
            50,
            877.0468140000022
          ],
          [
            60,
            877.0468140000022
          ],
          [
            70,
            877.0468140000022
          ],
          [
            80,
            877.0468140000022
          ],
          [
            90,
            834.9655339999978
          ],
          [
            100,
            834.9655339999978
          ],
          [
            110,
            833.3325010000016
          ],
          [
            120,
            833.3325010000016
          ],
          [
            130,
            833.3325010000016
          ],
          [
            140,
            833.3325010000016
          ],
          [
            150,
            833.3325010000016
          ],
          [
            159,
            833.3325010000016
          ],
          [
            169,
            833.3325010000016
          ],
          [
            179,
            833.3325010000016
          ],
          [
            189,
            832.419488
          ],
          [
            199,
            832.4144829999999
          ],
          [
            209,
            832.4144829999999
          ],
          [
            219,
            832.4144829999999
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=5",
        "multiplier": 10,
        "seed": 5,
        "curve": [
          [
            40,
            896.7895560000005
          ],
          [
            60,
            847.1709389999987
          ],
          [
            80,
            846.0388070000012
          ],
          [
            100,
            845.3557240000024
          ],
          [
            120,
            832.465534
          ],
          [
            140,
            832.465534
          ],
          [
            160,
            832.465534
          ],
          [
            180,
            832.413482
          ],
          [
            200,
            832.413482
          ],
          [
            220,
            832.3854540000001
          ],
          [
            240,
            832.3854540000001
          ],
          [
            260,
            832.3854540000001
          ],
          [
            280,
            832.376445
          ],
          [
            300,
            832.37144
          ],
          [
            320,
            832.37144
          ],
          [
            340,
            832.37144
          ],
          [
            360,
            832.37144
          ],
          [
            380,
            832.37144
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=4",
        "multiplier": 10,
        "seed": 4,
        "curve": [
          [
            41,
            880.2294969999975
          ],
          [
            61,
            880.2294969999975
          ],
          [
            81,
            880.2294969999975
          ],
          [
            101,
            837.4636319999993
          ],
          [
            121,
            837.4376059999993
          ],
          [
            141,
            837.4376059999993
          ],
          [
            161,
            837.4376059999993
          ],
          [
            181,
            834.4175859999992
          ],
          [
            201,
            833.0965649999986
          ],
          [
            221,
            832.5725410000033
          ],
          [
            240,
            832.387456
          ],
          [
            259,
            832.387456
          ],
          [
            279,
            832.387456
          ],
          [
            298,
            832.387456
          ],
          [
            318,
            832.387456
          ],
          [
            338,
            832.387456
          ],
          [
            358,
            832.3854540000001
          ],
          [
            378,
            832.3814500000001
          ],
          [
            398,
            832.373442
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=3",
        "multiplier": 10,
        "seed": 3,
        "curve": [
          [
            41,
            847.444713000001
          ],
          [
            61,
            847.444713000001
          ],
          [
            81,
            847.444713000001
          ],
          [
            101,
            836.2016699999988
          ],
          [
            121,
            836.2016699999988
          ],
          [
            141,
            836.2016699999988
          ],
          [
            161,
            836.2016699999988
          ],
          [
            181,
            834.713582000002
          ],
          [
            201,
            834.713582000002
          ],
          [
            221,
            834.713582000002
          ],
          [
            241,
            832.4254940000001
          ],
          [
            261,
            832.4254940000001
          ],
          [
            281,
            832.413482
          ],
          [
            301,
            832.413482
          ],
          [
            321,
            832.404473
          ],
          [
            341,
            832.397466
          ],
          [
            361,
            832.3894580000001
          ],
          [
            380,
            832.3754440000001
          ],
          [
            399,
            832.3754440000001
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=2",
        "multiplier": 10,
        "seed": 2,
        "curve": [
          [
            41,
            885.0625300000006
          ],
          [
            61,
            866.7189869999995
          ],
          [
            81,
            855.6209890000005
          ],
          [
            101,
            855.6209890000005
          ],
          [
            121,
            855.6209890000005
          ],
          [
            141,
            855.6209890000005
          ],
          [
            161,
            855.6209890000005
          ],
          [
            181,
            843.3087769999967
          ],
          [
            201,
            839.2487169999989
          ],
          [
            221,
            839.0046729999993
          ],
          [
            241,
            832.387456
          ],
          [
            261,
            832.387456
          ],
          [
            281,
            832.387456
          ],
          [
            301,
            832.387456
          ],
          [
            321,
            832.387456
          ],
          [
            341,
            832.387456
          ],
          [
            361,
            832.387456
          ],
          [
            381,
            832.3854540000001
          ],
          [
            401,
            832.374443
          ]
        ]
      },
      {
        "name": "Exp-D Guangzhou seed=1",
        "multiplier": 10,
        "seed": 1,
        "curve": [
          [
            41,
            885.1262929999987
          ],
          [
            61,
            855.9562239999967
          ],
          [
            81,
            851.8961639999987
          ],
          [
            101,
            845.8408090000015
          ],
          [
            121,
            843.4737420000032
          ],
          [
            141,
            837.6216900000026
          ],
          [
            161,
            837.6216900000026
          ],
          [
            181,
            832.3944630000001
          ],
          [
            201,
            832.3944630000001
          ],
          [
            221,
            832.3944630000001
          ],
          [
            241,
            832.3944630000001
          ],
          [
            261,
            832.3944630000001
          ],
          [
            281,
            832.3944630000001
          ],
          [
            301,
            832.387456
          ],
          [
            321,
            832.3814500000001
          ],
          [
            341,
            832.3814500000001
          ]
        ]
      },
      {
        "name": "Exp-B Guangzhou skin_exceedance \u2264 0.1 + peak_core \u2264 38",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            913.8961620000011
          ],
          [
            61,
            856.4090770000024
          ],
          [
            80,
            856.4090770000024
          ],
          [
            100,
            835.4835520000001
          ],
          [
            119,
            835.4835520000001
          ],
          [
            139,
            835.4835520000001
          ],
          [
            159,
            835.4835520000001
          ],
          [
            179,
            835.4835520000001
          ],
          [
            199,
            835.4835520000001
          ],
          [
            219,
            835.4835520000001
          ],
          [
            239,
            835.4835520000001
          ],
          [
            259,
            832.395464
          ],
          [
            279,
            832.395464
          ],
          [
            299,
            832.395464
          ],
          [
            318,
            832.387456
          ],
          [
            338,
            832.387456
          ],
          [
            358,
            832.387456
          ],
          [
            378,
            832.380449
          ],
          [
            398,
            832.378447
          ]
        ]
      },
      {
        "name": "Guangzhou August requirement search",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            913.8961620000011
          ],
          [
            61,
            856.4090770000024
          ],
          [
            80,
            856.4090770000024
          ],
          [
            100,
            835.4835520000001
          ],
          [
            119,
            835.4835520000001
          ],
          [
            139,
            835.4835520000001
          ],
          [
            159,
            835.4835520000001
          ],
          [
            179,
            835.4835520000001
          ],
          [
            199,
            835.4835520000001
          ],
          [
            219,
            835.4835520000001
          ],
          [
            239,
            835.4835520000001
          ],
          [
            259,
            832.395464
          ],
          [
            279,
            832.395464
          ],
          [
            299,
            832.395464
          ],
          [
            318,
            832.387456
          ],
          [
            338,
            832.387456
          ],
          [
            358,
            832.387456
          ],
          [
            378,
            832.380449
          ],
          [
            398,
            832.378447
          ]
        ]
      }
    ],
    [
      {
        "name": "J-tol-1e-4-b",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            1004.099012
          ],
          [
            31,
            1004.099012
          ],
          [
            41,
            1004.099012
          ],
          [
            50,
            1004.099012
          ],
          [
            60,
            1004.099006
          ],
          [
            70,
            1004.098788
          ],
          [
            80,
            1004.098602
          ],
          [
            90,
            1004.098386
          ],
          [
            100,
            1004.098274
          ],
          [
            109,
            1004.098274
          ],
          [
            119,
            1004.098268
          ]
        ]
      }
    ],
    [
      {
        "name": "J-tol-1e-5",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            1004.099012
          ],
          [
            31,
            1004.099012
          ],
          [
            41,
            1004.099012
          ],
          [
            50,
            1004.099012
          ],
          [
            60,
            1004.099006
          ],
          [
            70,
            1004.098788
          ],
          [
            80,
            1004.098602
          ],
          [
            90,
            1004.098386
          ],
          [
            100,
            1004.098274
          ],
          [
            109,
            1004.098274
          ],
          [
            119,
            1004.098268
          ],
          [
            129,
            1004.098268
          ],
          [
            138,
            1004.098268
          ],
          [
            148,
            1004.098268
          ]
        ]
      }
    ],
    [
      {
        "name": "J-tol-1e-4",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            0.12419886329825881
          ],
          [
            31,
            0.12419886329825881
          ],
          [
            41,
            0.02650373477167746
          ],
          [
            48,
            0.003126385869926268
          ],
          [
            55,
            0.003126385869926268
          ],
          [
            62,
            0.0019088905598226096
          ],
          [
            69,
            1.4294289389337618e-05
          ],
          [
            79,
            1.4294289389337618e-05
          ],
          [
            87,
            1.4294289389337618e-05
          ],
          [
            95,
            1.4294289389337618e-05
          ],
          [
            100,
            1.4294289389337618e-05
          ],
          [
            106,
            1.4294289389337618e-05
          ],
          [
            112,
            1.3417167359001636e-05
          ]
        ]
      }
    ],
    [
      {
        "name": "I-Lhasa-min-demand-seed-6",
        "multiplier": 10,
        "seed": 6,
        "curve": [
          [
            41,
            2.725480144698141
          ],
          [
            61,
            1.598835370531701
          ],
          [
            81,
            1.5478510981423146
          ],
          [
            101,
            1.5478510981423146
          ],
          [
            121,
            1.5478510981423146
          ],
          [
            140,
            1.5369202950974914
          ],
          [
            160,
            1.465948708721182
          ],
          [
            180,
            1.3675561438005515
          ],
          [
            200,
            1.3634688732763527
          ],
          [
            220,
            1.3634688732763527
          ],
          [
            240,
            1.3634688732763527
          ],
          [
            260,
            1.3634688732763527
          ],
          [
            280,
            1.3634688732763527
          ],
          [
            300,
            1.339794197141067
          ],
          [
            320,
            1.339794197141067
          ],
          [
            340,
            1.3306093445884033
          ],
          [
            360,
            1.3306093445884033
          ],
          [
            380,
            1.3306093445884033
          ],
          [
            400,
            1.3306093445884033
          ],
          [
            420,
            1.3306093445884033
          ],
          [
            440,
            1.3297571142457987
          ],
          [
            460,
            1.3291632894734318
          ],
          [
            480,
            1.3291632894734318
          ],
          [
            500,
            1.3287215096567502
          ],
          [
            520,
            1.3287215096567502
          ],
          [
            540,
            1.3287215096567502
          ],
          [
            560,
            1.3287215096567502
          ],
          [
            580,
            1.3284476752662768
          ],
          [
            600,
            1.3281794657026815
          ],
          [
            620,
            1.3281794657026815
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-5",
        "multiplier": 10,
        "seed": 5,
        "curve": [
          [
            41,
            1.5292830036810803
          ],
          [
            61,
            1.5292830036810803
          ],
          [
            81,
            1.5292830036810803
          ],
          [
            101,
            1.5292830036810803
          ],
          [
            121,
            1.4607648156879218
          ],
          [
            141,
            1.4607648156879218
          ],
          [
            161,
            1.4607648156879218
          ],
          [
            181,
            1.4171332085650026
          ],
          [
            201,
            1.4171332085650026
          ],
          [
            221,
            1.3728744617458266
          ],
          [
            240,
            1.3728744617458266
          ],
          [
            260,
            1.361810141718447
          ],
          [
            279,
            1.3536817243271273
          ],
          [
            299,
            1.3468589721727313
          ],
          [
            319,
            1.3386054717959472
          ],
          [
            339,
            1.3386054717959472
          ],
          [
            358,
            1.3343128841499385
          ],
          [
            378,
            1.3307640871083941
          ],
          [
            397,
            1.3307640871083941
          ],
          [
            416,
            1.3307640871083941
          ],
          [
            436,
            1.3307640871083941
          ],
          [
            456,
            1.3307640871083941
          ],
          [
            476,
            1.3303804838488786
          ],
          [
            496,
            1.3299043303075035
          ],
          [
            516,
            1.3299043303075035
          ],
          [
            536,
            1.3295923702657089
          ],
          [
            556,
            1.328056453426605
          ],
          [
            576,
            1.328056453426605
          ],
          [
            596,
            1.3278584691055884
          ],
          [
            616,
            1.3278584691055884
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-4",
        "multiplier": 10,
        "seed": 4,
        "curve": [
          [
            41,
            1.729880422247806
          ],
          [
            61,
            1.6799872040850212
          ],
          [
            81,
            1.6799872040850212
          ],
          [
            101,
            1.6547900846508197
          ],
          [
            121,
            1.6437144237757906
          ],
          [
            141,
            1.623616521621123
          ],
          [
            161,
            1.623616521621123
          ],
          [
            181,
            1.5641344168798426
          ],
          [
            201,
            1.3559318642132812
          ],
          [
            221,
            1.3559318642132812
          ],
          [
            241,
            1.3559318642132812
          ],
          [
            261,
            1.3419121720792855
          ],
          [
            281,
            1.3419121720792855
          ],
          [
            301,
            1.3320194322777945
          ],
          [
            321,
            1.3320194322777945
          ],
          [
            341,
            1.3320194322777945
          ],
          [
            361,
            1.3320194322777945
          ],
          [
            381,
            1.3320194322777945
          ],
          [
            401,
            1.3300724140689446
          ],
          [
            421,
            1.3290957659648432
          ],
          [
            441,
            1.3289414245448143
          ],
          [
            461,
            1.3289414245448143
          ],
          [
            481,
            1.3282399626102788
          ],
          [
            501,
            1.3280759133480309
          ],
          [
            520,
            1.3280759133480309
          ],
          [
            540,
            1.3280143179772
          ],
          [
            560,
            1.3280143179772
          ],
          [
            578,
            1.3280143179772
          ],
          [
            598,
            1.327990757817316
          ],
          [
            618,
            1.3279587323065796
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-3",
        "multiplier": 10,
        "seed": 3,
        "curve": [
          [
            41,
            1.8527381509754774
          ],
          [
            60,
            1.8527381509754774
          ],
          [
            80,
            1.4154372964864161
          ],
          [
            99,
            1.4154372964864161
          ],
          [
            118,
            1.3691064459319628
          ],
          [
            138,
            1.3691064459319628
          ],
          [
            158,
            1.3691064459319628
          ],
          [
            177,
            1.3691064459319628
          ],
          [
            197,
            1.3691064459319628
          ],
          [
            217,
            1.345921601140767
          ],
          [
            237,
            1.345921601140767
          ],
          [
            256,
            1.3330455565885628
          ],
          [
            276,
            1.3293164099520034
          ],
          [
            296,
            1.3293164099520034
          ],
          [
            316,
            1.3293164099520034
          ],
          [
            336,
            1.3293164099520034
          ],
          [
            356,
            1.3293164099520034
          ],
          [
            376,
            1.3293164099520034
          ],
          [
            396,
            1.3281384448367912
          ],
          [
            416,
            1.3281384448367912
          ],
          [
            436,
            1.3281384448367912
          ],
          [
            456,
            1.3281384448367912
          ],
          [
            476,
            1.3281384448367912
          ],
          [
            496,
            1.327807766946713
          ],
          [
            516,
            1.327807766946713
          ],
          [
            536,
            1.327807766946713
          ],
          [
            555,
            1.327787456200275
          ],
          [
            574,
            1.327787456200275
          ],
          [
            594,
            1.327787456200275
          ],
          [
            613,
            1.327787456200275
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-2",
        "multiplier": 10,
        "seed": 2,
        "curve": [
          [
            41,
            1.5664646926005046
          ],
          [
            61,
            1.5664646926005046
          ],
          [
            81,
            1.5664646926005046
          ],
          [
            101,
            1.5664646926005046
          ],
          [
            121,
            1.5664646926005046
          ],
          [
            141,
            1.4719367335876792
          ],
          [
            161,
            1.3822842548434382
          ],
          [
            181,
            1.3822842548434382
          ],
          [
            201,
            1.3822842548434382
          ],
          [
            220,
            1.3822842548434382
          ],
          [
            240,
            1.3822842548434382
          ],
          [
            260,
            1.3781904250433226
          ],
          [
            280,
            1.3680592186835276
          ],
          [
            300,
            1.351534187048356
          ],
          [
            320,
            1.3350660871380085
          ],
          [
            340,
            1.3350660871380085
          ],
          [
            360,
            1.3348799081452878
          ],
          [
            379,
            1.3348799081452878
          ],
          [
            399,
            1.330306471618344
          ],
          [
            419,
            1.330306471618344
          ],
          [
            439,
            1.3283548384395156
          ],
          [
            459,
            1.3283548384395156
          ],
          [
            479,
            1.327928722651613
          ],
          [
            498,
            1.327928722651613
          ],
          [
            518,
            1.327928722651613
          ],
          [
            538,
            1.327928722651613
          ],
          [
            558,
            1.327928722651613
          ],
          [
            577,
            1.327928722651613
          ],
          [
            597,
            1.3278826544129452
          ],
          [
            617,
            1.3278582904823035
          ]
        ]
      },
      {
        "name": "I-Lhasa-min-demand-seed-1",
        "multiplier": 10,
        "seed": 1,
        "curve": [
          [
            41,
            1.8118347063681985
          ],
          [
            61,
            1.7758508943555684
          ],
          [
            81,
            1.5007268420767232
          ],
          [
            100,
            1.5007268420767232
          ],
          [
            120,
            1.4122775078159184
          ],
          [
            140,
            1.4122775078159184
          ],
          [
            160,
            1.4122775078159184
          ],
          [
            180,
            1.3817195153238748
          ],
          [
            200,
            1.3817195153238748
          ],
          [
            220,
            1.3817195153238748
          ],
          [
            240,
            1.3577050714747463
          ],
          [
            260,
            1.3577050714747463
          ],
          [
            280,
            1.3577050714747463
          ],
          [
            300,
            1.3577050714747463
          ],
          [
            319,
            1.3577050714747463
          ],
          [
            339,
            1.3577050714747463
          ],
          [
            359,
            1.3577050714747463
          ],
          [
            378,
            1.3485231072777852
          ],
          [
            397,
            1.3397171477488845
          ],
          [
            416,
            1.3397171477488845
          ],
          [
            436,
            1.3373984308259703
          ],
          [
            456,
            1.3324943879126787
          ],
          [
            476,
            1.3324943879126787
          ],
          [
            496,
            1.3317163027859131
          ],
          [
            516,
            1.3294027261203512
          ],
          [
            536,
            1.3294027261203512
          ],
          [
            556,
            1.3294027261203512
          ],
          [
            576,
            1.3284983396148815
          ],
          [
            595,
            1.3284983396148815
          ],
          [
            615,
            1.3279349382132637
          ]
        ]
      }
    ],
    [
      {
        "name": "H2 - Jul",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            61,
            1007.756422
          ],
          [
            91,
            1007.562784
          ],
          [
            120,
            1007.51585
          ],
          [
            150,
            1007.51585
          ],
          [
            180,
            1007.432442
          ],
          [
            210,
            1007.307522
          ],
          [
            240,
            1007.307522
          ],
          [
            270,
            1007.307522
          ],
          [
            300,
            1007.295212
          ],
          [
            330,
            1007.286162
          ],
          [
            360,
            1007.260034
          ],
          [
            390,
            1007.258342
          ],
          [
            420,
            1007.247392
          ],
          [
            450,
            1007.218202
          ],
          [
            480,
            1007.212878
          ],
          [
            510,
            1007.212878
          ],
          [
            539,
            1007.2096
          ],
          [
            569,
            1007.2096
          ],
          [
            599,
            1007.201024
          ],
          [
            629,
            1007.201024
          ],
          [
            659,
            1007.201024
          ],
          [
            689,
            1007.198248
          ],
          [
            719,
            1007.198248
          ],
          [
            749,
            1007.197504
          ],
          [
            779,
            1007.197504
          ],
          [
            809,
            1007.197504
          ],
          [
            839,
            1007.197504
          ],
          [
            869,
            1007.197504
          ],
          [
            899,
            1007.197504
          ],
          [
            929,
            1007.197504
          ]
        ]
      }
    ],
    [
      {
        "name": "H1 -  Aug",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            61,
            1007.962926
          ],
          [
            91,
            1007.962926
          ],
          [
            121,
            1007.86505
          ],
          [
            151,
            1007.86505
          ],
          [
            181,
            1007.86505
          ],
          [
            211,
            1007.805542
          ],
          [
            241,
            1007.805542
          ],
          [
            271,
            1007.805542
          ],
          [
            301,
            1007.805542
          ],
          [
            331,
            1007.805542
          ],
          [
            361,
            1007.805542
          ],
          [
            391,
            1007.805542
          ],
          [
            421,
            1007.805542
          ],
          [
            451,
            1007.805542
          ],
          [
            481,
            1007.80406
          ],
          [
            511,
            1007.795122
          ],
          [
            541,
            1007.793032
          ],
          [
            571,
            1007.781754
          ],
          [
            601,
            1007.777556
          ],
          [
            631,
            1007.777556
          ],
          [
            661,
            1007.775496
          ],
          [
            691,
            1007.77518
          ],
          [
            721,
            1007.76721
          ],
          [
            751,
            1007.766408
          ],
          [
            781,
            1007.766408
          ],
          [
            811,
            1007.766398
          ],
          [
            841,
            1007.762224
          ],
          [
            871,
            1007.762224
          ],
          [
            901,
            1007.762206
          ],
          [
            931,
            1007.762206
          ]
        ]
      }
    ],
    [
      {
        "name": "G2 - Equal to air (shaded)",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.028599277494516084
          ],
          [
            31,
            -0.028599277494516084
          ],
          [
            41,
            -0.028599277494516084
          ],
          [
            50,
            -0.028599277494516084
          ],
          [
            60,
            -0.02864318981492294
          ],
          [
            70,
            -0.029294336729074406
          ],
          [
            80,
            -0.029917516249253807
          ],
          [
            90,
            -0.030502763497541354
          ],
          [
            100,
            -0.030984115447982748
          ],
          [
            110,
            -0.03098411712512213
          ],
          [
            120,
            -0.030994095917564895
          ],
          [
            130,
            -0.031022045106164593
          ],
          [
            139,
            -0.03102205148363758
          ]
        ]
      }
    ],
    [
      {
        "name": "G1 - Air + linear solar gain",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            21,
            -0.23980558011366981
          ],
          [
            31,
            -0.23980558011366981
          ],
          [
            41,
            -0.24271134962652227
          ],
          [
            48,
            -0.24336568736141298
          ],
          [
            55,
            -0.24336568736141298
          ],
          [
            62,
            -0.24340580911094425
          ],
          [
            69,
            -0.24346999857057136
          ]
        ]
      }
    ],
    [
      {
        "name": "F2-degree-hours-gradient",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            1003.568282
          ],
          [
            61,
            1003.36176
          ],
          [
            80,
            1003.36176
          ],
          [
            100,
            1003.276918
          ],
          [
            119,
            1003.276918
          ],
          [
            139,
            1003.276918
          ],
          [
            159,
            1003.276918
          ],
          [
            179,
            1003.276918
          ],
          [
            199,
            1003.276918
          ],
          [
            219,
            1003.276918
          ],
          [
            239,
            1003.275298
          ],
          [
            259,
            1003.26127
          ],
          [
            279,
            1003.26127
          ],
          [
            299,
            1003.26127
          ],
          [
            319,
            1003.26127
          ]
        ]
      }
    ],
    [
      {
        "name": "F1-infeasible-out-of-reach",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            1009.437382
          ],
          [
            61,
            1009.17116
          ],
          [
            80,
            1009.17116
          ],
          [
            100,
            1009.062618
          ],
          [
            119,
            1009.062618
          ],
          [
            139,
            1009.062618
          ],
          [
            159,
            1009.062618
          ],
          [
            179,
            1009.062618
          ],
          [
            199,
            1009.062618
          ],
          [
            219,
            1009.062618
          ],
          [
            239,
            1009.060598
          ],
          [
            259,
            1009.04257
          ],
          [
            279,
            1009.04257
          ],
          [
            299,
            1009.04257
          ],
          [
            319,
            1009.04257
          ],
          [
            339,
            1009.041766
          ],
          [
            359,
            1009.033464
          ],
          [
            379,
            1009.033464
          ],
          [
            399,
            1009.031698
          ],
          [
            419,
            1009.031698
          ],
          [
            439,
            1009.031698
          ],
          [
            458,
            1009.031698
          ],
          [
            478,
            1009.031698
          ],
          [
            497,
            1009.031698
          ],
          [
            516,
            1009.031698
          ],
          [
            536,
            1009.031698
          ],
          [
            556,
            1009.031698
          ],
          [
            576,
            1009.031698
          ],
          [
            596,
            1009.031698
          ],
          [
            616,
            1009.031564
          ]
        ]
      }
    ],
    [
      {
        "name": "L-W \u62c9\u85a9\u6b0a\u91cd 2:1 / 1:2",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ],
          [
            121,
            0.0
          ]
        ]
      }
    ],
    [
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 5",
        "multiplier": 10,
        "seed": 5,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ]
        ]
      },
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 4",
        "multiplier": 10,
        "seed": 4,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ]
        ]
      },
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 3",
        "multiplier": 10,
        "seed": 3,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ]
        ]
      },
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 2",
        "multiplier": 10,
        "seed": 2,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ]
        ]
      },
      {
        "name": "Exp-C Lhasa July skin_exceedance \u2264 0.1 + peak_core \u2264 38",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            40,
            0.0
          ],
          [
            59,
            0.0
          ],
          [
            79,
            0.0
          ]
        ]
      }
    ],
    [
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09seed 1",
        "multiplier": 10,
        "seed": 1,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            100,
            0.0
          ],
          [
            120,
            0.0
          ],
          [
            140,
            0.0
          ],
          [
            160,
            0.0
          ]
        ]
      }
    ],
    [
      {
        "name": "L \u62c9\u85a9\uff1a\u6700\u4f4e\u9700\u6c42\uff08parameter_demand\uff0c\u6b0a\u91cd 1:1\uff09",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            0.0
          ],
          [
            61,
            0.0
          ],
          [
            81,
            0.0
          ],
          [
            101,
            0.0
          ],
          [
            121,
            0.0
          ]
        ]
      }
    ],
    [
      {
        "name": "Exp-C Dubai July skin_exceedance \u2264 0.1 + peak_core \u2264 38",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            2208.255085000003
          ],
          [
            61,
            2208.255085000003
          ],
          [
            81,
            2178.0948249999983
          ],
          [
            101,
            2161.7336640000003
          ],
          [
            121,
            2161.7336640000003
          ],
          [
            141,
            2161.7336640000003
          ],
          [
            161,
            2158.2036339999977
          ],
          [
            181,
            2157.297628000003
          ],
          [
            201,
            2154.674605000002
          ],
          [
            221,
            2154.572602999999
          ],
          [
            241,
            2154.572602999999
          ],
          [
            261,
            2154.572602999999
          ],
          [
            281,
            2152.5525829999965
          ],
          [
            300,
            2152.5525829999965
          ],
          [
            320,
            2152.2495800000006
          ],
          [
            340,
            2152.2495800000006
          ],
          [
            360,
            2152.2495800000006
          ],
          [
            380,
            2151.9475779999984
          ],
          [
            400,
            2151.8465770000016
          ],
          [
            420,
            2151.3405709999993
          ],
          [
            440,
            2151.3405709999993
          ],
          [
            460,
            2151.3405709999993
          ],
          [
            480,
            2151.140571
          ],
          [
            500,
            2151.0385690000035
          ]
        ]
      }
    ],
    [
      {
        "name": "Exp-A Guangzhou peak_skin \u2264 33",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            3083.594161999997
          ],
          [
            61,
            3044.3620770000007
          ],
          [
            80,
            3044.3620770000007
          ],
          [
            100,
            3027.921551999998
          ],
          [
            119,
            3027.921551999998
          ],
          [
            139,
            3027.921551999998
          ],
          [
            159,
            3027.921551999998
          ],
          [
            179,
            3027.921551999998
          ],
          [
            199,
            3027.921551999998
          ],
          [
            219,
            3027.921551999998
          ],
          [
            239,
            3027.5515950000013
          ],
          [
            259,
            3024.7315060000014
          ],
          [
            279,
            3024.7315060000014
          ],
          [
            299,
            3024.7315060000014
          ],
          [
            319,
            3024.7315060000014
          ],
          [
            339,
            3024.5815050000033
          ],
          [
            359,
            3023.0214559999986
          ],
          [
            379,
            3023.0214559999986
          ]
        ]
      }
    ],
    [
      {
        "name": "Guangzhou August requirement search",
        "multiplier": 10,
        "seed": 42,
        "curve": [
          [
            41,
            734.067234
          ],
          [
            61,
            728.749922
          ],
          [
            81,
            720.40959
          ],
          [
            101,
            706.588783
          ],
          [
            121,
            706.588783
          ],
          [
            141,
            706.588783
          ],
          [
            161,
            706.588783
          ],
          [
            181,
            706.588783
          ],
          [
            200,
            706.588783
          ],
          [
            220,
            704.742939
          ],
          [
            240,
            704.742939
          ],
          [
            260,
            704.4246210000001
          ],
          [
            280,
            704.4246210000001
          ],
          [
            300,
            704.312509
          ],
          [
            320,
            704.214411
          ],
          [
            340,
            704.151348
          ],
          [
            360,
            703.9141109999999
          ]
        ]
      }
    ]
  ]
}
```

### File: `backend/docs/acceptance/stage-11-radiant/optimization-summary.md`
```markdown
| name | verdict | best | objective | violation | upper feasible (viol) | min x @ max y | min y @ max x | lower bound binding | plateau |
|---|---|---|---|---|---|---|---|---|---|
| S11-F3 Guangzhou Aug degree-hours, physical env | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.5} | 2.599091 | 0.3354 | False (0.5342) | None | None | False | 0.008264462809917356 |
| S11-H3 Dubai Jul selective, physical env | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.5, 'infrared_emissivity_outside_window': 0.05} | 4.038676 | 1.2582 | False (1.2845) | None | None | False | 0.008264462809917356 |
| S11-G3 Dubai Jul gray eps, physical env, K=40 | unconstrained | {'infrared_emissivity': 0.05} | 39.5111 | 0.0 | True (0.0) | None | None | None | None |
| S11-G3 Dubai Jul gray eps, physical env, K=5 | unconstrained | {'infrared_emissivity': 0.05} | 39.5341 | 0.0 | True (0.0) | None | None | None | None |
| S11-G3 Dubai Jul gray eps, physical env | unconstrained | {'infrared_emissivity': 0.05} | 39.5228 | 0.0 | True (0.0) | None | None | None | None |
| S10-J Dubai Jul peak core, atol 1e-05 | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| S10-J Dubai Jul peak core, atol 0.0001 | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| S10-J Dubai Jul peak core, atol 0.001 | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| S10-I Lhasa Jul material demand seed 5 | feasible | {'solar_reflectance': 0.6821, 'infrared_emissivity': 0.5} | 0.28099027611044414 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 5: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 4 | feasible | {'solar_reflectance': 0.6822, 'infrared_emissivity': 0.5} | 0.28102028811524615 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 4: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 3 | feasible | {'solar_reflectance': 0.6823, 'infrared_emissivity': 0.5} | 0.2811007352941177 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 3: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 2 | feasible | {'solar_reflectance': 0.6821, 'infrared_emissivity': 0.5} | 0.2810093337334935 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 2: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 1 | feasible | {'solar_reflectance': 0.6821, 'infrared_emissivity': 0.5} | 0.28101970288115247 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 1: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 42 | feasible | {'solar_reflectance': 0.6822, 'infrared_emissivity': 0.5002} | 0.28116919267707086 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 42: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-H2 Dubai Jul selective, MRT = air | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.579197 | 0.9026 | False (0.9026) | None | None | False | 0.008264462809917356 |
| S10-H1 Dubai Jul selective, MRT air+solar | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.786867 | 1.0543 | False (1.0543) | None | None | False | 0.008264462809917356 |
| S10-G2 Dubai Jul gray eps, MRT = air | unconstrained | {'infrared_emissivity': 0.9898} | 39.2552 | 0.0 | True (0.0) | None | None | None | None |
| S10-G1 Dubai Jul gray eps, MRT air+solar | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| S10-F2 Guangzhou Aug degree-hours | feasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 2.126385 | 0.0 | True (0.0) | 0.98 | 0.99 | False | 0.008264462809917356 |
| S10-F1 Guangzhou Aug exceedance (rerun Exp-B) | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 0.931436 | 8.31436 | False (8.31436) | None | None | False | 0.008264462809917356 |
| J-tol-1e-4-b | infeasible | {'infrared_emissivity': 0.99} | 2.439081 | 4.098262 | False (4.098262) | None | None | None | None |
| J-tol-1e-5 | infeasible | {'infrared_emissivity': 0.99} | 2.439081 | 4.098262 | False (4.098262) | None | None | None | None |
| J-tol-1e-4 | feasible | {'infrared_emissivity': 0.5} | 0.0 | 0.0 | True (0.0) | None | None | None | None |
| I-Lhasa-min-demand-seed-6 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13281778211284515 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-6: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-5 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13278593937575026 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-5: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-4 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.1327957833133253 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-4: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-3 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13277891656662663 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-3: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-2 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13278631452581038 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-2: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-1 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13279345738295323 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-1: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| H2 - Jul | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.601119 | 7.196338 | False (7.196338) | None | None | False | 0.008264462809917356 |
| H1 -  Aug | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.81147 | 7.75924 | False (7.75924) | None | None | False | 0.008264462809917356 |
| G2 - Equal to air (shaded) | unconstrained | {'infrared_emissivity': 0.99} | 2.375719 | 0.0 | True (0.0) | None | None | None | None |
| G1 - Air + linear solar gain | unconstrained | {'infrared_emissivity': 0.05} | 4.399347 | 0.0 | True (0.0) | None | None | None | None |
| F2-degree-hours-gradient | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 2.126385 | 3.25277 | False (3.25277) | None | None | False | 0.008264462809917356 |
| F1-infeasible-out-of-reach | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 2.126385 | 9.03097 | False (9.03097) | None | None | False | 0.008264462809917356 |
| L-W 拉薩權重 2:1 / 1:2 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.614 | 0.1 | False | 0.2727272727272727 |
|  ⚠ L-W 拉薩權重 2:1 / 1:2: 27% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.628 | 0.55 | False | 0.3305785123966942 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1: 33% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1） | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.628 | 0.05 | False | 0.2809917355371901 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）: 28% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| H Dubai peak_core min, ε [0.05,0.99] | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| Exp-E Guangzhou mult=20 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9885} | 0.93144 | 0.8314400000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-E Guangzhou mult=10 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-E Guangzhou mult=5 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9524} | 0.931483 | 0.831483 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=5 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9894} | 0.93144 | 0.8314400000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=4 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9873} | 0.931442 | 0.831442 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=3 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9899} | 0.931444 | 0.8314440000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=2 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9853} | 0.931443 | 0.831443 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=1 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9842} | 0.93145 | 0.83145 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | feasible | {'solar_reflectance': 0.827, 'infrared_emissivity': 0.7751} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| Exp-C Dubai July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.5004} | 0.969569 | 2.150069000000004 | False (2.2187320000000015) | None | None | False | 0.008264462809917356 |
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-A Guangzhou peak_skin ≤ 33 | infeasible | {'solar_reflectance': 0.9798, 'infrared_emissivity': 0.9886} | 0.931456 | 3.0220899999999986 | False (3.021630000000002) | None | None | False | 0.008264462809917356 |
| Guangzhou August requirement search | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9866} | 0.803111 | 0.703111 | False (0.702697) | None | None | False | 0.008264462809917356 |
| Guangzhou August requirement search | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |

## Seed groups

| first name | n | ρ | ε | objective |
|---|---|---|---|---|
| S10-J Dubai Jul peak core, atol 0.0001 | 3 | — | 0.0500 ± 0.0000 | 39.4968 ± 0.0000 |
| S10-I Lhasa Jul material demand seed 5 | 6 | 0.6822 ± 0.0001 | 0.5000 ± 0.0001 | 0.2811 ± 0.0001 |
| S10-F1 Guangzhou Aug exceedance (rerun Exp-B) | 9 | 0.9799 ± 0.0001 | 0.9877 ± 0.0020 | 0.9314 ± 0.0000 |
| I-Lhasa-min-demand-seed-6 | 6 | 0.4806 ± 0.0000 | 0.5000 ± 0.0000 | 0.1328 ± 0.0000 |
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | 5 | 0.8854 ± 0.0326 | 0.9150 ± 0.0782 | 0.0000 ± 0.0000 |

```

### File: `backend/docs/acceptance/stage-2/golden-refresh.md`
```markdown
# Stage 2 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Cause: evaporation limited by explicit Re,cl. Previous factor 1/(1 + 0.45·clo·h_c)
was equivalent to Re,cl ≈ 27.3·clo m²·Pa/W; new default derivation R_cl/(LR·i_cl)
with i_cl = 0.45 gives Re,cl ≈ 20.9·clo m²·Pa/W (control 0.5 clo: 13.6 → 10.4;
RC 0.4 clo: 10.9 → 8.4). Expect slightly lower skin temperatures for both garments.

| metric | before | after | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 1.3193 | <fill> | |
| final_core_temperature_improvement_c | 0.6571 | <fill> | |
| average_skin_temperature_improvement_c | 0.9531 | <fill> | |

model_parameter_set_sha256: <fill>
```

### File: `backend/docs/acceptance/stage-3-reference-comparison/golden-refresh.md`
```markdown
# Stage 3 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes (all intentional, see ADR 0001-0003):
1. Heat capacities 280 -> 135.7 kJ/(m^2 K) (70 kg / 1.8 m^2). Transients are
   roughly twice as fast; the 2 h case is closer to steady state.
2. Explicit clothing surface temperature with f_cl = 1 + 0.15 clo replaces the
   linearised coupling factor.
3. Gagge 1986 controllers replace the prototype's linear gains.

| metric | before (2.0.0) | after (3.0.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 0.7846 | <fill> | |
| final_core_temperature_improvement_c | 0.1362 | <fill> | |
| average_skin_temperature_improvement_c | 0.43 | <fill> | |

model_parameter_set_sha256: ebc0c642... -> <fill>
Gagge benchmark (default fixture, 60 min): core max|dT| = <fill> C, skin max|dT| = <fill> C
Reference port parity (60 min, 70 kg): max|dT| = <fill> C
```

### File: `backend/docs/acceptance/stage-3-reference-comparison/pytest-all.txt`
```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.14.2, asyncio-1.4.0, cov-7.1.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 203 items

tests/core/test_numba_cache_integration.py::test_numba_writes_cache_files_to_configured_directory PASSED [  0%]
tests/core/test_runtime.py::test_uses_configured_cache_directory PASSED  [  0%]
tests/core/test_runtime.py::test_environment_variable_takes_precedence PASSED [  1%]
tests/core/test_runtime.py::test_uses_cross_platform_temporary_default PASSED [  1%]
tests/core/test_runtime.py::test_creates_missing_parent_directories PASSED [  2%]
tests/test_api.py::test_health_endpoint PASSED                           [  2%]
tests/test_api.py::test_simulation_endpoint PASSED                       [  3%]
tests/test_api.py::test_invalid_material_is_rejected PASSED              [  3%]
tests/test_api.py::test_identical_material_api_improvement_is_zero PASSED [  4%]
tests/test_body.py::test_default_person_reproduces_gagge_lumped_value PASSED [  4%]
tests/test_body.py::test_heavier_person_has_larger_capacity_per_area PASSED [  5%]
tests/test_body.py::test_larger_surface_area_lowers_capacity_per_area PASSED [  5%]
tests/test_cities.py::test_get_city_returns_supported_city PASSED        [  6%]
tests/test_cities.py::test_get_city_normalizes_case_and_spaces PASSED    [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[dubai] PASSED [  7%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[guangzhou] PASSED [  7%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[lhasa] PASSED [  8%]
tests/test_cities.py::test_get_city_rejects_unknown_city PASSED          [  8%]
tests/test_cities.py::test_unknown_city_error_lists_supported_cities PASSED [  9%]
tests/test_climate_adaptation.py::test_global_batch_month_range PASSED   [  9%]
tests/test_climate_adaptation.py::test_global_batch_rejects_duplicate_cities PASSED [ 10%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_dry-42.0-20.0-2.0-900.0] PASSED [ 10%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_humid-34.0-85.0-1.0-700.0] PASSED [ 11%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[high_altitude_solar-24.0-25.0-2.5-1000.0] PASSED [ 11%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[night-30.0-60.0-0.5-0.0] PASSED [ 12%]
tests/test_clothing.py::test_derived_evaporative_resistance_matches_formula PASSED [ 12%]
tests/test_clothing.py::test_none_resistance_is_derived_and_flagged PASSED [ 13%]
tests/test_clothing.py::test_explicit_resistance_overrides_derivation PASSED [ 13%]
tests/test_clothing.py::test_higher_resistance_lowers_maximum_evaporation PASSED [ 14%]
tests/test_clothing.py::test_explicit_derived_value_reproduces_none_result PASSED [ 14%]
tests/test_clothing.py::test_impermeable_garment_ends_warmer PASSED      [ 15%]
tests/test_clothing.py::test_infrared_transmittance_amplifies_longwave_exchange PASSED [ 15%]
tests/test_clothing.py::test_area_factor_is_derived_and_flagged PASSED   [ 16%]
tests/test_clothing.py::test_explicit_area_factor_overrides_derivation PASSED [ 16%]
tests/test_clothing.py::test_clothing_surface_balance_is_consistent PASSED [ 17%]
tests/test_clothing.py::test_nude_surface_temperature_equals_skin PASSED [ 17%]
tests/test_clothing.py::test_emissivity_plus_transmittance_above_one_is_rejected PASSED [ 18%]
tests/test_clothing.py::test_unknown_parameter_source_key_is_rejected PASSED [ 18%]
tests/test_cors.py::test_allows_configured_origin PASSED                 [ 19%]
tests/test_cors.py::test_allows_configured_preflight_request PASSED      [ 19%]
tests/test_cors.py::test_rejects_unknown_preflight_origin PASSED         [ 20%]
tests/test_cors.py::test_rejects_duplicate_cors_registration PASSED      [ 20%]
tests/test_cors.py::test_main_application_registers_cors_once PASSED     [ 21%]
tests/test_environment_model.py::test_defaults_reproduce_stage_1_formulas PASSED [ 21%]
tests/test_environment_model.py::test_swinbank_clear_sky PASSED          [ 22%]
tests/test_environment_model.py::test_wind_scaling_and_negative_inputs_are_clamped PASSED [ 22%]
tests/test_environment_model.py::test_describe_mentions_every_active_rule PASSED [ 23%]
tests/test_exposure_statistics.py::test_time_weighted_mean_matches_trapezoid PASSED [ 23%]
tests/test_exposure_statistics.py::test_statistics_use_exposure_window_not_padded_points PASSED [ 24%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[1] PASSED [ 24%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[3] PASSED [ 25%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[6] PASSED [ 25%]
tests/test_exposure_statistics.py::test_half_hour_start_uses_interpolated_boundary PASSED [ 26%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_returns_finite_values PASSED [ 26%]
tests/test_gagge_benchmark.py::test_gagge_output_is_in_broad_range PASSED [ 27%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_api PASSED           [ 27%]
tests/test_gagge_benchmark.py::test_gagge_api_converts_service_error_to_500 PASSED [ 28%]
tests/test_gagge_benchmark.py::test_benchmark_returns_aligned_transient_series PASSED [ 28%]
tests/test_gagge_benchmark.py::test_default_case_is_within_stage_3_tolerances PASSED [ 29%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[38.0-45.0-1.5-40.0-2.6-0.5] PASSED [ 29%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[30.0-30.0-0.3-60.0-1.2-0.6] PASSED [ 30%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[42.0-42.0-2.0-20.0-2.0-0.4] PASSED [ 30%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[34.0-36.0-1.0-85.0-1.8-0.5] PASSED [ 31%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[25.0-25.0-0.1-50.0-1.0-1.0] PASSED [ 31%]
tests/test_gagge_reference.py::test_port_returns_one_point_per_minute_plus_initial_state PASSED [ 32%]
tests/test_gagge_reference.py::test_heavier_body_warms_more_slowly PASSED [ 32%]
tests/test_global_batch_geojson.py::test_geojson_structure PASSED        [ 33%]
tests/test_golden_dubai_2h.py::test_dubai_two_hour_golden_case PASSED    [ 33%]
tests/test_job_service.py::test_job_to_response_maps_job_fields PASSED   [ 33%]
tests/test_job_service.py::test_job_to_detail_validates_saved_request PASSED [ 34%]
tests/test_job_service.py::test_get_job_or_none_uses_session_get PASSED  [ 34%]
tests/test_job_service.py::test_get_job_or_none_returns_none PASSED      [ 35%]
tests/test_model_parameters.py::test_every_parameter_has_unit_and_reference PASSED [ 35%]
tests/test_model_parameters.py::test_manifest_sha_is_stable_and_hex PASSED [ 36%]
tests/test_model_parameters.py::test_unknown_parameter_raises PASSED     [ 36%]
tests/test_model_parameters.py::test_model_parameter_endpoint PASSED     [ 37%]
tests/test_model_parameters.py::test_default_assumptions_endpoint PASSED [ 37%]
tests/test_parameter_participation.py::test_every_material_field_participates[absorbed_solar_to_body_fraction-0.6] PASSED [ 38%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_area_factor-1.4] PASSED [ 38%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_insulation_clo-0.9] PASSED [ 39%]
tests/test_parameter_participation.py::test_every_material_field_participates[evaporative_resistance_m2pa_w-40.0] PASSED [ 39%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_emissivity-0.5] PASSED [ 40%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_transmittance-0.15] PASSED [ 40%]
tests/test_parameter_participation.py::test_every_material_field_participates[projected_solar_area_factor-0.4] PASSED [ 41%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_reflectance-0.7] PASSED [ 41%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_transmittance-0.2] PASSED [ 42%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_mass_kg-95.0] PASSED [ 42%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_surface_area_m2-2.4] PASSED [ 43%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_core_temperature_c-37.4] PASSED [ 43%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_skin_temperature_c-31.0] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_person_field_participates[met-1.2] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update0-perturbed_update0] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update1-perturbed_update1] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update2-perturbed_update2] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update3-perturbed_update3] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update4-perturbed_update4] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update5-perturbed_update5] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update6-perturbed_update6] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update7-perturbed_update7] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update8-perturbed_update8] PASSED [ 49%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update9-perturbed_update9] PASSED [ 49%]
tests/test_physics.py::test_saturation_pressure_increases_with_temperature PASSED [ 50%]
tests/test_physics.py::test_saturation_pressure_near_reference_value PASSED [ 50%]
tests/test_physics.py::test_invalid_optical_sum_is_rejected PASSED       [ 51%]
tests/test_physics.py::test_higher_reflectance_reduces_solar_absorption PASSED [ 51%]
tests/test_physics.py::test_flux_calculation_is_finite[0.0] PASSED       [ 52%]
tests/test_physics.py::test_flux_calculation_is_finite[0.1] PASSED       [ 52%]
tests/test_physics.py::test_flux_calculation_is_finite[1.0] PASSED       [ 53%]
tests/test_physics.py::test_flux_calculation_is_finite[3.0] PASSED       [ 53%]
tests/test_physics.py::test_flux_calculation_is_finite[8.0] PASSED       [ 54%]
tests/test_result_export.py::test_missing_stage_3_diagnostics_export_as_blank_cells PASSED [ 54%]
tests/test_result_export.py::test_stage_3_diagnostics_are_exported_when_present PASSED [ 55%]
tests/test_result_export.py::test_result_csv_contains_expected_headers PASSED [ 55%]
tests/test_result_export.py::test_result_csv_contains_control_and_rc_values PASSED [ 56%]
tests/test_result_export.py::test_result_csv_with_empty_time_series_contains_only_headers PASSED [ 56%]
tests/test_result_export.py::test_result_csv_rejects_different_time_series_lengths PASSED [ 57%]
tests/test_result_export.py::test_result_json_serializes_model_dump_as_unicode PASSED [ 57%]
tests/test_result_storage.py::test_save_simulation_result_creates_gzip_json_file PASSED [ 58%]
tests/test_result_storage.py::test_save_simulation_result_creates_missing_directory PASSED [ 58%]
tests/test_result_storage.py::test_save_simulation_result_removes_temporary_file PASSED [ 59%]
tests/test_result_storage.py::test_save_simulation_result_preserves_unicode PASSED [ 59%]
tests/test_result_storage.py::test_save_simulation_result_replaces_existing_file PASSED [ 60%]
tests/test_result_storage.py::test_load_simulation_result_reads_and_validates_payload PASSED [ 60%]
tests/test_result_storage.py::test_load_simulation_result_raises_for_missing_file PASSED [ 61%]
tests/test_spectrum_parser.py::test_parse_valid_spectrum_csv PASSED      [ 61%]
tests/test_spectrum_parser.py::test_reject_value_above_one PASSED        [ 62%]
tests/test_spectrum_parser.py::test_reject_unsorted_wavelengths PASSED   [ 62%]
tests/test_spectrum_parser.py::test_parse_spectrum_returns_checksum PASSED [ 63%]
tests/test_spectrum_parser.py::test_parse_normalizes_header_names PASSED [ 63%]
tests/test_spectrum_parser.py::test_reject_empty_spectrum PASSED         [ 64%]
tests/test_spectrum_parser.py::test_reject_non_utf8_spectrum PASSED      [ 64%]
tests/test_spectrum_parser.py::test_reject_missing_wavelength_column PASSED [ 65%]
tests/test_spectrum_parser.py::test_reject_missing_value_column PASSED   [ 65%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[not-a-number,0.8] PASSED [ 66%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[0.3,not-a-number] PASSED [ 66%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[nan,0.8-wavelength] PASSED [ 66%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,nan-spectrum value] PASSED [ 67%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[-0.3,0.8-positive] PASSED [ 67%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,-0.1-between 0 and 1] PASSED [ 68%]
tests/test_spectrum_parser.py::test_reject_single_data_point PASSED      [ 68%]
tests/test_spectrum_parser.py::test_reject_file_above_size_limit PASSED  [ 69%]
tests/test_spectrum_parser.py::test_reject_too_many_points PASSED        [ 69%]
tests/test_stage_4_2_export.py::test_export_contains_required_files PASSED [ 70%]
tests/test_stage_4_2_exposure.py::test_all_mode_requires_all_thresholds PASSED [ 70%]
tests/test_stage_4_2_exposure.py::test_any_mode_requires_one_threshold PASSED [ 71%]
tests/test_stage_4_2_exposure.py::test_no_threshold_means_all_samples_eligible PASSED [ 71%]
tests/test_stage_4_2_sampling.py::test_three_samples_cover_entire_month PASSED [ 72%]
tests/test_stage_4_2_sampling.py::test_one_legacy_sample_uses_requested_day PASSED [ 72%]
tests/test_stage_4_2_sampling.py::test_sample_count_cannot_exceed_month_days PASSED [ 73%]
tests/test_stage_4_3_estimate.py::test_daily_batch_estimate PASSED       [ 73%]
tests/test_stage_4_3_sampling.py::test_daily_stride_one_has_one_sample_per_day PASSED [ 74%]
tests/test_stage_4_3_sampling.py::test_daily_stride_seven_covers_month PASSED [ 74%]
tests/test_stage_4_3_sampling.py::test_leap_year_daily_plan_has_366_samples PASSED [ 75%]
tests/test_stage_4_3_sampling.py::test_month_plan_returns_actual_dates PASSED [ 75%]
tests/test_stage_4_3_weather_slice.py::test_slice_weather_includes_padding PASSED [ 76%]
tests/test_stage_4_3_weather_slice.py::test_slice_fails_when_range_not_covered PASSED [ 76%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile PASSED       [ 77%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile_uses_weights PASSED [ 77%]
tests/test_stage_4_4_analytics.py::test_detects_consecutive_heatwave PASSED [ 78%]
tests/test_stage_4_4_analytics.py::test_non_consecutive_hot_days_are_not_heatwave PASSED [ 78%]
tests/test_stage_4_4_checkpoint.py::test_retry_preserves_checkpoint_when_enabled PASSED [ 79%]
tests/test_stage_4_4_checkpoint.py::test_monthly_checkpoint_round_trip PASSED [ 79%]
tests/test_two_node.py::test_simulation_returns_expected_number_of_points PASSED [ 80%]
tests/test_two_node.py::test_initial_temperatures_are_preserved PASSED   [ 80%]
tests/test_two_node.py::test_all_temperatures_are_finite PASSED          [ 81%]
tests/test_two_node.py::test_temperature_stays_in_broad_physiological_range PASSED [ 81%]
tests/test_two_node.py::test_energy_balance_residual_is_small PASSED     [ 82%]
tests/test_two_node.py::test_rc_material_reduces_skin_temperature PASSED [ 82%]
tests/test_two_node.py::test_identical_materials_produce_identical_results PASSED [ 83%]
tests/test_weather_api.py::test_weather_cities_endpoint PASSED           [ 83%]
tests/test_weather_api.py::test_weather_history_endpoint PASSED          [ 84%]
tests/test_weather_api.py::test_weather_history_rejects_unknown_city PASSED [ 84%]
tests/test_weather_api.py::test_weather_history_converts_service_error_to_502 PASSED [ 85%]
tests/test_weather_api.py::test_weather_history_validates_duration[0] PASSED [ 85%]
tests/test_weather_api.py::test_weather_history_validates_duration[1441] PASSED [ 86%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_start PASSED [ 86%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_half_hour PASSED [ 87%]
tests/test_weather_interpolation.py::test_environment_clamps_negative_wind_and_solar PASSED [ 87%]
tests/test_weather_interpolation.py::test_mean_radiant_temperature_increase_is_capped PASSED [ 88%]
tests/test_weather_interpolation.py::test_interpolation_outside_range_raises PASSED [ 88%]
tests/test_weather_interpolation.py::test_interpolation_at_exact_boundaries_is_allowed PASSED [ 89%]
tests/test_weather_interpolation.py::test_from_series_rejects_series_not_covering_requested_window PASSED [ 89%]
tests/test_weather_quality.py::test_unsorted_input_is_sorted_and_noted PASSED [ 90%]
tests/test_weather_quality.py::test_identical_duplicate_is_removed PASSED [ 90%]
tests/test_weather_quality.py::test_conflicting_duplicate_is_rejected PASSED [ 91%]
tests/test_weather_quality.py::test_naive_timestamp_is_rejected PASSED   [ 91%]
tests/test_weather_quality.py::test_gap_is_reported_but_not_raised_by_normalize PASSED [ 92%]
tests/test_weather_quality.py::test_window_with_gap_inside_is_rejected PASSED [ 92%]
tests/test_weather_quality.py::test_window_outside_gap_is_accepted PASSED [ 93%]
tests/test_weather_quality.py::test_missing_tail_is_rejected PASSED      [ 93%]
tests/test_weather_quality.py::test_exact_boundaries_are_accepted PASSED [ 94%]
tests/test_weather_service.py::test_historical_weather_with_mock PASSED  [ 94%]
tests/test_weather_simulation.py::test_execute_weather_simulation PASSED [ 95%]
tests/test_weather_simulation.py::test_execute_weather_simulation_without_callback PASSED [ 95%]
tests/test_worker_tasks.py::test_update_job_updates_fields_and_commits PASSED [ 96%]
tests/test_worker_tasks.py::test_update_job_rejects_missing_job PASSED   [ 96%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[queued] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[running] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[completed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[failed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelling] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelled] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_rejects_missing_job PASSED [100%]

============================= 203 passed in 2.83s =============================

```

### File: `backend/docs/acceptance/stage-4-material-library/pytest-all.txt`
```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.14.2, asyncio-1.4.0, cov-7.1.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 229 items

tests/core/test_numba_cache_integration.py::test_numba_writes_cache_files_to_configured_directory PASSED [  0%]
tests/core/test_runtime.py::test_uses_configured_cache_directory PASSED  [  0%]
tests/core/test_runtime.py::test_environment_variable_takes_precedence PASSED [  1%]
tests/core/test_runtime.py::test_uses_cross_platform_temporary_default PASSED [  1%]
tests/core/test_runtime.py::test_creates_missing_parent_directories PASSED [  2%]
tests/test_api.py::test_health_endpoint PASSED                           [  2%]
tests/test_api.py::test_simulation_endpoint PASSED                       [  3%]
tests/test_api.py::test_invalid_material_is_rejected PASSED              [  3%]
tests/test_api.py::test_identical_material_api_improvement_is_zero PASSED [  3%]
tests/test_body.py::test_default_person_reproduces_gagge_lumped_value PASSED [  4%]
tests/test_body.py::test_heavier_person_has_larger_capacity_per_area PASSED [  4%]
tests/test_body.py::test_larger_surface_area_lowers_capacity_per_area PASSED [  5%]
tests/test_cities.py::test_get_city_returns_supported_city PASSED        [  5%]
tests/test_cities.py::test_get_city_normalizes_case_and_spaces PASSED    [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[dubai] PASSED [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[guangzhou] PASSED [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[lhasa] PASSED [  7%]
tests/test_cities.py::test_get_city_rejects_unknown_city PASSED          [  7%]
tests/test_cities.py::test_unknown_city_error_lists_supported_cities PASSED [  8%]
tests/test_climate_adaptation.py::test_global_batch_month_range PASSED   [  8%]
tests/test_climate_adaptation.py::test_global_batch_rejects_duplicate_cities PASSED [  9%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_dry-42.0-20.0-2.0-900.0] PASSED [  9%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_humid-34.0-85.0-1.0-700.0] PASSED [ 10%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[high_altitude_solar-24.0-25.0-2.5-1000.0] PASSED [ 10%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[night-30.0-60.0-0.5-0.0] PASSED [ 10%]
tests/test_clothing.py::test_derived_evaporative_resistance_matches_formula PASSED [ 11%]
tests/test_clothing.py::test_none_resistance_is_derived_and_flagged PASSED [ 11%]
tests/test_clothing.py::test_explicit_resistance_overrides_derivation PASSED [ 12%]
tests/test_clothing.py::test_higher_resistance_lowers_maximum_evaporation PASSED [ 12%]
tests/test_clothing.py::test_explicit_derived_value_reproduces_none_result PASSED [ 13%]
tests/test_clothing.py::test_impermeable_garment_ends_warmer PASSED      [ 13%]
tests/test_clothing.py::test_infrared_transmittance_amplifies_longwave_exchange PASSED [ 13%]
tests/test_clothing.py::test_area_factor_is_derived_and_flagged PASSED   [ 14%]
tests/test_clothing.py::test_explicit_area_factor_overrides_derivation PASSED [ 14%]
tests/test_clothing.py::test_clothing_surface_balance_is_consistent PASSED [ 15%]
tests/test_clothing.py::test_nude_surface_temperature_equals_skin PASSED [ 15%]
tests/test_clothing.py::test_emissivity_plus_transmittance_above_one_is_rejected PASSED [ 16%]
tests/test_clothing.py::test_unknown_parameter_source_key_is_rejected PASSED [ 16%]
tests/test_cors.py::test_allows_configured_origin PASSED                 [ 17%]
tests/test_cors.py::test_allows_configured_preflight_request PASSED      [ 17%]
tests/test_cors.py::test_rejects_unknown_preflight_origin PASSED         [ 17%]
tests/test_cors.py::test_rejects_duplicate_cors_registration PASSED      [ 18%]
tests/test_cors.py::test_main_application_registers_cors_once PASSED     [ 18%]
tests/test_environment_model.py::test_defaults_reproduce_stage_1_formulas PASSED [ 19%]
tests/test_environment_model.py::test_swinbank_clear_sky PASSED          [ 19%]
tests/test_environment_model.py::test_wind_scaling_and_negative_inputs_are_clamped PASSED [ 20%]
tests/test_environment_model.py::test_describe_mentions_every_active_rule PASSED [ 20%]
tests/test_exposure_statistics.py::test_time_weighted_mean_matches_trapezoid PASSED [ 20%]
tests/test_exposure_statistics.py::test_statistics_use_exposure_window_not_padded_points PASSED [ 21%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[1] PASSED [ 21%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[3] PASSED [ 22%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[6] PASSED [ 22%]
tests/test_exposure_statistics.py::test_half_hour_start_uses_interpolated_boundary PASSED [ 23%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_returns_finite_values PASSED [ 23%]
tests/test_gagge_benchmark.py::test_gagge_output_is_in_broad_range PASSED [ 24%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_api PASSED           [ 24%]
tests/test_gagge_benchmark.py::test_gagge_api_converts_service_error_to_500 PASSED [ 24%]
tests/test_gagge_benchmark.py::test_benchmark_returns_aligned_transient_series PASSED [ 25%]
tests/test_gagge_benchmark.py::test_default_case_is_within_stage_3_tolerances PASSED [ 25%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[38.0-45.0-1.5-40.0-2.6-0.5] PASSED [ 26%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[30.0-30.0-0.3-60.0-1.2-0.6] PASSED [ 26%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[42.0-42.0-2.0-20.0-2.0-0.4] PASSED [ 27%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[34.0-36.0-1.0-85.0-1.8-0.5] PASSED [ 27%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[25.0-25.0-0.1-50.0-1.0-1.0] PASSED [ 27%]
tests/test_gagge_reference.py::test_port_returns_one_point_per_minute_plus_initial_state PASSED [ 28%]
tests/test_gagge_reference.py::test_heavier_body_warms_more_slowly PASSED [ 28%]
tests/test_global_batch_geojson.py::test_geojson_structure PASSED        [ 29%]
tests/test_golden_dubai_2h.py::test_dubai_two_hour_golden_case PASSED    [ 29%]
tests/test_job_service.py::test_job_to_response_maps_job_fields PASSED   [ 30%]
tests/test_job_service.py::test_job_to_detail_validates_saved_request PASSED [ 30%]
tests/test_job_service.py::test_get_job_or_none_uses_session_get PASSED  [ 31%]
tests/test_job_service.py::test_get_job_or_none_returns_none PASSED      [ 31%]
tests/test_material_fields.py::test_manifest_covers_every_physical_field_in_order PASSED [ 31%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[clothing_insulation_clo] PASSED [ 32%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[evaporative_resistance_m2pa_w] PASSED [ 32%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[clothing_area_factor] PASSED [ 33%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[solar_reflectance] PASSED [ 33%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[solar_transmittance] PASSED [ 34%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[infrared_emissivity] PASSED [ 34%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[infrared_transmittance] PASSED [ 34%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[projected_solar_area_factor] PASSED [ 35%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[absorbed_solar_to_body_fraction] PASSED [ 35%]
tests/test_material_fields.py::test_nullable_fields_declare_their_derivation PASSED [ 36%]
tests/test_material_resolution.py::test_input_without_version_id_is_returned_untouched PASSED [ 36%]
tests/test_material_resolution.py::test_omitted_fields_are_hydrated_from_the_version PASSED [ 37%]
tests/test_material_resolution.py::test_matching_explicit_values_are_accepted PASSED [ 37%]
tests/test_material_resolution.py::test_conflicting_explicit_value_is_rejected PASSED [ 37%]
tests/test_material_resolution.py::test_explicit_null_against_stored_value_is_a_conflict PASSED [ 38%]
tests/test_material_resolution.py::test_unknown_version_raises PASSED    [ 38%]
tests/test_material_resolution.py::test_legacy_version_outside_bounds_is_reported PASSED [ 39%]
tests/test_material_resolution.py::test_display_name_is_truncated_to_input_limit PASSED [ 39%]
tests/test_material_resolution.py::test_request_level_resolution_only_replaces_linked_materials PASSED [ 40%]
tests/test_materials_api.py::test_material_library_round_trip PASSED     [ 40%]
tests/test_materials_api.py::test_version_with_unknown_provenance_key_is_rejected_on_write PASSED [ 41%]
tests/test_model_parameters.py::test_every_parameter_has_unit_and_reference PASSED [ 41%]
tests/test_model_parameters.py::test_manifest_sha_is_stable_and_hex PASSED [ 41%]
tests/test_model_parameters.py::test_unknown_parameter_raises PASSED     [ 42%]
tests/test_model_parameters.py::test_model_parameter_endpoint PASSED     [ 42%]
tests/test_model_parameters.py::test_default_assumptions_endpoint PASSED [ 43%]
tests/test_model_parameters.py::test_model_metadata_endpoint PASSED      [ 43%]
tests/test_model_parameters.py::test_single_parameter_endpoint PASSED    [ 44%]
tests/test_model_parameters.py::test_material_fields_endpoint PASSED     [ 44%]
tests/test_parameter_participation.py::test_every_material_field_participates[absorbed_solar_to_body_fraction-0.6] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_area_factor-1.4] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_insulation_clo-0.9] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_material_field_participates[evaporative_resistance_m2pa_w-40.0] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_emissivity-0.5] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_transmittance-0.15] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_material_field_participates[projected_solar_area_factor-0.4] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_reflectance-0.7] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_transmittance-0.2] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_mass_kg-95.0] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_surface_area_m2-2.4] PASSED [ 49%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_core_temperature_c-37.4] PASSED [ 49%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_skin_temperature_c-31.0] PASSED [ 50%]
tests/test_parameter_participation.py::test_every_person_field_participates[met-1.2] PASSED [ 50%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update0-perturbed_update0] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update1-perturbed_update1] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update2-perturbed_update2] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update3-perturbed_update3] PASSED [ 52%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update4-perturbed_update4] PASSED [ 52%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update5-perturbed_update5] PASSED [ 53%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update6-perturbed_update6] PASSED [ 53%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update7-perturbed_update7] PASSED [ 54%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update8-perturbed_update8] PASSED [ 54%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update9-perturbed_update9] PASSED [ 55%]
tests/test_physics.py::test_saturation_pressure_increases_with_temperature PASSED [ 55%]
tests/test_physics.py::test_saturation_pressure_near_reference_value PASSED [ 55%]
tests/test_physics.py::test_invalid_optical_sum_is_rejected PASSED       [ 56%]
tests/test_physics.py::test_higher_reflectance_reduces_solar_absorption PASSED [ 56%]
tests/test_physics.py::test_flux_calculation_is_finite[0.0] PASSED       [ 57%]
tests/test_physics.py::test_flux_calculation_is_finite[0.1] PASSED       [ 57%]
tests/test_physics.py::test_flux_calculation_is_finite[1.0] PASSED       [ 58%]
tests/test_physics.py::test_flux_calculation_is_finite[3.0] PASSED       [ 58%]
tests/test_physics.py::test_flux_calculation_is_finite[8.0] PASSED       [ 58%]
tests/test_result_export.py::test_missing_stage_3_diagnostics_export_as_blank_cells PASSED [ 59%]
tests/test_result_export.py::test_stage_3_diagnostics_are_exported_when_present PASSED [ 59%]
tests/test_result_export.py::test_result_csv_contains_expected_headers PASSED [ 60%]
tests/test_result_export.py::test_result_csv_contains_control_and_rc_values PASSED [ 60%]
tests/test_result_export.py::test_result_csv_with_empty_time_series_contains_only_headers PASSED [ 61%]
tests/test_result_export.py::test_result_csv_rejects_different_time_series_lengths PASSED [ 61%]
tests/test_result_export.py::test_result_json_serializes_model_dump_as_unicode PASSED [ 62%]
tests/test_result_storage.py::test_save_simulation_result_creates_gzip_json_file PASSED [ 62%]
tests/test_result_storage.py::test_save_simulation_result_creates_missing_directory PASSED [ 62%]
tests/test_result_storage.py::test_save_simulation_result_removes_temporary_file PASSED [ 63%]
tests/test_result_storage.py::test_save_simulation_result_preserves_unicode PASSED [ 63%]
tests/test_result_storage.py::test_save_simulation_result_replaces_existing_file PASSED [ 64%]
tests/test_result_storage.py::test_load_simulation_result_reads_and_validates_payload PASSED [ 64%]
tests/test_result_storage.py::test_load_simulation_result_raises_for_missing_file PASSED [ 65%]
tests/test_route_registration.py::test_method_and_path_pairs_are_unique PASSED [ 65%]
tests/test_spectrum_parser.py::test_parse_valid_spectrum_csv PASSED      [ 65%]
tests/test_spectrum_parser.py::test_reject_value_above_one PASSED        [ 66%]
tests/test_spectrum_parser.py::test_reject_unsorted_wavelengths PASSED   [ 66%]
tests/test_spectrum_parser.py::test_parse_spectrum_returns_checksum PASSED [ 67%]
tests/test_spectrum_parser.py::test_parse_normalizes_header_names PASSED [ 67%]
tests/test_spectrum_parser.py::test_reject_empty_spectrum PASSED         [ 68%]
tests/test_spectrum_parser.py::test_reject_non_utf8_spectrum PASSED      [ 68%]
tests/test_spectrum_parser.py::test_reject_missing_wavelength_column PASSED [ 68%]
tests/test_spectrum_parser.py::test_reject_missing_value_column PASSED   [ 69%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[not-a-number,0.8] PASSED [ 69%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[0.3,not-a-number] PASSED [ 70%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[nan,0.8-wavelength] PASSED [ 70%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,nan-spectrum value] PASSED [ 71%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[-0.3,0.8-positive] PASSED [ 71%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,-0.1-between 0 and 1] PASSED [ 72%]
tests/test_spectrum_parser.py::test_reject_single_data_point PASSED      [ 72%]
tests/test_spectrum_parser.py::test_reject_file_above_size_limit PASSED  [ 72%]
tests/test_spectrum_parser.py::test_reject_too_many_points PASSED        [ 73%]
tests/test_stage_4_2_export.py::test_export_contains_required_files PASSED [ 73%]
tests/test_stage_4_2_exposure.py::test_all_mode_requires_all_thresholds PASSED [ 74%]
tests/test_stage_4_2_exposure.py::test_any_mode_requires_one_threshold PASSED [ 74%]
tests/test_stage_4_2_exposure.py::test_no_threshold_means_all_samples_eligible PASSED [ 75%]
tests/test_stage_4_2_sampling.py::test_three_samples_cover_entire_month PASSED [ 75%]
tests/test_stage_4_2_sampling.py::test_one_legacy_sample_uses_requested_day PASSED [ 75%]
tests/test_stage_4_2_sampling.py::test_sample_count_cannot_exceed_month_days PASSED [ 76%]
tests/test_stage_4_3_estimate.py::test_daily_batch_estimate PASSED       [ 76%]
tests/test_stage_4_3_sampling.py::test_daily_stride_one_has_one_sample_per_day PASSED [ 77%]
tests/test_stage_4_3_sampling.py::test_daily_stride_seven_covers_month PASSED [ 77%]
tests/test_stage_4_3_sampling.py::test_leap_year_daily_plan_has_366_samples PASSED [ 78%]
tests/test_stage_4_3_sampling.py::test_month_plan_returns_actual_dates PASSED [ 78%]
tests/test_stage_4_3_weather_slice.py::test_slice_weather_includes_padding PASSED [ 79%]
tests/test_stage_4_3_weather_slice.py::test_slice_fails_when_range_not_covered PASSED [ 79%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile PASSED       [ 79%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile_uses_weights PASSED [ 80%]
tests/test_stage_4_4_analytics.py::test_detects_consecutive_heatwave PASSED [ 80%]
tests/test_stage_4_4_analytics.py::test_non_consecutive_hot_days_are_not_heatwave PASSED [ 81%]
tests/test_stage_4_4_checkpoint.py::test_retry_preserves_checkpoint_when_enabled PASSED [ 81%]
tests/test_stage_4_4_checkpoint.py::test_monthly_checkpoint_round_trip PASSED [ 82%]
tests/test_two_node.py::test_simulation_returns_expected_number_of_points PASSED [ 82%]
tests/test_two_node.py::test_initial_temperatures_are_preserved PASSED   [ 82%]
tests/test_two_node.py::test_all_temperatures_are_finite PASSED          [ 83%]
tests/test_two_node.py::test_temperature_stays_in_broad_physiological_range PASSED [ 83%]
tests/test_two_node.py::test_energy_balance_residual_is_small PASSED     [ 84%]
tests/test_two_node.py::test_rc_material_reduces_skin_temperature PASSED [ 84%]
tests/test_two_node.py::test_identical_materials_produce_identical_results PASSED [ 85%]
tests/test_weather_api.py::test_weather_cities_endpoint PASSED           [ 85%]
tests/test_weather_api.py::test_weather_history_endpoint PASSED          [ 86%]
tests/test_weather_api.py::test_weather_history_rejects_unknown_city PASSED [ 86%]
tests/test_weather_api.py::test_weather_history_converts_service_error_to_502 PASSED [ 86%]
tests/test_weather_api.py::test_weather_history_validates_duration[0] PASSED [ 87%]
tests/test_weather_api.py::test_weather_history_validates_duration[1441] PASSED [ 87%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_start PASSED [ 88%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_half_hour PASSED [ 88%]
tests/test_weather_interpolation.py::test_environment_clamps_negative_wind_and_solar PASSED [ 89%]
tests/test_weather_interpolation.py::test_mean_radiant_temperature_increase_is_capped PASSED [ 89%]
tests/test_weather_interpolation.py::test_interpolation_outside_range_raises PASSED [ 89%]
tests/test_weather_interpolation.py::test_interpolation_at_exact_boundaries_is_allowed PASSED [ 90%]
tests/test_weather_interpolation.py::test_from_series_rejects_series_not_covering_requested_window PASSED [ 90%]
tests/test_weather_quality.py::test_unsorted_input_is_sorted_and_noted PASSED [ 91%]
tests/test_weather_quality.py::test_identical_duplicate_is_removed PASSED [ 91%]
tests/test_weather_quality.py::test_conflicting_duplicate_is_rejected PASSED [ 92%]
tests/test_weather_quality.py::test_naive_timestamp_is_rejected PASSED   [ 92%]
tests/test_weather_quality.py::test_gap_is_reported_but_not_raised_by_normalize PASSED [ 93%]
tests/test_weather_quality.py::test_window_with_gap_inside_is_rejected PASSED [ 93%]
tests/test_weather_quality.py::test_window_outside_gap_is_accepted PASSED [ 93%]
tests/test_weather_quality.py::test_missing_tail_is_rejected PASSED      [ 94%]
tests/test_weather_quality.py::test_exact_boundaries_are_accepted PASSED [ 94%]
tests/test_weather_service.py::test_historical_weather_with_mock PASSED  [ 95%]
tests/test_weather_simulation.py::test_execute_weather_simulation PASSED [ 95%]
tests/test_weather_simulation.py::test_execute_weather_simulation_without_callback PASSED [ 96%]
tests/test_worker_tasks.py::test_update_job_updates_fields_and_commits PASSED [ 96%]
tests/test_worker_tasks.py::test_update_job_rejects_missing_job PASSED   [ 96%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[queued] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[running] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[completed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[failed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelling] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelled] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_rejects_missing_job PASSED [100%]

============================= 229 passed in 3.03s =============================

```

### File: `backend/docs/acceptance/stage-5-solar-surface/golden-refresh.md`
```markdown
# Stage 5 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes (all intentional, ADR 0005-0006):
1. Absorbed solar is a source term in the clothing surface balance; the
   0.35 skin fraction is gone. Expect less solar heat reaching the skin for
   the control garment (dark, alpha = 0.6) at 5-6 m/s wind.
2. Body-incident shortwave uses the ERA5 beam/diffuse split with f_p on DNI,
   sky-diffuse and ground-reflected terms (albedo 0.2). At Dubai noon the
   incident irradiance rises from ~225 to ~280 W/m^2 (per A_D).
3. Registry key rename (effective_radiation_area_ratio -> _standing) and two
   new constants change the fingerprint even where values are unchanged.

| metric | before (3.0.0) | after (4.0.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 1.7815 | <fill> | |
| final_core_temperature_improvement_c | 1.6117 | <fill> | |
| average_skin_temperature_improvement_c | 1.0721 | <fill> | |

model_parameter_set_sha256: 5e0cbe09... -> <fill>
parameter_fingerprint: 40799058... -> <fill>
Gagge benchmark (default fixture, 60 min): unchanged (solar = 0 in the benchmark).
```

### File: `backend/docs/acceptance/stage-5-solar-surface/pytest-all.txt`
```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.14.2, asyncio-1.4.0, cov-7.1.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 243 items

tests/core/test_numba_cache_integration.py::test_numba_writes_cache_files_to_configured_directory PASSED [  0%]
tests/core/test_runtime.py::test_uses_configured_cache_directory PASSED  [  0%]
tests/core/test_runtime.py::test_environment_variable_takes_precedence PASSED [  1%]
tests/core/test_runtime.py::test_uses_cross_platform_temporary_default PASSED [  1%]
tests/core/test_runtime.py::test_creates_missing_parent_directories PASSED [  2%]
tests/test_api.py::test_health_endpoint PASSED                           [  2%]
tests/test_api.py::test_simulation_endpoint PASSED                       [  2%]
tests/test_api.py::test_invalid_material_is_rejected PASSED              [  3%]
tests/test_api.py::test_identical_material_api_improvement_is_zero PASSED [  3%]
tests/test_body.py::test_default_person_reproduces_gagge_lumped_value PASSED [  4%]
tests/test_body.py::test_heavier_person_has_larger_capacity_per_area PASSED [  4%]
tests/test_body.py::test_larger_surface_area_lowers_capacity_per_area PASSED [  4%]
tests/test_cities.py::test_get_city_returns_supported_city PASSED        [  5%]
tests/test_cities.py::test_get_city_normalizes_case_and_spaces PASSED    [  5%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[dubai] PASSED [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[guangzhou] PASSED [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[lhasa] PASSED [  6%]
tests/test_cities.py::test_get_city_rejects_unknown_city PASSED          [  7%]
tests/test_cities.py::test_unknown_city_error_lists_supported_cities PASSED [  7%]
tests/test_climate_adaptation.py::test_global_batch_month_range PASSED   [  8%]
tests/test_climate_adaptation.py::test_global_batch_rejects_duplicate_cities PASSED [  8%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_dry-42.0-20.0-2.0-900.0] PASSED [  9%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_humid-34.0-85.0-1.0-700.0] PASSED [  9%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[high_altitude_solar-24.0-25.0-2.5-1000.0] PASSED [  9%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[night-30.0-60.0-0.5-0.0] PASSED [ 10%]
tests/test_clothing.py::test_derived_evaporative_resistance_matches_formula PASSED [ 10%]
tests/test_clothing.py::test_none_resistance_is_derived_and_flagged PASSED [ 11%]
tests/test_clothing.py::test_explicit_resistance_overrides_derivation PASSED [ 11%]
tests/test_clothing.py::test_higher_resistance_lowers_maximum_evaporation PASSED [ 11%]
tests/test_clothing.py::test_explicit_derived_value_reproduces_none_result PASSED [ 12%]
tests/test_clothing.py::test_impermeable_garment_ends_warmer PASSED      [ 12%]
tests/test_clothing.py::test_infrared_transmittance_amplifies_longwave_exchange PASSED [ 13%]
tests/test_clothing.py::test_area_factor_is_derived_and_flagged PASSED   [ 13%]
tests/test_clothing.py::test_explicit_area_factor_overrides_derivation PASSED [ 13%]
tests/test_clothing.py::test_clothing_surface_balance_is_consistent PASSED [ 14%]
tests/test_clothing.py::test_nude_surface_temperature_equals_skin PASSED [ 14%]
tests/test_clothing.py::test_emissivity_plus_transmittance_above_one_is_rejected PASSED [ 15%]
tests/test_clothing.py::test_unknown_parameter_source_key_is_rejected PASSED [ 15%]
tests/test_cors.py::test_allows_configured_origin PASSED                 [ 16%]
tests/test_cors.py::test_allows_configured_preflight_request PASSED      [ 16%]
tests/test_cors.py::test_rejects_unknown_preflight_origin PASSED         [ 16%]
tests/test_cors.py::test_rejects_duplicate_cors_registration PASSED      [ 17%]
tests/test_cors.py::test_main_application_registers_cors_once PASSED     [ 17%]
tests/test_environment_model.py::test_defaults_reproduce_stage_1_formulas PASSED [ 18%]
tests/test_environment_model.py::test_swinbank_clear_sky PASSED          [ 18%]
tests/test_environment_model.py::test_wind_scaling_and_negative_inputs_are_clamped PASSED [ 18%]
tests/test_environment_model.py::test_describe_mentions_every_active_rule PASSED [ 19%]
tests/test_exposure_statistics.py::test_time_weighted_mean_matches_trapezoid PASSED [ 19%]
tests/test_exposure_statistics.py::test_statistics_use_exposure_window_not_padded_points PASSED [ 20%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[1] PASSED [ 20%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[3] PASSED [ 20%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[6] PASSED [ 21%]
tests/test_exposure_statistics.py::test_half_hour_start_uses_interpolated_boundary PASSED [ 21%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_returns_finite_values PASSED [ 22%]
tests/test_gagge_benchmark.py::test_gagge_output_is_in_broad_range PASSED [ 22%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_api PASSED           [ 23%]
tests/test_gagge_benchmark.py::test_gagge_api_converts_service_error_to_500 PASSED [ 23%]
tests/test_gagge_benchmark.py::test_benchmark_returns_aligned_transient_series PASSED [ 23%]
tests/test_gagge_benchmark.py::test_default_case_is_within_stage_3_tolerances PASSED [ 24%]
tests/test_gagge_benchmark.py::test_sitting_posture_runs_and_reports_seated_area_ratio PASSED [ 24%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[38.0-45.0-1.5-40.0-2.6-0.5] PASSED [ 25%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[30.0-30.0-0.3-60.0-1.2-0.6] PASSED [ 25%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[42.0-42.0-2.0-20.0-2.0-0.4] PASSED [ 25%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[34.0-36.0-1.0-85.0-1.8-0.5] PASSED [ 26%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[25.0-25.0-0.1-50.0-1.0-1.0] PASSED [ 26%]
tests/test_gagge_reference.py::test_port_returns_one_point_per_minute_plus_initial_state PASSED [ 27%]
tests/test_gagge_reference.py::test_heavier_body_warms_more_slowly PASSED [ 27%]
tests/test_global_batch_geojson.py::test_geojson_structure PASSED        [ 27%]
tests/test_global_batches_api.py::test_global_batch_records_material_version_links PASSED [ 28%]
tests/test_golden_dubai_2h.py::test_dubai_two_hour_golden_case PASSED    [ 28%]
tests/test_job_service.py::test_job_to_response_maps_job_fields PASSED   [ 29%]
tests/test_job_service.py::test_job_to_detail_validates_saved_request PASSED [ 29%]
tests/test_job_service.py::test_get_job_or_none_uses_session_get PASSED  [ 30%]
tests/test_job_service.py::test_get_job_or_none_returns_none PASSED      [ 30%]
tests/test_material_fields.py::test_manifest_covers_every_physical_field_in_order PASSED [ 30%]
tests/test_material_fields.py::test_deprecated_field_is_still_accepted_in_provenance PASSED [ 31%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[clothing_insulation_clo] PASSED [ 31%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[evaporative_resistance_m2pa_w] PASSED [ 32%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[clothing_area_factor] PASSED [ 32%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[solar_reflectance] PASSED [ 32%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[solar_transmittance] PASSED [ 33%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[infrared_emissivity] PASSED [ 33%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[infrared_transmittance] PASSED [ 34%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[projected_solar_area_factor] PASSED [ 34%]
tests/test_material_fields.py::test_nullable_fields_declare_their_derivation PASSED [ 34%]
tests/test_material_resolution.py::test_input_without_version_id_is_returned_untouched PASSED [ 35%]
tests/test_material_resolution.py::test_omitted_fields_are_hydrated_from_the_version PASSED [ 35%]
tests/test_material_resolution.py::test_matching_explicit_values_are_accepted PASSED [ 36%]
tests/test_material_resolution.py::test_conflicting_explicit_value_is_rejected PASSED [ 36%]
tests/test_material_resolution.py::test_explicit_null_against_stored_value_is_a_conflict PASSED [ 37%]
tests/test_material_resolution.py::test_unknown_version_raises PASSED    [ 37%]
tests/test_material_resolution.py::test_legacy_version_outside_bounds_is_reported PASSED [ 37%]
tests/test_material_resolution.py::test_display_name_is_truncated_to_input_limit PASSED [ 38%]
tests/test_material_resolution.py::test_request_level_resolution_only_replaces_linked_materials PASSED [ 38%]
tests/test_materials_api.py::test_material_library_round_trip PASSED     [ 39%]
tests/test_materials_api.py::test_version_with_unknown_provenance_key_is_rejected_on_write PASSED [ 39%]
tests/test_model_parameters.py::test_every_parameter_has_unit_and_reference PASSED [ 39%]
tests/test_model_parameters.py::test_manifest_sha_is_stable_and_hex PASSED [ 40%]
tests/test_model_parameters.py::test_unknown_parameter_raises PASSED     [ 40%]
tests/test_model_parameters.py::test_model_parameter_endpoint PASSED     [ 41%]
tests/test_model_parameters.py::test_default_assumptions_endpoint PASSED [ 41%]
tests/test_model_parameters.py::test_model_metadata_endpoint PASSED      [ 41%]
tests/test_model_parameters.py::test_single_parameter_endpoint PASSED    [ 42%]
tests/test_model_parameters.py::test_material_fields_endpoint PASSED     [ 42%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_area_factor-1.4] PASSED [ 43%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_insulation_clo-0.9] PASSED [ 43%]
tests/test_parameter_participation.py::test_every_material_field_participates[evaporative_resistance_m2pa_w-40.0] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_emissivity-0.5] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_transmittance-0.15] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_material_field_participates[projected_solar_area_factor-0.4] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_reflectance-0.7] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_transmittance-0.2] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_mass_kg-95.0] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_surface_area_m2-2.4] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_core_temperature_c-37.4] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_skin_temperature_c-31.0] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_person_field_participates[met-1.2] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_person_field_participates[position-sitting] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update0-perturbed_update0] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update1-perturbed_update1] PASSED [ 49%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update2-perturbed_update2] PASSED [ 49%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update3-perturbed_update3] PASSED [ 50%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update4-perturbed_update4] PASSED [ 50%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update5-perturbed_update5] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update6-perturbed_update6] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update7-perturbed_update7] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update8-perturbed_update8] PASSED [ 52%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update9-perturbed_update9] PASSED [ 52%]
tests/test_parameter_participation.py::test_every_solar_environment_field_participates[baseline_update0-perturbed_update0] PASSED [ 53%]
tests/test_parameter_participation.py::test_every_solar_environment_field_participates[baseline_update1-perturbed_update1] PASSED [ 53%]
tests/test_parameter_participation.py::test_every_solar_environment_field_participates[baseline_update2-perturbed_update2] PASSED [ 53%]
tests/test_parameter_participation.py::test_every_solar_environment_field_participates[baseline_update3-perturbed_update3] PASSED [ 54%]
tests/test_physics.py::test_saturation_pressure_increases_with_temperature PASSED [ 54%]
tests/test_physics.py::test_saturation_pressure_near_reference_value PASSED [ 55%]
tests/test_physics.py::test_invalid_optical_sum_is_rejected PASSED       [ 55%]
tests/test_physics.py::test_higher_reflectance_reduces_solar_absorption PASSED [ 55%]
tests/test_physics.py::test_flux_calculation_is_finite[0.0] PASSED       [ 56%]
tests/test_physics.py::test_flux_calculation_is_finite[0.1] PASSED       [ 56%]
tests/test_physics.py::test_flux_calculation_is_finite[1.0] PASSED       [ 57%]
tests/test_physics.py::test_flux_calculation_is_finite[3.0] PASSED       [ 57%]
tests/test_physics.py::test_flux_calculation_is_finite[8.0] PASSED       [ 58%]
tests/test_result_export.py::test_missing_stage_3_diagnostics_export_as_blank_cells PASSED [ 58%]
tests/test_result_export.py::test_stage_3_diagnostics_are_exported_when_present PASSED [ 58%]
tests/test_result_export.py::test_result_csv_contains_expected_headers PASSED [ 59%]
tests/test_result_export.py::test_result_csv_contains_control_and_rc_values PASSED [ 59%]
tests/test_result_export.py::test_result_csv_with_empty_time_series_contains_only_headers PASSED [ 60%]
tests/test_result_export.py::test_result_csv_rejects_different_time_series_lengths PASSED [ 60%]
tests/test_result_export.py::test_result_json_serializes_model_dump_as_unicode PASSED [ 60%]
tests/test_result_storage.py::test_save_simulation_result_creates_gzip_json_file PASSED [ 61%]
tests/test_result_storage.py::test_save_simulation_result_creates_missing_directory PASSED [ 61%]
tests/test_result_storage.py::test_save_simulation_result_removes_temporary_file PASSED [ 62%]
tests/test_result_storage.py::test_save_simulation_result_preserves_unicode PASSED [ 62%]
tests/test_result_storage.py::test_save_simulation_result_replaces_existing_file PASSED [ 62%]
tests/test_result_storage.py::test_load_simulation_result_reads_and_validates_payload PASSED [ 63%]
tests/test_result_storage.py::test_load_simulation_result_raises_for_missing_file PASSED [ 63%]
tests/test_route_registration.py::test_method_and_path_pairs_are_unique PASSED [ 64%]
tests/test_solar.py::test_without_split_ghi_is_beam_on_projected_area PASSED [ 64%]
tests/test_solar.py::test_split_components_follow_ashrae_55_geometry PASSED [ 65%]
tests/test_solar.py::test_partial_split_is_rejected PASSED               [ 65%]
tests/test_solar.py::test_transmittance_routes_solar_to_skin PASSED      [ 65%]
tests/test_solar.py::test_posture_selects_radiation_area_ratio PASSED    [ 66%]
tests/test_spectrum_parser.py::test_parse_valid_spectrum_csv PASSED      [ 66%]
tests/test_spectrum_parser.py::test_reject_value_above_one PASSED        [ 67%]
tests/test_spectrum_parser.py::test_reject_unsorted_wavelengths PASSED   [ 67%]
tests/test_spectrum_parser.py::test_parse_spectrum_returns_checksum PASSED [ 67%]
tests/test_spectrum_parser.py::test_parse_normalizes_header_names PASSED [ 68%]
tests/test_spectrum_parser.py::test_reject_empty_spectrum PASSED         [ 68%]
tests/test_spectrum_parser.py::test_reject_non_utf8_spectrum PASSED      [ 69%]
tests/test_spectrum_parser.py::test_reject_missing_wavelength_column PASSED [ 69%]
tests/test_spectrum_parser.py::test_reject_missing_value_column PASSED   [ 69%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[not-a-number,0.8] PASSED [ 70%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[0.3,not-a-number] PASSED [ 70%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[nan,0.8-wavelength] PASSED [ 71%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,nan-spectrum value] PASSED [ 71%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[-0.3,0.8-positive] PASSED [ 72%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,-0.1-between 0 and 1] PASSED [ 72%]
tests/test_spectrum_parser.py::test_reject_single_data_point PASSED      [ 72%]
tests/test_spectrum_parser.py::test_reject_file_above_size_limit PASSED  [ 73%]
tests/test_spectrum_parser.py::test_reject_too_many_points PASSED        [ 73%]
tests/test_stage_4_2_export.py::test_export_contains_required_files PASSED [ 74%]
tests/test_stage_4_2_exposure.py::test_all_mode_requires_all_thresholds PASSED [ 74%]
tests/test_stage_4_2_exposure.py::test_any_mode_requires_one_threshold PASSED [ 74%]
tests/test_stage_4_2_exposure.py::test_no_threshold_means_all_samples_eligible PASSED [ 75%]
tests/test_stage_4_2_sampling.py::test_three_samples_cover_entire_month PASSED [ 75%]
tests/test_stage_4_2_sampling.py::test_one_legacy_sample_uses_requested_day PASSED [ 76%]
tests/test_stage_4_2_sampling.py::test_sample_count_cannot_exceed_month_days PASSED [ 76%]
tests/test_stage_4_3_estimate.py::test_daily_batch_estimate PASSED       [ 76%]
tests/test_stage_4_3_sampling.py::test_daily_stride_one_has_one_sample_per_day PASSED [ 77%]
tests/test_stage_4_3_sampling.py::test_daily_stride_seven_covers_month PASSED [ 77%]
tests/test_stage_4_3_sampling.py::test_leap_year_daily_plan_has_366_samples PASSED [ 78%]
tests/test_stage_4_3_sampling.py::test_month_plan_returns_actual_dates PASSED [ 78%]
tests/test_stage_4_3_weather_slice.py::test_slice_weather_includes_padding PASSED [ 79%]
tests/test_stage_4_3_weather_slice.py::test_slice_fails_when_range_not_covered PASSED [ 79%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile PASSED       [ 79%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile_uses_weights PASSED [ 80%]
tests/test_stage_4_4_analytics.py::test_detects_consecutive_heatwave PASSED [ 80%]
tests/test_stage_4_4_analytics.py::test_non_consecutive_hot_days_are_not_heatwave PASSED [ 81%]
tests/test_stage_4_4_checkpoint.py::test_retry_preserves_checkpoint_when_enabled PASSED [ 81%]
tests/test_stage_4_4_checkpoint.py::test_monthly_checkpoint_round_trip PASSED [ 81%]
tests/test_two_node.py::test_simulation_returns_expected_number_of_points PASSED [ 82%]
tests/test_two_node.py::test_initial_temperatures_are_preserved PASSED   [ 82%]
tests/test_two_node.py::test_all_temperatures_are_finite PASSED          [ 83%]
tests/test_two_node.py::test_temperature_stays_in_broad_physiological_range PASSED [ 83%]
tests/test_two_node.py::test_energy_balance_residual_is_small PASSED     [ 83%]
tests/test_two_node.py::test_rc_material_reduces_skin_temperature PASSED [ 84%]
tests/test_two_node.py::test_identical_materials_produce_identical_results PASSED [ 84%]
tests/test_two_node.py::test_absorbed_solar_raises_clothing_surface_temperature PASSED [ 85%]
tests/test_two_node.py::test_surface_re_emits_part_of_the_absorbed_solar PASSED [ 85%]
tests/test_two_node.py::test_deprecated_absorbed_fraction_is_ignored PASSED [ 86%]
tests/test_weather_api.py::test_weather_cities_endpoint PASSED           [ 86%]
tests/test_weather_api.py::test_weather_history_endpoint PASSED          [ 86%]
tests/test_weather_api.py::test_weather_history_rejects_unknown_city PASSED [ 87%]
tests/test_weather_api.py::test_weather_history_converts_service_error_to_502 PASSED [ 87%]
tests/test_weather_api.py::test_weather_history_validates_duration[0] PASSED [ 88%]
tests/test_weather_api.py::test_weather_history_validates_duration[1441] PASSED [ 88%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_start PASSED [ 88%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_half_hour PASSED [ 89%]
tests/test_weather_interpolation.py::test_environment_clamps_negative_wind_and_solar PASSED [ 89%]
tests/test_weather_interpolation.py::test_mean_radiant_temperature_increase_is_capped PASSED [ 90%]
tests/test_weather_interpolation.py::test_interpolation_outside_range_raises PASSED [ 90%]
tests/test_weather_interpolation.py::test_interpolation_at_exact_boundaries_is_allowed PASSED [ 90%]
tests/test_weather_interpolation.py::test_from_series_rejects_series_not_covering_requested_window PASSED [ 91%]
tests/test_weather_quality.py::test_unsorted_input_is_sorted_and_noted PASSED [ 91%]
tests/test_weather_quality.py::test_identical_duplicate_is_removed PASSED [ 92%]
tests/test_weather_quality.py::test_conflicting_duplicate_is_rejected PASSED [ 92%]
tests/test_weather_quality.py::test_naive_timestamp_is_rejected PASSED   [ 93%]
tests/test_weather_quality.py::test_gap_is_reported_but_not_raised_by_normalize PASSED [ 93%]
tests/test_weather_quality.py::test_window_with_gap_inside_is_rejected PASSED [ 93%]
tests/test_weather_quality.py::test_window_outside_gap_is_accepted PASSED [ 94%]
tests/test_weather_quality.py::test_missing_tail_is_rejected PASSED      [ 94%]
tests/test_weather_quality.py::test_exact_boundaries_are_accepted PASSED [ 95%]
tests/test_weather_service.py::test_historical_weather_with_mock PASSED  [ 95%]
tests/test_weather_simulation.py::test_execute_weather_simulation PASSED [ 95%]
tests/test_weather_simulation.py::test_execute_weather_simulation_without_callback PASSED [ 96%]
tests/test_worker_tasks.py::test_update_job_updates_fields_and_commits PASSED [ 96%]
tests/test_worker_tasks.py::test_update_job_rejects_missing_job PASSED   [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[queued] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[running] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[completed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[failed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelling] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelled] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_rejects_missing_job PASSED [100%]

============================= 243 passed in 3.95s =============================

```

### File: `backend/docs/acceptance/stage-6-consistency/golden-refresh.md`
```markdown
# Stage 6 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes (all intentional):
1. Summary average is now the time-weighted trapezoidal mean shared by all
   three pipelines (PR-1a). Trajectories are unchanged.
2. `EnvironmentAssumptions.radiation_time_convention` added (default keeps the
   legacy linear behaviour) -> parameter fingerprint changes although no
   constant changed. MODEL_PARAMETER_SET_VERSION stays 4.0.0.
3. MODEL_VERSION 0.6.0 -> 0.7.0.

| metric | before (0.6.0) | after (0.7.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 2.1232 | 2.1232 | 0 |
| final_core_temperature_improvement_c | 1.9117 | 1.9117 | 0 |
| average_skin_temperature_improvement_c | 1.2703 | 1.2876 | +0.0173 (definition) |

Every control/radiative_cooling point: unchanged to 1e-6 (audit grid does not
alter solve_ivp stepping). parameter_fingerprint: 19ebfc73... -> <fill from run>
```

### File: `backend/docs/acceptance/stage-8-observability/README.md`
```markdown
# Stage 8 acceptance: observability, frontend reliability surface, resume benchmark

## Stage 7 defects fixed first (Step 0)
1. Beat schedule pointed at a non-existent task name -> reaper never ran.
2. `from fastapi import logger` -> AttributeError on the city failure path.
3. `/cancel` registered twice; the live one never set `cancel_requested_at`.
4. `BatchStatus` lacked `partial_completed`; `derive_batch_status` disagreed
   with `refresh_batch_status`.
5. `load_resume_state` assumed `start_month == 1`.

## New surface
- `GET  /global-batches/{id}`                      lease_state, checkpoint_months, attempt, cancel_requested_at
- `GET  /global-batches/{id}/events`               SSE: progress / terminal (lightweight snapshot)
- `GET  /global-batches/{id}/cities/{cid}/checkpoints`  durable checkpoints + resume_from_month
- `GET  /ops/status`                               broker, workers, lease summary, recovery bound
- Frontend: Reliability panel, lease badges, checkpoint timeline, data-quality
  panel, durable checkpoint list, batch list page, Operations page.

## Manual drills (record outputs in drills.md)
1. Start a 12-month batch for 3 cities. Confirm the batch page shows
   "Updates via server-sent events" and per-city cells turn green monthly.
2. `kill -9` the worker. Within TTL + reaper interval the city shows
   "Lease expired" then "Lease live" with a new owner and the "Resumed" tag;
   `resume_from_month` on the checkpoint endpoint equals last green cell + 1.
3. Stop the API's reverse proxy SSE support (or block /events): the page
   switches to "Updates via polling" without losing state.
4. Cancel a running batch: button turns into "Cancel requested - finishing
   current month"; no new checkpoint rows appear after the request timestamp.
5. Stop Redis: /ops shows "Broker unreachable", API still answers 200.
6. `RECORD_BENCHMARK=1 pytest tests/test_stage_8_resume_benchmark.py`
   -> resume-benchmark.json with resumed_equals_full == true.

## Known limitation carried from Stage 7
Months restored from a checkpoint have no `monthly_weather_payload_sha256`
entry (no weather is fetched for them). The checkpoint row's own
`payload_sha256` (exposed in Stage 8) is the reproducibility anchor instead.
```

### File: `backend/docs/acceptance/stage-8-observability/resume-benchmark.json`
```json
{
  "recorded_at": "2026-11-19T17:17:55.628429+08:00",
  "crash_after_month": 4,
  "full_run_seconds": 0.434,
  "resumed_run_seconds": 0.374,
  "months_restored": 4,
  "months_computed": 8,
  "weather_fetches_full": 12,
  "weather_fetches_resumed": 8,
  "resumed_equals_full": true
}
```

### File: `backend/docs/acceptance/stage-9-reliability/drills.md`
```markdown
# Stage 9 reliability drills

Each drill is run against docker-compose with one API, one Celery worker on
`default,global_standard,global_large`, and beat. Record the raw command and
the observed values; a drill without a recorded value is not accepted.

| # | Drill | Expected | Observed (fill) |
|---|---|---|---|
| 1 | Submit a single job, `kill -9` the worker mid-run | within TTL + reaper interval (180 + 60 s) `/simulations/jobs/{id}` shows `lease_state: expired` then `queued`, then `running` with a new `lease_owner`; `attempt` == 2 | |
| 2 | Redeliver a completed job message (`celery call simulation.run_weather --args '["<id>"]'`) | task returns `{"status": "skipped", "reason": "lease_not_acquired"}`; row untouched | |
| 3 | Cancel a running single job | status `cancelling` -> `cancelled` within one heartbeat; no result file written | |
| 4 | 12-month, 3-city batch, `kill -9` the worker after month 4 | city shows `Lease expired` -> `Lease live` (new owner) with the `Resumed` tag; `/checkpoints` has `resume_from_month: 5`; all rows `provenance_matches_batch: true` | |
| 5 | Bump `MODEL_VERSION` locally, retry the batch from drill 4 | `/checkpoints` shows every row `not resumable`; `data_quality.checkpoints_discarded` lists 12 months; result recomputed from month 1 | |
| 6 | Retry with `resume_from_checkpoint: false` | checkpoint rows deleted before the worker starts; `resumed_from_checkpoint: false` | |
| 7 | Block `/events` at the reverse proxy | both pages switch to "Updates via polling" and stop polling at terminal status | |
| 8 | Stop Redis | `/ops/status` -> `broker_reachable: false`; `/simulations/run-weather` still 200 from cache | |
| 9 | `global_large` batch, force one city failure | re-queued task appears on `global_large`, not `global_standard` (`celery -A app.worker.celery_app inspect reserved`) | |
```

### File: `backend/docs/acceptance/stage-optimization/optimization-summary.md`
```markdown
| name | verdict | best | objective | violation | upper feasible (viol) | min x @ max y | min y @ max x | x lower binding | plateau |
|---|---|---|---|---|---|---|---|---|---|
| Exp-A Guangzhou peak_skin ≤ 33 | infeasible | {'solar_reflectance': 0.9798, 'infrared_emissivity': 0.9886} | 0.931456 | 3.0220899999999986 | False (3.021630000000002) | None | None | False | 0.008264462809917356 |
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-C Dubai July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.5004} | 0.969569 | 2.150069000000004 | False (2.2187320000000015) | None | None | False | 0.008264462809917356 |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | feasible | {'solar_reflectance': 0.827, 'infrared_emissivity': 0.7751} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| Exp-D Guangzhou seed=1 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9842} | 0.93145 | 0.83145 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=2 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9853} | 0.931443 | 0.831443 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=3 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9899} | 0.931444 | 0.8314440000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=4 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9873} | 0.931442 | 0.831442 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-D Guangzhou seed=5 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9894} | 0.93144 | 0.8314400000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-E Guangzhou mult=10 | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-E Guangzhou mult=20 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9885} | 0.93144 | 0.8314400000000001 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Exp-E Guangzhou mult=5 | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9524} | 0.931483 | 0.831483 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| F1-infeasible-out-of-reach | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 2.126385 | 9.03097 | False (9.03097) | None | None | False | 0.008264462809917356 |
| F2-degree-hours-gradient | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 2.126385 | 3.25277 | False (3.25277) | None | None | False | 0.008264462809917356 |
| G1 - Air + linear solar gain | unconstrained | {'infrared_emissivity': 0.05} | 4.399347 | 0.0 | True (0.0) | None | None | None | None |
| G2 - Equal to air (shaded) | unconstrained | {'infrared_emissivity': 0.99} | 2.375719 | 0.0 | True (0.0) | None | None | None | None |
| Guangzhou August requirement search | infeasible | {'solar_reflectance': 0.9799, 'infrared_emissivity': 0.9876} | 0.931447 | 0.831447 | False (0.8314360000000001) | None | None | False | 0.008264462809917356 |
| Guangzhou August requirement search | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.9866} | 0.803111 | 0.703111 | False (0.702697) | None | None | False | 0.008264462809917356 |
| H Dubai peak_core min, ε [0.05,0.99] | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| H1 -  Aug | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.81147 | 7.75924 | False (7.75924) | None | None | False | 0.008264462809917356 |
| H2 - Jul | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.601119 | 7.196338 | False (7.196338) | None | None | False | 0.008264462809917356 |
| I-Lhasa-min-demand-seed-1 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13279345738295323 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-1: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-2 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13278631452581038 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-2: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-3 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13277891656662663 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-3: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-4 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.1327957833133253 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-4: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-5 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13278593937575026 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-5: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| I-Lhasa-min-demand-seed-6 | feasible | {'solar_reflectance': 0.4806, 'infrared_emissivity': 0.5} | 0.13281778211284515 | 0.0 | True (0.0) | 0.368 | 0.5 | False | 0.4132231404958678 |
|  ⚠ I-Lhasa-min-demand-seed-6: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| J-tol-1e-4 | feasible | {'infrared_emissivity': 0.5} | 0.0 | 0.0 | True (0.0) | None | None | None | None |
| J-tol-1e-4-b | infeasible | {'infrared_emissivity': 0.99} | 2.439081 | 4.098262 | False (4.098262) | None | None | None | None |
| J-tol-1e-5 | infeasible | {'infrared_emissivity': 0.99} | 2.439081 | 4.098262 | False (4.098262) | None | None | None | None |
| L 拉薩：最低需求（parameter_demand，權重 1:1） | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.628 | 0.05 | False | 0.2809917355371901 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）: 28% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.628 | 0.55 | False | 0.3305785123966942 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 1: 33% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 2: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 3: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 4: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ L 拉薩：最低需求（parameter_demand，權重 1:1）seed 5: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| L-W 拉薩權重 2:1 / 1:2 | feasible | {'solar_reflectance': 0.9, 'infrared_emissivity': 0.95} | 0.0 | 0.0 | True (0.0) | 0.614 | 0.1 | False | 0.2727272727272727 |
|  ⚠ L-W 拉薩權重 2:1 / 1:2: 27% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-F1 Guangzhou Aug exceedance (rerun Exp-B) | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 0.931436 | 8.31436 | False (8.31436) | None | None | False | 0.008264462809917356 |
| S10-F2 Guangzhou Aug degree-hours | feasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.99} | 2.126385 | 0.0 | True (0.0) | 0.98 | 0.99 | False | 0.008264462809917356 |
| S10-G1 Dubai Jul gray eps, MRT air+solar | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| S10-G2 Dubai Jul gray eps, MRT = air | unconstrained | {'infrared_emissivity': 0.9898} | 39.2552 | 0.0 | True (0.0) | None | None | None | None |
| S10-H1 Dubai Jul selective, MRT air+solar | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.786867 | 1.0543 | False (1.0543) | None | None | False | 0.008264462809917356 |
| S10-H2 Dubai Jul selective, MRT = air | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.99, 'infrared_emissivity_outside_window': 0.05} | 3.579197 | 0.9026 | False (0.9026) | None | None | False | 0.008264462809917356 |
| S10-I Lhasa Jul material demand seed 1 | feasible | {'solar_reflectance': 0.6821, 'infrared_emissivity': 0.5} | 0.28101970288115247 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 1: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 2 | feasible | {'solar_reflectance': 0.6821, 'infrared_emissivity': 0.5} | 0.2810093337334935 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 2: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 3 | feasible | {'solar_reflectance': 0.6823, 'infrared_emissivity': 0.5} | 0.2811007352941177 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 3: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 4 | feasible | {'solar_reflectance': 0.6822, 'infrared_emissivity': 0.5} | 0.28102028811524615 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 4: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 42 | feasible | {'solar_reflectance': 0.6822, 'infrared_emissivity': 0.5002} | 0.28116919267707086 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 42: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-I Lhasa Jul material demand seed 5 | feasible | {'solar_reflectance': 0.6821, 'infrared_emissivity': 0.5} | 0.28099027611044414 | 0.0 | True (0.0) | 0.572 | 0.5 | False | 0.4132231404958678 |
|  ⚠ S10-I Lhasa Jul material demand seed 5: 41% of map cells share the minimum; the reported optimum is arbitrary |||||||||
| S10-J Dubai Jul peak core, atol 0.0001 | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| S10-J Dubai Jul peak core, atol 0.001 | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| S10-J Dubai Jul peak core, atol 1e-05 | unconstrained | {'infrared_emissivity': 0.05} | 39.4968 | 0.0 | True (0.0) | None | None | None | None |
| S11-F3 Guangzhou Aug degree-hours, physical env | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.5} | 2.599091 | 0.3354 | False (0.5342) | None | None | False | 0.008264462809917356 |
| S11-G3 Dubai Jul gray eps, physical env | unconstrained | {'infrared_emissivity': 0.05} | 39.5228 | 0.0 | True (0.0) | None | None | None | None |
| S11-G3 Dubai Jul gray eps, physical env, K=40 | unconstrained | {'infrared_emissivity': 0.05} | 39.5111 | 0.0 | True (0.0) | None | None | None | None |
| S11-G3 Dubai Jul gray eps, physical env, K=5 | unconstrained | {'infrared_emissivity': 0.05} | 39.5341 | 0.0 | True (0.0) | None | None | None | None |
| S11-H3 Dubai Jul selective, physical env | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity_window': 0.5, 'infrared_emissivity_outside_window': 0.05} | 4.038676 | 1.2582 | False (1.2845) | None | None | False | 0.008264462809917356 |
| S12-L2 Dubai Jul eps + eps_g, s=0.0 | unconstrained | {'infrared_emissivity': 0.05, 'infrared_emissivity_ground_facing': 0.05} | 39.5228 | 0.0 | True (0.0) | 0.05 | 0.99 | True | 0.008264462809917356 |
| S12-L2 Dubai Jul eps + eps_g, s=0.25 | unconstrained | {'infrared_emissivity': 0.05, 'infrared_emissivity_ground_facing': 0.05} | 39.5228 | 0.0 | True (0.0) | 0.05 | 0.99 | True | 0.008264462809917356 |
| S12-L2 Dubai Jul eps + eps_g, s=0.5 | unconstrained | {'infrared_emissivity': 0.05, 'infrared_emissivity_ground_facing': 0.05} | 39.5228 | 0.0 | True (0.0) | 0.05 | 0.99 | True | 0.008264462809917356 |
| S12-L2 Dubai Jul eps + eps_g, s=0.75 | unconstrained | {'infrared_emissivity': 0.9899, 'infrared_emissivity_ground_facing': 0.05} | 39.4187 | 0.0 | True (0.0) | 0.05 | 0.99 | True | 0.008264462809917356 |
| S12-L5 Guangzhou Aug eps + eps_g | infeasible | {'solar_reflectance': 0.98, 'infrared_emissivity': 0.05, 'infrared_emissivity_ground_facing': 0.05} | 2.318463 | 0.1163 | False (0.1554) | None | None | False | 0.008264462809917356 |

## Seed groups

| first name | n | solar_reflectance | infrared_emissivity | infrared_emissivity_window | infrared_emissivity_outside_window | infrared_emissivity_ground_facing | objective |
|---|---|---|---|---|---|---|---|
| Exp-B Guangzhou skin_exceedance ≤ 0.1 + peak_core ≤ 38 | 9 | 0.9799 ± 0.0001 | 0.9877 ± 0.0020 | — | — | — | 0.9314 ± 0.0000 |
| Exp-C Lhasa July skin_exceedance ≤ 0.1 + peak_core ≤ 38 | 5 | 0.8854 ± 0.0326 | 0.9150 ± 0.0782 | — | — | — | 0.0000 ± 0.0000 |
| H Dubai peak_core min, ε [0.05,0.99] | 3 | — | 0.0500 ± 0.0000 | — | — | — | 39.4968 ± 0.0000 |
| I-Lhasa-min-demand-seed-1 | 6 | 0.4806 ± 0.0000 | 0.5000 ± 0.0000 | — | — | — | 0.1328 ± 0.0000 |
| S10-I Lhasa Jul material demand seed 1 | 6 | 0.6822 ± 0.0001 | 0.5000 ± 0.0001 | — | — | — | 0.2811 ± 0.0001 |

```

### File: `backend/docs/decisions/0001-body-surface-area.md`
```markdown
# ADR 0001: body_surface_area_m2 is currently informational — RESOLVED (Stage 3)

Finding (Stage 2): heat capacities were fixed per m^2 (245 + 35 kJ/(m^2 K)), so
`PersonInput.body_surface_area_m2` had no effect and the lumped value was
about 2x the Gagge two-node value for 70 kg / 1.8 m^2.

Resolution (Stage 3, PR-1): `PersonInput.body_mass_kg` (default 70) added.
C_core = m c_p (1 - alpha) / A_D, C_skin = m c_p alpha / A_D with
c_p = 3490 J/(kg K) and alpha = 0.1 (Gagge 1986). Default person gives
135.7 kJ/(m^2 K), matching the reference model. alpha is kept constant
(Gagge varies it with skin blood flow) so node capacities are state-independent
and the energy diagnostics stay exact. `test_body_surface_area_participates`
xfail removed; both fields are now covered by test_parameter_participation.
```

### File: `backend/docs/decisions/0002-gagge-controllers.md`
```markdown
# ADR 0002: adopt the Gagge (1986) thermoregulatory controllers

Context: the prototype used separate linear gains for sweating and skin blood
flow (170/200 g/(h m^2 K), 75/20 kg/(h m^2 K)) marked `assumed`. A transient
comparison with the reference cannot separate controller differences from
clothing/radiation differences while these remain arbitrary.

Decision: use the controllers of Gagge, Fobelets & Berglund (1986) as
implemented in the ASHRAE 55 SET reference procedure:
- m_rsw = 170 * WSIG_body * exp(WSIG_sk / 10.7), <= 500 g/(h m^2)
- SKBF  = (6.3 + 120 * WSIG_cr) / (1 + 0.5 * CSIG_sk), clamped [0.5, 90]
- w     = min(0.06 + 0.94 E_rsw / E_max, w_max), w_max = 0.59 v^-0.08 (clothed)
- M_shiv = 19.4 * CSIG_sk * CSIG_cr
All constants are `literature`. The platform's contribution is the clothing
optical/radiative model, not thermoregulation.

Known difference kept: when w is capped, the reference sets
E_skin = (0.06 + w_max) E_max; the prototype uses E_skin = w_max E_max.
```

### File: `backend/docs/decisions/0003-clothing-surface-balance.md`
```markdown
# ADR 0003: explicit clothing surface temperature; solar stays on the skin node

Decision: solve (T_sk - T_cl)/R_cl = f_cl [h_c (T_cl - T_a) + eps sigma (T_cl^4 - T_env^4)]
each evaluation (Newton, monotone). f_cl = material value or 1 + 0.15 clo, and
also enters Re,a = 1/(LR f_cl h_c). The `assumed` linearised h_r is removed.
T_cl is exported (`clothing_surface_temperature_c`) because it governs the net
sky radiation of a radiative-cooling garment.

Kept simplification: absorbed solar is still deposited on the skin via
`absorbed_solar_to_body_fraction` and does not enter the surface balance.
Moving it to the surface would remove a MaterialInput field and a DB column
and requires spectral data; scheduled for Stage 4. Recorded in
`assumptions_applied` of every result.

Effective radiation area (added after the first Stage 3 benchmark run): the
surface balance and both longwave terms are scaled by A_r/A_D = 0.73
(Fanger 1970, standing). Without it the prototype exchanged ~37 % more
longwave radiation than the reference, which appeared as a +0.30 K core bias
after 60 min in the default benchmark scenario (T_mrt = 45 C > T_cl).
```

### File: `backend/docs/decisions/0004-material-library-provenance.md`
```markdown
# ADR 0004: material library references are resolved server-side and verified

Context: `MaterialInput.material_version_id` existed since Stage 2 but had no
effect; any client could claim a version while sending different numbers.

Decision (Stage 4, PR-4):
- Resolution happens once at the API boundary (`services/material_resolution`).
  Omitted physical fields are hydrated from the immutable version; supplied
  fields must match (rel/abs 1e-9) or the request fails with
  `MATERIAL_PARAMETER_CONFLICT`. Provenance fields are hydrated when omitted.
- The resolved request is what is persisted; workers never touch the library.
- `simulation_jobs` / `global_batch_jobs` record the version ids (FK, SET NULL)
  so a material version can list the simulations that used it.
- Every stored version must be a valid `MaterialInput`: write bounds and DB
  CHECK constraints now mirror the input schema.

Not changed: physics, `MODEL_PARAMETER_SET_VERSION` (3.0.0), golden fixture.
```

### File: `backend/docs/decisions/0005-solar-on-clothing-surface.md`
```markdown
# ADR 0005: absorbed solar enters the clothing surface balance

Context: since Stage 0 the solar radiation absorbed by the textile was
deposited on the skin node scaled by `absorbed_solar_to_body_fraction` (0.35,
`assumed`). ADR 0003 deferred moving it to the surface to Stage 4; Stage 4
did not do it.

Decision (Stage 5):
- The surface balance gains a source term:
  (T_sk - T_cl)/R_cl + S_abs = f_cl [h_c (T_cl - T_a) + (A_r/A_D) eps sigma (T_cl^4 - T_env^4)],
  S_abs = alpha_sol * I_body per unit A_D. The residual stays strictly
  decreasing and concave, so the Newton solver is unchanged.
- Solar transmitted through the textile (tau_sol * I_body) is deposited on
  the skin node (skin shortwave reflectance neglected; first-order).
- `TimeSeriesPoint.absorbed_solar_w_m2` now means "solar entering the
  clothing-body system" (= S_abs + S_trans). The skin storage equation keeps
  its form, so the energy diagnostics are unchanged.
- `absorbed_solar_to_body_fraction` is DEPRECATED: kept in MaterialInput,
  MaterialVersionCreate and the DB column so stored requests and versions
  keep loading; removed from MATERIAL_PHYSICAL_FIELD_ORDER, the field
  manifest, the participation test and library-conflict verification.
  Provenance keys naming it are still accepted.

Consequence: the share of absorbed solar that reaches the skin is now an
outcome (higher with low wind and dark textiles, lower with high wind), not a
fixed 35 %. Removes one `assumed` model input.
```

### File: `backend/docs/decisions/0006-shortwave-geometry-and-posture.md`
```markdown
# ADR 0006: beam/diffuse split for body-incident shortwave; posture

Context: ERA5 supplies GHI, DNI, DHI. Stages 0-4 used GHI only and applied
the projected area factor f_p (a beam quantity) to it, which is geometrically
inconsistent. A_r/A_D was fixed at the standing value.

Decision (Stage 5):
- I_body = f_p * DNI + 0.5 f_eff F_sky DHI + 0.5 f_eff rho_g GHI
  (ASHRAE 55-2020 Appendix C geometry; measured DHI instead of 0.2 I_dir;
  sky view factor limits the sky-diffuse term; f_bes = 1).
- Fallback without DNI/DHI: I_body = f_p * GHI (legacy). Recorded in
  `assumptions_applied`. `EnvironmentInput` rejects a partial split.
- `EnvironmentAssumptions.ground_albedo` (0.2, assumed) feeds the reflected term.
- `PersonInput.position` in {standing, sitting} selects
  `effective_radiation_area_ratio_{standing,sitting}` (0.73 / 0.70) for both
  longwave exchange and the diffuse shortwave terms. The Gagge reference and
  library receive the same posture.

Not done (Stage 6): f_p as a function of solar altitude and posture
(ASHRAE 55 Table C-1; requires solar position from lat/lon/time, which the
weather series already carries); f_bes < 1 for partial shade; spectral
weighting of rho_sol / eps_IR from uploaded spectra.

MODEL_PARAMETER_SET_VERSION 3.0.0 -> 4.0.0; MODEL_VERSION 0.5.0 -> 0.6.0.
```

### File: `backend/docs/decisions/0007-two-band-longwave-and-requirement-search.md`
```markdown
# ADR 0007: two-band longwave exchange; feasibility-first requirement search

## Context
Stage 9 acceptance runs (docs/acceptance/stage-optimization):
1. Dubai July: the optimum sat at eps = 0.5 (lower bound); with eps in
   [0.05, 0.99], eps = 0.05 lowered peak core by ~0.1 K. A single broadband
   eps cannot represent a selective emitter, and the default
   T_mrt = T_air + min(15, 0.012 GHI) makes the non-sky hemisphere hotter
   than the clothing surface.
2. Guangzhou August: skin_exceedance_fraction stayed 0.93-0.97 over the
   whole design space; the time-fraction metric has no gradient there.
3. Lhasa: 41 % of map cells tied at 0; the reported "best" was the baseline.
4. A 39.5 C objective with tol = 1e-3 converged after one generation.

## Decision
Physics
- MaterialInput.infrared_emissivity is the broadband value Planck-weighted at
  emissivity_reference_temperature (305 K). Optional infrared_emissivity_window
  is eps_W in 8-13 um; eps_N follows from
  F_W eps_W + (1 - F_W) eps_N = eps.
- Selective path: emission and absorption are split into window and
  out-of-window bands. Outside the window the sky is opaque at T_air; inside
  it eps_sky,W is chosen so the broadband sky radiance equals sigma T_sky^4 of
  the configured sky method. Surroundings (1 - F_sky) are blackbodies at T_mrt.
- Gray materials keep the Stage 6 code path: trajectories unchanged.
- Skin emission through tau_IR stays gray (first order).
Search
- New metrics skin/core_excess_degree_hours (exact integral of
  max(0, T - threshold)).
- Constraints normalised by per-metric scales; feasible points always rank
  above infeasible ones; objective normalised against the baseline; DE uses
  tol = 0, atol = convergence_tolerance.
- material_demand objective and tie-breaker; per-variable demand_direction.
- Requirement readings are least-demanding feasible values (no monotonicity
  assumption); backend emits warnings and a sensitivity table.

## Consequences
- MODEL_PARAMETER_SET_VERSION 4.0.0 -> 5.0.0 (four constants);
  MODEL_VERSION 0.7.0 -> 0.8.0. Fingerprint changes; gray trajectories do not.
- Stage 9 checkpoints become non-resumable (model_version differs).
- Results that favour low eps or low eps_N under air_plus_solar_linear must be
  repeated with equal_to_air before being reported (experiment G).

## Not done
Solar spectral weighting (needs ASTM G173), angle-dependent f_p,
sky emissivity from cloud cover, multi-objective search.
```

### File: `backend/docs/decisions/0008-physical-radiant-environment.md`
```markdown
# ADR 0008: physical sky and ground temperatures

## Context
Since Stage 5 the body-incident shortwave (beam, sky diffuse, ground reflected)
is computed explicitly. The legacy rule T_mrt = T_air + min(15 K, 0.012 GHI)
still raises the longwave temperature of the non-sky view with GHI, so the
sun is counted twice and the surroundings act as a hot longwave source.
Stage 10 experiment G was designed to expose the consequence: optimizers
favour low (out-of-window) emissivity in Dubai.

## Decision
New, opt-in methods using ERA5 variables available from Open-Meteo:
- sky_temperature_method = brutsaert_cloud:
  eps = c + (1 - c) 1.24 (e_a[hPa]/T_a[K])^(1/7), T_sky = eps^(1/4) T_a,
  c = ERA5 total cloud cover. Consistent with ADR 0007: overcast -> T_sky = T_air.
- mean_radiant_temperature_method = ground_energy_balance: the non-sky view is
  the ground surface at the root of
  (1 - rho_g) GHI + eps_g sigma T_sky^4 = eps_g sigma T_g^4 + h_g (T_g - T_a) + K (T_g - T_soil),
  h_g = 2.8 + 3.0 v (Watmuff 1977), T_soil = ERA5 0-7 cm layer.
- Extra Open-Meteo variables are requested only when these methods are active;
  default requests, caches and payload hashes are byte-identical.
- Time series record the sky and surroundings temperatures used.

## Consequences
- MODEL_PARAMETER_SET_VERSION 6.0.0 (4 constants), MODEL_VERSION 0.9.0.
  Default trajectories unchanged; fingerprints and checkpoint request hashes change.
- Defaults are NOT switched. Switching is a Stage 12 decision gated by experiment K.

## Limitations
- Steady ground balance: no thermal inertia beyond the 0-7 cm layer, so the
  afternoon peak is reached too early and the evening ground is too cool.
- K (surface-soil conductance) is assumed; experiment K4 quantifies its effect.
- Horizontal open ground only; walls, shading and urban canyons are not modelled.
- Using ERA5 total cloud cover as the Crawford-Duchon cloud fraction is an approximation.
```

### File: `backend/docs/decisions/0009-physical-environment-default.md`
```markdown
# ADR 0009: physical radiant environment becomes the default

## Context
Stage 11 (ADR 0008) added opt-in physical sky and ground temperatures and gated a
default switch on experiment K. K1 passed in all three cities; K4 showed the
material conclusions do not depend on the unmeasured surface-soil conductance;
K5 showed annual skin improvement changes by ~0.03 C in Dubai and Guangzhou.
The legacy rule counts the sun twice (ADR 0008) and has no remaining advantage.

## Decision
- EnvironmentAssumptions() defaults to ground_energy_balance + brutsaert_cloud.
- Named presets: open_ground_physical (= default) and legacy_stage1.
- Stored request_json without environment_assumptions (pre-Stage 2) is loaded
  with legacy_stage1 through services.stored_requests; payloads with explicit
  assumptions (Stage 2+) keep them.
- Golden fixture pinned to legacy_stage1; its temperatures must not change.

## Consequences
- Default requests fetch cloud_cover and soil_temperature_0_to_7cm: new cache
  entries and payload hashes for default runs; samples with missing values are
  skipped as WEATHER_MISSING_VARIABLE.
- Tests on synthetic weather must pin legacy_stage1 or provide the variables.
- API clients that omit environment_assumptions get different results.
```

### File: `backend/docs/decisions/0010-two-zone-garment-longwave.md`
```markdown
# ADR 0010: sky-facing and ground-facing garment zones

## Context
Under the physical environment the ground can be 10-20 K warmer than the air
(K1), and optimisers choose low emissivity (K2-K4) even though high emissivity
is what radiates to the sky. A uniform garment must compromise (K3: eps_W 0.5).

## Decision
- Optional MaterialInput.infrared_emissivity_ground_facing (gray). None -> the
  Stage 11 code path, bit-identical.
- Zone areas F and 1 - F (F = sky view factor); sky views F + s(1 - F) and
  F(1 - s), s = zone_view_separation in [0, 1], default 0.5 (assumed).
  The area-weighted sky view equals F for every s.
- Sky-facing zone: existing gray or selective optics. Ground-facing zone: gray.
- One clothing surface temperature shared by both zones; skin emission
  transmitted through the textile sees the body-average field.
- Optimisation variable infrared_emissivity_ground_facing (demand: decreasing).

## Consequences
- MODEL_VERSION 0.10.0; parameter registry unchanged (6.0.0).
- s = 0 makes the two zones indistinguishable (area-weighted emissivity only).

## Limitations
- Shared surface temperature: in reality the ground-facing zone can be warmer
  than the sky-facing one; the benefit of a low eps_g is therefore uncertain
  in both directions and should be read as a first-order estimate.
- Zone areas tied to F is an idealisation of an open site and a standing person.
- s is not measured; results are reported as a sweep (experiment L2).
- The ground-facing zone has the same solar optics as the rest of the garment.
```

### File: `backend/docs/environment-assumptions.md`
```markdown
# Environment assumptions

ERA5 (via Open-Meteo) supplies air temperature, RH, 10 m wind and GHI.
Everything else the two-node model needs is derived by
`app/services/environment_model.py` using `EnvironmentAssumptions`, which is
part of every weather-driven request and echoed in every response.

| field | default | what it controls | status |
|---|---|---|---|
| mean_radiant_temperature_method | air_plus_solar_linear | T_mrt = T_air + min(cap, gain·GHI) | assumed (Stage 1 prototype) |
| solar_mrt_gain_k_per_w_m2 / solar_mrt_gain_cap_k | 0.012 / 15 | slope and cap above | assumed |
| sky_temperature_method | humidity_offset | T_sky = T_air − (5 + 10·(1−RH)) | assumed |
| sky_temperature_method = swinbank | — | clear-sky T_sky = 0.0552·T_air[K]^1.5 (Swinbank 1963) | literature |
| sky_view_factor | 0.5 | share of view occupied by sky | assumed; open site |
| wind_speed_scaling_factor | 1.0 | 10 m → body height | assumed; 0.67 ≈ log profile to 1.1 m |
| ground_albedo | 0.2 | reflected-diffuse shortwave term (ADR 0006) | assumed |

What these do **not** represent: cloud-cover dependent sky emissivity, 
ground surface temperature, urban canyon geometry, solar-altitude dependent f_p
(the solar term uses GHI only).

Selective emitters (infrared_emissivity_window set, ADR 0007): the sky is split
into the 8-13 um window, whose emissivity is back-calculated from T_sky above,
and the rest of the spectrum, treated as a blackbody at T_air. The non-sky part
of the view is a blackbody at T_mrt in every band. With the default
air_plus_solar_linear rule, T_mrt can exceed T_air by up to 15 K, which favours
low out-of-window emissivity; repeat key results with equal_to_air.

# ADR 0008: physical sky and ground temperatures

## Context
Since Stage 5 the body-incident shortwave (beam, sky diffuse, ground reflected)
is computed explicitly. The legacy rule T_mrt = T_air + min(15 K, 0.012 GHI)
still raises the longwave temperature of the non-sky view with GHI, so the
sun is counted twice and the surroundings act as a hot longwave source.
Stage 10 experiment G was designed to expose the consequence: optimizers
favour low (out-of-window) emissivity in Dubai.

## Decision
New, opt-in methods using ERA5 variables available from Open-Meteo:
- sky_temperature_method = brutsaert_cloud:
  eps = c + (1 - c) 1.24 (e_a[hPa]/T_a[K])^(1/7), T_sky = eps^(1/4) T_a,
  c = ERA5 total cloud cover. Consistent with ADR 0007: overcast -> T_sky = T_air.
- mean_radiant_temperature_method = ground_energy_balance: the non-sky view is
  the ground surface at the root of
  (1 - rho_g) GHI + eps_g sigma T_sky^4 = eps_g sigma T_g^4 + h_g (T_g - T_a) + K (T_g - T_soil),
  h_g = 2.8 + 3.0 v (Watmuff 1977), T_soil = ERA5 0-7 cm layer.
- Extra Open-Meteo variables are requested only when these methods are active;
  default requests, caches and payload hashes are byte-identical.
- Time series record the sky and surroundings temperatures used.

## Consequences
- MODEL_PARAMETER_SET_VERSION 6.0.0 (4 constants), MODEL_VERSION 0.9.0.
  Default trajectories unchanged; fingerprints and checkpoint request hashes change.
- Defaults are NOT switched. Switching is a Stage 12 decision gated by experiment K.

## Limitations
- Steady ground balance: no thermal inertia beyond the 0-7 cm layer, so the
  afternoon peak is reached too early and the evening ground is too cool.
- K (surface-soil conductance) is assumed; experiment K4 quantifies its effect.
- Horizontal open ground only; walls, shading and urban canyons are not modelled.
- Using ERA5 total cloud cover as the Crawford-Duchon cloud fraction is an approximation.
```

### File: `backend/docs/model-parameters.md`
```markdown
# Model parameters

Parameter set version: `5.0.0`  
SHA-256: `4e08b169ffe11abb73de5a6b130c0cca4a5880cd848c2f6f9f3e42c189ab524c`

Generated by `scripts/render_model_parameters_doc.py`. Do not edit by hand.

| name | value | unit | source type | reference | note |
|---|---|---|---|---|---|
| `stefan_boltzmann_constant` | 5.67037e-08 | W/(m^2 K^4) | standard | CODATA 2018 |  |
| `magnus_a` | 0.61078 | kPa | literature | Murray (1967) J. Appl. Meteorol. 6:203-204 |  |
| `magnus_b` | 17.2694 | - | literature | Murray (1967) J. Appl. Meteorol. 6:203-204 |  |
| `magnus_c` | 237.3 | C | literature | Murray (1967) J. Appl. Meteorol. 6:203-204 |  |
| `body_specific_heat` | 3490 | J/(kg K) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_mass_fraction` | 0.1 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 | Gagge lets alpha vary with skin blood flow (alpha = 0.0418 + 0.745/(SKBF + 0.585)). Kept constant here so the node heat capacities are state-independent. |
| `natural_convection_minimum_coefficient` | 3.1 | W/(m^2 K) | literature | ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort, Table 6 (seated, v < 0.2 m/s) |  |
| `forced_convection_coefficient` | 8.3 | W/(m^2 K (m/s)^-0.5) | literature | ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort, Table 6 (Mitchell 1974: 8.3 v^0.6) | Exponent simplified from 0.6 to 0.5 in this prototype. |
| `effective_radiation_area_ratio_standing` | 0.73 | - | literature | Fanger (1970) Thermal Comfort, McGraw-Hill; ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort (0.73 standing); ASHRAE Standard 55-2020, Normative Appendix D (SET reference procedure); reference implementations: pythermalcomfort.two_nodes_gagge, comf::calc2Node |  |
| `effective_radiation_area_ratio_sitting` | 0.7 | - | literature | Fanger (1970) Thermal Comfort, McGraw-Hill; ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort (0.70 seated); ASHRAE Standard 55-2020, Normative Appendix D (SET reference procedure); reference implementations: pythermalcomfort.two_nodes_gagge, comf::calc2Node |  |
| `diffuse_hemisphere_fraction` | 0.5 | - | standard | ASHRAE Standard 55-2020, Normative Appendix C (Arens et al. 2015): ERF = [0.5 f_eff f_svv (I_diff + I_TH R_floor) + f_p f_bes I_dir] alpha_SW / alpha_LW |  |
| `second_radiation_constant` | 14387.8 | um K | standard | CODATA 2018 |  |
| `atmospheric_window_lower_um` | 8 | um | literature | Granqvist & Hjortsberg (1981) J. Appl. Phys. 52:4205-4220 |  |
| `atmospheric_window_upper_um` | 13 | um | literature | Granqvist & Hjortsberg (1981) J. Appl. Phys. 52:4205-4220 |  |
| `emissivity_reference_temperature` | 305 | K | assumed | Project prototype value (radiative-cooling-platform, Stage 0-1) | Typical clothing surface temperature outdoors; affects only the split of selective materials, never gray ones. |
| `clo_to_si` | 0.155 | m^2 K/(W clo) | standard | ISO 9920:2007 |  |
| `clothing_area_factor_slope` | 0.15 | 1/clo | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731; ASHRAE Standard 55-2020, Normative Appendix D (SET reference procedure); reference implementations: pythermalcomfort.two_nodes_gagge, comf::calc2Node | ASHRAE Fundamentals Ch. 9 quotes 1 + 0.3 clo (McCullough & Jones 1984). 0.15 is retained for parity with the reference model. |
| `lewis_relation` | 16.5 | K/kPa | standard | ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort |  |
| `clothing_vapor_permeation_efficiency` | 0.45 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731; ASHRAE 55 SET procedure |  |
| `skin_emissivity` | 0.95 | - | literature | Steketee (1973) Phys. Med. Biol. 18:686-694 |  |
| `core_setpoint_temperature` | 36.8 | C | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_setpoint_temperature` | 33.7 | C | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `sweating_gain_body` | 170 | g/(h m^2 K) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `sweating_skin_signal_scale` | 10.7 | K | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_sweat_rate` | 500 | g/(h m^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `latent_heat_of_sweat` | 0.68 | W h/g | standard | ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort |  |
| `skin_diffusion_fraction` | 0.06 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_wettedness_clothed_coefficient` | 0.59 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_wettedness_clothed_exponent` | -0.08 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_wettedness_nude_coefficient` | 0.38 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_wettedness_nude_exponent` | -0.29 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_blood_flow_basal` | 6.3 | kg/(h m^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `vasodilation_gain` | 120 | kg/(h m^2 K) | literature | ASHRAE Standard 55-2020, Normative Appendix D (SET reference procedure); reference implementations: pythermalcomfort.two_nodes_gagge, comf::calc2Node | ASHRAE Fundamentals Ch. 9 prints 200; 120 is the value of the SET reference code and is kept for benchmark parity. |
| `vasoconstriction_gain` | 0.5 | 1/K | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_blood_flow_minimum` | 0.5 | kg/(h m^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_blood_flow_maximum` | 90 | kg/(h m^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `core_skin_conductance_basal` | 5.28 | W/(m^2 K) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `blood_heat_capacity_per_flow` | 1.163 | W h/(kg K) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `shivering_coefficient` | 19.4 | W/(m^2 K^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `metabolic_rate_per_met` | 58.15 | W/m^2 | standard | ISO 7730:2005 (58.2 W/m^2); ASHRAE 55 (58.15) |  |
| `respiratory_latent_coefficient` | 1.7e-05 | 1/Pa | standard | ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss) | ISO 7730 uses 1.72e-5. |
| `respiratory_reference_vapor_pressure` | 5867 | Pa | standard | ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss) |  |
| `respiratory_sensible_coefficient` | 0.0014 | 1/K | standard | ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss) |  |
| `exhaled_air_temperature` | 34 | C | standard | ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss) |  |
| `fallback_sky_temperature_offset` | 15 | K | assumed | Project prototype value (radiative-cooling-platform, Stage 0-1) |  |
| `swinbank_coefficient` | 0.0552 | K^-0.5 | literature | Swinbank (1963) Q. J. R. Meteorol. Soc. 89:339-348 |  |
| `brutsaert_coefficient` | 1.24 | (K/hPa)^(1/7) | literature | Brutsaert (1975) Water Resour. Res. 11:742-744 |  |
| `brutsaert_exponent` | 0.142857 | - | literature | Brutsaert (1975) Water Resour. Res. 11:742-744 |  |
| `ground_convection_still_air_coefficient` | 2.8 | W/(m^2 K) | literature | Watmuff, Charters & Proctor (1977) COMPLES 2:56 |  |
| `ground_convection_wind_coefficient` | 3 | W/(m^2 K (m/s)) | literature | Watmuff, Charters & Proctor (1977) COMPLES 2:56 | Evaluated with the body-height wind; a 2 m wind would be slightly lower. |

```

### File: `backend/tests/__init__.py`
```python

```

### File: `backend/tests/conftest.py`
```python
import os
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import get_settings, settings
from app.core.runtime import configure_runtime

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from app.schemas.weather import (
    CityResponse, WeatherPoint, WeatherSourceMetadata, WeatherTimeSeries,
)


_test_settings = get_settings()

configure_runtime(
    numba_cache_dir=_test_settings.numba_cache_dir,
)

NUMBA_CACHE_DIR = Path(
    os.environ.get(
        "NUMBA_CACHE_DIR",
        Path(tempfile.gettempdir())
        / "radiative-cooling-numba-cache",
    )
)

NUMBA_CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

os.environ["NUMBA_CACHE_DIR"] = str(
    NUMBA_CACHE_DIR
)


from app.core.config import settings
from app.db.session import get_db
from app.main import app
from app.schemas.simulation import (
    EnvironmentInput,
    MaterialInput,
    PersonInput,
    SimulationRequest,
)

@pytest.fixture(scope="session")
def engine():
    """One engine for the whole run; disposed so no psycopg connection is
    left for the garbage collector (that is the ResourceWarning pytest was
    reporting as an unraisable exception at shutdown)."""
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    try:
        yield engine
    finally:
        engine.dispose()

@pytest.fixture
def db_session(engine):
    """Each test runs inside one outer transaction that is always rolled back.

    ``join_transaction_mode="create_savepoint"`` is essential: service code
    (leases._heartbeat) calls ``session.rollback()`` when a lease is lost.
    With the SQLAlchemy 2.0 default (``conservative_savepoint``) that would
    roll back the *outer* transaction and wipe every row the test seeded;
    with savepoints it only undoes the work staged since the last commit.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(
        bind=connection,
        autoflush=False,
        expire_on_commit=False,
        join_transaction_mode="create_savepoint",
    )
    try:
        yield session
    finally:
        session.close()
        if transaction.is_active:
            transaction.rollback()
        connection.close()

@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = (
        override_get_db
    )

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(
            get_db,
            None,
        )


@pytest.fixture
def environment() -> EnvironmentInput:
    return EnvironmentInput(
        air_temperature_c=38.0,
        mean_radiant_temperature_c=45.0,
        sky_temperature_c=23.0,
        relative_humidity_percent=40.0,
        wind_speed_m_s=1.5,
        solar_radiation_w_m2=800.0,
        sky_view_factor=0.5,
    )


@pytest.fixture
def person() -> PersonInput:
    return PersonInput(
        met=2.6,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )


@pytest.fixture
def control_material() -> MaterialInput:
    return MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.4,
        solar_transmittance=0.0,
        infrared_emissivity=0.8,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )


@pytest.fixture
def rc_material() -> MaterialInput:
    return MaterialInput(
        name="Radiative Cooling",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0.0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )


@pytest.fixture
def simulation_request(
    environment: EnvironmentInput,
    person: PersonInput,
    control_material: MaterialInput,
    rc_material: MaterialInput,
) -> SimulationRequest:
    return SimulationRequest(
        city="Dubai",
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

@pytest.fixture
def hourly_weather() -> WeatherTimeSeries:
    """Five hourly points 11:00-15:00 Asia/Dubai; exposure 12:00-14:00."""
    tz = ZoneInfo("Asia/Dubai")
    start = datetime(2023, 7, 15, 12, tzinfo=tz)

    temperatures = [41.8, 43.4, 44.2, 44.9, 44.7]
    humidities = [29.0, 26.0, 25.0, 24.0, 24.0]
    winds = [6.17, 5.11, 4.32, 3.69, 3.62]
    ghis = [807.0, 901.0, 929.0, 892.0, 789.0]

    points = [
        WeatherPoint(
            timestamp=start + timedelta(hours=i - 1),
            air_temperature_c=temperatures[i],
            relative_humidity_percent=humidities[i],
            wind_speed_m_s=winds[i],
            ghi_w_m2=ghis[i],
            direct_radiation_w_m2=ghis[i] * 0.75,
            diffuse_radiation_w_m2=ghis[i] * 0.25,
            dni_w_m2=ghis[i] * 0.8,
        )
        for i in range(5)
    ]

    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai", name="Dubai", country="United Arab Emirates",
            latitude=25.2048, longitude=55.2708, elevation_m=16.0,
            timezone="Asia/Dubai", climate_type="hot_dry",
        ),
        requested_start_time=start,
        requested_end_time=start + timedelta(hours=2),
        points=points,
        source=WeatherSourceMetadata(
            provider="test", dataset="test", model="test",
            latitude=25.2, longitude=55.3, elevation_m=16.0,
            timezone="Asia/Dubai", downloaded_at=start,
            from_cache=True, attribution="test",
        ),
    )
```

### File: `backend/tests/core/test_numba_cache_integration.py`
```python
"""Integration test for the Numba compilation cache."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


BACKEND_ROOT = Path(__file__).resolve().parents[2]


def test_numba_writes_cache_files_to_configured_directory(
    tmp_path: Path,
) -> None:
    module_directory = tmp_path / "module"
    module_directory.mkdir()

    target_module = (
        module_directory
        / "cached_kernel.py"
    )

    target_module.write_text(
        "\n".join(
            [
                '"""Temporary Numba integration target."""',
                "",
                "from numba import njit",
                "",
                "",
                "@njit(cache=True)",
                "def add(left: int, right: int) -> int:",
                "    return left + right",
                "",
            ]
        ),
        encoding="utf-8",
    )

    cache_directory = tmp_path / "numba-cache"

    environment = os.environ.copy()
    environment["NUMBA_CACHE_DIR"] = str(
        cache_directory
    )
    environment["NUMBA_DISABLE_JIT"] = "0"

    python_path_entries = [
        str(module_directory),
        str(BACKEND_ROOT),
    ]

    existing_python_path = environment.get(
        "PYTHONPATH"
    )

    if existing_python_path:
        python_path_entries.append(
            existing_python_path
        )

    environment["PYTHONPATH"] = os.pathsep.join(
        python_path_entries
    )

    command = "\n".join(
        [
            "from app.core.runtime import configure_numba_cache",
            "configure_numba_cache()",
            "from cached_kernel import add",
            "assert add(2, 3) == 5",
        ]
    )

    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            command,
        ],
        cwd=BACKEND_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
    )

    assert completed.returncode == 0, (
        "The Numba subprocess failed.\n"
        f"stdout:\n{completed.stdout}\n"
        f"stderr:\n{completed.stderr}"
    )

    index_files = list(
        cache_directory.rglob("*.nbi")
    )
    object_files = list(
        cache_directory.rglob("*.nbc")
    )

    assert index_files, (
        "Numba did not create an .nbi cache index."
    )
    assert object_files, (
        "Numba did not create an .nbc cache object."
    )
```

### File: `backend/tests/core/test_runtime.py`
```python
"""Tests for process-level runtime configuration."""

from pathlib import Path

from app.core.runtime import configure_numba_cache


def test_uses_configured_cache_directory(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    configured_directory = tmp_path / "configured-cache"

    result = configure_numba_cache(configured_directory)

    assert result == configured_directory.resolve()
    assert result.is_dir()
    assert result.exists()
    assert result.as_posix() in (
        Path(result).as_posix(),
    )


def test_environment_variable_takes_precedence(
    monkeypatch,
    tmp_path: Path,
) -> None:
    environment_directory = tmp_path / "environment-cache"
    configured_directory = tmp_path / "configured-cache"

    monkeypatch.setenv(
        "NUMBA_CACHE_DIR",
        str(environment_directory),
    )

    result = configure_numba_cache(configured_directory)

    assert result == environment_directory.resolve()
    assert result.is_dir()


def test_uses_cross_platform_temporary_default(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    result = configure_numba_cache(
        temporary_root=tmp_path,
    )

    expected = (
        tmp_path
        / "radiative-cooling-platform"
        / "numba"
    ).resolve()

    assert result == expected
    assert result.is_dir()


def test_creates_missing_parent_directories(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    configured_directory = (
        tmp_path
        / "first"
        / "second"
        / "numba"
    )

    assert not configured_directory.exists()

    result = configure_numba_cache(configured_directory)

    assert result.exists()
    assert result.is_dir()
```

### File: `backend/tests/fixtures/dubai_2h/expected_results.json`
```json
{
  "city": "Dubai",
  "control": [
    {
      "core_temperature_c": 36.8,
      "minute": 0.0,
      "skin_temperature_c": 33.7
    },
    {
      "core_temperature_c": 37.3371,
      "minute": 10.0,
      "skin_temperature_c": 36.9878
    },
    {
      "core_temperature_c": 37.8104,
      "minute": 20.0,
      "skin_temperature_c": 37.3227
    },
    {
      "core_temperature_c": 38.2399,
      "minute": 30.0,
      "skin_temperature_c": 37.6983
    },
    {
      "core_temperature_c": 38.6416,
      "minute": 40.0,
      "skin_temperature_c": 38.05
    },
    {
      "core_temperature_c": 39.0174,
      "minute": 50.0,
      "skin_temperature_c": 38.3797
    },
    {
      "core_temperature_c": 39.3695,
      "minute": 60.0,
      "skin_temperature_c": 38.6892
    },
    {
      "core_temperature_c": 39.6985,
      "minute": 70.0,
      "skin_temperature_c": 38.9743
    },
    {
      "core_temperature_c": 40.0044,
      "minute": 80.0,
      "skin_temperature_c": 39.239
    },
    {
      "core_temperature_c": 40.2891,
      "minute": 90.0,
      "skin_temperature_c": 39.4856
    },
    {
      "core_temperature_c": 40.5541,
      "minute": 100.0,
      "skin_temperature_c": 39.7156
    },
    {
      "core_temperature_c": 40.8011,
      "minute": 110.0,
      "skin_temperature_c": 39.9305
    },
    {
      "core_temperature_c": 41.0316,
      "minute": 120.0,
      "skin_temperature_c": 40.1314
    }
  ],
  "duration_minutes": 120,
  "model_version": "0.10.0",
  "parameter_fingerprint": "80d30c26549f43a45fa553e843ea2b1a73788bf23819c0b72b8fb9d3d6103e7b",
  "parameter_snapshot": {
    "environment_assumptions": {
      "fixed_sky_offset_k": 15.0,
      "ground_albedo": 0.2,
      "ground_emissivity": 0.95,
      "ground_soil_conductance_w_m2k": 15.0,
      "mean_radiant_temperature_method": "air_plus_solar_linear",
      "radiation_time_convention": "instantaneous_linear",
      "sky_offset_base_k": 5.0,
      "sky_offset_humidity_range_k": 10.0,
      "sky_temperature_method": "humidity_offset",
      "sky_view_factor": 0.5,
      "solar_mrt_gain_cap_k": 15.0,
      "solar_mrt_gain_k_per_w_m2": 0.012,
      "wind_speed_scaling_factor": 1.0,
      "zone_view_separation": 0.5
    },
    "model_parameter_set_sha256": "4e08b169ffe11abb73de5a6b130c0cca4a5880cd848c2f6f9f3e42c189ab524c",
    "model_parameter_set_version": "5.0.0",
    "model_parameters": {
      "atmospheric_window_lower_um": 8.0,
      "atmospheric_window_upper_um": 13.0,
      "blood_heat_capacity_per_flow": 1.163,
      "body_specific_heat": 3490.0,
      "brutsaert_coefficient": 1.24,
      "brutsaert_exponent": 0.14285714285714285,
      "clo_to_si": 0.155,
      "clothing_area_factor_slope": 0.15,
      "clothing_vapor_permeation_efficiency": 0.45,
      "core_setpoint_temperature": 36.8,
      "core_skin_conductance_basal": 5.28,
      "diffuse_hemisphere_fraction": 0.5,
      "effective_radiation_area_ratio_sitting": 0.7,
      "effective_radiation_area_ratio_standing": 0.73,
      "emissivity_reference_temperature": 305.0,
      "exhaled_air_temperature": 34.0,
      "fallback_sky_temperature_offset": 15.0,
      "forced_convection_coefficient": 8.3,
      "ground_convection_still_air_coefficient": 2.8,
      "ground_convection_wind_coefficient": 3.0,
      "latent_heat_of_sweat": 0.68,
      "lewis_relation": 16.5,
      "magnus_a": 0.61078,
      "magnus_b": 17.2694,
      "magnus_c": 237.3,
      "maximum_sweat_rate": 500.0,
      "maximum_wettedness_clothed_coefficient": 0.59,
      "maximum_wettedness_clothed_exponent": -0.08,
      "maximum_wettedness_nude_coefficient": 0.38,
      "maximum_wettedness_nude_exponent": -0.29,
      "metabolic_rate_per_met": 58.15,
      "natural_convection_minimum_coefficient": 3.1,
      "respiratory_latent_coefficient": 1.7e-05,
      "respiratory_reference_vapor_pressure": 5867.0,
      "respiratory_sensible_coefficient": 0.0014,
      "second_radiation_constant": 14387.768775,
      "shivering_coefficient": 19.4,
      "skin_blood_flow_basal": 6.3,
      "skin_blood_flow_maximum": 90.0,
      "skin_blood_flow_minimum": 0.5,
      "skin_diffusion_fraction": 0.06,
      "skin_emissivity": 0.95,
      "skin_mass_fraction": 0.1,
      "skin_setpoint_temperature": 33.7,
      "stefan_boltzmann_constant": 5.670374419e-08,
      "sweating_gain_body": 170.0,
      "sweating_skin_signal_scale": 10.7,
      "swinbank_coefficient": 0.0552,
      "vasoconstriction_gain": 0.5,
      "vasodilation_gain": 120.0
    },
    "schema_version": 1
  },
  "radiative_cooling": [
    {
      "core_temperature_c": 36.8,
      "minute": 0.0,
      "skin_temperature_c": 33.7
    },
    {
      "core_temperature_c": 37.2571,
      "minute": 10.0,
      "skin_temperature_c": 36.5487
    },
    {
      "core_temperature_c": 37.5956,
      "minute": 20.0,
      "skin_temperature_c": 36.7592
    },
    {
      "core_temperature_c": 37.8057,
      "minute": 30.0,
      "skin_temperature_c": 36.8502
    },
    {
      "core_temperature_c": 37.9913,
      "minute": 40.0,
      "skin_temperature_c": 37.0136
    },
    {
      "core_temperature_c": 38.1657,
      "minute": 50.0,
      "skin_temperature_c": 37.1679
    },
    {
      "core_temperature_c": 38.3299,
      "minute": 60.0,
      "skin_temperature_c": 37.3138
    },
    {
      "core_temperature_c": 38.4842,
      "minute": 70.0,
      "skin_temperature_c": 37.4487
    },
    {
      "core_temperature_c": 38.6283,
      "minute": 80.0,
      "skin_temperature_c": 37.5746
    },
    {
      "core_temperature_c": 38.7631,
      "minute": 90.0,
      "skin_temperature_c": 37.6928
    },
    {
      "core_temperature_c": 38.8895,
      "minute": 100.0,
      "skin_temperature_c": 37.8041
    },
    {
      "core_temperature_c": 39.0082,
      "minute": 110.0,
      "skin_temperature_c": 37.909
    },
    {
      "core_temperature_c": 39.1199,
      "minute": 120.0,
      "skin_temperature_c": 38.0082
    }
  ],
  "summary": {
    "average_skin_temperature_improvement_c": 1.2876,
    "averaging_method": "time_weighted_trapezoid",
    "final_core_temperature_improvement_c": 1.9117,
    "final_skin_temperature_improvement_c": 2.1232
  },
  "weather": {
    "payload_sha256": "b568200999e8bc079896b86d451e3c82213682d90698ef1f846100fcc863f9d3",
    "point_count": 5,
    "quality": {
      "duplicates_removed": 0,
      "expected_step_seconds": 3600,
      "first_timestamp": "2023-07-15T00:00:00+04:00",
      "gaps": [],
      "last_timestamp": "2023-07-15T23:00:00+04:00",
      "notes": [],
      "point_count": 24,
      "was_sorted": true
    }
  }
}
```

### File: `backend/tests/fixtures/dubai_2h/open_meteo_payload.json`
```json
{"elevation":16.0,"generationtime_ms":0.1323223114013672,"hourly":{"diffuse_radiation":[0.0,0.0,0.0,0.0,0.0,0.0,3.0,55.0,111.0,151.0,175.0,195.0,205.0,208.0,203.0,192.0,196.0,150.0,106.0,42.0,1.0,0.0,0.0,0.0],"direct_normal_irradiance":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,184.1,396.8,539.4,638.7,686.0,716.3,724.2,716.1,683.2,569.0,459.4,318.5,130.9,0.0,0.0,0.0,0.0],"direct_radiation":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,32.0,155.0,319.0,487.0,612.0,696.0,721.0,689.0,597.0,419.0,257.0,113.0,19.0,0.0,0.0,0.0,0.0],"relative_humidity_2m":[42,39,36,33,28,26,25,30,34,32,30,29,26,25,24,24,25,28,36,39,41,42,42,42],"shortwave_radiation":[0.0,0.0,0.0,0.0,0.0,0.0,3.0,87.0,266.0,470.0,662.0,807.0,901.0,929.0,892.0,789.0,615.0,407.0,219.0,61.0,1.0,0.0,0.0,0.0],"temperature_2m":[38.4,38.0,37.5,37.3,37.4,37.6,37.7,37.5,37.9,39.8,41.0,41.8,43.4,44.2,44.9,44.7,44.3,43.1,40.5,39.3,38.4,37.8,37.6,37.3],"time":["2023-07-15T00:00","2023-07-15T01:00","2023-07-15T02:00","2023-07-15T03:00","2023-07-15T04:00","2023-07-15T05:00","2023-07-15T06:00","2023-07-15T07:00","2023-07-15T08:00","2023-07-15T09:00","2023-07-15T10:00","2023-07-15T11:00","2023-07-15T12:00","2023-07-15T13:00","2023-07-15T14:00","2023-07-15T15:00","2023-07-15T16:00","2023-07-15T17:00","2023-07-15T18:00","2023-07-15T19:00","2023-07-15T20:00","2023-07-15T21:00","2023-07-15T22:00","2023-07-15T23:00"],"wind_speed_10m":[3.96,3.97,4.16,4.38,4.92,5.85,6.45,6.38,7.33,7.48,7.01,6.17,5.11,4.32,3.69,3.62,4.02,4.7,4.9,4.02,2.8,2.58,2.5,2.06]},"hourly_units":{"diffuse_radiation":"W/m\u00b2","direct_normal_irradiance":"W/m\u00b2","direct_radiation":"W/m\u00b2","relative_humidity_2m":"%","shortwave_radiation":"W/m\u00b2","temperature_2m":"\u00b0C","time":"iso8601","wind_speed_10m":"m/s"},"latitude":25.0,"longitude":55.25,"timezone":"Asia/Dubai","timezone_abbreviation":"GMT+4","utc_offset_seconds":14400}
```

### File: `backend/tests/fixtures/dubai_2h/open_meteo_payload.sha256`
```
b568200999e8bc079896b86d451e3c82213682d90698ef1f846100fcc863f9d3

```

### File: `backend/tests/fixtures/dubai_2h/request.json`
```json
{
  "city_id": "dubai",
  "start_time_local": "2023-07-15T12:00:00",
  "duration_minutes": 120,
  "output_interval_minutes": 10,
  "person": {
    "met": 2.6,
    "body_surface_area_m2": 1.8,
    "initial_core_temperature_c": 36.8,
    "initial_skin_temperature_c": 33.7
  },
  "control_material": {
    "name": "Control",
    "clothing_insulation_clo": 0.5,
    "solar_reflectance": 0.4,
    "solar_transmittance": 0.0,
    "infrared_emissivity": 0.8,
    "projected_solar_area_factor": 0.25,
    "absorbed_solar_to_body_fraction": 0.35
  },
  "rc_material": {
    "name": "Radiative Cooling",
    "clothing_insulation_clo": 0.4,
    "solar_reflectance": 0.92,
    "solar_transmittance": 0.0,
    "infrared_emissivity": 0.95,
    "projected_solar_area_factor": 0.25,
    "absorbed_solar_to_body_fraction": 0.35
  }
}
```

### File: `backend/tests/fixtures/dubai_2h/request_params.json`
```json
{
  "cell_selection": "land",
  "elevation": 16.0,
  "end_date": "2023-07-15",
  "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,shortwave_radiation,direct_radiation,diffuse_radiation,direct_normal_irradiance",
  "latitude": 25.2048,
  "longitude": 55.2708,
  "models": "era5",
  "start_date": "2023-07-15",
  "temperature_unit": "celsius",
  "timezone": "Asia/Dubai",
  "wind_speed_unit": "ms"
}
```

### File: `backend/tests/helpers/__init__.py`
```python

```

### File: `backend/tests/helpers/environment.py`
```python
"""Test helpers for environment assumptions (Stage 12, ADR 0009).

* LEGACY / legacy(...): pin the Stage 1 proxy rules on synthetic weather that
  carries no cloud cover or soil temperature.
* with_physical_series(...): add constant cloud cover and soil temperature to a
  synthetic series so the physical default (open_ground_physical) can run.
* make_fake_fetch(...): replacement for get_historical_weather(_range) that
  asserts the right extra variables were requested.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from app.schemas.environment import LEGACY_PRESET, EnvironmentAssumptions, preset_assumptions
from app.schemas.weather import WeatherPoint, WeatherTimeSeries
from app.services.environment_model import required_weather_variables

LEGACY = preset_assumptions(LEGACY_PRESET)
PHYSICAL = EnvironmentAssumptions()
PHYSICAL_EXTRAS = required_weather_variables(PHYSICAL)

SYNTHETIC_CLOUD_COVER_PERCENT = 20.0
SYNTHETIC_SOIL_TEMPERATURE_C = 38.0


def legacy(**overrides: Any) -> EnvironmentAssumptions:
    """LEGACY with overrides, validated (model_copy(update=) would not validate)."""
    return EnvironmentAssumptions(**{**LEGACY.model_dump(), **overrides})


def physical(**overrides: Any) -> EnvironmentAssumptions:
    return EnvironmentAssumptions(**{**PHYSICAL.model_dump(), **overrides})


def with_physical_variables(
    points: Sequence[WeatherPoint],
    *,
    cloud_cover_percent: float = SYNTHETIC_CLOUD_COVER_PERCENT,
    soil_temperature_c: float = SYNTHETIC_SOIL_TEMPERATURE_C,
) -> list[WeatherPoint]:
    return [
        p.model_copy(update={
            "cloud_cover_percent": cloud_cover_percent,
            "soil_temperature_c": soil_temperature_c,
        })
        for p in points
    ]


def with_physical_series(weather: WeatherTimeSeries, **kwargs: Any) -> WeatherTimeSeries:
    return weather.model_copy(update={"points": with_physical_variables(weather.points, **kwargs)})


def make_fake_fetch(weather: WeatherTimeSeries, assumptions: EnvironmentAssumptions):
    """Async stand-in for get_historical_weather / get_historical_weather_range."""
    expected = tuple(required_weather_variables(assumptions))

    async def fake(*args: Any, extra_variables: Sequence[str] = (), **kwargs: Any) -> WeatherTimeSeries:
        assert tuple(extra_variables) == expected, (tuple(extra_variables), expected)
        return with_physical_series(weather) if extra_variables else weather

    return fake
```

### File: `backend/tests/test_api.py`
```python
import pytest


@pytest.mark.integration
def test_health_endpoint(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["service"] == (
        "radiative-cooling-api"
    )


@pytest.mark.integration
def test_simulation_endpoint(
    client,
    simulation_request,
):
    response = client.post(
        "/api/v1/simulations/run",
        json=simulation_request.model_dump(),
    )

    assert response.status_code == 200

    body = response.json()

    assert body["city"] == "Dubai"
    assert "control" in body
    assert "radiative_cooling" in body
    assert "summary" in body

    assert len(
        body["control"]["time_series"]
    ) == 121

    assert (
        body["control"]["diagnostics"]
        ["normalized_residual_percent"]
        < 1.0
    )


@pytest.mark.integration
def test_invalid_material_is_rejected(
    client,
    simulation_request,
):
    payload = simulation_request.model_dump()

    payload["rc_material"][
        "solar_reflectance"
    ] = 0.8

    payload["rc_material"][
        "solar_transmittance"
    ] = 0.4

    response = client.post(
        "/api/v1/simulations/run",
        json=payload,
    )

    assert response.status_code == 422


@pytest.mark.integration
def test_identical_material_api_improvement_is_zero(
    client,
    simulation_request,
):
    payload = simulation_request.model_dump()

    payload["rc_material"] = payload[
        "control_material"
    ].copy()

    response = client.post(
        "/api/v1/simulations/run",
        json=payload,
    )

    assert response.status_code == 200

    summary = response.json()["summary"]

    assert abs(
        summary[
            "final_skin_temperature_improvement_c"
        ]
    ) < 1e-6

    assert abs(
        summary[
            "final_core_temperature_improvement_c"
        ]
    ) < 1e-6
```

### File: `backend/tests/test_batch_single_consistency.py`
```python
"""Stage 0: the annual pipeline and a single weather run must agree on the
same exposure window (same weather slice, same materials, same summary)."""

from datetime import datetime, timedelta

import pytest

from app.core.cities import get_city
from app.schemas.simulation import WeatherSimulationRequest
from app.services import climate_adaptation
from app.services.climate_adaptation import analyze_city_climate_adaptation
from app.services.weather import slice_weather_time_series
from app.services.weather_simulation import execute_weather_simulation_with_weather
from tests.test_stage_8_resume_benchmark import SyntheticWeatherProvider, make_request
from app.services.environment_model import required_weather_variables
from tests.helpers.environment import PHYSICAL

@pytest.mark.integration
@pytest.mark.asyncio
async def test_batch_sample_matches_single_run(monkeypatch, person, control_material, rc_material):
    provider = SyntheticWeatherProvider()
    monkeypatch.setattr(climate_adaptation, "get_historical_weather_range", provider)

    request = make_request(
        person, control_material, rc_material, environment_assumptions=PHYSICAL
    ).model_copy(update={"start_month": 7, "end_month": 7})
    annual = await analyze_city_climate_adaptation(city_id="dubai", request=request)
    sample = annual["monthly_results"][0]["samples"][0]
    assert provider.extra_variables_seen == [required_weather_variables(PHYSICAL)]
    assert sample["mean_sky_temperature_c"] is not None
    start = datetime.fromisoformat(sample["sample_date_local"]).replace(tzinfo=None)

    city = get_city("dubai")
    month_weather = await provider(
        city=city,
        start_time_local=datetime(2023, 7, 1),
        end_time_local=datetime(2023, 8, 1) + timedelta(
            hours=request.local_start_hour, minutes=request.duration_minutes
        ),
        padding_hours=1,
        require_window_coverage=False,
        extra_variables=required_weather_variables(request.environment_assumptions),
    )
    sliced = slice_weather_time_series(
        weather=month_weather, start_time_local=start,
        duration_minutes=request.duration_minutes, padding_hours=1,
    )
    single = execute_weather_simulation_with_weather(
        request=WeatherSimulationRequest(
            city_id="dubai", start_time_local=start,
            duration_minutes=request.duration_minutes,
            output_interval_minutes=request.output_interval_minutes,
            person=person, control_material=control_material, rc_material=rc_material,
            environment_assumptions=request.environment_assumptions,
        ),
        weather=sliced, city_name="Dubai",
    )

    assert sample["average_skin_improvement_c"] == pytest.approx(
        single.summary.average_skin_temperature_improvement_c, abs=1e-4
    )
    assert sample["final_skin_improvement_c"] == pytest.approx(
        single.summary.final_skin_temperature_improvement_c, abs=1e-4
    )
```

### File: `backend/tests/test_body.py`
```python
import pytest

from app.schemas.simulation import PersonInput
from app.services.body import body_heat_capacities


@pytest.mark.unit
def test_default_person_reproduces_gagge_lumped_value():
    capacities = body_heat_capacities(PersonInput())

    # 3490 * 70 / 1.8 = 135 722 J/(m^2 K); alpha = 0.1
    assert capacities.total_j_m2k == pytest.approx(135_722.2, abs=0.5)
    assert capacities.skin_j_m2k == pytest.approx(13_572.2, abs=0.5)
    assert capacities.core_j_m2k == pytest.approx(122_150.0, abs=0.5)


@pytest.mark.unit
def test_heavier_person_has_larger_capacity_per_area():
    light = body_heat_capacities(PersonInput(body_mass_kg=55.0))
    heavy = body_heat_capacities(PersonInput(body_mass_kg=95.0))

    assert heavy.total_j_m2k > light.total_j_m2k


@pytest.mark.unit
def test_larger_surface_area_lowers_capacity_per_area():
    small = body_heat_capacities(PersonInput(body_surface_area_m2=1.6))
    large = body_heat_capacities(PersonInput(body_surface_area_m2=2.2))

    assert large.total_j_m2k < small.total_j_m2k
```

### File: `backend/tests/test_cities.py`
```python
import pytest

from app.core.cities import (
    CITIES,
    get_city,
)


@pytest.mark.unit
def test_get_city_returns_supported_city():
    city = get_city("dubai")

    assert city.id == "dubai"
    assert city.name == "Dubai"
    assert city.country == (
        "United Arab Emirates"
    )
    assert city.timezone == "Asia/Dubai"


@pytest.mark.unit
def test_get_city_normalizes_case_and_spaces():
    city = get_city("  DuBaI  ")

    assert city is CITIES["dubai"]


@pytest.mark.unit
@pytest.mark.parametrize(
    "city_id",
    [
        "dubai",
        "guangzhou",
        "lhasa",
    ],
)
def test_all_configured_cities_can_be_loaded(
    city_id,
):
    city = get_city(city_id)

    assert city.id == city_id
    assert city.latitude != 0
    assert city.longitude != 0
    assert city.timezone


@pytest.mark.unit
def test_get_city_rejects_unknown_city():
    with pytest.raises(
        ValueError,
        match="City not supported",
    ):
        get_city("hong-kong")


@pytest.mark.unit
def test_unknown_city_error_lists_supported_cities():
    with pytest.raises(ValueError) as error:
        get_city("unknown")

    message = str(error.value)

    assert "dubai" in message
    assert "guangzhou" in message
    assert "lhasa" in message
```

### File: `backend/tests/test_climate_adaptation.py`
```python
from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)


def make_batch_request():
    return GlobalBatchCreate(
        city_ids=[
            "dubai",
            "guangzhou",
        ],
        year=2023,
        start_month=1,
        end_month=3,
        representative_day=15,
        local_start_hour=12,
        duration_minutes=120,
        output_interval_minutes=10,
        minimum_skin_improvement_c=0.2,
        person=PersonInput(
            met=2.0,
            body_surface_area_m2=1.8,
            initial_core_temperature_c=36.8,
            initial_skin_temperature_c=33.7,
        ),
        control_material=MaterialInput(
            name="Control",
            clothing_insulation_clo=0.5,
            solar_reflectance=0.3,
            solar_transmittance=0,
            infrared_emissivity=0.9,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        ),
        rc_material=MaterialInput(
            name="RC",
            clothing_insulation_clo=0.4,
            solar_reflectance=0.92,
            solar_transmittance=0,
            infrared_emissivity=0.95,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        ),
    )


def test_global_batch_month_range():
    request = make_batch_request()

    assert request.start_month == 1
    assert request.end_month == 3
    assert len(request.city_ids) == 2


def test_global_batch_rejects_duplicate_cities():
    request = make_batch_request().model_dump()
    request["city_ids"] = [
        "dubai",
        "dubai",
    ]

    try:
        GlobalBatchCreate.model_validate(
            request
        )
        assert False
    except ValueError as error:
        assert "duplicate" in str(error)
```

### File: `backend/tests/test_climate_scenarios.py`
```python
import pytest

from app.schemas.simulation import EnvironmentInput
from app.services.two_node import simulate_material


@pytest.mark.unit
@pytest.mark.parametrize(
    (
        "name",
        "air_temperature",
        "humidity",
        "wind_speed",
        "solar_radiation",
    ),
    [
        (
            "hot_dry",
            42.0,
            20.0,
            2.0,
            900.0,
        ),
        (
            "hot_humid",
            34.0,
            85.0,
            1.0,
            700.0,
        ),
        (
            "high_altitude_solar",
            24.0,
            25.0,
            2.5,
            1000.0,
        ),
        (
            "night",
            30.0,
            60.0,
            0.5,
            0.0,
        ),
    ],
)
def test_typical_climate_scenarios_run_successfully(
    name,
    air_temperature,
    humidity,
    wind_speed,
    solar_radiation,
    person,
    rc_material,
):
    environment = EnvironmentInput(
        air_temperature_c=air_temperature,
        mean_radiant_temperature_c=(
            air_temperature + 5.0
        ),
        sky_temperature_c=(
            air_temperature - 12.0
        ),
        relative_humidity_percent=humidity,
        wind_speed_m_s=wind_speed,
        solar_radiation_w_m2=solar_radiation,
        sky_view_factor=0.5,
    )

    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert len(result.time_series) == 121

    assert (
        result.diagnostics
        .normalized_residual_percent
        < 1.0
    ), f"{name} Excessive energy residual"
```

### File: `backend/tests/test_clothing.py`
```python
import pytest
from pydantic import ValidationError

from app.schemas.simulation import MaterialInput
from app.services.clothing import (
    derive_evaporative_resistance_m2pa_w,
    maximum_evaporation_w_m2,
    resolve_clothing,
)
from app.services.two_node import calculate_fluxes, simulate_material


@pytest.mark.unit
def test_derived_evaporative_resistance_matches_formula():
    # 0.155 * 0.5 / (16.5 * 0.45) * 1000
    assert derive_evaporative_resistance_m2pa_w(0.5) == pytest.approx(10.4377, abs=1e-3)


@pytest.mark.unit
def test_none_resistance_is_derived_and_flagged(control_material):
    clothing = resolve_clothing(control_material)

    assert clothing.evaporative_resistance_source == "derived_from_clo"
    assert clothing.evaporative_resistance_m2pa_w == pytest.approx(
        derive_evaporative_resistance_m2pa_w(control_material.clothing_insulation_clo)
    )


@pytest.mark.unit
def test_explicit_resistance_overrides_derivation(control_material):
    material = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 30.0})
    clothing = resolve_clothing(material)

    assert clothing.evaporative_resistance_source == "material_input"
    assert clothing.evaporative_resistance_m2pa_w == pytest.approx(30.0)


@pytest.mark.unit
def test_higher_resistance_lowers_maximum_evaporation(control_material):
    low = resolve_clothing(control_material.model_copy(update={"evaporative_resistance_m2pa_w": 5.0}))
    high = resolve_clothing(control_material.model_copy(update={"evaporative_resistance_m2pa_w": 50.0}))

    e_low = maximum_evaporation_w_m2(low, 10.0, 5.6, 2.0)
    e_high = maximum_evaporation_w_m2(high, 10.0, 5.6, 2.0)

    assert e_high < e_low
    assert e_high > 0.0


@pytest.mark.unit
def test_explicit_derived_value_reproduces_none_result(environment, person, control_material):
    derived = derive_evaporative_resistance_m2pa_w(control_material.clothing_insulation_clo)
    explicit = control_material.model_copy(update={"evaporative_resistance_m2pa_w": derived})

    a = simulate_material(60, 1, environment, person, control_material)
    b = simulate_material(60, 1, environment, person, explicit)

    assert a.final_skin_temperature_c == pytest.approx(b.final_skin_temperature_c, abs=1e-8)
    assert a.clothing.evaporative_resistance_source == "derived_from_clo"
    assert b.clothing.evaporative_resistance_source == "material_input"

    # Stage 3: f_cl and the ADR 0003 solar note are always reported; only the
    # Re,cl derivation note must disappear when the value is supplied.
    assert any("evaporative_resistance" in note for note in a.assumptions_applied)
    assert not any("evaporative_resistance" in note for note in b.assumptions_applied)




@pytest.mark.unit
def test_impermeable_garment_ends_warmer(environment, person, control_material):
    permeable = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 5.0})
    impermeable = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 200.0})

    warm = simulate_material(120, 1, environment, person, impermeable)
    cool = simulate_material(120, 1, environment, person, permeable)

    assert warm.final_skin_temperature_c > cool.final_skin_temperature_c
    assert warm.time_series[-1].skin_wettedness >= cool.time_series[-1].skin_wettedness


@pytest.mark.unit
def test_infrared_transmittance_amplifies_longwave_exchange(
    environment, person, control_material
):
    opaque = control_material.model_copy(update={"infrared_emissivity": 0.5})
    transparent = opaque.model_copy(update={"infrared_transmittance": 0.4})

    # Cold radiant surroundings: the body loses heat; transmittance increases
    # the loss (more positive under the "positive = loss" convention).
    cold = environment.model_copy(
        update={"mean_radiant_temperature_c": 15.0, "sky_temperature_c": 0.0}
    )
    opaque_cold = calculate_fluxes(36.8, 33.7, cold, person, opaque)
    transparent_cold = calculate_fluxes(36.8, 33.7, cold, person, transparent)
    assert opaque_cold.longwave_radiation > 0
    assert transparent_cold.longwave_radiation > opaque_cold.longwave_radiation

    # Hot radiant surroundings well above any clothing surface temperature:
    # the body gains heat; transmittance increases the gain (more negative).
    hot = environment.model_copy(
        update={"mean_radiant_temperature_c": 60.0, "sky_temperature_c": 60.0}
    )
    opaque_hot = calculate_fluxes(36.8, 33.7, hot, person, opaque)
    transparent_hot = calculate_fluxes(36.8, 33.7, hot, person, transparent)
    assert opaque_hot.longwave_radiation < 0
    assert transparent_hot.longwave_radiation < opaque_hot.longwave_radiation

@pytest.mark.unit
def test_area_factor_is_derived_and_flagged(control_material):
    clothing = resolve_clothing(control_material)

    assert clothing.area_factor_source == "derived_from_clo"
    assert clothing.area_factor == pytest.approx(1.0 + 0.15 * 0.5)

@pytest.mark.unit
def test_explicit_area_factor_overrides_derivation(control_material):
    material = control_material.model_copy(update={"clothing_area_factor": 1.4})
    clothing = resolve_clothing(material)

    assert clothing.area_factor_source == "material_input"
    assert clothing.area_factor == pytest.approx(1.4)

@pytest.mark.unit
def test_clothing_surface_balance_is_consistent(environment, person, control_material):
    """Conduction through the textile plus absorbed solar equals what leaves
    the outer surface (ADR 0003 + ADR 0005)."""
    clothing = resolve_clothing(control_material)
    fluxes = calculate_fluxes(36.8, 33.7, environment, person, control_material, clothing)

    conduction = (33.7 - fluxes.clothing_surface_temperature_c) / clothing.dry_resistance_m2k_w
    surface_losses = fluxes.convection + fluxes.longwave_radiation - fluxes.longwave_transmitted

    assert conduction + fluxes.solar_absorbed_by_textile == pytest.approx(
        surface_losses, abs=1e-3
    )

@pytest.mark.unit
def test_nude_surface_temperature_equals_skin(environment, person, control_material):
    nude = control_material.model_copy(update={"clothing_insulation_clo": 0.0})
    fluxes = calculate_fluxes(36.8, 33.7, environment, person, nude)

    assert fluxes.clothing_surface_temperature_c == pytest.approx(33.7)
    
    
@pytest.mark.unit
def test_emissivity_plus_transmittance_above_one_is_rejected():
    with pytest.raises(ValidationError, match="infrared_emissivity"):
        MaterialInput(name="bad", infrared_emissivity=0.8, infrared_transmittance=0.3)


@pytest.mark.unit
def test_unknown_parameter_source_key_is_rejected():
    with pytest.raises(ValidationError, match="unknown material fields"):
        MaterialInput(name="bad", parameter_sources={"not_a_field": {"source_type": "measured"}})
```

### File: `backend/tests/test_cors.py`
```python
"""Tests for centralized CORS configuration."""

import pytest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient

from app.core.cors import add_cors_middleware


ALLOWED_ORIGIN = "http://localhost:3000"
DISALLOWED_ORIGIN = "https://untrusted.example.com"


def create_test_application() -> FastAPI:
    application = FastAPI()

    @application.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    add_cors_middleware(
        application,
        origins=[ALLOWED_ORIGIN],
        methods=["GET", "POST", "OPTIONS"],
        headers=["Authorization", "Content-Type"],
        expose_headers=["Content-Disposition"],
        allow_credentials=True,
    )

    return application


def test_allows_configured_origin() -> None:
    client = TestClient(create_test_application())

    response = client.get(
        "/health",
        headers={"Origin": ALLOWED_ORIGIN},
    )

    assert response.status_code == 200
    assert (
        response.headers["access-control-allow-origin"]
        == ALLOWED_ORIGIN
    )
    assert (
        response.headers["access-control-allow-credentials"]
        == "true"
    )


def test_allows_configured_preflight_request() -> None:
    client = TestClient(create_test_application())

    response = client.options(
        "/health",
        headers={
            "Origin": ALLOWED_ORIGIN,
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "Authorization",
        },
    )

    assert response.status_code == 200
    assert (
        response.headers["access-control-allow-origin"]
        == ALLOWED_ORIGIN
    )


def test_rejects_unknown_preflight_origin() -> None:
    client = TestClient(create_test_application())

    response = client.options(
        "/health",
        headers={
            "Origin": DISALLOWED_ORIGIN,
            "Access-Control-Request-Method": "GET",
        },
    )

    assert response.status_code == 400
    assert "access-control-allow-origin" not in response.headers


def test_rejects_duplicate_cors_registration() -> None:
    application = create_test_application()

    with pytest.raises(
        RuntimeError,
        match="CORS middleware has already been registered",
    ):
        add_cors_middleware(
            application,
            origins=[ALLOWED_ORIGIN],
            methods=["GET"],
            headers=["Authorization"],
            expose_headers=[],
            allow_credentials=True,
        )


def test_main_application_registers_cors_once() -> None:
    from app.main import app

    cors_middleware = [
        middleware
        for middleware in app.user_middleware
        if getattr(middleware, "cls", None) is CORSMiddleware
    ]

    assert len(cors_middleware) == 1
```

### File: `backend/tests/test_daily_maximum.py`
```python
from datetime import datetime, timedelta, timezone

import pytest

from app.schemas.global_batch import DailyAdaptationResult
from app.services.climate_analytics import detect_heatwave_events
from app.services.exposure_statistics import (
    compute_daily_maximum_air_temperature,
    compute_exposure_window_statistics,
)
from app.services.weather import slice_weather_time_series
from tests.test_exposure_statistics import make_day_weather


@pytest.mark.unit
def test_daily_maximum_differs_from_exposure_window_maximum():
    weather = make_day_weather()  # T = 20 + 0.1 i^2 rises all day, exposure 12:00-14:00

    sliced = slice_weather_time_series(
        weather=weather, start_time_local=datetime(2023, 7, 1, 12), duration_minutes=120
    )
    window_max = compute_exposure_window_statistics(sliced).maximum_air_temperature_c
    daily_max = compute_daily_maximum_air_temperature(
        weather, local_date=datetime(2023, 7, 1).date(), timezone_name="UTC"
    )

    assert window_max == pytest.approx(39.6)
    assert daily_max is None  # series ends 23:00, does not bracket 24:00 -> refuse partial day


@pytest.mark.unit
def test_daily_maximum_requires_full_day_coverage():
    weather = make_day_weather()
    extended = weather.model_copy(update={"points": weather.points + [
        weather.points[-1].model_copy(update={
            "timestamp": weather.points[-1].timestamp + timedelta(hours=1),
            "air_temperature_c": 10.0,
        })
    ]})
    daily_max = compute_daily_maximum_air_temperature(
        extended, local_date=datetime(2023, 7, 1).date(), timezone_name="UTC"
    )
    assert daily_max == pytest.approx(20.0 + 0.1 * 23 * 23)


def make_sample(day, exposure_max, daily_max):
    return DailyAdaptationResult(
        sample_date_local=datetime(2025, 7, day, 12), weight_days=1,
        mean_air_temperature_c=exposure_max - 3, maximum_air_temperature_c=exposure_max,
        daily_maximum_air_temperature_c=daily_max,
        mean_solar_radiation_w_m2=500, maximum_solar_radiation_w_m2=800,
        exposure_eligible=True, beneficial=True,
        average_skin_improvement_c=0.5, final_skin_improvement_c=0.5,
        average_core_improvement_c=0.1, maximum_skin_improvement_c=0.6,
        weather_from_cache=True,
    )


@pytest.mark.unit
def test_heatwave_uses_daily_maximum_not_exposure_window():
    # Cool noon window every day, but afternoons above 35 C for three days.
    samples = [make_sample(d, exposure_max=33.0, daily_max=37.0) for d in (1, 2, 3)]
    events = detect_heatwave_events(samples=samples, temperature_threshold_c=35, minimum_consecutive_days=3)
    assert len(events) == 1
    assert events[0].peak_air_temperature_c == 37.0


@pytest.mark.unit
def test_heatwave_refuses_samples_without_daily_maximum():
    samples = [make_sample(d, exposure_max=38.0, daily_max=None) for d in (1, 2, 3)]
    with pytest.raises(ValueError, match="daily_maximum_air_temperature_c"):
        detect_heatwave_events(samples=samples, temperature_threshold_c=35, minimum_consecutive_days=3)
```

### File: `backend/tests/test_environment_model.py`
```python
import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.environment_model import derive_environment
from tests.helpers.environment import LEGACY, legacy


@pytest.mark.unit
def test_legacy_preset_reproduces_stage_1_formulas():
    env = derive_environment(
        air_temperature_c=40.0, relative_humidity_percent=30.0,
        wind_speed_m_s=3.0, ghi_w_m2=800.0, assumptions=LEGACY,
    )

    assert env.mean_radiant_temperature_c == pytest.approx(40.0 + 0.012 * 800.0)
    assert env.sky_temperature_c == pytest.approx(40.0 - (5.0 + 10.0 * 0.7))
    assert env.sky_view_factor == 0.5
    assert env.wind_speed_m_s == pytest.approx(3.0)


@pytest.mark.unit
def test_swinbank_clear_sky():
    env = derive_environment(
        air_temperature_c=30.0, relative_humidity_percent=50.0, wind_speed_m_s=1.0,
        ghi_w_m2=0.0, assumptions=legacy(sky_temperature_method="swinbank"),
    )
    # 0.0552 * 303.15^1.5 - 273.15
    assert env.sky_temperature_c == pytest.approx(18.2, abs=0.1)


@pytest.mark.unit
def test_wind_scaling_and_negative_inputs_are_clamped():
    env = derive_environment(
        air_temperature_c=30.0, relative_humidity_percent=120.0, wind_speed_m_s=-1.0,
        ghi_w_m2=-50.0, assumptions=legacy(wind_speed_scaling_factor=0.67),
    )
    assert env.wind_speed_m_s == 0.0
    assert env.solar_radiation_w_m2 == 0.0
    assert env.relative_humidity_percent == 100.0


@pytest.mark.unit
def test_describe_mentions_every_active_rule():
    lines = EnvironmentAssumptions(sky_temperature_method="fixed_offset").describe()
    text = " ".join(lines)
    assert "T_sky = T_air - 15.0 K" in text
    assert "Sky view factor = 0.5" in text
```

### File: `backend/tests/test_exposure_statistics.py`
```python
from datetime import datetime, timedelta, timezone

import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.exposure_statistics import (
    compute_exposure_window_statistics,
    time_weighted_mean,
)
from app.services.weather import slice_weather_time_series


def make_day_weather() -> WeatherTimeSeries:
    """24 hourly points with a non-linear temperature profile so that padded
    and un-padded averages differ."""
    start = datetime(2023, 7, 1, 0, tzinfo=timezone.utc)

    points = [
        WeatherPoint(
            timestamp=start + timedelta(hours=i),
            air_temperature_c=20.0 + 0.1 * i * i,
            relative_humidity_percent=50.0,
            wind_speed_m_s=2.0,
            ghi_w_m2=float(50 * i),
            direct_radiation_w_m2=0.0,
            diffuse_radiation_w_m2=0.0,
            dni_w_m2=0.0,
        )
        for i in range(24)
    ]

    city = CityResponse(
        id="test", name="Test", country="Test",
        latitude=0, longitude=0, elevation_m=0,
        timezone="UTC", climate_type="test",
    )

    return WeatherTimeSeries(
        city=city,
        requested_start_time=start,
        requested_end_time=start + timedelta(hours=23),
        points=points,
        source=WeatherSourceMetadata(
            provider="test", dataset="test", model="test",
            latitude=0, longitude=0, elevation_m=0, timezone="UTC",
            downloaded_at=start, from_cache=True, attribution="test",
        ),
    )


@pytest.mark.unit
def test_time_weighted_mean_matches_trapezoid():
    assert time_weighted_mean([0, 1, 2], [0, 2, 4]) == pytest.approx(2.0)
    assert time_weighted_mean([0, 1, 3], [0, 0, 6]) == pytest.approx(2.0)
    assert time_weighted_mean([5], [7]) == pytest.approx(7.0)


@pytest.mark.unit
def test_statistics_use_exposure_window_not_padded_points():
    weather = make_day_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(2023, 7, 1, 12),
        duration_minutes=120,
        padding_hours=1,
    )

    stats = compute_exposure_window_statistics(sliced)

    # Knots 12:00 (34.4), 13:00 (36.9), 14:00 (39.6) -> trapezoid = 36.95
    assert stats.mean_air_temperature_c == pytest.approx(36.95)
    assert stats.maximum_air_temperature_c == pytest.approx(39.6)

    padded_arithmetic_mean = sum(
        p.air_temperature_c for p in sliced.points
    ) / len(sliced.points)  # 11:00..15:00 -> 37.5 (the old, wrong number)

    assert stats.mean_air_temperature_c != pytest.approx(padded_arithmetic_mean)


@pytest.mark.unit
@pytest.mark.parametrize("padding_hours", [1, 3, 6])
def test_statistics_are_invariant_to_padding(padding_hours):
    weather = make_day_weather()

    reference = compute_exposure_window_statistics(
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(2023, 7, 1, 12),
            duration_minutes=120,
            padding_hours=1,
        )
    )

    candidate = compute_exposure_window_statistics(
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(2023, 7, 1, 12),
            duration_minutes=120,
            padding_hours=padding_hours,
        )
    )

    assert candidate.mean_air_temperature_c == pytest.approx(
        reference.mean_air_temperature_c, abs=1e-9
    )
    assert candidate.maximum_air_temperature_c == pytest.approx(
        reference.maximum_air_temperature_c, abs=1e-9
    )
    assert candidate.mean_solar_radiation_w_m2 == pytest.approx(
        reference.mean_solar_radiation_w_m2, abs=1e-9
    )


@pytest.mark.unit
def test_half_hour_start_uses_interpolated_boundary():
    weather = make_day_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(2023, 7, 1, 12, 30),
        duration_minutes=60,
        padding_hours=1,
    )

    stats = compute_exposure_window_statistics(sliced)

    # Linear between 12:00 (34.4) and 13:00 (36.9) and 13:00..14:00 (39.6)
    t_1230 = 35.65
    t_1330 = 38.25
    expected = ((t_1230 + 36.9) / 2 * 0.5 + (36.9 + t_1330) / 2 * 0.5) / 1.0

    assert stats.mean_air_temperature_c == pytest.approx(expected)
```

### File: `backend/tests/test_frontend_mirrors.py`
```python
"""Constants duplicated in the frontend must equal the backend values."""

import re
from pathlib import Path

import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.model_parameters import get_parameter_value

FRONTEND = Path(__file__).resolve().parents[2] / "frontend" / "src" / "lib"


def _read(name: str) -> str:
    path = FRONTEND / name
    if not path.exists():
        pytest.skip("frontend sources not available")
    return path.read_text(encoding="utf-8")


@pytest.mark.unit
def test_planck_constants_match_registry():
    text = _read("planck.ts")
    expected = {
        "SECOND_RADIATION_CONSTANT": get_parameter_value("second_radiation_constant"),
        "WINDOW_LOWER_UM": get_parameter_value("atmospheric_window_lower_um"),
        "WINDOW_UPPER_UM": get_parameter_value("atmospheric_window_upper_um"),
        "EMISSIVITY_REFERENCE_K": get_parameter_value("emissivity_reference_temperature"),
    }
    for name, value in expected.items():
        match = re.search(rf"export const {name} = ([0-9.]+)", text)
        assert match, name
        assert float(match.group(1)) == pytest.approx(value), name


@pytest.mark.unit
def test_environment_defaults_match_schema():
    text = _read("environment-assumptions.ts")
    block = re.search(r"DEFAULT_ENVIRONMENT_ASSUMPTIONS[^=]*=\s*\{(.*?)\};", text, flags=re.S)
    assert block, "DEFAULT_ENVIRONMENT_ASSUMPTIONS block not found"
    pairs = dict(re.findall(r"^\s*(\w+):\s*\"?([\w.]+)\"?,?\s*$", block.group(1), flags=re.M))
    for key, value in EnvironmentAssumptions().model_dump().items():
        assert key in pairs, f"{key} missing in DEFAULT_ENVIRONMENT_ASSUMPTIONS"
        if isinstance(value, (int, float)):
            assert float(pairs[key]) == pytest.approx(value), key
        else:
            assert pairs[key] == value, key


@pytest.mark.unit
def test_environment_presets_are_mirrored():
    from app.schemas.environment import ENVIRONMENT_PRESETS
    text = _read("environment-assumptions.ts")
    for name in ENVIRONMENT_PRESETS:
        assert re.search(rf"\b{name}\b", text), f"preset {name} missing in frontend"
```

### File: `backend/tests/test_gagge_benchmark.py`
```python
import math

import pytest

from app.schemas.simulation import (
    GaggeBenchmarkRequest,
)
from app.services.gagge_benchmark import (
    run_gagge_benchmark,
)


@pytest.mark.benchmark
def test_gagge_benchmark_returns_finite_values(
    environment,
    person,
    control_material,
):
    request = GaggeBenchmarkRequest(
        duration_minutes=60,
        environment=environment,
        person=person,
        material=control_material,
    )

    result = run_gagge_benchmark(request)

    assert math.isfinite(
        result.gagge.core_temperature_c
    )

    assert math.isfinite(
        result.gagge.skin_temperature_c
    )

    assert math.isfinite(
        result.prototype.core_temperature_c
    )

    assert math.isfinite(
        result.prototype.skin_temperature_c
    )


@pytest.mark.benchmark
def test_gagge_output_is_in_broad_range(
    environment,
    person,
    control_material,
):
    request = GaggeBenchmarkRequest(
        duration_minutes=60,
        environment=environment,
        person=person,
        material=control_material,
    )

    result = run_gagge_benchmark(request)

    assert (
        34.0
        < result.gagge.core_temperature_c
        < 42.0
    )

    assert (
        15.0
        < result.gagge.skin_temperature_c
        < 45.0
    )

    assert result.gagge.skin_evaporation_w_m2 >= 0


@pytest.mark.integration
def test_gagge_benchmark_api(
    client,
    environment,
    person,
    control_material,
):
    response = client.post(
        "/api/v1/benchmarks/gagge",
        json={
            "duration_minutes": 60,
            "environment": (
                environment.model_dump()
            ),
            "person": person.model_dump(),
            "material": (
                control_material.model_dump()
            ),
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["reference_model"] == (
        "Gagge Two-Node"
    )

    assert "prototype" in body
    assert "gagge" in body

import pytest
from fastapi import HTTPException

from app.api import benchmarks


@pytest.mark.unit
def test_gagge_api_converts_service_error_to_500(
    monkeypatch,
):
    def fake_run_gagge_benchmark(request):
        raise ValueError(
            "invalid benchmark input"
        )

    monkeypatch.setattr(
        benchmarks,
        "run_gagge_benchmark",
        fake_run_gagge_benchmark,
    )

    with pytest.raises(
        HTTPException,
    ) as error:
        benchmarks.compare_with_gagge(
            object()
        )

    assert error.value.status_code == 500
    assert (
        "invalid benchmark input"
        in error.value.detail
    )
    
@pytest.mark.benchmark
def test_benchmark_returns_aligned_transient_series(environment, person, control_material):
    request = GaggeBenchmarkRequest(
        duration_minutes=90, environment=environment, person=person, material=control_material
    )

    result = run_gagge_benchmark(request)

    assert len(result.time_series) == 91
    assert result.time_series[0].minute == 0
    assert result.time_series[-1].minute == 90
    assert result.core_temperature.maximum_absolute_difference_c >= abs(
        result.core_temperature.final_difference_c
    )
    assert result.reference_port_parity.maximum_absolute_difference_c < 0.05
    assert any("solar_radiation" in note for note in result.alignment_applied)


@pytest.mark.benchmark
def test_default_case_is_within_stage_3_tolerances(environment, person, control_material):
    """Acceptance criterion of Stage 3 for the reference scenario."""
    result = run_gagge_benchmark(
        GaggeBenchmarkRequest(environment=environment, person=person, material=control_material)
    )

    assert result.core_temperature.passed, result.core_temperature
    assert result.skin_temperature.passed, result.skin_temperature
    assert result.passed
    
@pytest.mark.benchmark
def test_sitting_posture_runs_and_reports_seated_area_ratio(
    environment, person, control_material
):
    result = run_gagge_benchmark(
        GaggeBenchmarkRequest(
            environment=environment,
            person=person.model_copy(update={"position": "sitting"}),
            material=control_material,
        )
    )
    assert result.reference_port_parity.maximum_absolute_difference_c < 0.05
```

### File: `backend/tests/test_gagge_reference.py`
```python
import math

import pytest
from pythermalcomfort.models import two_nodes_gagge

from app.services.gagge_reference import run_gagge_reference


PARITY_TOLERANCE_C = 0.05

CASES = [
    # tdb, tr, v, rh, met, clo
    (38.0, 45.0, 1.5, 40.0, 2.6, 0.5),
    (30.0, 30.0, 0.3, 60.0, 1.2, 0.6),
    (42.0, 42.0, 2.0, 20.0, 2.0, 0.4),
    (34.0, 36.0, 1.0, 85.0, 1.8, 0.5),
    (25.0, 25.0, 0.1, 50.0, 1.0, 1.0),
]


@pytest.mark.benchmark
@pytest.mark.parametrize(("tdb", "tr", "v", "rh", "met", "clo"), CASES)
def test_port_matches_library_after_sixty_minutes(tdb, tr, v, rh, met, clo):
    library = two_nodes_gagge(
        tdb=tdb, tr=tr, v=v, rh=rh, met=met, clo=clo, wme=0,
        body_surface_area=1.8, p_atm=101325, position="standing",
        max_skin_blood_flow=90, max_sweating=500, round_output=False,
    )

    port = run_gagge_reference(
        tdb=tdb, tr=tr, v=v, rh=rh, met=met, clo=clo,
        body_surface_area=1.8, body_mass_kg=70.0, duration_minutes=60,
    ).final

    assert port.core_temperature_c == pytest.approx(
        float(library.t_core), abs=PARITY_TOLERANCE_C
    )
    assert port.skin_temperature_c == pytest.approx(
        float(library.t_skin), abs=PARITY_TOLERANCE_C
    )
    assert port.skin_wettedness == pytest.approx(float(library.w), abs=0.02)


@pytest.mark.unit
def test_port_returns_one_point_per_minute_plus_initial_state():
    result = run_gagge_reference(
        tdb=38.0, tr=45.0, v=1.5, rh=40.0, met=2.6, clo=0.5, duration_minutes=90
    )

    assert len(result.points) == 91
    assert result.points[0].minute == 0
    assert result.points[0].skin_temperature_c == 33.7
    assert result.points[-1].minute == 90
    assert all(math.isfinite(p.core_temperature_c) for p in result.points)


@pytest.mark.unit
def test_heavier_body_warms_more_slowly():
    light = run_gagge_reference(
        tdb=40.0, tr=40.0, v=0.5, rh=40.0, met=2.0, clo=0.5, body_mass_kg=55.0
    ).final
    heavy = run_gagge_reference(
        tdb=40.0, tr=40.0, v=0.5, rh=40.0, met=2.0, clo=0.5, body_mass_kg=95.0
    ).final

    assert heavy.core_temperature_c < light.core_temperature_c
```

### File: `backend/tests/test_global_batch_geojson.py`
```python
def test_geojson_structure():
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        55.2708,
                        25.2048,
                    ],
                },
                "properties": {
                    "city_id": "dubai",
                    "climate_adaptation_rate_percent": 75,
                },
            }
        ],
    }

    assert geojson["type"] == (
        "FeatureCollection"
    )

    assert (
        geojson["features"][0]
        ["geometry"]["type"]
        == "Point"
    )
```

### File: `backend/tests/test_global_batches_api.py`
```python
"""Regression: material library links must be persisted for global batches."""

from types import SimpleNamespace

import pytest

from app.api import global_batches as global_batches_api


def fake_submit_city_tasks(*, city_results, queue_name):
    return SimpleNamespace(
        id="group-test",
        results=[
            SimpleNamespace(id=f"task-{result.city_id}") for result in city_results
        ],
    )


@pytest.mark.integration
def test_global_batch_records_material_version_links(
    client, monkeypatch, person, control_material
):
    monkeypatch.setattr(
        global_batches_api, "submit_city_tasks", fake_submit_city_tasks
    )

    created = client.post(
        "/api/v1/materials",
        json={
            "name": "Batch Link Fabric",
            "slug": "batch-link-fabric",
            "initial_version": {
                "clothing_insulation_clo": 0.4,
                "solar_reflectance": 0.92,
                "infrared_emissivity": 0.95,
            },
        },
    )
    assert created.status_code == 201, created.text
    version_id = created.json()["versions"][0]["id"]

    response = client.post(
        "/api/v1/global-batches",
        json={
            "city_ids": ["dubai"],
            "year": 2023,
            "start_month": 7,
            "end_month": 7,
            "person": person.model_dump(mode="json"),
            "control_material": control_material.model_dump(mode="json"),
            "rc_material": {"name": "RC", "material_version_id": version_id},
        },
    )
    assert response.status_code == 202, response.text

    body = response.json()
    assert body["rc_material_version_id"] == version_id
    assert body["control_material_version_id"] is None
    assert body["celery_group_id"] == "group-test"

    detail = client.get(f"/api/v1/global-batches/{body['id']}").json()
    assert detail["request"]["rc_material"]["solar_reflectance"] == pytest.approx(0.92)
    assert detail["city_results"][0]["celery_task_id"] == "task-dubai"
```

### File: `backend/tests/test_golden_dubai_2h.py`
```python
"""Golden regression case: Dubai, 2023-07-15 12:00 local, two hours.

Offline: the Open-Meteo payload is a frozen fixture. First run (or
UPDATE_GOLDEN=1) writes expected_results.json; subsequent runs compare.
"""

import json
import os
from pathlib import Path

import pytest

from app.schemas.simulation import WeatherSimulationRequest
from app.services.reproducibility import (
    compare_regression_payloads,
    summarize_result_for_regression,
)
from app.services.weather_simulation import execute_weather_simulation
from tests.helpers.environment import LEGACY


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "dubai_2h"
PAYLOAD_PATH = FIXTURE_DIR / "open_meteo_payload.json"
REQUEST_PATH = FIXTURE_DIR / "request.json"
EXPECTED_PATH = FIXTURE_DIR / "expected_results.json"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_dubai_two_hour_golden_case(monkeypatch):
    if not PAYLOAD_PATH.exists():
        pytest.skip(
            "Fixture missing. Run: python scripts/capture_weather_fixture.py "
            "tests/fixtures/dubai_2h"
        )

    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))

    async def fake_request_open_meteo(params):
        return payload, True

    monkeypatch.setattr(
        "app.services.weather.request_open_meteo",
        fake_request_open_meteo,
    )

    request = WeatherSimulationRequest.model_validate(
        json.loads(REQUEST_PATH.read_text(encoding="utf-8"))
    )
    request = request.model_copy(
        update={"environment_assumptions": LEGACY}
    )

    result = await execute_weather_simulation(request)
    actual = summarize_result_for_regression(result)

    if os.environ.get("UPDATE_GOLDEN") == "1" or not EXPECTED_PATH.exists():
        EXPECTED_PATH.write_text(
            json.dumps(actual, indent=2, sort_keys=True), encoding="utf-8"
        )
        pytest.fail(
            f"Wrote new golden file {EXPECTED_PATH}. Review, commit, and re-run."
        )

    expected = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))

    differences = compare_regression_payloads(expected, actual)

    assert not differences, "\n".join(differences)

    # Sanity: the fixture must be clean data, otherwise the case is not golden.
    quality = actual["weather"]["quality"]
    assert quality["gaps"] == []
    assert quality["duplicates_removed"] == 0
```

### File: `backend/tests/test_job_service.py`
```python
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.models.simulation_job import (
    SimulationJob,
)
from app.services.job_service import (
    get_job_or_none,
    job_to_detail,
    job_to_response,
)


def make_job(
    *,
    simulation_request,
):
    now = datetime.now(timezone.utc)

    return SimpleNamespace(
        id="job-123",
        celery_task_id="task-456",
        status="completed",
        stage="completed",
        progress=100,
        city_id="dubai",
        summary_json={
            "final_skin_temperature_improvement_c": 1.2,
        },
        error_message=None,
        request_json={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
            "output_interval_minutes": 1,
            "person": (
                simulation_request
                .person.model_dump(
                    mode="json"
                )
            ),
            "control_material": (
                simulation_request
                .control_material.model_dump(
                    mode="json"
                )
            ),
            "rc_material": (
                simulation_request
                .rc_material.model_dump(
                    mode="json"
                )
            ),
        },
        created_at=now,
        updated_at=now,
        started_at=now,
        completed_at=now,
    )


@pytest.mark.unit
def test_job_to_response_maps_job_fields(
    simulation_request,
):
    job = make_job(
        simulation_request=simulation_request,
    )

    response = job_to_response(job)

    assert response.id == "job-123"
    assert response.celery_task_id == "task-456"
    assert response.status == "completed"
    assert response.stage == "completed"
    assert response.progress == 100
    assert response.city_id == "dubai"
    assert response.error_message is None
    assert response.summary == {
        "final_skin_temperature_improvement_c": 1.2,
    }


@pytest.mark.unit
def test_job_to_detail_validates_saved_request(
    simulation_request,
):
    job = make_job(
        simulation_request=simulation_request,
    )

    detail = job_to_detail(job)

    assert detail.id == "job-123"
    assert detail.request.city_id == "dubai"
    assert (
        detail.request.duration_minutes
        == 120
    )
    assert (
        detail.request.person.met
        == simulation_request.person.met
    )
    assert (
        detail.request.control_material.name
        == simulation_request
        .control_material.name
    )


@pytest.mark.unit
def test_get_job_or_none_uses_session_get():
    expected_job = object()
    session = Mock()
    session.get.return_value = expected_job

    result = get_job_or_none(
        session=session,
        job_id="job-123",
    )

    assert result is expected_job
    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )


@pytest.mark.unit
def test_get_job_or_none_returns_none():
    session = Mock()
    session.get.return_value = None

    result = get_job_or_none(
        session=session,
        job_id="missing-job",
    )

    assert result is None
```

### File: `backend/tests/test_longwave.py`
```python
import pytest
from pydantic import ValidationError

from app.schemas.simulation import MaterialInput
from app.services.clothing import resolve_clothing
from app.services.longwave import radiant_field, resolve_longwave_optics
from app.services.two_node import calculate_fluxes, simulate_material


KELVIN = 273.15


@pytest.mark.unit
def test_field_total_equals_gray_environment(environment):
    field = radiant_field(environment)
    f = environment.sky_view_factor
    expected = (
        f * (environment.sky_temperature_c + KELVIN) ** 4
        + (1 - f) * (environment.mean_radiant_temperature_c + KELVIN) ** 4
    )
    assert field.total_k4 == pytest.approx(expected, rel=1e-9)
    assert 0.0 < field.sky_window_emissivity < 1.0


@pytest.mark.unit
def test_equal_band_emissivities_reproduce_the_gray_path(environment, person, control_material):
    selective = control_material.model_copy(
        update={"infrared_emissivity_window": control_material.infrared_emissivity}
    )
    assert resolve_longwave_optics(selective).selective

    gray = calculate_fluxes(36.8, 33.7, environment, person, control_material)
    split = calculate_fluxes(36.8, 33.7, environment, person, selective)

    assert split.longwave_radiation == pytest.approx(gray.longwave_radiation, abs=1e-6)
    assert split.clothing_surface_temperature_c == pytest.approx(
        gray.clothing_surface_temperature_c, abs=1e-6
    )
    assert gray.longwave_window is None and split.longwave_window is not None


@pytest.mark.unit
def test_selective_emitter_loses_more_heat_in_hot_surroundings(environment, person, control_material):
    hot = environment.model_copy(update={"mean_radiant_temperature_c": 55.0, "sky_temperature_c": 18.0})
    gray = control_material.model_copy(update={"infrared_emissivity": 0.5})
    selective = MaterialInput.model_validate(
        {**gray.model_dump(), "infrared_emissivity_window": 0.95}
    )

    gray_flux = calculate_fluxes(36.8, 33.7, hot, person, gray)
    selective_flux = calculate_fluxes(36.8, 33.7, hot, person, selective)

    assert selective_flux.longwave_radiation > gray_flux.longwave_radiation


@pytest.mark.unit
def test_inconsistent_band_split_is_rejected():
    with pytest.raises(ValidationError, match="out-of-window emissivity"):
        MaterialInput(name="bad", infrared_emissivity=0.9, infrared_emissivity_window=0.0)


@pytest.mark.unit
def test_selective_surface_balance_and_energy(environment, person, rc_material):
    selective = MaterialInput.model_validate(
        {**rc_material.model_dump(), "infrared_emissivity": 0.6, "infrared_emissivity_window": 0.95}
    )
    clothing = resolve_clothing(selective)
    fluxes = calculate_fluxes(36.8, 33.7, environment, person, selective, clothing)

    conduction = (33.7 - fluxes.clothing_surface_temperature_c) / clothing.dry_resistance_m2k_w
    losses = fluxes.convection + fluxes.longwave_radiation - fluxes.longwave_transmitted
    assert conduction + fluxes.solar_absorbed_by_textile == pytest.approx(losses, abs=1e-3)

    result = simulate_material(120, 1, environment, person, selective)
    assert result.diagnostics.normalized_residual_percent < 1.0
    assert result.clothing.infrared_emissivity_window == pytest.approx(0.95)
    assert any("selective longwave emitter" in note for note in result.assumptions_applied)
```

### File: `backend/tests/test_material_fields.py`
```python
import pytest
from pydantic import ValidationError

from app.schemas.provenance import MATERIAL_PHYSICAL_FIELD_ORDER
from app.schemas.simulation import MaterialInput
from app.services.material_fields import build_material_field_manifest
from app.services.planck import broadband_emissivity


@pytest.mark.unit
def test_manifest_covers_every_physical_field_in_order():
    manifest = build_material_field_manifest()
    assert [f.name for f in manifest.fields] == list(MATERIAL_PHYSICAL_FIELD_ORDER)
    assert manifest.parameter_set_version == "5.0.0"
    assert "absorbed_solar_to_body_fraction" not in [f.name for f in manifest.fields]

@pytest.mark.unit
def test_deprecated_field_is_still_accepted_in_provenance():
    MaterialInput(
        name="legacy",
        parameter_sources={"absorbed_solar_to_body_fraction": {"source_type": "assumed"}},
    )

@pytest.mark.unit
@pytest.mark.parametrize("name", MATERIAL_PHYSICAL_FIELD_ORDER)
def test_manifest_bounds_match_validation(name):
    descriptor = next(f for f in build_material_field_manifest().fields if f.name == name)

    assert descriptor.unit
    assert descriptor.description
    assert descriptor.minimum is not None and descriptor.maximum is not None

    base = {"name": "x", "solar_reflectance": 0.0, "infrared_emissivity": 0.0}

    def with_value(value):
        payload = {**base, name: value}
        if name == "infrared_emissivity_window":
            # keep the implied eps_N at 0.5 so only the field's own bound is tested
            payload["infrared_emissivity"] = broadband_emissivity(min(max(value, 0.0), 1.0), 0.5)
        return payload

    MaterialInput(**with_value(descriptor.minimum))
    MaterialInput(**with_value(descriptor.maximum))
    with pytest.raises(ValidationError):
        MaterialInput(**with_value(descriptor.minimum - 1e-6))
    with pytest.raises(ValidationError):
        MaterialInput(**with_value(descriptor.maximum + 1e-6))


@pytest.mark.unit
def test_nullable_fields_declare_their_derivation():
    for field in build_material_field_manifest().fields:
        assert field.nullable == (field.derived_when_null is not None), field.name
```

### File: `backend/tests/test_material_resolution.py`
```python
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.schemas.simulation import MaterialInput, WeatherSimulationRequest
from app.services.material_resolution import (
    MaterialParameterConflictError,
    MaterialVersionInvalidError,
    MaterialVersionNotFoundError,
    material_input_from_version,
    resolve_material_input,
    resolve_request_materials,
)


def make_version(**overrides) -> SimpleNamespace:
    values = dict(
        id="ver-1",
        version_number=2,
        material=SimpleNamespace(name="Cool Fabric"),
        clothing_insulation_clo=0.4,
        evaporative_resistance_m2pa_w=18.0,
        clothing_area_factor=None,
        solar_reflectance=0.92,
        solar_transmittance=0.0,
        infrared_emissivity=0.95,
        infrared_transmittance=0.0,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
        source_type="measured",
        source_reference="Lab report 12",
        parameter_sources_json={"solar_reflectance": {"source_type": "measured"}},
    )
    values.update(overrides)
    return SimpleNamespace(**values)


def make_session(version) -> Mock:
    session = Mock()
    session.scalar.return_value = version
    return session


@pytest.mark.unit
def test_input_without_version_id_is_returned_untouched():
    material = MaterialInput(name="Control")
    session = Mock()

    assert resolve_material_input(session, material) is material
    session.scalar.assert_not_called()


@pytest.mark.unit
def test_omitted_fields_are_hydrated_from_the_version():
    resolved = resolve_material_input(
        make_session(make_version()),
        MaterialInput(name="RC", material_version_id="ver-1"),
    )

    assert resolved.name == "RC"
    assert resolved.clothing_insulation_clo == 0.4
    assert resolved.evaporative_resistance_m2pa_w == 18.0
    assert resolved.solar_reflectance == 0.92
    assert resolved.source_type == "measured"
    assert resolved.source_reference == "Lab report 12"
    assert resolved.parameter_sources["solar_reflectance"].source_type == "measured"


@pytest.mark.unit
def test_matching_explicit_values_are_accepted():
    resolved = resolve_material_input(
        make_session(make_version()),
        MaterialInput(
            name="RC", material_version_id="ver-1",
            clothing_insulation_clo=0.4, solar_reflectance=0.92,
        ),
    )
    assert resolved.material_version_id == "ver-1"


@pytest.mark.unit
def test_conflicting_explicit_value_is_rejected():
    with pytest.raises(MaterialParameterConflictError) as error:
        resolve_material_input(
            make_session(make_version()),
            MaterialInput(name="RC", material_version_id="ver-1", solar_reflectance=0.5),
        )

    detail = error.value.to_detail()
    assert detail["code"] == "MATERIAL_PARAMETER_CONFLICT"
    assert detail["conflicts"][0]["field"] == "solar_reflectance"


@pytest.mark.unit
def test_explicit_null_against_stored_value_is_a_conflict():
    with pytest.raises(MaterialParameterConflictError):
        resolve_material_input(
            make_session(make_version()),
            MaterialInput(name="RC", material_version_id="ver-1", evaporative_resistance_m2pa_w=None),
        )


@pytest.mark.unit
def test_unknown_version_raises():
    with pytest.raises(MaterialVersionNotFoundError):
        resolve_material_input(make_session(None), MaterialInput(name="RC", material_version_id="ghost"))


@pytest.mark.unit
def test_legacy_version_outside_bounds_is_reported():
    with pytest.raises(MaterialVersionInvalidError, match="cannot be used"):
        material_input_from_version(make_version(evaporative_resistance_m2pa_w=5000.0))


@pytest.mark.unit
def test_display_name_is_truncated_to_input_limit():
    version = make_version(material=SimpleNamespace(name="x" * 150))
    assert len(material_input_from_version(version).name) == 100


@pytest.mark.unit
def test_request_level_resolution_only_replaces_linked_materials(person, control_material):
    request = WeatherSimulationRequest(
        start_time_local="2023-07-15T12:00:00",
        person=person,
        control_material=control_material,
        rc_material=MaterialInput(name="RC", material_version_id="ver-1"),
    )

    resolved = resolve_request_materials(make_session(make_version()), request)

    assert resolved is not request
    assert resolved.control_material is control_material
    assert resolved.rc_material.solar_reflectance == 0.92
```

### File: `backend/tests/test_materials_api.py`
```python
from types import SimpleNamespace

import pytest

from app.api import simulations as simulations_api


@pytest.mark.integration
def test_material_library_round_trip(client, monkeypatch, simulation_request):
    created = client.post(
        "/api/v1/materials",
        json={
            "name": "PR-4 Test Fabric",
            "slug": "pr-4-test-fabric",
            "institution": "Test Lab",
            # 刪掉外層的 infrared_emissivity_window
            "initial_version": {
                "clothing_insulation_clo": 0.4,
                "evaporative_resistance_m2pa_w": 18.0,
                "solar_reflectance": 0.92,
                "infrared_emissivity": 0.95,
                "infrared_emissivity_window": 0.97,  # ← 放這裡
                "source_type": "measured",
                "parameter_sources": {
                    "solar_reflectance": {
                        "source_type": "measured",
                        "reference": "UV-Vis-NIR, 2024-03",
                    }
                },
            },
        },
    )
    assert created.status_code == 201, created.text
    version_id = created.json()["versions"][0]["id"]

    listing = client.get("/api/v1/materials/versions").json()
    assert any(item["id"] == version_id for item in listing["items"])

    simulation_input = client.get(
        f"/api/v1/materials/versions/{version_id}/simulation-input"
    ).json()
    assert simulation_input["name"] == "PR-4 Test Fabric v1"
    assert simulation_input["material_version_id"] == version_id
    assert simulation_input["infrared_emissivity_window"] == pytest.approx(0.97)

    # Hydration: only the id is sent.
    body = simulation_request.model_dump(mode="json")
    body["rc_material"] = {"name": "RC from library", "material_version_id": version_id}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 200, response.text
    rc = response.json()["radiative_cooling"]
    assert rc["material_name"] == "RC from library"
    assert rc["clothing"]["evaporative_resistance_source"] == "material_input"
    assert rc["clothing"]["evaporative_resistance_m2pa_w"] == pytest.approx(18.0)

    # Conflict: id plus a different value.
    body["rc_material"] = {"name": "Edited", "material_version_id": version_id, "solar_reflectance": 0.5}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "MATERIAL_PARAMETER_CONFLICT"

    # Unknown id.
    body["rc_material"] = {"name": "Ghost", "material_version_id": "does-not-exist"}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "MATERIAL_VERSION_NOT_FOUND"

    # Job link is recorded and queryable.
    monkeypatch.setattr(
        simulations_api,
        "run_weather_simulation_task",
        SimpleNamespace(delay=lambda job_id: SimpleNamespace(id="celery-test-task")),
    )
    job = client.post(
        "/api/v1/simulations/jobs",
        json={
            "city_id": "dubai",
            "start_time_local": "2023-07-15T12:00:00",
            "duration_minutes": 120,
            "output_interval_minutes": 10,
            "person": body["person"],
            "control_material": body["control_material"],
            "rc_material": {"name": "RC", "material_version_id": version_id},
        },
    )
    assert job.status_code == 202, job.text
    assert job.json()["rc_material_version_id"] == version_id
    assert job.json()["control_material_version_id"] is None

    detail = client.get(f"/api/v1/simulations/jobs/{job.json()['id']}").json()
    assert detail["request"]["rc_material"]["solar_reflectance"] == pytest.approx(0.92)

    listed = client.get("/api/v1/simulations/jobs", params={"material_version_id": version_id}).json()
    assert any(item["id"] == job.json()["id"] for item in listed["items"])


@pytest.mark.integration
def test_version_with_unknown_provenance_key_is_rejected_on_write(client):
    response = client.post(
        "/api/v1/materials",
        json={
            "name": "Bad provenance",
            "slug": "bad-provenance",
            "initial_version": {"parameter_sources": {"not_a_field": {"source_type": "measured"}}},
        },
    )
    assert response.status_code == 422
```

### File: `backend/tests/test_materials_update_delete.py`
```python
"""Material metadata update (PATCH) and delete (DELETE)."""

from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.api import simulations as simulations_api


def create_material(client) -> dict:
    suffix = uuid4().hex[:8]
    response = client.post(
        "/api/v1/materials",
        json={
            "name": f"Edit Fabric {suffix}",
            "slug": f"edit-fabric-{suffix}",
            "description": "original",
            "institution": "Test Lab",
            "initial_version": {
                "clothing_insulation_clo": 0.4,
                "solar_reflectance": 0.92,
                "infrared_emissivity": 0.95,
            },
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


@pytest.mark.integration
def test_patch_changes_only_given_fields(client):
    material = create_material(client)

    response = client.patch(
        f"/api/v1/materials/{material['id']}", json={"description": "  updated  "}
    )

    assert response.status_code == 200, response.text
    body = response.json()
    assert body["description"] == "updated"
    assert body["name"] == material["name"]
    assert body["institution"] == "Test Lab"
    assert len(body["versions"]) == 1


@pytest.mark.integration
def test_patch_clears_optional_text_with_blank(client):
    material = create_material(client)
    body = client.patch(
        f"/api/v1/materials/{material['id']}", json={"institution": "   "}
    ).json()
    assert body["institution"] is None


@pytest.mark.integration
@pytest.mark.parametrize(
    "payload",
    [{"name": None}, {"name": "   "}, {"is_archived": None}, {"slug": "renamed"}],
)
def test_patch_rejects_invalid_payload(client, payload):
    material = create_material(client)
    response = client.patch(f"/api/v1/materials/{material['id']}", json=payload)
    assert response.status_code == 422


@pytest.mark.integration
def test_patch_and_delete_missing_material_return_404(client):
    assert client.patch("/api/v1/materials/nope", json={"name": "x"}).status_code == 404
    assert client.delete("/api/v1/materials/nope").status_code == 404


@pytest.mark.integration
def test_unreferenced_material_is_deleted_with_its_versions(client):
    material = create_material(client)
    version_id = material["versions"][0]["id"]

    response = client.delete(f"/api/v1/materials/{material['id']}")

    assert response.status_code == 204
    assert client.get(f"/api/v1/materials/{material['id']}").status_code == 404
    assert client.get(
        f"/api/v1/materials/versions/{version_id}/simulation-input"
    ).status_code == 404


@pytest.mark.integration
def test_referenced_material_cannot_be_deleted_but_can_be_archived(
    client, monkeypatch, simulation_request
):
    material = create_material(client)
    version_id = material["versions"][0]["id"]

    monkeypatch.setattr(
        simulations_api,
        "run_weather_simulation_task",
        SimpleNamespace(delay=lambda job_id: SimpleNamespace(id="celery-test-task")),
    )
    base = simulation_request.model_dump(mode="json")
    job = client.post(
        "/api/v1/simulations/jobs",
        json={
            "city_id": "dubai",
            "start_time_local": "2023-07-15T12:00:00",
            "duration_minutes": 120,
            "output_interval_minutes": 10,
            "person": base["person"],
            "control_material": base["control_material"],
            "rc_material": {"name": "RC", "material_version_id": version_id},
        },
    )
    assert job.status_code == 202, job.text

    blocked = client.delete(f"/api/v1/materials/{material['id']}")
    assert blocked.status_code == 409
    detail = blocked.json()["detail"]
    assert detail["code"] == "MATERIAL_IN_USE"
    assert detail["simulation_job_count"] == 1
    assert detail["global_batch_count"] == 0
    assert client.get(f"/api/v1/materials/{material['id']}").status_code == 200

    archived = client.patch(
        f"/api/v1/materials/{material['id']}", json={"is_archived": True}
    )
    assert archived.status_code == 200
    assert archived.json()["is_archived"] is True

    hidden = client.get("/api/v1/materials", params={"search": material["name"]}).json()
    assert all(item["id"] != material["id"] for item in hidden["items"])

    shown = client.get(
        "/api/v1/materials",
        params={"search": material["name"], "include_archived": "true"},
    ).json()
    assert any(item["id"] == material["id"] for item in shown["items"])

    picker = client.get(
        "/api/v1/materials/versions", params={"material_id": material["id"]}
    ).json()
    assert picker["items"] == []
```

### File: `backend/tests/test_model_parameters.py`
```python
import re

import pytest

from app.services import model_parameters as mp


@pytest.mark.unit
def test_every_parameter_has_unit_and_reference():
    for parameter in mp.list_model_parameters():
        assert parameter.unit, parameter.name
        assert parameter.reference, parameter.name


@pytest.mark.unit
def test_manifest_sha_is_stable_and_hex():
    first = mp.model_parameter_set_sha256()
    assert re.fullmatch(r"[0-9a-f]{64}", first)
    assert first == mp.model_parameter_set_sha256()


@pytest.mark.unit
def test_unknown_parameter_raises():
    with pytest.raises(KeyError, match="Unknown model parameter"):
        mp.get_parameter_value("does_not_exist")


@pytest.mark.api
def test_model_parameter_endpoint(client):
    response = client.get("/api/v1/model/parameters")
    assert response.status_code == 200
    body = response.json()
    assert body["parameter_set_version"] == mp.MODEL_PARAMETER_SET_VERSION
    assert len(body["parameters"]) == len(mp.MODEL_PARAMETERS)


@pytest.mark.api
def test_default_assumptions_endpoint(client):
    response = client.get("/api/v1/model/environment-assumptions/defaults")
    assert response.status_code == 200
    assert response.json()["sky_view_factor"] == 0.5
    
@pytest.mark.api
def test_model_metadata_endpoint(client):
    body = client.get("/api/v1/model/metadata").json()
    assert body["parameter_set_version"] == mp.MODEL_PARAMETER_SET_VERSION
    assert body["parameter_set_sha256"] == mp.model_parameter_set_sha256()


@pytest.mark.api
def test_single_parameter_endpoint(client):
    assert client.get("/api/v1/model/parameters/clo_to_si").json()["value"] == 0.155
    assert client.get("/api/v1/model/parameters/nope").status_code == 404


@pytest.mark.api
def test_material_fields_endpoint(client):
    body = client.get("/api/v1/model/material-fields").json()
    names = [f["name"] for f in body["fields"]]
    assert "evaporative_resistance_m2pa_w" in names
    assert body["fields"][0]["unit"] == "clo"
```

### File: `backend/tests/test_optimization.py`
```python
from types import SimpleNamespace

import numpy as np
import pytest
from pydantic import ValidationError

from app.api import optimizations as optimizations_api
from app.schemas.optimization import (
    DecisionVariable,
    EvaluationMetrics,
    MetricConstraint,
    OptimizationCreate,
    RequirementMapSpec,
)
from app.services.optimization.evaluator import MaterialEvaluator, PreparedSample
from app.services.optimization.metrics import fraction_above
from app.services.optimization.requirement_map import build_requirement_map
from app.services.optimization.runner import OptimizationCancelled, run_differential_evolution
from app.services.optimization.search_space import build_search_space
from app.services.optimization.service import estimate_optimization
from app.services.two_node import simulate_material_with_interpolator
from app.services.weather_interpolation import WeatherInterpolator
from tests.helpers.environment import LEGACY


RHO_EPS = [
    DecisionVariable(name="solar_reflectance", lower=0.3, upper=0.98),
    DecisionVariable(name="infrared_emissivity", lower=0.5, upper=0.99),
]


def make_request(person, control_material, rc_material, **overrides) -> OptimizationCreate:
    payload = dict(
        city_id="dubai", months=[7], duration_minutes=120, output_interval_minutes=10,
        person=person, control_material=control_material, base_material=rc_material,
        variables=RHO_EPS, requirement_map=RequirementMapSpec(resolution=3),
        population_multiplier=4, max_generations=2,
        environment_assumptions=LEGACY,
    )
    payload.update(overrides)
    return OptimizationCreate(**payload)


# --- metrics -----------------------------------------------------------------

@pytest.mark.unit
def test_fraction_above_is_exact_for_linear_segments():
    assert fraction_above([0, 10], [30, 40], 35) == pytest.approx(0.5)
    assert fraction_above([0, 10, 20], [36, 36, 34], 35) == pytest.approx(0.75)
    assert fraction_above([0, 10], [30, 31], 35) == 0.0


# --- schema / search space -------------------------------------------------

@pytest.mark.unit
def test_map_axes_must_be_decision_variables(person, control_material, rc_material):
    with pytest.raises(ValidationError, match="requirement_map axes"):
        make_request(person, control_material, rc_material,
                     variables=[RHO_EPS[0]], requirement_map=RequirementMapSpec())


@pytest.mark.unit
def test_single_optical_variable_is_tightened_by_fixed_partner(person, control_material, rc_material):
    base = rc_material.model_copy(
        update={"solar_reflectance": 0.8, "solar_transmittance": 0.1}
    )
    request = make_request(
        person, control_material, base,
        variables=[DecisionVariable(name="solar_reflectance", lower=0.3, upper=1.0)],
        requirement_map=None,
    )
    space = build_search_space(request)
    assert space.upper[0] == pytest.approx(0.9)
    assert space.linear_pairs == ()


@pytest.mark.unit
def test_paired_optical_variables_become_linear_constraint(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        variables=[
            DecisionVariable(name="solar_reflectance", lower=0.3, upper=1.0),
            DecisionVariable(name="solar_transmittance", lower=0.0, upper=0.5),
        ],
        requirement_map=None,
    )
    assert build_search_space(request).linear_pairs == ((0, 1),)


@pytest.mark.unit
def test_estimate_counts(person, control_material, rc_material):
    request = make_request(person, control_material, rc_material, sample_days_per_month=3)
    estimate = estimate_optimization(request)
    assert estimate.population_size == 8
    assert estimate.optimizer_evaluation_budget == 24
    assert estimate.requirement_map_evaluations == 9
    assert estimate.corner_evaluations == 4
    assert estimate.sensitivity_evaluations == 4
    assert estimate.thermal_simulation_budget == (24 + 9 + 4 + 4 + 2) * 3 + 3   # = 132


# --- evaluator (real physics on the fixture window) ------------------------

@pytest.fixture
def prepared(hourly_weather, person, control_material):
    interpolator = WeatherInterpolator.from_series(hourly_weather, assumptions=LEGACY)
    control = simulate_material_with_interpolator(120, 10, interpolator, person, control_material)
    return PreparedSample(hourly_weather.requested_start_time, 1, interpolator, control)


@pytest.mark.unit
def test_higher_reflectance_lowers_skin_temperature(prepared, person, control_material, rc_material):
    evaluator = MaterialEvaluator(make_request(person, control_material, rc_material), [prepared])

    low = evaluator.evaluate([0.3, 0.9])
    high = evaluator.evaluate([0.95, 0.9])

    assert high.mean_skin_temperature_c < low.mean_skin_temperature_c
    assert high.mean_skin_cooling_c > low.mean_skin_cooling_c
    assert 0.0 <= high.skin_exceedance_fraction <= 1.0

    count = evaluator.evaluation_count
    evaluator.evaluate([0.95, 0.9])
    assert evaluator.evaluation_count == count  # memoised


@pytest.mark.unit
def test_optically_impossible_candidate_returns_none(prepared, person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material, requirement_map=None,
        variables=[
            DecisionVariable(name="solar_reflectance", lower=0.3, upper=1.0),
            DecisionVariable(name="solar_transmittance", lower=0.0, upper=0.5),
        ],
    )
    evaluator = MaterialEvaluator(request, [prepared])
    assert evaluator.evaluate([0.8, 0.5]) is None
    assert evaluator.evaluation_count == 0


# --- runner / map with an analytic evaluator -------------------------------

class AnalyticEvaluator:
    """skin_exceedance_fraction = distance^2 to (0.8, 0.9); feasibility via
    mean_skin_cooling_c = rho + eps."""

    def __init__(self, names=("solar_reflectance", "infrared_emissivity")):
        self.names = names
        self.evaluation_count = 0

    def parameters(self, x):
        return {n: float(v) for n, v in zip(self.names, x)}

    def evaluate(self, x):
        self.evaluation_count += 1
        rho, eps = float(x[0]), float(x[1])
        distance = (rho - 0.8) ** 2 + (eps - 0.9) ** 2
        return EvaluationMetrics(
            sample_count=1, mean_skin_temperature_c=35.0, peak_skin_temperature_c=36.0,
            peak_core_temperature_c=37.5,
            skin_exceedance_fraction=distance, core_exceedance_fraction=0.0,
            skin_excess_degree_hours=distance, core_excess_degree_hours=0.0,
            mean_skin_cooling_c=rho + eps, mean_core_cooling_c=0.0,
        )


@pytest.mark.unit
def test_differential_evolution_finds_known_minimum(person, control_material, rc_material):
    request = make_request(person, control_material, rc_material,
                           population_multiplier=10, max_generations=60)
    outcome = run_differential_evolution(AnalyticEvaluator(), request)

    assert outcome.x == pytest.approx([0.8, 0.9], abs=0.02)
    assert outcome.generations == len(outcome.history) >= 1
    assert outcome.history[-1].best_feasible  # no constraints


@pytest.mark.unit
def test_cancel_from_generation_callback_stops_the_search(person, control_material, rc_material):
    request = make_request(person, control_material, rc_material, max_generations=50)

    def cancel(_record):
        raise OptimizationCancelled()

    with pytest.raises(OptimizationCancelled):
        run_differential_evolution(AnalyticEvaluator(), request, on_generation=cancel)


@pytest.mark.unit
def test_requirement_frontier(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        variables=[
            DecisionVariable(name="solar_reflectance", lower=0.5, upper=1.0),
            DecisionVariable(name="infrared_emissivity", lower=0.5, upper=1.0),
        ],
        constraints=[MetricConstraint(metric="mean_skin_cooling_c", operator=">=", threshold=1.6)],
        requirement_map=RequirementMapSpec(resolution=6),  # steps of 0.1
    )
    space = build_search_space(request)
    result = build_requirement_map(
        AnalyticEvaluator(), request, {"solar_reflectance": 0.8, "infrared_emissivity": 0.9}, space=space
    )

    frontier = {round(p.y, 2): p.minimum_x for p in result.frontier}
    assert frontier[1.0] == pytest.approx(0.6)
    assert frontier[0.6] == pytest.approx(1.0)
    assert frontier[0.5] is None
    assert result.minimum_x_at_max_y == pytest.approx(0.6)
    assert result.minimum_y_at_max_x == pytest.approx(0.6)
    assert result.required_x_at_best_y == pytest.approx(0.6)
    assert result.x_demand_direction == "increasing"
    assert result.frontier[-1].required_x == pytest.approx(0.6)

# --- API -------------------------------------------------------------------

@pytest.mark.integration
def test_optimization_api_round_trip(client, monkeypatch, person, control_material, rc_material):
    monkeypatch.setattr(
        optimizations_api, "run_optimization_task",
        SimpleNamespace(delay=lambda job_id: SimpleNamespace(id="celery-opt")),
    )
    monkeypatch.setattr(optimizations_api.celery_app.control, "revoke", lambda *a, **k: None)

    body = make_request(person, control_material, rc_material).model_dump(mode="json")

    estimate = client.post("/api/v1/optimizations/estimate", json=body)
    assert estimate.status_code == 200, estimate.text

    created = client.post("/api/v1/optimizations", json=body)
    assert created.status_code == 202, created.text
    job_id = created.json()["id"]
    assert created.json()["celery_task_id"] == "celery-opt"

    detail = client.get(f"/api/v1/optimizations/{job_id}").json()
    assert detail["status"] == "queued"
    assert detail["history"] == [] and detail["result"] is None

    cancelled = client.post(f"/api/v1/optimizations/{job_id}/cancel").json()
    assert cancelled["status"] == "cancelled"
    assert client.post(f"/api/v1/optimizations/{job_id}/cancel").status_code == 409

    bad = {**body, "city_id": "atlantis"}
    assert client.post("/api/v1/optimizations", json=bad).status_code == 422
```

### File: `backend/tests/test_optimization_stage10.py`
```python
import pytest

from app.schemas.optimization import (
    DecisionVariable,
    EvaluationMetrics,
    MetricConstraint,
    RequirementMapSpec,
)
from app.services.longwave import resolve_longwave_optics
from app.services.optimization.metrics import excess_integral
from app.services.optimization.objective import (
    INFEASIBLE_OFFSET,
    ObjectiveFunction,
    constraint_violation,
)
from app.services.optimization.requirement_map import build_requirement_map
from app.services.optimization.search_space import build_search_space
from app.services.optimization.service import rank_points
from app.services.optimization.variables import candidate_material, variable_value
from tests.test_optimization import RHO_EPS, AnalyticEvaluator, make_request


def metrics(**overrides) -> EvaluationMetrics:
    values = dict(
        sample_count=1, mean_skin_temperature_c=35.0, peak_skin_temperature_c=36.0,
        peak_core_temperature_c=37.5, skin_exceedance_fraction=0.5, core_exceedance_fraction=0.0,
        skin_excess_degree_hours=0.0, core_excess_degree_hours=0.0,
        mean_skin_cooling_c=1.0, mean_core_cooling_c=0.5,
    )
    values.update(overrides)
    return EvaluationMetrics(**values)


@pytest.mark.unit
def test_excess_integral_is_exact():
    assert excess_integral([0, 10], [34, 36], 35) == pytest.approx(2.5)
    assert excess_integral([0, 10], [36, 36], 35) == pytest.approx(10.0)
    assert excess_integral([0, 10], [30, 34], 35) == 0.0


@pytest.mark.unit
def test_violation_is_normalised_and_infeasible_ranks_last(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        constraints=[MetricConstraint(metric="skin_excess_degree_hours", operator="<=", threshold=0.5)],
    )
    bad = metrics(skin_excess_degree_hours=1.0)
    good = metrics(skin_excess_degree_hours=0.2)
    assert constraint_violation(bad, request.constraints) == pytest.approx(1.0)  # 0.5 / 0.5

    objective = ObjectiveFunction(request, reference=0.2)
    params = {"solar_reflectance": 0.9, "infrared_emissivity": 0.9}
    assert objective(good, params) < INFEASIBLE_OFFSET <= objective(bad, params)


@pytest.mark.unit
def test_plateau_ties_resolve_to_least_demanding(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        constraints=[MetricConstraint(metric="skin_excess_degree_hours", operator="<=", threshold=0.1)],
    )
    points = [
        ({"solar_reflectance": 0.98, "infrared_emissivity": 0.99}, metrics()),
        ({"solar_reflectance": 0.6, "infrared_emissivity": 0.7}, metrics()),
        ({"solar_reflectance": 0.3, "infrared_emissivity": 0.5}, metrics(skin_excess_degree_hours=0.4)),
    ]
    best = rank_points(points, request)
    assert best.parameters == {"solar_reflectance": 0.6, "infrared_emissivity": 0.7}
    assert best.feasible


@pytest.mark.unit
def test_band_variables_use_band_pairs(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material, requirement_map=None,
        variables=[
            DecisionVariable(name="infrared_emissivity_window", lower=0.5, upper=1.0),
            DecisionVariable(name="infrared_transmittance", lower=0.0, upper=0.3),
        ],
    )
    space = build_search_space(request)
    assert space.linear_pairs == ((0, 1),)          # eps_W + tau_IR <= 1
    assert space.upper[1] == pytest.approx(0.05)    # eps_N fixed at 0.95


@pytest.mark.unit
def test_gray_and_band_variables_cannot_be_combined(person, control_material, rc_material):
    with pytest.raises(ValueError, match="cannot be combined"):
        make_request(
            person, control_material, rc_material, requirement_map=None,
            variables=[
                DecisionVariable(name="infrared_emissivity", lower=0.5, upper=0.99),
                DecisionVariable(name="infrared_emissivity_window", lower=0.5, upper=0.99),
            ],
        )


@pytest.mark.unit
def test_outside_window_variable_round_trips(rc_material):
    candidate = candidate_material(
        rc_material,
        {"infrared_emissivity_window": 0.95, "infrared_emissivity_outside_window": 0.2},
    )
    optics = resolve_longwave_optics(candidate)
    assert optics.window == pytest.approx(0.95)
    assert optics.outside == pytest.approx(0.2, abs=1e-9)
    assert candidate.material_version_id is None


@pytest.mark.unit
def test_variable_value_derives_missing_evaporative_resistance(rc_material):
    assert rc_material.evaporative_resistance_m2pa_w is None
    assert variable_value(rc_material, "evaporative_resistance_m2pa_w") > 0


@pytest.mark.unit
def test_decreasing_direction_reads_largest_feasible_x(person, control_material, rc_material):
    request = make_request(
        person, control_material, rc_material,
        variables=[
            DecisionVariable(name="solar_reflectance", lower=0.5, upper=1.0, demand_direction="decreasing"),
            DecisionVariable(name="infrared_emissivity", lower=0.5, upper=1.0),
        ],
        constraints=[MetricConstraint(metric="mean_skin_cooling_c", operator=">=", threshold=1.6)],
        requirement_map=RequirementMapSpec(resolution=6),
    )
    space = build_search_space(request)
    result = build_requirement_map(
        AnalyticEvaluator(), request, {"solar_reflectance": 0.8, "infrared_emissivity": 0.9}, space=space
    )
    frontier = {round(p.y, 2): p.required_x for p in result.frontier}
    assert result.x_demand_direction == "decreasing"
    assert frontier[1.0] == pytest.approx(1.0)
    assert result.required_x_at_best_y == pytest.approx(1.0)
```

### File: `backend/tests/test_parameter_participation.py`
```python
"""Stage 2 definition of done: every input participates in the computation.

Each case perturbs exactly one input and requires the final skin temperature
to change. A parameter that is stored but never used fails here.
"""

import pytest

from app.schemas.environment import EnvironmentAssumptions
from tests.helpers.environment import legacy, physical, with_physical_series
from app.services.two_node import (
    simulate_material,
    simulate_material_with_weather,
)


THRESHOLD_C = 1e-4


def final_skin(result) -> float:
    return result.final_skin_temperature_c


MATERIAL_PERTURBATIONS = {
    "clothing_insulation_clo": 0.9,
    "evaporative_resistance_m2pa_w": 40.0,
    "clothing_area_factor": 1.4,           # Stage 3
    "solar_reflectance": 0.7,
    "solar_transmittance": 0.2,
    "infrared_emissivity": 0.5,
    "infrared_transmittance": 0.15,
    "projected_solar_area_factor": 0.4,
    "infrared_emissivity_window": 0.95,
}


@pytest.mark.unit
@pytest.mark.parametrize(("field", "value"), sorted(MATERIAL_PERTURBATIONS.items()))
def test_every_material_field_participates(
    environment, person, control_material, field, value
):
    baseline = simulate_material(60, 1, environment, person, control_material)
    perturbed = simulate_material(
        60, 1, environment, person, control_material.model_copy(update={field: value})
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C, (
        f"MaterialInput.{field} does not influence the result"
    )


PERSON_PERTURBATIONS = {
    "met": 1.2,
    "body_surface_area_m2": 2.4,           # Stage 3: was xfail (ADR 0001)
    "body_mass_kg": 95.0,                  # Stage 3
    "initial_core_temperature_c": 37.4,
    "initial_skin_temperature_c": 31.0,
    "position": "sitting",  # Stage 5
}


@pytest.mark.unit
@pytest.mark.parametrize(("field", "value"), sorted(PERSON_PERTURBATIONS.items()))
def test_every_person_field_participates(
    environment, person, control_material, field, value
):
    baseline = simulate_material(60, 1, environment, person, control_material)
    perturbed = simulate_material(
        60, 1, environment, person.model_copy(update={field: value}), control_material
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C

# (baseline update, perturbed update). Method-dependent parameters are tested
# with the method that uses them switched on in both runs.
ASSUMPTION_PERTURBATIONS = [
    ({}, {"mean_radiant_temperature_method": "equal_to_air"}),
    ({}, {"solar_mrt_gain_k_per_w_m2": 0.02}),
    ({}, {"solar_mrt_gain_cap_k": 5.0}),
    ({}, {"sky_temperature_method": "swinbank"}),
    ({}, {"sky_temperature_method": "fixed_offset"}),
    ({}, {"sky_offset_base_k": 8.0}),
    ({}, {"sky_offset_humidity_range_k": 2.0}),
    (
        {"sky_temperature_method": "fixed_offset"},
        {"sky_temperature_method": "fixed_offset", "fixed_sky_offset_k": 25.0},
    ),
    ({}, {"sky_view_factor": 0.2}),
    ({}, {"wind_speed_scaling_factor": 0.67}),
]

SOLAR_SPLIT = {
    "direct_normal_irradiance_w_m2": 700.0,
    "diffuse_horizontal_irradiance_w_m2": 150.0,
}

# (baseline update, perturbed update) on the fixed EnvironmentInput.
ENVIRONMENT_PERTURBATIONS = [
    ({}, SOLAR_SPLIT),
    (SOLAR_SPLIT, {**SOLAR_SPLIT, "direct_normal_irradiance_w_m2": 400.0}),
    (SOLAR_SPLIT, {**SOLAR_SPLIT, "diffuse_horizontal_irradiance_w_m2": 350.0}),
    (SOLAR_SPLIT, {**SOLAR_SPLIT, "ground_albedo": 0.6}),
]

# Stage 11/12: parameters of the physical default (ADR 0008, 0009).
PHYSICAL_PERTURBATIONS = [
    {"ground_emissivity": 0.85},
    {"ground_soil_conductance_w_m2k": 60.0},
    {"ground_albedo": 0.5},
]


@pytest.mark.unit
@pytest.mark.parametrize("perturbed_update", PHYSICAL_PERTURBATIONS)
def test_every_physical_assumption_participates(hourly_weather, person, rc_material, perturbed_update):
    weather = with_physical_series(hourly_weather)
    baseline = simulate_material_with_weather(120, 10, weather, person, rc_material, assumptions=physical())
    perturbed = simulate_material_with_weather(
        120, 10, weather, person, rc_material, assumptions=physical(**perturbed_update)
    )
    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C, perturbed_update


@pytest.mark.unit
@pytest.mark.parametrize("weather_update", [{"cloud_cover_percent": 80.0}, {"soil_temperature_c": 30.0}])
def test_physical_weather_variables_participate(hourly_weather, person, rc_material, weather_update):
    baseline = simulate_material_with_weather(
        120, 10, with_physical_series(hourly_weather), person, rc_material, assumptions=physical()
    )
    perturbed = simulate_material_with_weather(
        120, 10, with_physical_series(hourly_weather, **weather_update), person, rc_material,
        assumptions=physical(),
    )
    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C, weather_update
    
@pytest.mark.unit
@pytest.mark.parametrize(("baseline_update", "perturbed_update"), ENVIRONMENT_PERTURBATIONS)
def test_every_solar_environment_field_participates(
    environment, person, control_material, baseline_update, perturbed_update
):
    baseline = simulate_material(
        60, 1, environment.model_copy(update=baseline_update), person, control_material
    )
    perturbed = simulate_material(
        60, 1, environment.model_copy(update=perturbed_update), person, control_material
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C, (
        f"EnvironmentInput {perturbed_update} does not influence the result"
    )
```

### File: `backend/tests/test_physics.py`
```python
import pytest
from pydantic import ValidationError

from app.schemas.simulation import MaterialInput
from app.services.two_node import (
    calculate_fluxes,
    saturation_vapor_pressure_kpa,
)


@pytest.mark.unit
def test_saturation_pressure_increases_with_temperature():
    pressure_20 = saturation_vapor_pressure_kpa(20.0)
    pressure_30 = saturation_vapor_pressure_kpa(30.0)
    pressure_40 = saturation_vapor_pressure_kpa(40.0)

    assert pressure_20 < pressure_30 < pressure_40


@pytest.mark.unit
def test_saturation_pressure_near_reference_value():
    pressure = saturation_vapor_pressure_kpa(30.0)

    assert pressure == pytest.approx(
        4.24,
        abs=0.08,
    )


@pytest.mark.unit
def test_invalid_optical_sum_is_rejected():
    with pytest.raises(ValidationError):
        MaterialInput(
            name="Invalid material",
            clothing_insulation_clo=0.5,
            solar_reflectance=0.8,
            solar_transmittance=0.4,
            infrared_emissivity=0.9,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        )


@pytest.mark.unit
def test_higher_reflectance_reduces_solar_absorption(
    environment,
    person,
    control_material,
    rc_material,
):
    control_fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=environment,
        person=person,
        material=control_material,
    )

    rc_fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert (
        rc_fluxes.absorbed_solar
        < control_fluxes.absorbed_solar
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "wind_speed",
    [0.0, 0.1, 1.0, 3.0, 8.0],
)
def test_flux_calculation_is_finite(
    wind_speed,
    environment,
    person,
    control_material,
):
    modified_environment = environment.model_copy(
        update={
            "wind_speed_m_s": wind_speed,
        }
    )

    fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=modified_environment,
        person=person,
        material=control_material,
    )

    assert fluxes.metabolism > 0
    assert fluxes.evaporation >= 0
    assert fluxes.absorbed_solar >= 0
```

### File: `backend/tests/test_planck.py`
```python
import pytest

from app.services.planck import (
    SECOND_RADIATION_CONSTANT,
    band_fraction,
    band_power_k4,
    blackbody_fraction,
    blackbody_fraction_slope,
    broadband_emissivity,
    outside_window_emissivity,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("lambda_t", "expected"),
    [(1000.0, 0.00032), (2898.0, 0.2501), (5000.0, 0.6337), (10000.0, 0.9142)],
)
def test_blackbody_fraction_matches_tables(lambda_t, expected):
    assert blackbody_fraction(lambda_t) == pytest.approx(expected, abs=5e-4)


@pytest.mark.unit
def test_series_are_continuous_at_the_switch():
    below = blackbody_fraction(SECOND_RADIATION_CONSTANT * (1 + 1e-9))
    above = blackbody_fraction(SECOND_RADIATION_CONSTANT * (1 - 1e-9))
    assert below == pytest.approx(above, abs=1e-9)


@pytest.mark.unit
def test_fraction_limits_and_monotonicity():
    values = [blackbody_fraction(x) for x in (100, 1000, 3000, 10000, 1e5, 1e7)]
    assert values == sorted(values)
    assert values[0] == pytest.approx(0.0, abs=1e-12)
    assert values[-1] == pytest.approx(1.0, abs=1e-9)


@pytest.mark.unit
def test_slope_matches_finite_difference():
    x, h = 4000.0, 1e-3
    numeric = (blackbody_fraction(x + h) - blackbody_fraction(x - h)) / (2 * h)
    assert blackbody_fraction_slope(x) == pytest.approx(numeric, rel=1e-6)


@pytest.mark.unit
def test_window_band_fraction_near_300_k():
    assert band_fraction(300.0) == pytest.approx(0.32, abs=0.01)


@pytest.mark.unit
def test_band_power_derivative():
    t, h = 305.0, 1e-3
    numeric = (band_power_k4(t + h)[0] - band_power_k4(t - h)[0]) / (2 * h)
    assert band_power_k4(t)[1] == pytest.approx(numeric, rel=1e-6)


@pytest.mark.unit
def test_band_split_round_trip():
    broadband = broadband_emissivity(0.9, 0.3)
    assert outside_window_emissivity(broadband, 0.9) == pytest.approx(0.3, abs=1e-12)
    assert outside_window_emissivity(0.7, 0.7) == pytest.approx(0.7, abs=1e-12)
```

### File: `backend/tests/test_radiant_environment.py`
```python
import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.environment_model import derive_environment, required_weather_variables
from app.services.ground_surface import (
    brutsaert_cloud_sky_emissivity,
    brutsaert_cloud_sky_temperature_c,
    ground_energy_residual,
    solve_ground_surface_temperature_c,
)
from app.services.weather_quality import WeatherMissingVariableError
from tests.helpers.environment import LEGACY


PHYSICAL = EnvironmentAssumptions(
    mean_radiant_temperature_method="ground_energy_balance",
    sky_temperature_method="brutsaert_cloud",
)

GROUND = dict(air_c=40.0, sky_c=25.0, ghi_w_m2=900.0, albedo=0.2,
              wind_speed_m_s=2.0, soil_c=38.0, emissivity=0.95, conductance_w_m2k=15.0)


@pytest.mark.unit
def test_defaults_need_physical_variables_and_legacy_needs_none():
    assert required_weather_variables(EnvironmentAssumptions()) == (
        "cloud_cover", "soil_temperature_0_to_7cm",
    )
    assert required_weather_variables(LEGACY) == ()


@pytest.mark.unit
def test_legacy_path_is_unchanged():
    env = derive_environment(air_temperature_c=35.0, relative_humidity_percent=40.0,
                             wind_speed_m_s=2.0, ghi_w_m2=800.0, assumptions=LEGACY)
    assert env.mean_radiant_temperature_c == pytest.approx(35.0 + 9.6)
    assert env.sky_temperature_c == pytest.approx(35.0 - (5.0 + 10.0 * 0.6))


@pytest.mark.unit
def test_brutsaert_clear_sky_value():
    # e_a = 15.8 hPa at 25 C / 50 % RH -> 1.24 (15.8 / 298.15)^(1/7) = 0.815
    assert brutsaert_cloud_sky_emissivity(25.0, 50.0, 0.0) == pytest.approx(0.815, abs=0.005)


@pytest.mark.unit
def test_overcast_sky_radiates_at_air_temperature():
    assert brutsaert_cloud_sky_temperature_c(30.0, 60.0, 100.0) == pytest.approx(30.0, abs=1e-9)


@pytest.mark.unit
def test_clouds_warm_the_sky():
    clear = brutsaert_cloud_sky_temperature_c(30.0, 40.0, 0.0)
    half = brutsaert_cloud_sky_temperature_c(30.0, 40.0, 50.0)
    assert clear < half < 30.0


@pytest.mark.unit
def test_ground_balance_closes():
    t = solve_ground_surface_temperature_c(**GROUND)
    assert ground_energy_residual(t, **GROUND) == pytest.approx(0.0, abs=1e-6)
    assert 45.0 < t < 75.0


@pytest.mark.unit
def test_ground_warms_with_sun_and_follows_soil_for_large_conductance():
    noon = solve_ground_surface_temperature_c(**GROUND)
    night = solve_ground_surface_temperature_c(**{**GROUND, "ghi_w_m2": 0.0})
    assert night < noon
    stiff = solve_ground_surface_temperature_c(**{**GROUND, "conductance_w_m2k": 200.0})
    assert abs(stiff - GROUND["soil_c"]) < abs(noon - GROUND["soil_c"])


@pytest.mark.unit
def test_physical_methods_require_their_variables():
    with pytest.raises(WeatherMissingVariableError):
        derive_environment(air_temperature_c=30.0, relative_humidity_percent=50.0,
                           wind_speed_m_s=1.0, ghi_w_m2=500.0, assumptions=PHYSICAL)


@pytest.mark.unit
def test_physical_environment_is_valid_input():
    env = derive_environment(air_temperature_c=40.0, relative_humidity_percent=20.0,
                             wind_speed_m_s=2.0, ghi_w_m2=900.0, assumptions=PHYSICAL,
                             cloud_cover_percent=0.0, soil_temperature_c=38.0)
    assert env.sky_temperature_c < 40.0 < env.mean_radiant_temperature_c
```

### File: `backend/tests/test_radiation_convention.py`
```python
import numpy as np
import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.weather_interpolation import WeatherInterpolator
from tests.helpers.environment import legacy

def make_interpolator(convention):
    return WeatherInterpolator(
        relative_seconds=np.array([-3600.0, 0.0, 3600.0, 7200.0]),
        temperatures=np.array([30.0, 32.0, 34.0, 36.0]),
        humidities=np.array([40.0] * 4),
        wind_speeds=np.array([1.0] * 4),
        ghi_values=np.array([200.0, 600.0, 800.0, 700.0]),
        assumptions=legacy(radiation_time_convention=convention),
    )


@pytest.mark.unit
def test_step_convention_conserves_hourly_irradiation():
    interp = make_interpolator("preceding_hour_mean_step")
    # Hour ending at t=3600 s has mean 800 W/m^2 -> 800 * 3600 J/m^2.
    ts = np.linspace(1.0, 3600.0, 3600)
    energy = np.trapezoid([interp.environment_at(t).solar_radiation_w_m2 for t in ts], ts)
    assert energy == pytest.approx(800.0 * 3599.0, rel=1e-6)


@pytest.mark.unit
def test_step_convention_leaves_instantaneous_variables_linear():
    interp = make_interpolator("preceding_hour_mean_step")
    env = interp.environment_at(1800.0)
    assert env.air_temperature_c == pytest.approx(33.0)   # still linear
    assert env.solar_radiation_w_m2 == pytest.approx(800.0)  # step


@pytest.mark.unit
def test_default_convention_is_unchanged_legacy_behaviour():
    interp = make_interpolator("instantaneous_linear")
    assert interp.environment_at(1800.0).solar_radiation_w_m2 == pytest.approx(700.0)
    assert "approximation" in " ".join(EnvironmentAssumptions().describe())
    assert EnvironmentAssumptions().radiation_time_convention == "instantaneous_linear"
```

### File: `backend/tests/test_result_export.py`
```python
import csv
import io
import json
from types import SimpleNamespace

import pytest

from app.services.result_export import (
    CSV_HEADERS,
    export_result_csv,
    export_result_json,
)


EXPECTED_HEADERS = CSV_HEADERS  # single source of truth


def make_point(
    *,
    minute, core_temperature_c, skin_temperature_c, convection_w_m2,
    longwave_radiation_w_m2, evaporation_w_m2, absorbed_solar_w_m2,
    maximum_evaporation_w_m2=None, skin_wettedness=None,
    clothing_surface_temperature_c=None,
):
    return SimpleNamespace(
        minute=minute,
        core_temperature_c=core_temperature_c,
        skin_temperature_c=skin_temperature_c,
        convection_w_m2=convection_w_m2,
        longwave_radiation_w_m2=longwave_radiation_w_m2,
        evaporation_w_m2=evaporation_w_m2,
        absorbed_solar_w_m2=absorbed_solar_w_m2,
        maximum_evaporation_w_m2=maximum_evaporation_w_m2,
        skin_wettedness=skin_wettedness,
        clothing_surface_temperature_c=clothing_surface_temperature_c,
    )

@pytest.mark.unit
def test_missing_stage_3_diagnostics_export_as_blank_cells():
    rows = list(csv.reader(io.StringIO(export_result_csv(make_export_result()))))
    assert rows[1][13:] == [""] * 12

@pytest.mark.unit
def test_stage_3_diagnostics_are_exported_when_present():
    point = make_point(
        minute=0, core_temperature_c=36.8, skin_temperature_c=33.7,
        convection_w_m2=1.0, longwave_radiation_w_m2=1.0, evaporation_w_m2=1.0,
        absorbed_solar_w_m2=1.0, maximum_evaporation_w_m2=120.0,
        skin_wettedness=0.25, clothing_surface_temperature_c=35.1,
    )
    rows = list(csv.reader(io.StringIO(export_result_csv(
        make_export_result(control_points=[point], rc_points=[point])
    ))))
    assert float(rows[1][13]) == pytest.approx(120.0)
    assert float(rows[1][15]) == pytest.approx(0.25)
    assert float(rows[1][17]) == pytest.approx(35.1)

def make_export_result(
    *,
    control_points=None,
    rc_points=None,
):
    """Create the minimal result object needed for CSV export."""
    if control_points is None:
        control_points = [
            make_point(
                minute=0,
                core_temperature_c=36.8,
                skin_temperature_c=33.7,
                convection_w_m2=12.5,
                longwave_radiation_w_m2=8.1,
                evaporation_w_m2=20.0,
                absorbed_solar_w_m2=100.0,
            )
        ]

    if rc_points is None:
        rc_points = [
            make_point(
                minute=0,
                core_temperature_c=36.7,
                skin_temperature_c=32.9,
                convection_w_m2=13.5,
                longwave_radiation_w_m2=10.2,
                evaporation_w_m2=18.0,
                absorbed_solar_w_m2=25.0,
            )
        ]

    return SimpleNamespace(
        control=SimpleNamespace(time_series=control_points),
        radiative_cooling=SimpleNamespace(time_series=rc_points),
    )


@pytest.mark.unit
def test_result_csv_contains_expected_headers():
    result = make_export_result()

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert rows[0] == EXPECTED_HEADERS
    assert "control_clothing_surface_temperature_c" in rows[0]
    assert len(rows[0]) == 1 + 2 * 12



@pytest.mark.unit
def test_result_csv_contains_control_and_rc_values():
    result = make_export_result()

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert len(rows) == 2

    data_row = rows[1]

    assert float(data_row[0]) == pytest.approx(0.0)

    assert float(data_row[1]) == pytest.approx(36.8)
    assert float(data_row[2]) == pytest.approx(33.7)

    assert float(data_row[3]) == pytest.approx(36.7)
    assert float(data_row[4]) == pytest.approx(32.9)

    assert float(data_row[5]) == pytest.approx(12.5)
    assert float(data_row[6]) == pytest.approx(13.5)

    assert float(data_row[7]) == pytest.approx(8.1)
    assert float(data_row[8]) == pytest.approx(10.2)

    assert float(data_row[9]) == pytest.approx(20.0)
    assert float(data_row[10]) == pytest.approx(18.0)

    assert float(data_row[11]) == pytest.approx(100.0)
    assert float(data_row[12]) == pytest.approx(25.0)


@pytest.mark.unit
def test_result_csv_with_empty_time_series_contains_only_headers():
    result = make_export_result(
        control_points=[],
        rc_points=[],
    )

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert rows == [EXPECTED_HEADERS]


@pytest.mark.unit
def test_result_csv_rejects_different_time_series_lengths():
    result = make_export_result(
        control_points=[
            make_point(
                minute=0,
                core_temperature_c=36.8,
                skin_temperature_c=33.7,
                convection_w_m2=12.5,
                longwave_radiation_w_m2=8.1,
                evaporation_w_m2=20.0,
                absorbed_solar_w_m2=100.0,
            )
        ],
        rc_points=[],
    )

    with pytest.raises(ValueError):
        export_result_csv(result)


@pytest.mark.unit
def test_result_json_serializes_model_dump_as_unicode():
    payload = {
        "city": "dubai",
        "duration_minutes": 120,
        "warning": "warning",
    }

    result = SimpleNamespace(
        model_dump=lambda *, mode: payload,
    )

    json_text = export_result_json(result)
    decoded = json.loads(json_text)

    assert decoded == payload
    assert "dubai" in json_text
    assert "warning" in json_text
    assert "\\u" not in json_text
    assert "\n" in json_text
```

### File: `backend/tests/test_result_storage.py`
```python
import gzip
import json
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.services import result_storage


class FakeSimulationResult:
    """Provides the minimum interface required for save_simulation_result."""

    def __init__(self, payload):
        self.payload = payload
        self.requested_mode = None

    def model_dump(self, *, mode):
        self.requested_mode = mode
        return self.payload


@pytest.mark.unit
def test_save_simulation_result_creates_gzip_json_file(
    tmp_path,
    monkeypatch,
):
    result_directory = tmp_path / "results"

    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        result_directory,
    )

    payload = {
        "city": "Dubai",
        "duration_minutes": 120,
        "warning": "warning",
    }
    result = FakeSimulationResult(payload)

    saved_path = result_storage.save_simulation_result(
        job_id="job-123",
        result=result,
    )

    assert saved_path == result_directory / "job-123.json.gz"
    assert saved_path.exists()
    assert saved_path.is_file()

    with gzip.open(
        saved_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        saved_payload = json.load(file)

    assert saved_payload == payload
    assert result.requested_mode == "json"


@pytest.mark.unit
def test_save_simulation_result_creates_missing_directory(
    tmp_path,
    monkeypatch,
):
    result_directory = (
        tmp_path
        / "nested"
        / "simulation"
        / "results"
    )

    assert not result_directory.exists()

    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        result_directory,
    )

    result = FakeSimulationResult(
        {
            "city": "Dubai",
            "duration_minutes": 60,
        }
    )

    saved_path = result_storage.save_simulation_result(
        job_id="directory-test",
        result=result,
    )

    assert result_directory.exists()
    assert saved_path.exists()


@pytest.mark.unit
def test_save_simulation_result_removes_temporary_file(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    result = FakeSimulationResult(
        {
            "city": "Tokyo",
            "warning": "",
        }
    )

    saved_path = result_storage.save_simulation_result(
        job_id="atomic-test",
        result=result,
    )

    temporary_path = tmp_path / "atomic-test.tmp.json.gz"

    assert saved_path.exists()
    assert not temporary_path.exists()


@pytest.mark.unit
def test_save_simulation_result_preserves_unicode(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    payload = {
        "city": "taipei",
        "environment_model_note": "Simulation results test",
        "warning": "high temperature warning",
    }
    result = FakeSimulationResult(payload)

    saved_path = result_storage.save_simulation_result(
        job_id="unicode-test",
        result=result,
    )

    with gzip.open(
        saved_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        raw_json = file.read()

    assert "taipei" in raw_json
    assert "Simulation results test" in raw_json
    assert "high temperature warning" in raw_json
    assert "\\u81fa" not in raw_json

    assert json.loads(raw_json) == payload


@pytest.mark.unit
def test_save_simulation_result_replaces_existing_file(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    old_result = FakeSimulationResult(
        {
            "city": "Old city",
            "duration_minutes": 30,
        }
    )
    new_result = FakeSimulationResult(
        {
            "city": "New city",
            "duration_minutes": 120,
        }
    )

    first_path = result_storage.save_simulation_result(
        job_id="same-job",
        result=old_result,
    )
    second_path = result_storage.save_simulation_result(
        job_id="same-job",
        result=new_result,
    )

    assert first_path == second_path

    with gzip.open(
        second_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        saved_payload = json.load(file)

    assert saved_payload == {
        "city": "New city",
        "duration_minutes": 120,
    }


@pytest.mark.unit
def test_load_simulation_result_reads_and_validates_payload(
    tmp_path,
    monkeypatch,
):
    result_path = tmp_path / "load-test.json.gz"

    payload = {
        "city": "Dubai",
        "duration_minutes": 120,
        "warning": "",
    }

    with gzip.open(
        result_path,
        mode="wt",
        encoding="utf-8",
    ) as file:
        json.dump(
            payload,
            file,
            ensure_ascii=False,
        )

    expected_result = object()
    model_validate = Mock(
        return_value=expected_result
    )

    fake_response_model = SimpleNamespace(
        model_validate=model_validate
    )

    monkeypatch.setattr(
        result_storage,
        "WeatherSimulationResponse",
        fake_response_model,
    )

    loaded_result = (
        result_storage.load_simulation_result(
            str(result_path)
        )
    )

    assert loaded_result is expected_result
    model_validate.assert_called_once_with(payload)


@pytest.mark.unit
def test_load_simulation_result_raises_for_missing_file(
    tmp_path,
):
    missing_path = (
        tmp_path / "does-not-exist.json.gz"
    )

    with pytest.raises(
        FileNotFoundError,
        match="The result file does not exist",
    ):
        result_storage.load_simulation_result(
            str(missing_path)
        )
```

### File: `backend/tests/test_route_registration.py`
```python
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
```

### File: `backend/tests/test_scenario_summary.py`
```python
import pytest

from app.schemas.simulation import WeatherSimulationRequest
from app.services.scenario_summary import (
    ScenarioPairingError,
    build_simulation_summary,
    pair_scenarios,
)
from app.services.two_node import simulate_material
from app.services.weather_simulation import execute_weather_simulation_with_weather
from tests.helpers.environment import with_physical_series

@pytest.mark.unit
def test_average_is_time_weighted_not_arithmetic(environment, person, control_material, rc_material):
    control = simulate_material(120, 10, environment, person, control_material)
    rc = simulate_material(120, 10, environment, person, rc_material)

    summary = build_simulation_summary(control, rc)
    paired = pair_scenarios(control, rc)

    arithmetic = sum(paired.skin_c) / len(paired.skin_c)
    trapezoid = (sum(paired.skin_c) - 0.5 * (paired.skin_c[0] + paired.skin_c[-1])) / (
        len(paired.skin_c) - 1
    )

    assert summary.average_skin_temperature_improvement_c == pytest.approx(trapezoid, abs=1e-4)
    assert summary.average_skin_temperature_improvement_c != pytest.approx(arithmetic, abs=1e-4)
    assert summary.averaging_method == "time_weighted_trapezoid"


@pytest.mark.unit
def test_single_run_and_annual_sample_agree(hourly_weather, person, control_material, rc_material):
    """The same weather window must give the same average in both pipelines."""
    from app.services.scenario_summary import pair_scenarios

    request = WeatherSimulationRequest(
        city_id="dubai",
        start_time_local=hourly_weather.requested_start_time,
        duration_minutes=120,
        output_interval_minutes=10,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )
    single = execute_weather_simulation_with_weather(
        request=request, weather=with_physical_series(hourly_weather), city_name="Dubai"
    )
    paired = pair_scenarios(single.control, single.radiative_cooling)  # what climate_adaptation uses

    assert single.summary.average_skin_temperature_improvement_c == pytest.approx(
        round(paired.average_skin_c, 4)
    )


@pytest.mark.unit
def test_mismatched_time_axis_is_rejected(environment, person, control_material):
    a = simulate_material(60, 1, environment, person, control_material)
    b = simulate_material(60, 2, environment, person, control_material)
    with pytest.raises(ScenarioPairingError):
        pair_scenarios(a, b)
```

### File: `backend/tests/test_solar.py`
```python
import pytest
from pydantic import ValidationError

from app.schemas.simulation import EnvironmentInput, MaterialInput
from app.services.solar import solar_load
from app.services.two_node import effective_radiation_area_ratio


@pytest.mark.unit
def test_without_split_ghi_is_beam_on_projected_area(control_material):
    load = solar_load(
        EnvironmentInput(solar_radiation_w_m2=800.0),
        control_material,
        effective_radiation_area_ratio("standing"),
    )

    assert load.split_available is False
    assert load.incident_w_m2 == pytest.approx(0.25 * 800.0)
    assert load.sky_diffuse_w_m2 == 0.0
    assert load.ground_reflected_w_m2 == 0.0
    # rho = 0.4, tau = 0 -> alpha = 0.6
    assert load.absorbed_by_textile_w_m2 == pytest.approx(0.6 * 200.0)
    assert load.transmitted_to_skin_w_m2 == 0.0


@pytest.mark.unit
def test_split_components_follow_ashrae_55_geometry(control_material):
    environment = EnvironmentInput(
        solar_radiation_w_m2=900.0,
        direct_normal_irradiance_w_m2=700.0,
        diffuse_horizontal_irradiance_w_m2=200.0,
        sky_view_factor=0.5,
        ground_albedo=0.2,
    )

    load = solar_load(environment, control_material, 0.73)

    assert load.split_available is True
    assert load.direct_w_m2 == pytest.approx(0.25 * 700.0)
    assert load.sky_diffuse_w_m2 == pytest.approx(0.5 * 0.73 * 0.5 * 200.0)
    assert load.ground_reflected_w_m2 == pytest.approx(0.5 * 0.73 * 0.2 * 900.0)
    assert load.incident_w_m2 == pytest.approx(
        load.direct_w_m2 + load.sky_diffuse_w_m2 + load.ground_reflected_w_m2
    )


@pytest.mark.unit
def test_partial_split_is_rejected():
    with pytest.raises(ValidationError, match="supplied together"):
        EnvironmentInput(direct_normal_irradiance_w_m2=500.0)


@pytest.mark.unit
def test_transmittance_routes_solar_to_skin():
    material = MaterialInput(name="sheer", solar_reflectance=0.5, solar_transmittance=0.3)

    load = solar_load(EnvironmentInput(solar_radiation_w_m2=800.0), material, 0.73)

    assert load.transmitted_to_skin_w_m2 == pytest.approx(0.3 * 200.0)
    assert load.absorbed_by_textile_w_m2 == pytest.approx(0.2 * 200.0)
    assert load.entering_system_w_m2 == pytest.approx(0.5 * 200.0)


@pytest.mark.unit
def test_posture_selects_radiation_area_ratio():
    assert effective_radiation_area_ratio("standing") == pytest.approx(0.73)
    assert effective_radiation_area_ratio("sitting") == pytest.approx(0.70)
```

### File: `backend/tests/test_spectral_summary.py`
```python
import pytest

from app.services.spectral_summary import summarize_ir_spectrum


def spectrum(fn, start=2.0, stop=25.0, step=0.01):
    count = int(round((stop - start) / step)) + 1
    return [
        {"wavelength_um": round(start + i * step, 4), "value": fn(start + i * step)}
        for i in range(count)
    ]


@pytest.mark.unit
def test_constant_spectrum():
    summary = summarize_ir_spectrum(spectrum(lambda _: 0.9), spectrum_type="mir_emissivity", temperature_k=305)
    assert summary.window_average == pytest.approx(0.9, abs=1e-4)
    assert summary.outside_window_average == pytest.approx(0.9, abs=1e-4)
    assert summary.window_coverage == pytest.approx(1.0)
    assert summary.broadband_coverage < 1.0


@pytest.mark.unit
def test_selective_step_spectrum():
    summary = summarize_ir_spectrum(
        spectrum(lambda w: 0.95 if 8.0 <= w <= 13.0 else 0.1),
        spectrum_type="mir_emissivity", temperature_k=305,
    )
    assert summary.window_average == pytest.approx(0.95, abs=0.01)
    assert summary.outside_window_average == pytest.approx(0.1, abs=0.01)


@pytest.mark.integration
def test_band_summary_endpoint_rejects_solar_spectra(client):
    response = client.get("/api/v1/materials/versions/x/spectra/solar_reflectance/band-summary")
    assert response.status_code == 422
```

### File: `backend/tests/test_spectrum_parser.py`
```python
import pytest

from app.services.spectrum_parser import (
    parse_spectrum_csv,
)


@pytest.mark.unit
def test_parse_valid_spectrum_csv():
    content = (
        "wavelength_um,value\n"
        "0.3,0.91\n"
        "0.5,0.92\n"
        "1.0,0.93\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert len(result.points) == 3
    assert (
        result.minimum_wavelength_um
        == pytest.approx(0.3)
    )
    assert (
        result.maximum_wavelength_um
        == pytest.approx(1.0)
    )


@pytest.mark.unit
def test_reject_value_above_one():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
        "0.5,1.2\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="0 and 1",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_unsorted_wavelengths():
    content = (
        "wavelength_um,value\n"
        "1.0,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="strictly increasing",
    ):
        parse_spectrum_csv(content)

import hashlib

from app.services import spectrum_parser


@pytest.mark.unit
def test_parse_spectrum_returns_checksum():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert result.checksum_sha256 == (
        hashlib.sha256(content).hexdigest()
    )


@pytest.mark.unit
def test_parse_normalizes_header_names():
    content = (
        " Wavelength µm , Reflectance \n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert len(result.points) == 2


@pytest.mark.unit
def test_reject_empty_spectrum():
    with pytest.raises(
        ValueError,
        match="empty",
    ):
        parse_spectrum_csv(b"")


@pytest.mark.unit
def test_reject_non_utf8_spectrum():
    with pytest.raises(
        ValueError,
        match="UTF-8",
    ):
        parse_spectrum_csv(b"\xff\xfe\xfa")


@pytest.mark.unit
def test_reject_missing_wavelength_column():
    content = (
        "frequency,value\n"
        "1.0,0.9\n"
        "2.0,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="wavelength_um",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_missing_value_column():
    content = (
        "wavelength_um,measurement\n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="'value'",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
@pytest.mark.parametrize(
    "row",
    [
        "not-a-number,0.8",
        "0.3,not-a-number",
    ],
)
def test_reject_invalid_numeric_values(row):
    content = (
        "wavelength_um,value\n"
        f"{row}\n"
        "0.5,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="invalid values",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("row", "message"),
    [
        ("nan,0.8", "wavelength"),
        ("0.3,nan", "spectrum value"),
        ("-0.3,0.8", "positive"),
        ("0.3,-0.1", "between 0 and 1"),
    ],
)
def test_reject_invalid_spectrum_ranges(
    row,
    message,
):
    content = (
        "wavelength_um,value\n"
        f"{row}\n"
        "0.5,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match=message,
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_single_data_point():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="at least two",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_file_above_size_limit(
    monkeypatch,
):
    monkeypatch.setattr(
        spectrum_parser,
        "MAX_SPECTRUM_FILE_SIZE",
        10,
    )

    with pytest.raises(
        ValueError,
        match="2 MB",
    ):
        spectrum_parser.parse_spectrum_csv(
            b"x" * 11
        )


@pytest.mark.unit
def test_reject_too_many_points(
    monkeypatch,
):
    monkeypatch.setattr(
        spectrum_parser,
        "MAX_SPECTRUM_POINTS",
        2,
    )

    content = (
        "wavelength_um,value\n"
        "0.1,0.9\n"
        "0.2,0.8\n"
        "0.3,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="cannot exceed",
    ):
        spectrum_parser.parse_spectrum_csv(
            content
        )

@pytest.mark.unit
def test_header_only_file_reports_too_few_points():
    with pytest.raises(ValueError, match="at least two"):
        parse_spectrum_csv(b"wavelength_um,value\n")
```

### File: `backend/tests/test_stage12_defaults.py`
```python
from datetime import datetime

import pytest

from app.schemas.environment import EnvironmentAssumptions, preset_assumptions
from app.schemas.simulation import MaterialInput, PersonInput, WeatherSimulationRequest
from app.services.stored_requests import load_stored_request
from tests.helpers.environment import LEGACY


@pytest.mark.unit
def test_default_is_open_ground_physical():
    assert EnvironmentAssumptions() == preset_assumptions("open_ground_physical")
    assert EnvironmentAssumptions().mean_radiant_temperature_method == "ground_energy_balance"


@pytest.mark.unit
def test_unknown_preset_is_rejected():
    with pytest.raises(ValueError):
        preset_assumptions("tropical_canyon")


@pytest.mark.unit
def test_pre_stage2_request_loads_as_legacy():
    material = MaterialInput(name="m")
    payload = WeatherSimulationRequest(
        start_time_local=datetime(2023, 7, 15, 12), person=PersonInput(),
        control_material=material, rc_material=material,
    ).model_dump(mode="json")
    payload.pop("environment_assumptions")
    assert load_stored_request(WeatherSimulationRequest, payload).environment_assumptions == LEGACY


@pytest.mark.unit
def test_explicit_stored_assumptions_are_kept():
    material = MaterialInput(name="m")
    payload = WeatherSimulationRequest(
        start_time_local=datetime(2023, 7, 15, 12), person=PersonInput(),
        control_material=material, rc_material=material,
        environment_assumptions=EnvironmentAssumptions(),
    ).model_dump(mode="json")
    loaded = load_stored_request(WeatherSimulationRequest, payload)
    assert loaded.environment_assumptions.mean_radiant_temperature_method == "ground_energy_balance"
```

### File: `backend/tests/test_stage_4_2_export.py`
```python
import zipfile
from io import BytesIO
from types import SimpleNamespace

import pytest

from app.services.global_batch_export import (
    build_batch_export_zip,
)


@pytest.mark.unit
def test_export_contains_required_files():
    city_result = SimpleNamespace(
        city_id="dubai",
        city_name="Dubai",
        country="United Arab Emirates",
        status="completed",
        latitude=25.2048,
        longitude=55.2708,
        climate_adaptation_rate_percent=80.0,
        exposure_coverage_percent=75.0,
        annual_average_skin_improvement_c=0.5,
        annual_average_core_improvement_c=0.1,
        maximum_skin_improvement_c=1.2,
        effective_cooling_hours=400,
        sampled_day_count=36,
        eligible_sample_count=27,
        evaluated_weighted_days=274,
        beneficial_weighted_days=219,
        retry_count=0,
        error_message=None,
        monthly_json=[],
    )

    batch = SimpleNamespace(
        id="test-batch",
        status="completed",
        request_json={
            "year": 2023,
            "sample_days_per_month": 3,
        },
        summary_json={},
        city_results=[city_result],
    )

    archive_bytes = build_batch_export_zip(
        batch
    )

    with zipfile.ZipFile(
        BytesIO(archive_bytes)
    ) as archive:
        names = set(
            archive.namelist()
        )

    assert "city-summary.csv" in names
    assert "sample-results.csv" in names
    assert "results.geojson" in names
    assert "results.json" in names

@pytest.mark.unit
def test_sample_csv_header_and_rows_have_same_width():
    import csv, io
    from app.services.global_batch_export import build_sample_results_csv

    sample = {
        "sample_date_local": "2023-07-16T12:00:00", "weight_days": 31,
        "mean_air_temperature_c": 40.0, "maximum_air_temperature_c": 42.0,
        "daily_maximum_air_temperature_c": 44.0,
        "mean_solar_radiation_w_m2": 800.0, "maximum_solar_radiation_w_m2": 900.0,
        "exposure_eligible": True, "beneficial": True,
        "average_skin_improvement_c": 1.0, "final_skin_improvement_c": 1.2,
        "average_core_improvement_c": 0.5, "maximum_skin_improvement_c": 1.5,
        "weather_from_cache": True,
    }
    city = SimpleNamespace(city_id="dubai", city_name="Dubai", country="UAE",
                           monthly_json=[{"month": 7, "samples": [sample]}])
    batch = SimpleNamespace(id="b", city_results=[city])

    rows = list(csv.reader(io.StringIO(build_sample_results_csv(batch))))
    assert len(rows[0]) == len(rows[1])
    header = rows[0]
    assert rows[1][header.index("daily_maximum_air_temperature_c")] == "44.0"
    assert rows[1][header.index("mean_solar_radiation_w_m2")] == "800.0"
```

### File: `backend/tests/test_stage_4_2_exposure.py`
```python
import pytest

from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)
from app.services.climate_adaptation import (
    is_exposure_eligible,
)


def make_request(
    *,
    match_mode: str = "all",
) -> GlobalBatchCreate:
    person = PersonInput(
        met=2.0,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )

    control = MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.3,
        solar_transmittance=0,
        infrared_emissivity=0.9,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    radiative = MaterialInput(
        name="Radiative",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    return GlobalBatchCreate(
        city_ids=["dubai"],
        sample_days_per_month=3,
        minimum_air_temperature_c=30,
        minimum_solar_radiation_w_m2=300,
        exposure_match_mode=match_mode,
        person=person,
        control_material=control,
        rc_material=radiative,
    )


@pytest.mark.unit
def test_all_mode_requires_all_thresholds():
    request = make_request(
        match_mode="all",
    )

    assert is_exposure_eligible(
        mean_air_temperature_c=35,
        mean_solar_radiation_w_m2=200,
        request=request,
    ) is False


@pytest.mark.unit
def test_any_mode_requires_one_threshold():
    request = make_request(
        match_mode="any",
    )

    assert is_exposure_eligible(
        mean_air_temperature_c=35,
        mean_solar_radiation_w_m2=200,
        request=request,
    ) is True


@pytest.mark.unit
def test_no_threshold_means_all_samples_eligible():
    request = make_request()

    request.minimum_air_temperature_c = None
    request.minimum_solar_radiation_w_m2 = None

    assert is_exposure_eligible(
        mean_air_temperature_c=5,
        mean_solar_radiation_w_m2=0,
        request=request,
    ) is True
```

### File: `backend/tests/test_stage_4_2_sampling.py`
```python
import pytest

from app.services.climate_adaptation import (
    build_weighted_sample_days,
)


@pytest.mark.unit
def test_three_samples_cover_entire_month():
    samples = build_weighted_sample_days(
        days_in_month=31,
        sample_count=3,
    )

    assert len(samples) == 3

    assert sum(
        weight
        for _, weight in samples
    ) == 31

    assert samples == sorted(
        samples,
        key=lambda item: item[0],
    )


@pytest.mark.unit
def test_one_legacy_sample_uses_requested_day():
    samples = build_weighted_sample_days(
        days_in_month=30,
        sample_count=1,
        legacy_representative_day=15,
    )

    assert samples == [
        (15, 30),
    ]


@pytest.mark.unit
def test_sample_count_cannot_exceed_month_days():
    samples = build_weighted_sample_days(
        days_in_month=3,
        sample_count=7,
    )

    assert len(samples) == 3

    assert sum(
        weight
        for _, weight in samples
    ) == 3
```

### File: `backend/tests/test_stage_4_3_estimate.py`
```python
import pytest


@pytest.mark.api
def test_daily_batch_estimate(
    client,
    person,
    control_material,
    rc_material,
):
    response = client.post(
        "/api/v1/global-batches/estimate",
        json={
            "name": "Daily estimate",
            "city_ids": [
                "dubai",
                "singapore",
            ],
            "year": 2024,
            "start_month": 1,
            "end_month": 12,
            "analysis_resolution": "daily",
            "daily_stride_days": 1,
            "sample_days_per_month": 3,
            "local_start_hour": 12,
            "duration_minutes": 120,
            "output_interval_minutes": 10,
            "minimum_skin_improvement_c": 0.2,
            "minimum_air_temperature_c": 30,
            "minimum_solar_radiation_w_m2": 300,
            "exposure_match_mode": "all",
            "person": person.model_dump(mode="json"),
            "control_material": control_material.model_dump(mode="json"),
            "rc_material": rc_material.model_dump(mode="json"),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["samples_per_city"] == 366
    assert data["total_samples"] == 732
    assert (
        data["thermal_simulation_count"]
        == 1464
    )
    assert (
        data["estimated_weather_requests"]
        == 24
    )
```

### File: `backend/tests/test_stage_4_3_sampling.py`
```python
import calendar

import pytest

from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)
from app.services.annual_sampling import (
    build_daily_stride_sample_days,
    build_month_sampling_plan,
    estimate_sample_count,
)


def make_request(
    *,
    resolution: str,
    stride: int = 1,
) -> GlobalBatchCreate:
    person = PersonInput(
        met=2.0,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )

    control = MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.3,
        solar_transmittance=0,
        infrared_emissivity=0.9,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    radiative = MaterialInput(
        name="Radiative cooling",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    return GlobalBatchCreate(
        city_ids=["dubai"],
        year=2024,
        start_month=1,
        end_month=12,
        analysis_resolution=resolution,
        daily_stride_days=stride,
        person=person,
        control_material=control,
        rc_material=radiative,
    )


@pytest.mark.unit
def test_daily_stride_one_has_one_sample_per_day():
    samples = build_daily_stride_sample_days(
        days_in_month=31,
        stride_days=1,
    )

    assert len(samples) == 31

    assert all(
        weight == 1
        for _, weight in samples
    )

    assert sum(
        weight
        for _, weight in samples
    ) == 31


@pytest.mark.unit
def test_daily_stride_seven_covers_month():
    samples = build_daily_stride_sample_days(
        days_in_month=31,
        stride_days=7,
    )

    assert len(samples) == 5

    assert sum(
        weight
        for _, weight in samples
    ) == 31


@pytest.mark.unit
def test_leap_year_daily_plan_has_366_samples():
    request = make_request(
        resolution="daily",
        stride=1,
    )

    assert calendar.isleap(
        request.year
    )

    assert estimate_sample_count(
        request
    ) == 366


@pytest.mark.unit
def test_month_plan_returns_actual_dates():
    request = make_request(
        resolution="daily",
        stride=1,
    )

    plan = build_month_sampling_plan(
        request=request,
        month=2,
    )

    assert len(plan) == 29
    assert plan[0].date_local.day == 1
    assert plan[-1].date_local.day == 29
```

### File: `backend/tests/test_stage_4_3_weather_slice.py`
```python
from datetime import (
    datetime,
    timedelta,
    timezone,
)

import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.weather import (
    slice_weather_time_series,
)

from app.services.weather_quality import WeatherInsufficientCoverageError


def make_weather() -> WeatherTimeSeries:
    start = datetime(
        2023,
        7,
        1,
        0,
        tzinfo=timezone.utc,
    )

    points = [
        WeatherPoint(
            timestamp=start
            + timedelta(hours=index),
            air_temperature_c=30,
            relative_humidity_percent=60,
            wind_speed_m_s=2,
            ghi_w_m2=500,
            direct_radiation_w_m2=300,
            diffuse_radiation_w_m2=200,
            dni_w_m2=600,
        )
        for index in range(72)
    ]

    city = CityResponse(
        id="test",
        name="Test City",
        country="Test",
        latitude=0,
        longitude=0,
        elevation_m=0,
        timezone="UTC",
        climate_type="test",
    )

    return WeatherTimeSeries(
        city=city,
        requested_start_time=start,
        requested_end_time=(
            start + timedelta(hours=71)
        ),
        points=points,
        source=WeatherSourceMetadata(
            provider="test",
            dataset="test",
            model="test",
            latitude=0,
            longitude=0,
            elevation_m=0,
            timezone="UTC",
            downloaded_at=start,
            from_cache=True,
            attribution="test",
        ),
    )


@pytest.mark.unit
def test_slice_weather_includes_padding():
    weather = make_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(
            2023,
            7,
            2,
            12,
        ),
        duration_minutes=120,
        padding_hours=1,
    )

    timestamps = [
        point.timestamp
        for point in sliced.points
    ]

    assert datetime(
        2023,
        7,
        2,
        11,
        tzinfo=timezone.utc,
    ) in timestamps

    assert datetime(
        2023,
        7,
        2,
        15,
        tzinfo=timezone.utc,
    ) in timestamps


@pytest.mark.unit
def test_slice_fails_when_range_not_covered():
    weather = make_weather()

    with pytest.raises(
        WeatherInsufficientCoverageError,
        match="does not cover",
    ):
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(2023, 8, 1, 12),
            duration_minutes=120,
        )

```

### File: `backend/tests/test_stage_4_4_analytics.py`
```python
from datetime import (
    datetime,
    timedelta,
)

import pytest

from app.schemas.global_batch import (
    DailyAdaptationResult,
)
from app.services.climate_analytics import (
    detect_heatwave_events,
    weighted_percentile,
)


def make_sample(
    *,
    day: int,
    maximum_temperature_c: float,
    skin_improvement_c: float = 0.5,
) -> DailyAdaptationResult:
    return DailyAdaptationResult(
        sample_date_local=datetime(
            2025,
            7,
            day,
            12,
        ),
        weight_days=1,
        mean_air_temperature_c=(
            maximum_temperature_c - 3
        ),
        maximum_air_temperature_c=(
            maximum_temperature_c
        ),
        daily_maximum_air_temperature_c=(
            maximum_temperature_c
        ),
        mean_solar_radiation_w_m2=500,
        maximum_solar_radiation_w_m2=800,
        exposure_eligible=True,
        beneficial=True,
        average_skin_improvement_c=(
            skin_improvement_c
        ),
        final_skin_improvement_c=(
            skin_improvement_c
        ),
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=(
            skin_improvement_c + 0.1
        ),
        weather_from_cache=True,
    )


@pytest.mark.unit
def test_weighted_percentile():
    values = [
        (0.1, 1),
        (0.2, 1),
        (0.3, 1),
        (0.4, 1),
        (0.5, 1),
    ]

    assert weighted_percentile(
        values,
        50,
    ) == 0.3

    assert weighted_percentile(
        values,
        90,
    ) == 0.5


@pytest.mark.unit
def test_weighted_percentile_uses_weights():
    values = [
        (0.1, 10),
        (1.0, 1),
    ]

    assert weighted_percentile(
        values,
        50,
    ) == 0.1


@pytest.mark.unit
def test_detects_consecutive_heatwave():
    samples = [
        make_sample(
            day=1,
            maximum_temperature_c=34,
        ),
        make_sample(
            day=2,
            maximum_temperature_c=36,
        ),
        make_sample(
            day=3,
            maximum_temperature_c=37,
        ),
        make_sample(
            day=4,
            maximum_temperature_c=38,
        ),
        make_sample(
            day=5,
            maximum_temperature_c=33,
        ),
    ]

    events = detect_heatwave_events(
        samples=samples,
        temperature_threshold_c=35,
        minimum_consecutive_days=3,
    )

    assert len(events) == 1
    assert events[0].duration_days == 3
    assert (
        events[0].peak_air_temperature_c
        == 38
    )


@pytest.mark.unit
def test_non_consecutive_hot_days_are_not_heatwave():
    samples = [
        make_sample(
            day=1,
            maximum_temperature_c=36,
        ),
        make_sample(
            day=3,
            maximum_temperature_c=37,
        ),
        make_sample(
            day=4,
            maximum_temperature_c=38,
        ),
    ]

    events = detect_heatwave_events(
        samples=samples,
        temperature_threshold_c=35,
        minimum_consecutive_days=3,
    )

    assert events == []
```

### File: `backend/tests/test_stage_4_4_checkpoint.py`
```python
from datetime import datetime
from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.schemas.global_batch import (
    DailyAdaptationResult,
    GlobalBatchCreate,
    MonthlyAdaptationResult,
)

@pytest.fixture
def completed_partial_batch(
    db_session,
    person,
    control_material,
    rc_material,
):
    request = GlobalBatchCreate(
        city_ids=["dubai"],
        year=2025,
        sample_days_per_month=1,
        resume_from_checkpoint=True,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )
    
    batch = GlobalBatchJob(
        id=str(uuid4()),
        status="failed",
        request_json=request.model_dump(
            mode="json",
        ),
        summary_json={},
    )

    db_session.add(batch)
    db_session.flush()

    city_result = GlobalCityResult(
        id=str(uuid4()),
        batch_id=batch.id,
        city_id="dubai",
        city_name="Dubai",
        country="United Arab Emirates",
        latitude=25.2048,
        longitude=55.2708,
        status="failed",
        stage="failed",
        progress=25,
        monthly_json=[
            {
                "month": 1,
                "sampled_day_count": 1,
                "eligible_sample_count": 1,
                "total_weighted_days": 31,
                "evaluated_weighted_days": 31,
                "beneficial_weighted_days": 31,
                "exposure_coverage_percent": 100,
                "climate_adaptation_rate_percent": 100,
                "average_skin_improvement_c": 0.5,
                "average_core_improvement_c": 0.1,
                "maximum_skin_improvement_c": 0.8,
                "samples": [],
            }
        ],
        completed_month_count=1,
        last_checkpoint_month=1,
        resumed_from_checkpoint=False,
        retry_count=0,
        error_message="Simulated interruption",
    )

    db_session.add(city_result)
    db_session.commit()

    db_session.refresh(batch)
    db_session.refresh(city_result)

    return SimpleNamespace(
        id=batch.id,
        batch=batch,
        city_result=city_result,
        session=db_session,
    )


@pytest.mark.integration
def test_retry_preserves_checkpoint_when_enabled(
    client,
    completed_partial_batch,
):
    session = completed_partial_batch.session
    batch = completed_partial_batch.batch
    city_result = completed_partial_batch.city_result

    # 驗證 fixture 符合 retry endpoint 的前置條件。
    assert batch.status == "failed"
    assert city_result.status == "failed"
    assert city_result.monthly_json is not None
    assert len(city_result.monthly_json) == 1
    assert city_result.completed_month_count == 1
    assert city_result.last_checkpoint_month == 1

    original_monthly_json = (
        city_result.monthly_json.copy()
    )

    response = client.post(
        (
            "/api/v1/global-batches/"
            f"{batch.id}"
            "/retry-failed"
        )
    )

    assert response.status_code == 202, (
        response.text
    )

    session.expire_all()

    refreshed_result = session.get(
        GlobalCityResult,
        city_result.id,
    )

    assert refreshed_result is not None

    # Checkpoint 不應在 retry 時被刪除。
    assert refreshed_result.monthly_json is not None
    assert (
        refreshed_result.monthly_json
        == original_monthly_json
    )
    assert (
        refreshed_result.completed_month_count
        == 1
    )
    assert (
        refreshed_result.last_checkpoint_month
        == 1
    )
    assert (
        refreshed_result.resumed_from_checkpoint
        is True
    )


@pytest.mark.unit
def test_monthly_checkpoint_round_trip():
    sample = DailyAdaptationResult(
        sample_date_local=datetime(
            2025,
            1,
            15,
            12,
        ),
        weight_days=31,
        mean_air_temperature_c=32,
        maximum_air_temperature_c=36,
        mean_solar_radiation_w_m2=500,
        maximum_solar_radiation_w_m2=800,
        exposure_eligible=True,
        beneficial=True,
        average_skin_improvement_c=0.5,
        final_skin_improvement_c=0.6,
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=0.8,
        weather_from_cache=True,
    )

    result = MonthlyAdaptationResult(
        month=1,
        sampled_day_count=1,
        eligible_sample_count=1,
        total_weighted_days=31,
        evaluated_weighted_days=31,
        beneficial_weighted_days=31,
        exposure_coverage_percent=100,
        climate_adaptation_rate_percent=100,
        average_skin_improvement_c=0.5,
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=0.8,
        samples=[sample],
    )

    payload = result.model_dump(
        mode="json"
    )

    restored = (
        MonthlyAdaptationResult
        .model_validate(payload)
    )

    assert restored.month == 1
    assert restored.sampled_day_count == 1
    assert len(restored.samples) == 1
```

### File: `backend/tests/test_stage_8_observability.py`
```python
from datetime import timedelta
from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.api import ops as ops_api
from app.core.time import utc_now
from app.models.global_batch import GlobalBatchJob, GlobalCityCheckpoint, GlobalCityResult
from app.schemas.global_batch import GlobalBatchCreate, MaterialInput, PersonInput
from app.schemas.ops import WorkerStatus
from app.services.checkpoints import CheckpointProvenance, load_resume_state
from app.services.global_batch_service import batch_progress_event, derive_lease_state
from app.services.job_state import BatchStatus, derive_batch_status


# --------------------------------------------------------------------------
# unit
# --------------------------------------------------------------------------
def make_request_json(city_id: str, *, start_month: int = 7, end_month: int = 12) -> dict:
    """Complete, schema-valid request so GlobalBatchDetail can re-validate it."""
    request = GlobalBatchCreate(
        city_ids=[city_id],
        year=2023,
        start_month=start_month,
        end_month=end_month,
        local_start_hour=12,  # belongs on the request, not PersonInput
        duration_minutes=120,
        output_interval_minutes=10,
        minimum_skin_improvement_c=0.2,
        person=PersonInput(
            met=2.0,
            body_surface_area_m2=1.8,
            initial_core_temperature_c=36.8,
            initial_skin_temperature_c=33.7,
        ),
        control_material=MaterialInput(
            name="Control",
            clothing_insulation_clo=0.5,
            solar_reflectance=0.3,
            solar_transmittance=0,
            infrared_emissivity=0.9,
            projected_solar_area_factor=0.25,
        ),
        rc_material=MaterialInput(
            name="RC",
            clothing_insulation_clo=0.4,
            solar_reflectance=0.92,
            solar_transmittance=0,
            infrared_emissivity=0.95,
            projected_solar_area_factor=0.25,
        ),
    )
    return request.model_dump(mode="json")


@pytest.mark.unit
def test_lease_state_is_derived_server_side():
    now = utc_now()
    assert derive_lease_state(None, None, now) == "none"
    assert derive_lease_state("w", None, now) == "none"
    assert derive_lease_state("w", now + timedelta(seconds=30), now) == "live"
    assert derive_lease_state("w", now - timedelta(seconds=1), now) == "expired"


@pytest.mark.unit
def test_progress_event_is_lightweight_and_carries_checkpoint_months():
    now = utc_now()
    city = SimpleNamespace(
        id="c1", city_id="dubai", status="running", stage="analyzing", progress=40,
        retry_count=1, completed_month_count=4, last_checkpoint_month=4,
        last_heartbeat_at=now, lease_owner="host:1:task", lease_expires_at=now + timedelta(minutes=2),
        error_message=None,
    )
    batch = SimpleNamespace(
        id="b1", celery_group_id=None, status="running", stage="analyzing_cities", progress=40,
        total_city_count=1, completed_city_count=0, failed_city_count=0, cancelled_city_count=0,
        summary_json=None, error_message=None, created_at=now, updated_at=now,
        started_at=now, completed_at=None, attempt=1, lease_owner=None, lease_expires_at=None,
        last_heartbeat_at=None, cancel_requested_at=None, city_results=[city],
    )

    event = batch_progress_event(batch, {"c1": [1, 2, 3, 4]})

    assert event.batch.attempt == 1
    assert event.cities[0].lease_state == "live"
    assert event.cities[0].checkpoint_months == [1, 2, 3, 4]
    assert "monthly_results" not in event.cities[0].model_dump()


@pytest.mark.unit
def test_derive_batch_status_matches_refresh_rules():
    assert derive_batch_status({"completed": 1}, 2, False) is None
    assert derive_batch_status({"completed": 2}, 2, False) == BatchStatus.COMPLETED
    assert derive_batch_status({"completed": 1, "failed": 1}, 2, False) == BatchStatus.PARTIAL_COMPLETED
    assert derive_batch_status({"failed": 2}, 2, False) == BatchStatus.FAILED
    assert derive_batch_status({"cancelled": 2}, 2, True) == BatchStatus.CANCELLED
    assert derive_batch_status({"completed": 1, "cancelled": 1}, 2, True) == BatchStatus.PARTIAL_COMPLETED


# --------------------------------------------------------------------------
# integration (PostgreSQL via the db_session / client fixtures)
# --------------------------------------------------------------------------

def seed_batch(session, *, start_month=7, end_month=12, checkpoint_months=(7, 8, 10)):
    request_json = make_request_json("dubai", start_month=start_month, end_month=end_month)
    provenance = CheckpointProvenance.for_request(GlobalBatchCreate.model_validate(request_json))

    batch = GlobalBatchJob(
        id=str(uuid4()), status="running", stage="analyzing_cities", progress=10,
        total_city_count=1, attempt=1, request_json=request_json,
    )
    session.add(batch)
    session.flush()

    city = GlobalCityResult(
        id=str(uuid4()), batch_id=batch.id, city_id="dubai", city_name="Dubai",
        country="United Arab Emirates", latitude=25.2, longitude=55.27,
        status="running", stage="analyzing", progress=30,
        lease_owner="host:1:task", lease_expires_at=utc_now() + timedelta(minutes=2),
        last_heartbeat_at=utc_now(),
    )
    session.add(city)
    session.flush()

    for month in checkpoint_months:
        session.add(GlobalCityCheckpoint(
            city_result_id=city.id, month=month, attempt=0,
            payload_json={"month": month, "sampled_day_count": 3, "skipped_samples": [], "samples": []},
            model_version=provenance.model_version,
            parameter_fingerprint=provenance.parameter_fingerprint,
            request_sha256=provenance.request_sha256,
        ))
    session.commit()
    return batch, city, provenance


@pytest.mark.integration
def test_resume_prefix_respects_start_month(db_session):
    _, city, provenance = seed_batch(db_session, start_month=7, checkpoint_months=(7, 8, 10))

    state = load_resume_state(db_session, city.id, start_month=7, provenance=provenance)

    assert state.next_month == 9  # hole at 9 -> resume there, discard 10
    assert [p["month"] for p in state.payloads] == [7, 8]


@pytest.mark.integration
def test_detail_and_checkpoint_endpoints_expose_stage_7_state(client, db_session):
    batch, city, _ = seed_batch(db_session)

    detail = client.get(f"/api/v1/global-batches/{batch.id}").json()
    row = detail["city_results"][0]
    assert detail["attempt"] == 1
    assert row["lease_state"] == "live"
    assert row["lease_owner"] == "host:1:task"
    assert row["checkpoint_months"] == [7, 8, 10]

    checkpoints = client.get(
        f"/api/v1/global-batches/{batch.id}/cities/{city.id}/checkpoints"
    ).json()
    assert checkpoints["start_month"] == 7
    assert checkpoints["resume_from_month"] == 9
    assert [item["month"] for item in checkpoints["items"]] == [7, 8, 10]
    assert len(checkpoints["items"][0]["payload_sha256"]) == 64

    assert client.get(
        f"/api/v1/global-batches/{batch.id}/cities/does-not-exist/checkpoints"
    ).status_code == 404


@pytest.mark.integration
def test_ops_status_reports_workers_and_leases(client, db_session, monkeypatch):
    seed_batch(db_session)
    monkeypatch.setattr(
        ops_api, "inspect_workers",
        lambda timeout=1.0: (True, [WorkerStatus(name="w1@host", active_task_count=1, reserved_task_count=0)]),
    )

    body = client.get("/api/v1/ops/status").json()

    assert body["broker_reachable"] is True
    assert body["worker_count"] == 1
    assert body["leases"]["running_cities"] >= 1
    assert body["leases"]["live_leases"] >= 1
    assert body["worst_case_recovery_seconds"] == body["lease_ttl_seconds"] + body["reaper_interval_seconds"]


@pytest.mark.integration
def test_ops_status_survives_broker_outage(client, monkeypatch):
    def broken_inspect(timeout=1.0):
        raise ConnectionError("redis down")

    # inspect_workers wraps exceptions itself; emulate by patching the Celery call.
    monkeypatch.setattr(ops_api.celery_app.control, "inspect", broken_inspect)

    body = client.get("/api/v1/ops/status").json()
    assert body["broker_reachable"] is False
    assert body["workers"] == []
```

### File: `backend/tests/test_stage_8_resume_benchmark.py`
```python
"""Stage 8 acceptance: resuming from monthly checkpoints is exact and cheap.

Fully offline. ``get_historical_weather_range`` is replaced by a deterministic
synthetic provider so the only cost measured is the thermal model.

Assertions
1. The uninterrupted run fetches one weather range per month.
2. A run that crashes after month N leaves exactly N checkpoints.
3. The resumed run fetches only the missing 12 - N months and reproduces the
   uninterrupted result exactly (monthly results and every annual metric).

Set RECORD_BENCHMARK=1 to write timings to docs/acceptance/stage-8-observability/.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
from datetime import datetime, timedelta
from pathlib import Path
from time import perf_counter
from zoneinfo import ZoneInfo

import pytest

from app.core.cities import CityConfig
from app.schemas.global_batch import GlobalBatchCreate, MonthlyAdaptationResult
from app.schemas.weather import (
    WeatherPoint,
    WeatherQualityReport,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services import climate_adaptation
from app.services.climate_adaptation import analyze_city_climate_adaptation
from app.services.weather import city_to_response, normalize_local_datetime, to_utc
from app.schemas.environment import EnvironmentAssumptions
from tests.helpers.environment import LEGACY, with_physical_variables

RECORD_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs" / "acceptance" / "stage-8-observability" / "resume-benchmark.json"
)

CRASH_AFTER_MONTH = 4

ANNUAL_METRIC_KEYS = (
    "climate_adaptation_rate_percent",
    "exposure_coverage_percent",
    "annual_average_skin_improvement_c",
    "annual_average_core_improvement_c",
    "maximum_skin_improvement_c",
    "effective_cooling_hours",
    "sampled_day_count",
    "eligible_sample_count",
    "evaluated_weighted_days",
    "beneficial_weighted_days",
    "completed_month_count",
    "skin_improvement_p50_c",
    "skin_improvement_p90_c",
    "skin_improvement_p95_c",
    "core_improvement_p50_c",
    "core_improvement_p90_c",
    "core_improvement_p95_c",
    "heatwave_event_count",
    "longest_heatwave_days",
    "heatwave_events",
)


class SyntheticWeatherProvider:
    """Deterministic hourly weather with a clear diurnal cycle. Counts calls."""

    def __init__(self) -> None:
        self.calls = 0
        self.extra_variables_seen: list[tuple[str, ...]] = []

    async def __call__(
        self, *, city, start_time_local, end_time_local, padding_hours=1,
        require_window_coverage=True, extra_variables: tuple[str, ...] = (),
    ) -> WeatherTimeSeries:
        self.calls += 1
        self.extra_variables_seen.append(tuple(extra_variables))

        tz = ZoneInfo(city.timezone)
        start = normalize_local_datetime(start_time_local, city.timezone)
        end = normalize_local_datetime(end_time_local, city.timezone)

        cursor = to_utc(start - timedelta(hours=padding_hours)).replace(minute=0, second=0, microsecond=0)
        stop = to_utc(end + timedelta(hours=padding_hours + 1))

        points: list[WeatherPoint] = []
        while cursor <= stop:
            local = cursor.astimezone(tz)
            hour = local.hour + local.minute / 60.0
            day_of_year = local.timetuple().tm_yday

            seasonal = 6.0 * math.sin(2.0 * math.pi * (day_of_year - 110) / 365.0)
            diurnal = 5.0 * math.sin(2.0 * math.pi * (hour - 9.0) / 24.0)
            temperature = 31.0 + seasonal + diurnal

            daylight = 6.0 <= hour <= 18.0
            ghi = 950.0 * math.sin(math.pi * (hour - 6.0) / 12.0) if daylight else 0.0

            points.append(
                WeatherPoint(
                    timestamp=local,
                    air_temperature_c=round(temperature, 3),
                    relative_humidity_percent=40.0,
                    wind_speed_m_s=2.5,
                    ghi_w_m2=round(ghi, 2),
                    direct_radiation_w_m2=round(ghi * 0.75, 2),
                    diffuse_radiation_w_m2=round(ghi * 0.25, 2),
                    dni_w_m2=round(ghi * 0.8, 2),
                )
            )
            cursor += timedelta(hours=1)

        if extra_variables:
            points = with_physical_variables(points)

        digest = hashlib.sha256(f"{city.id}|{start.isoformat()}|{end.isoformat()}".encode()).hexdigest()
        # delete the old line:  assert extra_variables == (), extra_variables

        return WeatherTimeSeries(
            city=city_to_response(city),
            requested_start_time=start,
            requested_end_time=end,
            points=points,
            source=WeatherSourceMetadata(
                provider="synthetic",
                dataset="stage-8-benchmark",
                model="synthetic",
                latitude=city.latitude,
                longitude=city.longitude,
                elevation_m=city.elevation_m,
                timezone=city.timezone,
                downloaded_at=start,
                from_cache=True,
                attribution="synthetic",
                payload_sha256=digest,
                quality=WeatherQualityReport(expected_step_seconds=3600, point_count=len(points)),
            ),
        )


def make_request(
    person, control_material, rc_material,
    environment_assumptions: EnvironmentAssumptions = LEGACY,
) -> GlobalBatchCreate:
    return GlobalBatchCreate(
        name="Stage 8 resume benchmark",
        city_ids=["dubai"],
        year=2023,
        start_month=1,
        end_month=12,
        analysis_resolution="representative",
        sample_days_per_month=1,
        local_start_hour=12,
        duration_minutes=60,
        output_interval_minutes=10,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
        environment_assumptions=environment_assumptions,
    )


@pytest.mark.benchmark
@pytest.mark.asyncio
async def test_resume_recomputes_only_missing_months_and_matches_uninterrupted(
    monkeypatch, person, control_material, rc_material
):
    provider = SyntheticWeatherProvider()
    monkeypatch.setattr(climate_adaptation, "get_historical_weather_range", provider)

    request = make_request(person, control_material, rc_material)

    # --- 1. uninterrupted reference run -------------------------------------
    started = perf_counter()
    full = await analyze_city_climate_adaptation(city_id="dubai", request=request)
    full_seconds = perf_counter() - started

    assert provider.calls == 12
    assert set(provider.extra_variables_seen) == {()}
    assert full["completed_month_count"] == 12

    # --- 2. crash after CRASH_AFTER_MONTH -----------------------------------
    saved: list[MonthlyAdaptationResult] = []

    def checkpoint_then_crash(monthly, completed_month, _completed_sample_count):
        saved[:] = [m.model_copy(deep=True) for m in monthly]
        if completed_month == CRASH_AFTER_MONTH:
            raise RuntimeError("simulated worker crash")

    provider.calls = 0
    with pytest.raises(RuntimeError, match="simulated worker crash"):
        await analyze_city_climate_adaptation(
            city_id="dubai", request=request, checkpoint_callback=checkpoint_then_crash
        )

    assert provider.calls == CRASH_AFTER_MONTH
    assert [m.month for m in saved] == list(range(1, CRASH_AFTER_MONTH + 1))

    # --- 3. resume from the saved checkpoints -------------------------------
    provider.calls = 0
    stages: list[str] = []
    started = perf_counter()
    resumed = await analyze_city_climate_adaptation(
        city_id="dubai",
        request=request,
        initial_monthly_results=saved,
        progress_callback=lambda _progress, stage: stages.append(stage),
    )
    resumed_seconds = perf_counter() - started

    assert provider.calls == 12 - CRASH_AFTER_MONTH, "resume must not refetch checkpointed months"
    assert sum(s.startswith("restored_checkpoint_") for s in stages) == CRASH_AFTER_MONTH

    # Exactness: resumed == uninterrupted, month by month and metric by metric.
    assert resumed["monthly_results"] == full["monthly_results"]
    for key in ANNUAL_METRIC_KEYS:
        assert resumed[key] == full[key], key

    # Known Stage 7 limitation, documented: restored months carry no weather
    # payload hash because no weather was fetched for them.
    restored_hashes = resumed["data_quality"]["monthly_weather_payload_sha256"]
    assert set(restored_hashes) == {f"{m:02d}" for m in range(CRASH_AFTER_MONTH + 1, 13)}

    # Cost: the resumed run should scale with the missing months, not the year.
    expected_fraction = (12 - CRASH_AFTER_MONTH) / 12
    assert resumed_seconds < full_seconds * (expected_fraction + 0.35), (
        f"resume took {resumed_seconds:.2f}s vs full {full_seconds:.2f}s"
    )

    if os.environ.get("RECORD_BENCHMARK") == "1":
        RECORD_PATH.parent.mkdir(parents=True, exist_ok=True)
        RECORD_PATH.write_text(
            json.dumps(
                {
                    "recorded_at": datetime.now().astimezone().isoformat(),
                    "crash_after_month": CRASH_AFTER_MONTH,
                    "full_run_seconds": round(full_seconds, 3),
                    "resumed_run_seconds": round(resumed_seconds, 3),
                    "months_restored": CRASH_AFTER_MONTH,
                    "months_computed": 12 - CRASH_AFTER_MONTH,
                    "weather_fetches_full": 12,
                    "weather_fetches_resumed": 12 - CRASH_AFTER_MONTH,
                    "resumed_equals_full": True,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
```

### File: `backend/tests/test_stage_9_leases_and_provenance.py`
```python
"""Stage 9: single-job leases, owner-guarded checkpoint writes, provenance."""

from datetime import datetime, timedelta
from uuid import uuid4

import pytest
from sqlalchemy import select

from app.models.global_batch import GlobalBatchJob, GlobalCityCheckpoint, GlobalCityResult
from app.models.simulation_job import SimulationJob
from app.schemas.global_batch import GlobalBatchCreate
from app.services.checkpoints import CheckpointProvenance, load_resume_state, upsert_month_checkpoint
from app.services.job_state import IllegalTransition, assert_city_transition, assert_job_transition
from app.services.leases import (
    acquire_city_lease,
    acquire_job_lease,
    heartbeat_city_lease,
    heartbeat_job_lease,
)
from tests.test_stage_8_observability import make_request_json


# --- unit ---------------------------------------------------------------

@pytest.mark.unit
def test_job_transitions():
    assert_job_transition("queued", "running")
    assert_job_transition("running", "queued")      # reaper
    assert_job_transition("cancelling", "completed")
    for current in ("completed", "failed", "cancelled"):
        with pytest.raises(IllegalTransition):
            assert_job_transition(current, "running")


@pytest.mark.unit
def test_failed_city_may_be_retried():
    assert_city_transition("failed", "queued")
    with pytest.raises(IllegalTransition):
        assert_city_transition("completed", "queued")


@pytest.mark.unit
def test_request_hash_ignores_non_physics_fields():
    base = GlobalBatchCreate.model_validate(make_request_json("dubai"))
    renamed = base.model_copy(update={"name": "other", "resume_from_checkpoint": False, "execution_profile": "large"})
    changed = base.model_copy(update={"duration_minutes": 60})

    assert CheckpointProvenance.for_request(base) == CheckpointProvenance.for_request(renamed)
    assert CheckpointProvenance.for_request(base) != CheckpointProvenance.for_request(changed)


# --- integration ----------------------------------------------------------

def seed_job(session, **overrides) -> SimulationJob:
    values = {
        "id": str(uuid4()), "city_id": "dubai", "status": "queued",
        "stage": "queued", "progress": 0, "request_json": {},
    }
    values.update(overrides)
    job = SimulationJob(**values)
    session.add(job)
    session.commit()
    return job


@pytest.mark.integration
def test_job_lease_is_exclusive_and_terminal_rows_cannot_be_acquired(db_session):
    job = seed_job(db_session)

    assert acquire_job_lease(db_session, job.id, "worker-a") is True
    assert acquire_job_lease(db_session, job.id, "worker-b") is False   # live lease
    assert acquire_job_lease(db_session, job.id, "worker-a") is True    # re-entrant

    db_session.refresh(job)
    assert job.status == "running"

    done = seed_job(db_session, status="completed")
    assert acquire_job_lease(db_session, done.id, "worker-a") is False  # never resurrect


@pytest.mark.integration
def test_job_heartbeat_by_non_owner_is_rejected_and_rolled_back(db_session):
    job = seed_job(db_session)
    acquire_job_lease(db_session, job.id, "worker-a")

    assert heartbeat_job_lease(db_session, job.id, "worker-b", progress=50) is False
    db_session.refresh(job)
    assert job.progress == 0
    assert job.lease_owner == "worker-a"


def seed_city(session, *, start_month=7, end_month=12):
    batch = GlobalBatchJob(
        id=str(uuid4()), status="running", stage="analyzing_cities", progress=0,
        total_city_count=1, request_json=make_request_json("dubai", start_month=start_month, end_month=end_month),
    )
    session.add(batch)
    session.flush()
    city = GlobalCityResult(
        id=str(uuid4()), batch_id=batch.id, city_id="dubai", city_name="Dubai",
        country="United Arab Emirates", latitude=25.2, longitude=55.27,
        status="queued", stage="queued", progress=0,
    )
    session.add(city)
    session.commit()
    return batch, city


@pytest.mark.integration
def test_checkpoint_write_requires_lease_and_rolls_back_with_lost_heartbeat(db_session):
    batch, city = seed_city(db_session)
    city_id = city.id
    request = GlobalBatchCreate.model_validate(batch.request_json)
    provenance = CheckpointProvenance.for_request(request)
    payload = {"month": 7, "sampled_day_count": 1, "skipped_samples": [], "samples": []}

    # No lease at all: nothing staged.
    assert upsert_month_checkpoint(
        db_session, city_result_id=city_id, owner="ghost", month=7, attempt=0,
        payload=payload, provenance=provenance,
    ) is False

    acquire_city_lease(db_session, city_id, "worker-a")

    # Staged by the owner but the heartbeat is attempted by someone else:
    # the rollback must discard the staged row.
    assert upsert_month_checkpoint(
        db_session, city_result_id=city_id, owner="worker-a", month=7, attempt=0,
        payload=payload, provenance=provenance,
    ) is True
    assert heartbeat_city_lease(db_session, city_id, "worker-b", last_checkpoint_month=7) is False
    assert db_session.scalar(select(GlobalCityCheckpoint).where(GlobalCityCheckpoint.city_result_id == city_id)) is None

    # Owner path: row and heartbeat land together.
    assert upsert_month_checkpoint(
        db_session, city_result_id=city_id, owner="worker-a", month=7, attempt=0,
        payload=payload, provenance=provenance,
    ) is True
    assert heartbeat_city_lease(db_session, city_id, "worker-a", last_checkpoint_month=7) is True
    row = db_session.scalar(select(GlobalCityCheckpoint).where(GlobalCityCheckpoint.city_result_id == city_id))
    assert row.model_version == provenance.model_version
    assert row.parameter_fingerprint == provenance.parameter_fingerprint


@pytest.mark.integration
def test_resume_discards_rows_with_foreign_provenance(db_session):
    batch, city = seed_city(db_session)
    request = GlobalBatchCreate.model_validate(batch.request_json)
    good = CheckpointProvenance.for_request(request)

    def add(month, **override):
        db_session.add(GlobalCityCheckpoint(
            city_result_id=city.id, month=month, attempt=0,
            payload_json={"month": month, "sampled_day_count": 1, "skipped_samples": [], "samples": []},
            model_version=override.get("model_version", good.model_version),
            parameter_fingerprint=override.get("parameter_fingerprint", good.parameter_fingerprint),
            request_sha256=override.get("request_sha256", good.request_sha256),
        ))

    add(7)
    add(8)
    add(9, model_version="0.0.1")   # written by an older model
    add(10)                          # valid, but behind the mismatch
    add(11, model_version=None, parameter_fingerprint=None, request_sha256=None)  # legacy
    db_session.commit()

    state = load_resume_state(db_session, city.id, start_month=7, provenance=good)

    assert state.next_month == 9
    assert [p["month"] for p in state.payloads] == [7, 8]
    assert [d["month"] for d in state.discarded] == [9, 10, 11]
    assert "model_version" in state.discarded[0]["reason"]
    assert "not contiguous" in state.discarded[1]["reason"]
    assert "legacy" in state.discarded[2]["reason"]


@pytest.mark.integration
def test_retry_without_resume_deletes_checkpoint_rows(client, db_session):
    batch, city = seed_city(db_session)
    request = GlobalBatchCreate.model_validate(batch.request_json)
    provenance = CheckpointProvenance.for_request(request)
    db_session.add(GlobalCityCheckpoint(
        city_result_id=city.id, month=7, attempt=0,
        payload_json={"month": 7, "sampled_day_count": 1, "skipped_samples": [], "samples": []},
        model_version=provenance.model_version,
        parameter_fingerprint=provenance.parameter_fingerprint,
        request_sha256=provenance.request_sha256,
    ))
    batch.status = "failed"
    batch.request_json = {**batch.request_json, "resume_from_checkpoint": False}
    city.status = "failed"
    db_session.commit()

    from app.api import global_batches as api
    from types import SimpleNamespace
    api_submit = lambda *, city_results, queue_name: SimpleNamespace(  # noqa: E731
        id="g", results=[SimpleNamespace(id=f"t-{r.city_id}") for r in city_results]
    )
    original = api.submit_city_tasks
    api.submit_city_tasks = api_submit
    try:
        response = client.post(f"/api/v1/global-batches/{batch.id}/retry-failed")
    finally:
        api.submit_city_tasks = original

    assert response.status_code == 202, response.text
    db_session.expire_all()
    assert db_session.scalar(select(GlobalCityCheckpoint).where(GlobalCityCheckpoint.city_result_id == city.id)) is None
    assert db_session.get(GlobalCityResult, city.id).status == "queued"
```

### File: `backend/tests/test_two_node.py`
```python
import math

import pytest

from app.services.two_node import simulate_material, calculate_fluxes


@pytest.mark.unit
def test_simulation_returns_expected_number_of_points(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert len(result.time_series) == 121
    assert result.time_series[0].minute == 0
    assert result.time_series[-1].minute == 120


@pytest.mark.unit
def test_initial_temperatures_are_preserved(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    initial = result.time_series[0]

    assert initial.core_temperature_c == pytest.approx(
        person.initial_core_temperature_c,
        abs=1e-4,
    )

    assert initial.skin_temperature_c == pytest.approx(
        person.initial_skin_temperature_c,
        abs=1e-4,
    )


@pytest.mark.unit
def test_all_temperatures_are_finite(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    for point in result.time_series:
        assert math.isfinite(
            point.core_temperature_c
        )
        assert math.isfinite(
            point.skin_temperature_c
        )


@pytest.mark.unit
def test_temperature_stays_in_broad_physiological_range(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    for point in result.time_series:
        assert 30.0 < point.core_temperature_c < 43.0
        assert 15.0 < point.skin_temperature_c < 45.0


@pytest.mark.unit
def test_energy_balance_residual_is_small(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert (
        result.diagnostics
        .normalized_residual_percent
        < 1.0
    )


@pytest.mark.unit
def test_rc_material_reduces_skin_temperature(
    environment,
    person,
    control_material,
    rc_material,
):
    control = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    rc = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert (
        rc.final_skin_temperature_c
        < control.final_skin_temperature_c
    )


@pytest.mark.unit
def test_identical_materials_produce_identical_results(
    environment,
    person,
    control_material,
):
    first = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    second = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert (
        first.final_core_temperature_c
        == pytest.approx(
            second.final_core_temperature_c,
            abs=1e-8,
        )
    )

    assert (
        first.final_skin_temperature_c
        == pytest.approx(
            second.final_skin_temperature_c,
            abs=1e-8,
        )
    )
    
@pytest.mark.unit
def test_absorbed_solar_raises_clothing_surface_temperature(
    environment, person, control_material
):
    sunlit = calculate_fluxes(36.8, 33.7, environment, person, control_material)
    shaded = calculate_fluxes(
        36.8, 33.7,
        environment.model_copy(update={"solar_radiation_w_m2": 0.0}),
        person, control_material,
    )

    assert sunlit.clothing_surface_temperature_c > shaded.clothing_surface_temperature_c


@pytest.mark.unit
def test_surface_re_emits_part_of_the_absorbed_solar(
    environment, person, control_material
):
    """ADR 0005: the extra surface losses caused by S_abs lie strictly between
    0 and S_abs, so only a fraction of the absorbed solar reaches the skin."""
    sunlit = calculate_fluxes(36.8, 33.7, environment, person, control_material)
    shaded = calculate_fluxes(
        36.8, 33.7,
        environment.model_copy(update={"solar_radiation_w_m2": 0.0}),
        person, control_material,
    )

    extra_surface_losses = (
        sunlit.convection + sunlit.longwave_radiation
    ) - (shaded.convection + shaded.longwave_radiation)

    assert 0.0 < extra_surface_losses < sunlit.solar_absorbed_by_textile
    assert sunlit.evaporation == pytest.approx(shaded.evaporation)


@pytest.mark.unit
def test_deprecated_absorbed_fraction_is_ignored(environment, person, control_material):
    baseline = simulate_material(30, 1, environment, person, control_material)
    altered = simulate_material(
        30, 1, environment, person,
        control_material.model_copy(update={"absorbed_solar_to_body_fraction": 0.9}),
    )

    assert altered.final_skin_temperature_c == pytest.approx(
        baseline.final_skin_temperature_c, abs=1e-9
    )
    
@pytest.mark.unit
def test_energy_diagnostics_do_not_depend_on_output_interval(environment, person, control_material):
    fine = simulate_material(120, 1, environment, person, control_material)
    coarse = simulate_material(120, 30, environment, person, control_material)

    assert coarse.diagnostics.integrated_net_heat_j_m2 == pytest.approx(
        fine.diagnostics.integrated_net_heat_j_m2, abs=1e-3
    )
    assert coarse.diagnostics.normalized_residual_percent == pytest.approx(
        fine.diagnostics.normalized_residual_percent, abs=1e-6
    )
    assert coarse.peak_skin_temperature_c == pytest.approx(fine.peak_skin_temperature_c, abs=1e-4)
    assert coarse.diagnostics.diagnostic_interval_seconds == 60.0


@pytest.mark.unit
def test_output_interval_does_not_change_trajectory(environment, person, control_material):
    fine = simulate_material(120, 1, environment, person, control_material)
    coarse = simulate_material(120, 10, environment, person, control_material)
    by_minute = {p.minute: p for p in fine.time_series}
    for p in coarse.time_series:
        assert p.skin_temperature_c == pytest.approx(by_minute[p.minute].skin_temperature_c, abs=1e-6)
```

### File: `backend/tests/test_weather_api.py`
```python
from datetime import datetime

import pytest

from app.api import weather as weather_api
from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)

@pytest.fixture
def weather_series() -> WeatherTimeSeries:
    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai",
            name="Dubai",
            country="United Arab Emirates",
            latitude=25.25,
            longitude=55.25,
            elevation_m=12.0,
            timezone="Asia/Dubai",
            climate_type="hot_arid",
        ),
        requested_start_time=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        requested_end_time=datetime(
            2025,
            7,
            15,
            12,
            0,
        ),
        points=[
            WeatherPoint(
                timestamp=datetime(
                    2025,
                    7,
                    15,
                    10,
                    0,
                ),
                air_temperature_c=38.0,
                relative_humidity_percent=40.0,
                wind_speed_m_s=1.5,
                ghi_w_m2=700.0,
                direct_radiation_w_m2=520.0,
                diffuse_radiation_w_m2=180.0,
                dni_w_m2=750.0,
            ),
            WeatherPoint(
                timestamp=datetime(
                    2025,
                    7,
                    15,
                    11,
                    0,
                ),
                air_temperature_c=39.0,
                relative_humidity_percent=38.0,
                wind_speed_m_s=2.0,
                ghi_w_m2=800.0,
                direct_radiation_w_m2=620.0,
                diffuse_radiation_w_m2=180.0,
                dni_w_m2=820.0,
            ),
        ],
        source=WeatherSourceMetadata(
            provider="Open-Meteo",
            dataset="Historical Weather API",
            model="ERA5",
            latitude=25.25,
            longitude=55.25,
            elevation_m=12.0,
            timezone="Asia/Dubai",
            downloaded_at=datetime(
                2025,
                7,
                15,
                13,
                0,
            ),
            from_cache=False,
            attribution="Weather data by Open-Meteo",
        ),
    )

@pytest.mark.unit
def test_weather_cities_endpoint(client):
    response = client.get(
        "/api/v1/weather/cities"
    )

    assert response.status_code == 200

    payload = response.json()

    assert len(payload) >= 3

    city_ids = {
        city["id"]
        for city in payload
    }

    assert {
        "dubai",
        "guangzhou",
        "lhasa",
    }.issubset(city_ids)

@pytest.mark.unit
def test_weather_history_endpoint(
    client,
    monkeypatch,
    weather_series,
):
    async def fake_get_historical_weather(
        **kwargs,
    ):
        return weather_series

    monkeypatch.setattr(
        weather_api,
        "get_historical_weather",
        fake_get_historical_weather,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["city"]["id"] == "dubai"
    assert len(payload["points"]) == 2

    assert (
        payload["points"][0]["air_temperature_c"]
        == pytest.approx(38.0)
    )

    assert payload["source"]["from_cache"] is False

@pytest.mark.unit
def test_weather_history_rejects_unknown_city(
    client,
    monkeypatch,
):
    def fake_get_city(city_id):
        raise ValueError(
            f"City not supported: {city_id}"
        )

    monkeypatch.setattr(
        weather_api,
        "get_city",
        fake_get_city,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "unknown",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 422

    assert (
        "City not supported"
        in response.json()["detail"]
    )


@pytest.mark.unit
def test_weather_history_converts_service_error_to_502(
    client,
    monkeypatch,
):
    async def fake_get_historical_weather(
        **kwargs,
    ):
        raise RuntimeError(
            "Open-Meteo unavailable"
        )

    monkeypatch.setattr(
        weather_api,
        "get_historical_weather",
        fake_get_historical_weather,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 502
    assert response.json()["detail"] == (
        "Open-Meteo unavailable"
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "duration",
    [
        0,
        1441,
    ],
)
def test_weather_history_validates_duration(
    client,
    duration,
):
    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": duration,
        },
    )

    assert response.status_code == 422
```

### File: `backend/tests/test_weather_extras.py`
```python
from datetime import date

import pytest

from app.core.cities import get_city
from app.services.weather import build_request_params, parse_weather_points

STAGE10_HOURLY = (
    "temperature_2m,relative_humidity_2m,wind_speed_10m,shortwave_radiation,"
    "direct_radiation,diffuse_radiation,direct_normal_irradiance"
)


@pytest.mark.unit
def test_default_request_is_byte_identical_to_stage10():
    params = build_request_params(get_city("dubai"), date(2023, 7, 1), date(2023, 7, 2))
    assert params["hourly"] == STAGE10_HOURLY  # cache key and golden payload hash depend on it


@pytest.mark.unit
def test_extra_variables_are_appended_sorted():
    params = build_request_params(get_city("dubai"), date(2023, 7, 1), date(2023, 7, 2),
                                  extra_variables=("soil_temperature_0_to_7cm", "cloud_cover"))
    assert params["hourly"].endswith(",cloud_cover,soil_temperature_0_to_7cm")
    with pytest.raises(ValueError):
        build_request_params(get_city("dubai"), date(2023, 7, 1), date(2023, 7, 2),
                             extra_variables=("snowfall",))


@pytest.mark.unit
def test_parse_optional_variables_with_nulls():
    base = {name: [1.0, 2.0] for name in STAGE10_HOURLY.split(",")}
    payload = {
        "utc_offset_seconds": 14400,
        "hourly": {"time": ["2023-07-01T00:00", "2023-07-01T01:00"], **base,
                   "cloud_cover": [10.0, None], "soil_temperature_0_to_7cm": [35.0, 34.5]},
    }
    points = parse_weather_points(payload, get_city("dubai"))
    assert points[0].cloud_cover_percent == 10.0
    assert points[1].cloud_cover_percent is None
    assert points[1].soil_temperature_c == 34.5
```

### File: `backend/tests/test_weather_interpolation.py`
```python
from datetime import datetime
from zoneinfo import ZoneInfo
from tests.helpers.environment import LEGACY


import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.weather_interpolation import (
    WeatherInterpolator,
)


@pytest.fixture
def weather_series():
    timezone = ZoneInfo("Asia/Dubai")

    start = datetime(
        2025,
        7,
        15,
        10,
        0,
        tzinfo=timezone,
    )

    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai",
            name="Dubai",
            country="United Arab Emirates",
            latitude=25.2048,
            longitude=55.2708,
            elevation_m=16,
            timezone="Asia/Dubai",
            climate_type="hot_dry",
        ),
        requested_start_time=start,
        requested_end_time=start.replace(
            hour=12
        ),
        points=[
            WeatherPoint(
                timestamp=start.replace(hour=9),
                air_temperature_c=36,
                relative_humidity_percent=45,
                wind_speed_m_s=1,
                ghi_w_m2=500,
                direct_radiation_w_m2=400,
                diffuse_radiation_w_m2=100,
                dni_w_m2=700,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=10),
                air_temperature_c=38,
                relative_humidity_percent=40,
                wind_speed_m_s=2,
                ghi_w_m2=700,
                direct_radiation_w_m2=550,
                diffuse_radiation_w_m2=150,
                dni_w_m2=800,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=11),
                air_temperature_c=40,
                relative_humidity_percent=35,
                wind_speed_m_s=3,
                ghi_w_m2=900,
                direct_radiation_w_m2=700,
                diffuse_radiation_w_m2=200,
                dni_w_m2=900,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=12),
                air_temperature_c=42,
                relative_humidity_percent=30,
                wind_speed_m_s=4,
                ghi_w_m2=1000,
                direct_radiation_w_m2=800,
                diffuse_radiation_w_m2=200,
                dni_w_m2=950,
            ),
        ],
        source=WeatherSourceMetadata(
            provider="test",
            dataset="test",
            model="test",
            latitude=25.2,
            longitude=55.2,
            elevation_m=16,
            timezone="Asia/Dubai",
            downloaded_at=start,
            from_cache=False,
            attribution="test",
        ),
    )


@pytest.mark.unit
def test_weather_interpolation_at_start(
    weather_series,
):
    interpolator = (
        WeatherInterpolator.from_series(
            weather_series, assumptions=LEGACY
        )
    )

    environment = interpolator.environment_at(
        0
    )

    assert (
        environment.air_temperature_c
        == pytest.approx(38)
    )

    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(700)
    )


@pytest.mark.unit
def test_weather_interpolation_at_half_hour(
    weather_series,
):
    interpolator = (
        WeatherInterpolator.from_series(
            weather_series, assumptions=LEGACY
        )
    )

    environment = interpolator.environment_at(
        1800
    )

    assert (
        environment.air_temperature_c
        == pytest.approx(39)
    )

    assert (
        environment.wind_speed_m_s
        == pytest.approx(2.5)
    )

    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(800)
    )

import numpy as np


@pytest.mark.unit
def test_environment_clamps_negative_wind_and_solar():
    interpolator = WeatherInterpolator(
        relative_seconds=np.array(
            [0.0, 3600.0]
        ),
        temperatures=np.array(
            [30.0, 30.0]
        ),
        humidities=np.array(
            [50.0, 50.0]
        ),
        wind_speeds=np.array(
            [-2.0, -1.0]
        ),
        ghi_values=np.array(
            [-100.0, -50.0]
        ),
        assumptions=LEGACY
    )

    environment = interpolator.environment_at(
        1800
    )

    assert environment.wind_speed_m_s == 0
    assert (
        environment.solar_radiation_w_m2
        == 0
    )
    assert (
        environment.mean_radiant_temperature_c
        == pytest.approx(30.0)
    )


@pytest.mark.unit
def test_mean_radiant_temperature_increase_is_capped():
    interpolator = WeatherInterpolator(
        relative_seconds=np.array(
            [0.0, 3600.0]
        ),
        temperatures=np.array(
            [30.0, 30.0]
        ),
        humidities=np.array(
            [50.0, 50.0]
        ),
        wind_speeds=np.array(
            [1.0, 1.0]
        ),
        ghi_values=np.array(
            [1500.0, 1500.0]
        ),
        assumptions=LEGACY
    )

    environment = interpolator.environment_at(
        0
    )
    
    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(1500.0)
    )
    
    assert (
        environment.mean_radiant_temperature_c
        == pytest.approx(45.0)
    )

from app.services.weather_interpolation import (
    InterpolationOutOfRangeError,
    WeatherInterpolator,
)
from app.services.weather_quality import WeatherInsufficientCoverageError


@pytest.mark.unit
def test_interpolation_outside_range_raises(weather_series):
    interpolator = WeatherInterpolator.from_series(weather_series, assumptions=LEGACY)

    with pytest.raises(InterpolationOutOfRangeError):
        interpolator.environment_at(24 * 60 * 60)

    with pytest.raises(InterpolationOutOfRangeError):
        interpolator.environment_at(-2 * 60 * 60)


@pytest.mark.unit
def test_interpolation_at_exact_boundaries_is_allowed(weather_series):
    interpolator = WeatherInterpolator.from_series(weather_series, assumptions=LEGACY)

    first = interpolator.environment_at(-3600)   # 09:00 point
    last = interpolator.environment_at(7200)     # 12:00 point

    assert first.air_temperature_c == pytest.approx(36.0)
    assert last.air_temperature_c == pytest.approx(42.0)


@pytest.mark.unit
def test_from_series_rejects_series_not_covering_requested_window(
    weather_series,
):
    truncated = weather_series.model_copy(
        update={"points": weather_series.points[:-1]}  # ends 11:00, needs 12:00
    )

    with pytest.raises(WeatherInsufficientCoverageError):
        WeatherInterpolator.from_series(truncated, assumptions=LEGACY)
```

### File: `backend/tests/test_weather_quality.py`
```python
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pytest

from app.schemas.weather import WeatherPoint
from app.services.weather_quality import (
    WeatherDuplicateConflictError,
    WeatherGapInWindowError,
    WeatherInsufficientCoverageError,
    WeatherNaiveTimestampError,
    ensure_window_covered,
    normalize_timeline,
)


TZ = ZoneInfo("Asia/Dubai")
BASE = datetime(2023, 7, 15, 9, tzinfo=TZ)


def make_point(timestamp: datetime, temperature: float = 30.0) -> WeatherPoint:
    return WeatherPoint(
        timestamp=timestamp,
        air_temperature_c=temperature,
        relative_humidity_percent=40.0,
        wind_speed_m_s=2.0,
        ghi_w_m2=600.0,
        direct_radiation_w_m2=450.0,
        diffuse_radiation_w_m2=150.0,
        dni_w_m2=700.0,
    )


def hourly(count: int, *, skip: set[int] = frozenset()) -> list[WeatherPoint]:
    return [
        make_point(BASE + timedelta(hours=index), 30.0 + index)
        for index in range(count)
        if index not in skip
    ]


@pytest.mark.unit
def test_unsorted_input_is_sorted_and_noted():
    points = list(reversed(hourly(4)))

    cleaned, report = normalize_timeline(points)

    assert [p.timestamp for p in cleaned] == sorted(p.timestamp for p in points)
    assert report.was_sorted is False
    assert any("not sorted" in note for note in report.notes)


@pytest.mark.unit
def test_identical_duplicate_is_removed():
    points = hourly(3) + [make_point(BASE + timedelta(hours=1), 31.0)]

    cleaned, report = normalize_timeline(points)

    assert len(cleaned) == 3
    assert report.duplicates_removed == 1


@pytest.mark.unit
def test_conflicting_duplicate_is_rejected():
    points = hourly(3) + [make_point(BASE + timedelta(hours=1), 99.0)]

    with pytest.raises(WeatherDuplicateConflictError):
        normalize_timeline(points)


@pytest.mark.unit
def test_naive_timestamp_is_rejected():
    naive = make_point(datetime(2023, 7, 15, 9))

    with pytest.raises(WeatherNaiveTimestampError):
        normalize_timeline([naive])


@pytest.mark.unit
def test_gap_is_reported_but_not_raised_by_normalize():
    cleaned, report = normalize_timeline(hourly(6, skip={3}))

    assert len(cleaned) == 5
    assert len(report.gaps) == 1
    assert report.gaps[0].missing_steps == 1
    assert report.expected_step_seconds == 3600


@pytest.mark.unit
def test_window_with_gap_inside_is_rejected():
    cleaned, report = normalize_timeline(hourly(6, skip={3}))

    with pytest.raises(WeatherGapInWindowError):
        ensure_window_covered(
            cleaned,
            window_start=BASE + timedelta(hours=1),
            window_end=BASE + timedelta(hours=4),
            step_seconds=report.expected_step_seconds,
        )


@pytest.mark.unit
def test_window_outside_gap_is_accepted():
    cleaned, report = normalize_timeline(hourly(6, skip={5}))

    ensure_window_covered(
        cleaned,
        window_start=BASE + timedelta(hours=1),
        window_end=BASE + timedelta(hours=3),
        step_seconds=report.expected_step_seconds,
    )


@pytest.mark.unit
def test_missing_tail_is_rejected():
    cleaned, report = normalize_timeline(hourly(4))  # 09:00 .. 12:00

    with pytest.raises(WeatherInsufficientCoverageError, match="does not cover"):
        ensure_window_covered(
            cleaned,
            window_start=BASE + timedelta(hours=1),
            window_end=BASE + timedelta(hours=3, minutes=1),
            step_seconds=report.expected_step_seconds,
        )


@pytest.mark.unit
def test_exact_boundaries_are_accepted():
    cleaned, report = normalize_timeline(hourly(4))

    ensure_window_covered(
        cleaned,
        window_start=BASE,
        window_end=BASE + timedelta(hours=3),
        step_seconds=report.expected_step_seconds,
    )
```

### File: `backend/tests/test_weather_service.py`
```python
from datetime import datetime

import pytest

from app.core.cities import get_city
from app.services.weather import (
    get_historical_weather,
)


OPEN_METEO_RESPONSE = {
    "latitude": 25.25,
    "longitude": 55.25,
    "elevation": 12.0,
    "timezone": "Asia/Dubai",
    "utc_offset_seconds": 14400,
    "hourly": {
        "time": [
            "2025-07-15T09:00",
            "2025-07-15T10:00",
            "2025-07-15T11:00",
            "2025-07-15T12:00",
            "2025-07-15T13:00",
        ],
        "temperature_2m": [
            36.0,
            38.0,
            39.0,
            40.0,
            40.5,
        ],
        "relative_humidity_2m": [
            45.0,
            40.0,
            38.0,
            35.0,
            34.0,
        ],
        "wind_speed_10m": [
            1.0,
            1.5,
            2.0,
            2.5,
            2.0,
        ],
        "shortwave_radiation": [
            500.0,
            700.0,
            800.0,
            900.0,
            850.0,
        ],
        "direct_radiation": [
            350.0,
            520.0,
            620.0,
            700.0,
            650.0,
        ],
        "diffuse_radiation": [
            150.0,
            180.0,
            180.0,
            200.0,
            200.0,
        ],
        "direct_normal_irradiance": [
            600.0,
            750.0,
            820.0,
            880.0,
            830.0,
        ],
    },
}


@pytest.mark.integration
@pytest.mark.asyncio
async def test_historical_weather_with_mock(
    monkeypatch,
):
    async def mock_request_open_meteo(
        params,
    ):
        return OPEN_METEO_RESPONSE, False

    monkeypatch.setattr(
        "app.services.weather.request_open_meteo",
        mock_request_open_meteo,
    )

    city = get_city("dubai")

    result = await get_historical_weather(
        city=city,
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=120,
    )

    assert result.city.id == "dubai"
    assert len(result.points) >= 2
    assert result.source.from_cache is False
    assert (
        result.points[1]
        .air_temperature_c
        == pytest.approx(38.0)
    )
```

### File: `backend/tests/test_weather_simulation.py`
```python
from datetime import datetime
from types import SimpleNamespace

import pytest

from app.schemas.simulation import (
    WeatherSimulationRequest,
)
from app.services import weather_simulation
from app.services.environment_model import required_weather_variables


class FakeWeatherSimulationResponse(
    SimpleNamespace
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_execute_weather_simulation(
    monkeypatch,
    person,
    control_material,
    rc_material,
):
    request = WeatherSimulationRequest(
        city_id="dubai",
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=120,
        output_interval_minutes=1,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

    city = SimpleNamespace(
        id="dubai",
        name="Dubai",
    )
    weather = object()

    control_result = SimpleNamespace(
        time_series=[
            SimpleNamespace(
            minute=0,
            skin_temperature_c=35.0,
            core_temperature_c=37.5,
            ),
            SimpleNamespace(
            minute=60,
            skin_temperature_c=36.0,
            core_temperature_c=38.0,
            ),
        ],
        final_skin_temperature_c=36.0,
        final_core_temperature_c=38.0,
    )

    rc_result = SimpleNamespace(
        time_series=[
            SimpleNamespace(
            minute=0,
            skin_temperature_c=33.0,
            core_temperature_c=37.0,
            ),
            SimpleNamespace(
            minute=60,
            skin_temperature_c=34.0,
            core_temperature_c=37.5,
            ),
        ],
        final_skin_temperature_c=34.0,
        final_core_temperature_c=37.5,
    )

    get_city_calls = []
    weather_calls = []
    simulation_calls = []
    assumption_calls = []
    
    def fake_get_city(city_id):
        get_city_calls.append(city_id)
        return city

    async def fake_get_historical_weather(
        *,
        city,
        start_time_local,
        duration_minutes,
        extra_variables: tuple[str, ...] = (),
    ):
        # The request's assumptions decide which extra variables are fetched.
        assert tuple(extra_variables) == required_weather_variables(
            request.environment_assumptions
        ), extra_variables
        weather_calls.append(
            {
                "city": city,
                "start_time_local": start_time_local,
                "duration_minutes": duration_minutes,
            }
        )
        return weather

    def fake_simulate_material_with_weather(
        *,
        duration_minutes,
        output_interval_minutes,
        weather,
        person,
        material,
        assumptions=None,
    ):
        simulation_calls.append(material.name)
        assumption_calls.append(assumptions)
        
        if material.name == control_material.name:
            return control_result

        return rc_result

    monkeypatch.setattr(
        weather_simulation,
        "get_city",
        fake_get_city,
    )
    monkeypatch.setattr(
        weather_simulation,
        "get_historical_weather",
        fake_get_historical_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "simulate_material_with_weather",
        fake_simulate_material_with_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "WeatherSimulationResponse",
        FakeWeatherSimulationResponse,
    )

    progress_events = []

    result = await (
        weather_simulation
        .execute_weather_simulation(
            request,
            progress_callback=lambda progress, stage: (
                progress_events.append(
                    (progress, stage)
                )
            ),
        )
    )

    assert get_city_calls == ["dubai"]

    assert len(weather_calls) == 1
    assert (
        weather_calls[0]["duration_minutes"]
        == 120
    )

    assert simulation_calls == [
        control_material.name,
        rc_material.name,
    ]

    assert assumption_calls == [
        request.environment_assumptions,
        request.environment_assumptions,
    ]
    
    assert progress_events == [
        (10, "downloading_weather"),
        (
            30,
            "running_control_simulation",
        ),
        (
            65,
            "running_radiative_cooling_simulation",
        ),
        (90, "generating_summary"),
    ]

    assert result.city == "Dubai"
    assert result.control is control_result
    assert (
        result.radiative_cooling
        is rc_result
    )

    assert (
        result.summary
        .final_skin_temperature_improvement_c
        == pytest.approx(2.0)
    )
    assert (
        result.summary
        .final_core_temperature_improvement_c
        == pytest.approx(0.5)
    )
    assert (
        result.summary
        .average_skin_temperature_improvement_c
        == pytest.approx(2.0)
    )


@pytest.mark.unit
@pytest.mark.asyncio
async def test_execute_weather_simulation_without_callback(
    monkeypatch,
    person,
    control_material,
    rc_material,
):
    request = WeatherSimulationRequest(
        city_id="dubai",
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=1,
        output_interval_minutes=1,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

    city = SimpleNamespace(
        id="dubai",
        name="Dubai",
    )
    weather = object()

    scenario = SimpleNamespace(
        time_series=[
            SimpleNamespace(
            minute=0,
            skin_temperature_c=34.0,
            core_temperature_c=37.0,
            )
        ],
        final_skin_temperature_c=34.0,
        final_core_temperature_c=37.0,
    )

    monkeypatch.setattr(
        weather_simulation,
        "get_city",
        lambda city_id: city,
    )

    async def fake_weather(**kwargs):
        return weather

    monkeypatch.setattr(
        weather_simulation,
        "get_historical_weather",
        fake_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "simulate_material_with_weather",
        lambda **kwargs: scenario,
    )
    monkeypatch.setattr(
        weather_simulation,
        "WeatherSimulationResponse",
        FakeWeatherSimulationResponse,
    )

    result = await (
        weather_simulation
        .execute_weather_simulation(
            request,
            progress_callback=None,
        )
    )

    assert result.city == "Dubai"
    assert (
        result.summary
        .final_skin_temperature_improvement_c
        == 0
    )
```

### File: `backend/tests/test_weather_timeline_stage6.py`
```python
from datetime import datetime, timedelta, timezone

import pytest

from app.core.cities import CityConfig
from app.services.weather import parse_weather_points, get_historical_weather
from app.services.weather_quality import WeatherGapInWindowError, normalize_timeline


BERLIN = CityConfig(
    id="berlin", name="Berlin", country="Germany", latitude=52.52, longitude=13.41,
    elevation_m=34.0, timezone="Europe/Berlin", climate_type="test",
)


def hourly_payload(times, offset_seconds, **overrides):
    n = len(times)
    hourly = {
        "time": times,
        "temperature_2m": [20.0 + i for i in range(n)],
        "relative_humidity_2m": [50.0] * n,
        "wind_speed_10m": [2.0] * n,
        "shortwave_radiation": [100.0] * n,
        "direct_radiation": [60.0] * n,
        "diffuse_radiation": [40.0] * n,
        "direct_normal_irradiance": [70.0] * n,
    }
    hourly.update(overrides)
    return {"utc_offset_seconds": offset_seconds, "hourly": hourly}


@pytest.mark.unit
def test_dst_fall_back_day_parses_without_duplicate_conflict():
    # 2023-10-29 Europe/Berlin: 02:00 occurs twice in wall-clock time.
    # Open-Meteo renders the day with one fixed offset (+7200 s here), so the
    # 24 strings are 24 distinct instants when parsed with that offset.
    times = [f"2023-10-29T{h:02d}:00" for h in range(24)]
    points = parse_weather_points(hourly_payload(times, 7200), BERLIN)

    instants = [p.timestamp.timestamp() for p in points]
    assert len(set(instants)) == 24
    assert all(b - a == 3600 for a, b in zip(instants, instants[1:]))

    cleaned, report = normalize_timeline(points, expected_step_seconds=3600)
    assert report.duplicates_removed == 0
    assert report.gaps == []


@pytest.mark.unit
@pytest.mark.asyncio
async def test_two_hourly_data_is_reported_as_gaps_not_as_normal_step(monkeypatch):
    # Every other hour missing: inference would call this a clean 2 h series.
    times = [f"2023-07-15T{h:02d}:00" for h in range(0, 24, 2)]

    async def fake_request(params):
        return hourly_payload(times, 14400), True

    monkeypatch.setattr("app.services.weather.request_open_meteo", fake_request)

    from app.core.cities import get_city
    with pytest.raises(WeatherGapInWindowError):
        await get_historical_weather(
            city=get_city("dubai"),
            start_time_local=datetime(2023, 7, 15, 12),
            duration_minutes=120,
        )


@pytest.mark.unit
def test_requested_window_is_two_elapsed_hours_across_dst(monkeypatch):
    from app.services.weather import normalize_local_datetime, to_utc
    start = normalize_local_datetime(datetime(2023, 10, 29, 1, 30), "Europe/Berlin")
    end = (to_utc(start) + timedelta(minutes=120)).astimezone(start.tzinfo)
    assert end.timestamp() - start.timestamp() == 7200
```

### File: `backend/tests/test_worker_tasks.py`
```python
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.models.simulation_job import (
    SimulationJob,
)
from app.worker import tasks


def make_session_context(session):
    context = MagicMock()
    context.__enter__.return_value = session
    context.__exit__.return_value = False

    return context


@pytest.mark.unit
def test_update_job_updates_fields_and_commits(
    monkeypatch,
):
    job = SimpleNamespace(
        status="queued",
        stage="queued",
        progress=0,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    tasks.update_job(
        "job-123",
        status="running",
        stage="initializing",
        progress=10,
    )

    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )

    assert job.status == "running"
    assert job.stage == "initializing"
    assert job.progress == 10

    session.commit.assert_called_once_with()


@pytest.mark.unit
def test_update_job_rejects_missing_job(
    monkeypatch,
):
    session = MagicMock()
    session.get.return_value = None

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        RuntimeError,
        match="Simulation task not found:job-404",
    ):
        tasks.update_job(
            "job-404",
            status="running",
        )

    session.commit.assert_not_called()


@pytest.mark.unit
@pytest.mark.parametrize(
    "status",
    [
        "queued",
        "running",
        "completed",
        "failed",
    ],
)
def test_ensure_not_cancelled_accepts_active_status(
    monkeypatch,
    status,
):
    job = SimpleNamespace(
        status=status,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    tasks.ensure_not_cancelled("job-123")

    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "status",
    [
        "cancelling",
        "cancelled",
    ],
)
def test_ensure_not_cancelled_raises_for_cancelled_job(
    monkeypatch,
    status,
):
    job = SimpleNamespace(
        status=status,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        tasks.JobCancelledError,
    ):
        tasks.ensure_not_cancelled(
            "job-123"
        )


@pytest.mark.unit
def test_ensure_not_cancelled_rejects_missing_job(
    monkeypatch,
):
    session = MagicMock()
    session.get.return_value = None

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        RuntimeError,
        match="Simulation task not found:job-404",
    ):
        tasks.ensure_not_cancelled(
            "job-404"
        )
```

### File: `backend/tests/test_zoned_longwave.py`
```python
import pytest

from app.schemas.simulation import EnvironmentInput, MaterialInput, PersonInput
from app.services.longwave import zone_sky_views
from app.services.two_node import simulate_material
from app.services.environment_model import derive_environment
from tests.helpers.environment import legacy

HOT_GROUND = EnvironmentInput(
    air_temperature_c=40.0, mean_radiant_temperature_c=60.0, sky_temperature_c=20.0,
    relative_humidity_percent=25.0, wind_speed_m_s=1.5, solar_radiation_w_m2=800.0,
    sky_view_factor=0.5, zone_view_separation=0.5,
)
PERSON = PersonInput()


def garment(**overrides) -> MaterialInput:
    values = dict(name="t", clothing_insulation_clo=0.4, solar_reflectance=0.9,
                  infrared_emissivity=0.95)
    values.update(overrides)
    return MaterialInput(**values)


def run(material: MaterialInput, environment: EnvironmentInput = HOT_GROUND):
    return simulate_material(60, 5, environment, PERSON, material)


def skins(result):
    return [p.skin_temperature_c for p in result.time_series]


@pytest.mark.unit
@pytest.mark.parametrize("f", [0.0, 0.3, 0.5, 1.0])
@pytest.mark.parametrize("s", [0.0, 0.5, 1.0])
def test_zone_views_are_area_consistent(f, s):
    up, down = zone_sky_views(f, s)
    assert f * up + (1 - f) * down == pytest.approx(f)
    assert 0.0 <= down <= up <= 1.0


@pytest.mark.unit
def test_equal_gray_zones_reproduce_uniform_garment():
    uniform = run(garment())
    zoned = run(garment(infrared_emissivity_ground_facing=0.95))
    assert skins(zoned) == pytest.approx(skins(uniform), abs=1e-3)


@pytest.mark.unit
def test_zero_separation_reduces_to_area_weighted_emissivity():
    env = HOT_GROUND.model_copy(update={"zone_view_separation": 0.0})
    zoned = run(garment(infrared_emissivity_ground_facing=0.35), env)
    uniform = run(garment(infrared_emissivity=0.5 * 0.95 + 0.5 * 0.35), env)
    assert skins(zoned) == pytest.approx(skins(uniform), abs=1e-3)


@pytest.mark.unit
def test_low_ground_facing_emissivity_rejects_hot_ground():
    uniform = run(garment())
    zoned = run(garment(infrared_emissivity_ground_facing=0.1))
    assert zoned.final_skin_temperature_c < uniform.final_skin_temperature_c
    assert zoned.clothing.infrared_emissivity_ground_facing == 0.1
    assert any("two-zone garment" in note for note in zoned.assumptions_applied)


@pytest.mark.unit
def test_selective_sky_zone_with_gray_ground_zone_runs():
    result = run(garment(infrared_emissivity=0.9, infrared_emissivity_window=0.95,
                         infrared_emissivity_ground_facing=0.2))
    assert result.time_series[0].longwave_window_w_m2 is not None
    assert result.diagnostics.normalized_residual_percent < 0.5


@pytest.mark.unit
def test_ground_facing_energy_sum_is_validated():
    with pytest.raises(ValueError):
        garment(infrared_emissivity=0.7, infrared_transmittance=0.2,
                infrared_emissivity_ground_facing=0.9)
        
@pytest.mark.unit
def test_zone_view_separation_reaches_environment_input():
    env = derive_environment(air_temperature_c=35.0, relative_humidity_percent=40.0,
                             wind_speed_m_s=2.0, ghi_w_m2=800.0,
                             assumptions=legacy(zone_view_separation=0.8))
    assert env.zone_view_separation == 0.8
```

