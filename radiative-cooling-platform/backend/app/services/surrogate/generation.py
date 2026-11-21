"""Physics-labelled rows for surrogate training (Stage 13, ADR 0011)."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import get_args

import pandas as pd

from app.core.cities import get_city
from app.schemas.optimization import EvaluationMetrics, MetricName
from app.schemas.simulation import MaterialInput
from app.schemas.surrogate import SurrogateDatasetCreate, SurrogateDatasetEstimate
from app.services.optimization.evaluator import PreparedSample, SampleWindowSpec, prepare_samples
from app.services.optimization.metrics import compute_metrics
from app.services.surrogate.features import WEATHER_FEATURES, weather_features
from app.services.surrogate.sampling import sample_materials
from app.services.two_node import simulate_material_with_interpolator

LABEL_COLUMNS: tuple[str, ...] = get_args(MetricName)
CONTEXT_COLUMNS: tuple[str, ...] = (
    "city_id", "latitude", "month", "sample_date", "weight_days", "material_index",
)
CANCEL_CHECK_EVERY = 16


class SurrogateCancelled(Exception):
    pass


@dataclass
class ChunkOutput:
    frame: pd.DataFrame
    skipped: list[dict] = field(default_factory=list)
    weather_payload_sha256: str | None = None
    simulation_count: int = 0
    rejected_material_count: int = 0


def frame_columns(spec: SurrogateDatasetCreate) -> list[str]:
    return [*CONTEXT_COLUMNS, *WEATHER_FEATURES, *spec.variable_names, *LABEL_COLUMNS]


def window_spec(spec: SurrogateDatasetCreate, city_id: str, month: int) -> SampleWindowSpec:
    return SampleWindowSpec(
        city_id=city_id, year=spec.year, months=(month,),
        sample_days_per_month=spec.sample_days_per_month,
        local_start_hour=spec.local_start_hour, duration_minutes=spec.duration_minutes,
        output_interval_minutes=spec.output_interval_minutes, person=spec.person,
        control_material=spec.control_material,
        environment_assumptions=spec.environment_assumptions,
    )


def evaluate_material(
    sample: PreparedSample, material: MaterialInput, spec: SurrogateDatasetCreate
) -> EvaluationMetrics:
    """The single physics evaluation shared by dataset generation and inference fallback."""
    candidate = simulate_material_with_interpolator(
        spec.duration_minutes, spec.output_interval_minutes,
        sample.interpolator, spec.person, material,
    )
    return compute_metrics(
        [(1, sample.control, candidate)],
        skin_threshold_c=spec.skin_threshold_c,
        core_threshold_c=spec.core_threshold_c,
    )


async def generate_chunk(
    spec: SurrogateDatasetCreate,
    city_id: str,
    month: int,
    *,
    should_cancel: Callable[[], bool] = lambda: False,
) -> ChunkOutput:
    preparation = await prepare_samples(window_spec(spec, city_id, month), require_samples=False)
    materials, rejected = sample_materials(spec)
    city = get_city(city_id)

    rows: list[dict] = []
    simulations = len(preparation.samples)  # one control run per sample day
    for sample in preparation.samples:
        weather = weather_features(sample.interpolator, spec.duration_minutes)
        for position, sampled in enumerate(materials):
            if position % CANCEL_CHECK_EVERY == 0 and should_cancel():
                raise SurrogateCancelled()
            metrics = evaluate_material(sample, sampled.material, spec)
            simulations += 1
            rows.append({
                "city_id": city.id,
                "latitude": city.latitude,
                "month": month,
                "sample_date": sample.start_time_local.date().isoformat(),
                "weight_days": sample.weight_days,
                "material_index": sampled.index,
                **weather,
                **sampled.parameters,
                **{label: getattr(metrics, label) for label in LABEL_COLUMNS},
            })

    return ChunkOutput(
        frame=pd.DataFrame(rows, columns=frame_columns(spec)),
        skipped=list(preparation.skipped),
        weather_payload_sha256=preparation.weather_payload_sha256.get(f"{month:02d}"),
        simulation_count=simulations,
        rejected_material_count=rejected,
    )


def estimate_dataset_cost(spec: SurrogateDatasetCreate) -> SurrogateDatasetEstimate:
    materials, rejected = sample_materials(spec)
    samples = spec.weather_sample_count()
    return SurrogateDatasetEstimate(
        chunk_count=len(spec.chunk_keys()),
        weather_sample_count=samples,
        material_count=spec.material_count,
        valid_material_count=len(materials),
        rejected_material_count=rejected,
        thermal_simulation_count=samples * (len(materials) + 1),
    )


def materials_frame(spec: SurrogateDatasetCreate) -> pd.DataFrame:
    materials, _ = sample_materials(spec)
    return pd.DataFrame([{"material_index": m.index, **m.parameters} for m in materials])