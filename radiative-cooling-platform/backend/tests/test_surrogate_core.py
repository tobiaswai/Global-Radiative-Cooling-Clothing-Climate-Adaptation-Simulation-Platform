from datetime import date

import numpy as np
import pandas as pd
import pytest
from pydantic import ValidationError

from app.schemas.optimization import DecisionVariable
from app.schemas.surrogate import SurrogateDatasetCreate, SurrogatePredictRequest, SurrogateTrainingCreate
from app.services.optimization import evaluator as evaluator_module
from app.services.surrogate.features import WEATHER_FEATURES, weather_features
from app.services.surrogate.generation import LABEL_COLUMNS, frame_columns, generate_chunk
from app.services.surrogate.inference import domain_violations, predict_from_weather
from app.services.surrogate.sampling import sample_materials
from app.services.surrogate.training import build_bundle, season_label, train_and_validate
from app.services.weather_interpolation import WeatherInterpolator
from tests.helpers.environment import LEGACY
from tests.test_stage_8_resume_benchmark import SyntheticWeatherProvider

RHO = DecisionVariable(name="solar_reflectance", lower=0.3, upper=0.98)
EPS = DecisionVariable(name="infrared_emissivity", lower=0.05, upper=0.99)


def make_spec(person, control_material, rc_material, **overrides) -> SurrogateDatasetCreate:
    payload = dict(city_ids=["dubai", "guangzhou", "lhasa", "sydney"], year=2023, months=[7],
                   sample_days_per_month=1, local_start_hour=12, duration_minutes=120,
                   output_interval_minutes=10, person=person, control_material=control_material,
                   base_material=rc_material, environment_assumptions=LEGACY,
                   variables=[RHO, EPS], material_count=16)
    payload.update(overrides)
    return SurrogateDatasetCreate(**payload)


# --- spec, sampling, features ---------------------------------------------

@pytest.mark.unit
def test_material_count_must_be_power_of_two(person, control_material, rc_material):
    with pytest.raises(ValidationError, match="power of two"):
        make_spec(person, control_material, rc_material, material_count=100)


@pytest.mark.unit
def test_sampling_is_deterministic_and_rejects_impossible_garments(person, control_material, rc_material):
    spec = make_spec(person, control_material, rc_material, material_count=64, variables=[
        DecisionVariable(name="solar_reflectance", lower=0.5, upper=1.0),
        DecisionVariable(name="solar_transmittance", lower=0.0, upper=0.5),
    ])
    first, rejected = sample_materials(spec)
    second, _ = sample_materials(spec)
    assert [m.parameters for m in first] == [m.parameters for m in second]
    assert rejected > 0 and len(first) + rejected == 64
    assert all(m.parameters["solar_reflectance"] + m.parameters["solar_transmittance"] <= 1 + 1e-6 for m in first)


@pytest.mark.unit
def test_weather_features_are_complete(hourly_weather):
    features = weather_features(WeatherInterpolator.from_series(hourly_weather, assumptions=LEGACY), 120)
    assert set(features) == set(WEATHER_FEATURES)
    assert features["air_temperature_max_c"] >= features["air_temperature_mean_c"]
    assert features["sky_temperature_mean_c"] < features["air_temperature_mean_c"]


@pytest.mark.unit
@pytest.mark.parametrize(("month", "latitude", "season"),
                         [(1, 25.0, "DJF"), (1, -33.0, "JJA"), (7, -12.0, "DJF"), (10, 1.0, "SON")])
def test_season_is_hemisphere_adjusted(month, latitude, season):
    assert season_label(month, latitude) == season


# --- generation (offline physics) -------------------------------------------

@pytest.mark.integration
@pytest.mark.asyncio
async def test_chunk_generation_is_deterministic(monkeypatch, person, control_material, rc_material):
    monkeypatch.setattr(evaluator_module, "get_historical_weather_range", SyntheticWeatherProvider())
    spec = make_spec(person, control_material, rc_material, duration_minutes=60)

    first = await generate_chunk(spec, "dubai", 7)
    second = await generate_chunk(spec, "dubai", 7)

    assert list(first.frame.columns) == frame_columns(spec)
    assert len(first.frame) == 16
    assert np.isfinite(first.frame[list(LABEL_COLUMNS)].to_numpy(dtype=float)).all()
    assert first.simulation_count == 17
    pd.testing.assert_frame_equal(first.frame, second.frame)


# --- training and inference on a synthetic response surface ------------------

def synthetic_frame(seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for city, latitude in (("a", 25.0), ("b", 10.0), ("c", -20.0), ("d", 40.0)):
        for month in range(1, 13):
            for day in (5, 20):
                weather = {name: float(rng.normal()) for name in WEATHER_FEATURES}
                weather["air_temperature_mean_c"] = 30 + 5 * np.sin(month / 12 * 2 * np.pi) * np.sign(latitude) + rng.normal()
                for index in range(16):
                    rho, eps = rng.uniform(0.3, 0.98), rng.uniform(0.05, 0.99)
                    y = 2 * rho + 0.4 * eps + 0.05 * (weather["air_temperature_mean_c"] - 30) + rng.normal(0, 0.02)
                    rows.append({"city_id": city, "latitude": latitude, "month": month,
                                 "sample_date": f"2023-{month:02d}-{day:02d}", "weight_days": 15,
                                 "material_index": index, **weather, "solar_reflectance": rho,
                                 "infrared_emissivity": eps, **{t: y for t in LABEL_COLUMNS}})
    return pd.DataFrame(rows)


def fast_training(**overrides) -> SurrogateTrainingCreate:
    payload = dict(dataset_id="d", targets=["mean_skin_cooling_c"], max_iter=60, min_samples_leaf=10,
                   mae_thresholds={"mean_skin_cooling_c": 0.2})
    payload.update(overrides)
    return SurrogateTrainingCreate(**payload)


@pytest.mark.unit
def test_training_reports_all_splits_and_accepts_learnable_surface(person, control_material, rc_material):
    spec = make_spec(person, control_material, rc_material)
    outcome = train_and_validate(synthetic_frame(), spec, fast_training())

    splits = {s.split: s for s in outcome.report.splits}
    assert set(splits) == {"grouped_kfold", "leave_one_city", "leave_one_season"}
    assert splits["leave_one_city"].fold_count == 4
    assert splits["leave_one_city"].metrics[0].mae < 0.15
    assert 0.5 < splits["leave_one_city"].metrics[0].interval_coverage <= 1.0
    assert outcome.report.passed
    assert outcome.feature_ranges["solar_reflectance"] == (0.3, 0.98)


@pytest.fixture
def bundle(person, control_material, rc_material):
    spec = make_spec(person, control_material, rc_material)
    outcome = train_and_validate(synthetic_frame(), spec, fast_training(validation_splits=[]))
    result = build_bundle(outcome, spec=spec, training=fast_training(), model_id="m", dataset_id="d")
    result["feature_ranges"].update({name: (-1e9, 1e9) for name in WEATHER_FEATURES})
    return result


@pytest.mark.unit
def test_domain_violations_ignore_missing_features():
    assert domain_violations({"a": 0.5, "b": float("nan")}, {"a": (0, 1), "b": (0, 1)}) == []
    assert domain_violations({"a": 1.5}, {"a": (0, 1)}) == ["a"]


@pytest.mark.unit
def test_out_of_domain_point_falls_back_to_physics(bundle, hourly_weather):
    request = SurrogatePredictRequest(city_id="dubai", sample_date=date(2023, 7, 15), materials=[
        {"solar_reflectance": 0.9, "infrared_emissivity": 0.9},
        {"solar_reflectance": 0.995, "infrared_emissivity": 0.9},
        {"solar_reflectance": 0.9, "made_up": 1.0},
    ])
    response = predict_from_weather(bundle=bundle, model_id="m", model_name="t", accepted=True,
                                    request=request, weather=hourly_weather)
    inside, outside, invalid = response.predictions

    assert inside.source == "surrogate" and inside.physics is None
    surrogate = inside.surrogate["mean_skin_cooling_c"]
    assert surrogate.lower <= surrogate.value <= surrogate.upper
    assert not outside.within_domain and outside.source == "physics"
    assert outside.out_of_domain_features == ["solar_reflectance"]
    assert not invalid.valid and invalid.source == "none"
    assert response.physics_evaluations == 1


@pytest.mark.unit
def test_rejected_model_never_reports_surrogate_source(bundle, hourly_weather):
    request = SurrogatePredictRequest(city_id="dubai", sample_date=date(2023, 7, 15),
                                      materials=[{"solar_reflectance": 0.9, "infrared_emissivity": 0.9}])
    response = predict_from_weather(bundle=bundle, model_id="m", model_name="t", accepted=False,
                                    request=request, weather=hourly_weather)
    assert response.predictions[0].source == "physics"
    assert any("validation thresholds" in w for w in response.warnings)


@pytest.mark.unit
def test_stale_model_is_flagged(bundle, hourly_weather):
    stale_bundle = {**bundle, "model_version": "0.0.0"}
    request = SurrogatePredictRequest(city_id="dubai", sample_date=date(2023, 7, 15),
                                      materials=[{"solar_reflectance": 0.9, "infrared_emissivity": 0.9}],
                                      physics_fallback=False)
    response = predict_from_weather(bundle=stale_bundle, model_id="m", model_name="t", accepted=True,
                                    request=request, weather=hourly_weather)
    assert response.stale and response.predictions[0].source == "none"
    
from app.services.surrogate.training import conformal_margin


@pytest.mark.unit
def test_conformal_margin_widens_undercovering_interval():
    y = np.linspace(-1.0, 1.0, 101)
    lower, upper = np.full(101, -0.5), np.full(101, 0.5)
    margin = conformal_margin(y, lower, upper, alpha=0.2)
    covered = np.mean((y >= lower - margin) & (y <= upper + margin))
    assert margin > 0 and covered >= 0.8