"""Surrogate prediction with domain checks and physics fallback (ADR 0011)."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import datetime, time
from time import perf_counter

import anyio
import numpy as np
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.cities import get_city
from app.models.surrogate import SurrogateModel
from app.schemas.simulation import MaterialInput
from app.schemas.surrogate import (
    MaterialPrediction,
    SurrogateDatasetCreate,
    SurrogatePredictRequest,
    SurrogatePredictResponse,
    TargetPrediction,
)
from app.schemas.weather import WeatherTimeSeries
from app.services.environment_model import required_weather_variables
from app.services.optimization.evaluator import PreparedSample
from app.services.optimization.variables import candidate_material, variable_value
from app.services.surrogate.context import current_fingerprint
from app.services.surrogate.features import weather_features
from app.services.surrogate.generation import evaluate_material
from app.services.surrogate.registry import load_bundle
from app.services.two_node import MODEL_VERSION, simulate_material_with_interpolator
from app.services.weather import get_historical_weather
from app.services.weather_interpolation import WeatherInterpolator

PHYSICS_LIMIT_PER_REQUEST = 25
DOMAIN_TOLERANCE = 1e-9


class SurrogateModelNotFoundError(LookupError):
    pass


def resolve_model(session: Session, model_id: str | None) -> SurrogateModel:
    if model_id:
        model = session.get(SurrogateModel, model_id)
        if model is None or model.status != "completed":
            raise SurrogateModelNotFoundError(f"Surrogate model {model_id} not found or not trained")
        return model
    model = session.scalar(
        select(SurrogateModel)
        .where(SurrogateModel.status == "completed", SurrogateModel.accepted.is_(True))
        .order_by(SurrogateModel.completed_at.desc())
        .limit(1)
    )
    if model is None:
        raise SurrogateModelNotFoundError("No accepted surrogate model is available")
    return model


def bundle_spec(bundle: dict) -> SurrogateDatasetCreate:
    return SurrogateDatasetCreate.model_validate(bundle["spec"])


def bundle_is_stale(bundle: dict, spec: SurrogateDatasetCreate) -> bool:
    return (bundle["model_version"] != MODEL_VERSION
            or bundle["parameter_fingerprint"] != current_fingerprint(spec))


def domain_violations(features: dict[str, float], ranges: dict[str, tuple[float, float]]) -> list[str]:
    violations = []
    for name, (low, high) in ranges.items():
        value = features.get(name)
        if value is None or not math.isfinite(value):
            continue
        margin = DOMAIN_TOLERANCE * max(1.0, abs(low), abs(high))
        if value < low - margin or value > high + margin:
            violations.append(name)
    return violations


def _first_error(error: ValueError) -> str:
    errors = getattr(error, "errors", None)
    if callable(errors):
        try:
            return str(errors()[0]["msg"])
        except Exception:  # noqa: BLE001
            pass
    return str(error)


@dataclass
class _Entry:
    parameters: dict[str, float]
    material: MaterialInput | None = None
    features: dict[str, float] | None = None
    violations: list[str] = field(default_factory=list)
    message: str | None = None
    surrogate: dict[str, TargetPrediction] | None = None
    physics: dict[str, float] | None = None


def _prepare_entries(raw_materials: list[dict[str, float]], spec: SurrogateDatasetCreate,
                     weather: dict[str, float], ranges: dict) -> list[_Entry]:
    names = spec.variable_names
    base = {n: variable_value(spec.base_material, n) for n in names}
    entries: list[_Entry] = []
    for raw in raw_materials:
        entry = _Entry(parameters={**base, **{k: float(v) for k, v in raw.items() if k in names}})
        unknown = sorted(set(raw) - set(names))
        if unknown:
            entry.message = "unknown variables: " + ", ".join(unknown)
        else:
            try:
                entry.material = candidate_material(spec.base_material, entry.parameters)
                entry.features = {**weather, **entry.parameters}
                entry.violations = domain_violations(entry.features, ranges)
            except ValueError as error:
                entry.message = f"physically impossible garment: {_first_error(error)}"[:300]
        entries.append(entry)
    return entries


def predict_from_weather(*, bundle: dict, model_id: str, model_name: str, accepted: bool,
                         request: SurrogatePredictRequest, weather: WeatherTimeSeries,
                         started: float | None = None) -> SurrogatePredictResponse:
    started = perf_counter() if started is None else started
    spec = bundle_spec(bundle)
    stale = bundle_is_stale(bundle, spec)
    trusted_model = accepted and not stale
    targets: list[str] = list(bundle["targets"])

    warnings: list[str] = []
    if stale:
        warnings.append("model was trained with a different physics version or parameter fingerprint")
    if not accepted:
        warnings.append("model did not pass its validation thresholds; physics results are authoritative")

    interpolator = WeatherInterpolator.from_series(weather, assumptions=spec.environment_assumptions)
    weather_values = weather_features(interpolator, spec.duration_minutes)
    entries = _prepare_entries(request.materials, spec, weather_values, bundle["feature_ranges"])
    valid = [e for e in entries if e.material is not None]

    def trusted(entry: _Entry) -> bool:
        return trusted_model and not entry.violations

    if request.mode != "physics" and valid:
        columns = bundle["feature_columns"]
        matrix = np.asarray([[e.features[c] for c in columns] for e in valid], dtype=float)
        outputs = {t: bundle["estimators"][t].predict(matrix) for t in targets}
        for i, entry in enumerate(valid):
            entry.surrogate = {
                t: TargetPrediction(value=round(float(p[i]), 6), lower=round(float(lo[i]), 6),
                                    upper=round(float(hi[i]), 6))
                for t, (p, lo, hi) in outputs.items()
            }

    wanted = [e for e in valid
              if request.mode != "surrogate" or (request.physics_fallback and not trusted(e))]
    limited = wanted[:PHYSICS_LIMIT_PER_REQUEST]
    if limited:
        control = simulate_material_with_interpolator(
            spec.duration_minutes, spec.output_interval_minutes, interpolator,
            spec.person, spec.control_material,
        )
        sample = PreparedSample(weather.requested_start_time, 1, interpolator, control)
        for entry in limited:
            metrics = evaluate_material(sample, entry.material, spec)
            entry.physics = {t: float(getattr(metrics, t)) for t in targets}
    if len(wanted) > len(limited):
        warnings.append(f"physics limited to {PHYSICS_LIMIT_PER_REQUEST} evaluations per request; "
                        f"{len(wanted) - len(limited)} point(s) have no trusted result")

    predictions = []
    for entry in entries:
        if entry.material is None:
            source = "none"
        elif request.mode == "physics":
            source = "physics" if entry.physics is not None else "none"
        elif trusted(entry):
            source = "surrogate"
        elif entry.physics is not None:
            source = "physics"
        else:
            source = "none"
        message = entry.message
        if source == "none" and entry.material is not None and message is None:
            message = "surrogate not trusted for this point and no physics evaluation was run"
        predictions.append(MaterialPrediction(
            parameters=entry.parameters, valid=entry.material is not None,
            within_domain=entry.material is not None and not entry.violations,
            out_of_domain_features=entry.violations, source=source,
            surrogate=entry.surrogate, physics=entry.physics, message=message,
        ))

    return SurrogatePredictResponse(
        model_id=model_id, model_name=model_name, accepted=accepted, stale=stale,
        city_id=request.city_id, sample_date=request.sample_date,
        city_in_training=request.city_id in bundle["training_cities"],
        start_time_local=weather.requested_start_time, duration_minutes=spec.duration_minutes,
        weather_features={k: (None if math.isnan(v) else round(v, 4)) for k, v in weather_values.items()},
        weather_payload_sha256=weather.source.payload_sha256,
        predictions=predictions, physics_evaluations=len(limited),
        physics_limit=PHYSICS_LIMIT_PER_REQUEST,
        elapsed_ms=round((perf_counter() - started) * 1000.0, 2), warnings=warnings,
    )


async def run_prediction(session: Session, request: SurrogatePredictRequest) -> SurrogatePredictResponse:
    started = perf_counter()
    model = await anyio.to_thread.run_sync(resolve_model, session, request.model_id)
    bundle = await anyio.to_thread.run_sync(load_bundle, model.artifact_path, model.artifact_sha256)
    spec = bundle_spec(bundle)
    city = get_city(request.city_id)
    weather = await get_historical_weather(
        city=city,
        start_time_local=datetime.combine(request.sample_date, time(spec.local_start_hour)),
        duration_minutes=spec.duration_minutes,
        extra_variables=required_weather_variables(spec.environment_assumptions),
    )
    model_id, model_name, accepted = model.id, model.name, model.accepted
    return await anyio.to_thread.run_sync(lambda: predict_from_weather(
        bundle=bundle, model_id=model_id, model_name=model_name, accepted=accepted,
        request=request.model_copy(update={"city_id": city.id}), weather=weather, started=started,
    ))