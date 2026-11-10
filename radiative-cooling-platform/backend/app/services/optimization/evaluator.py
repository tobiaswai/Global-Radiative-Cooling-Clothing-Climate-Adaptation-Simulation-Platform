"""Prepared samples and the pure evaluate(x) used by every search algorithm.

Preparation happens once: weather is fetched and sliced, interpolators are
built, and the control garment is simulated once per sample day. Afterwards
evaluate(x) only integrates the candidate garment.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from datetime import datetime, timedelta

from app.core.cities import get_city
from app.schemas.optimization import EvaluationMetrics, OptimizationCreate
from app.schemas.simulation import MaterialInput, ScenarioResult
from app.services.annual_sampling import build_weighted_sample_days
from app.services.climate_adaptation import get_next_month_start
from app.services.optimization.metrics import compute_metrics
from app.services.two_node import simulate_material_with_interpolator
from app.services.weather import get_historical_weather_range, slice_weather_time_series
from app.services.weather_interpolation import WeatherInterpolator
from app.services.weather_quality import WeatherDataError


CACHE_DECIMALS = 6
OPTICAL_SUM_TOLERANCE = 1e-6


@dataclass(frozen=True)
class PreparedSample:
    start_time_local: datetime
    weight_days: int
    interpolator: WeatherInterpolator
    control: ScenarioResult


@dataclass
class PreparationReport:
    samples: list[PreparedSample]
    skipped: list[dict] = field(default_factory=list)
    weather_payload_sha256: dict[str, str | None] = field(default_factory=dict)


async def prepare_samples(
    request: OptimizationCreate,
    *,
    progress: Callable[[int, str], None] | None = None,
) -> PreparationReport:
    city = get_city(request.city_id)
    report = PreparationReport(samples=[])

    for index, month in enumerate(request.months):
        if progress:
            progress(1 + round(18 * index / len(request.months)), f"preparing_{request.year}-{month:02d}")

        month_start = datetime(request.year, month, 1)
        prefetch_end = get_next_month_start(year=request.year, month=month) + timedelta(
            hours=request.local_start_hour, minutes=request.duration_minutes
        )
        month_weather = await get_historical_weather_range(
            city=city,
            start_time_local=month_start,
            end_time_local=prefetch_end,
            padding_hours=1,
            require_window_coverage=False,
        )
        report.weather_payload_sha256[f"{month:02d}"] = month_weather.source.payload_sha256

        days_in_month = (get_next_month_start(year=request.year, month=month) - month_start).days
        for day, weight in build_weighted_sample_days(
            days_in_month=days_in_month, sample_count=request.sample_days_per_month
        ):
            start = datetime(request.year, month, day, request.local_start_hour)
            try:
                sliced = slice_weather_time_series(
                    weather=month_weather, start_time_local=start,
                    duration_minutes=request.duration_minutes, padding_hours=1,
                )
                interpolator = WeatherInterpolator.from_series(
                    sliced, assumptions=request.environment_assumptions
                )
                control = simulate_material_with_interpolator(
                    request.duration_minutes, request.output_interval_minutes,
                    interpolator, request.person, request.control_material,
                )
            except WeatherDataError as error:
                report.skipped.append({
                    "sample_date_local": start.isoformat(),
                    "reason_code": error.code,
                    "message": str(error)[:500],
                })
                continue

            report.samples.append(PreparedSample(start, weight, interpolator, control))

    if not report.samples:
        raise RuntimeError("No usable sample day: every sample failed weather validation")

    return report


class MaterialEvaluator:
    """evaluate(x) -> metrics. Deterministic, memoised on x rounded to 1e-6."""

    def __init__(
        self,
        request: OptimizationCreate,
        samples: Sequence[PreparedSample],
        *,
        on_evaluation: Callable[[int], None] | None = None,
    ) -> None:
        if not samples:
            raise ValueError("MaterialEvaluator requires at least one prepared sample")
        self.request = request
        self.samples = list(samples)
        self.names: tuple[str, ...] = tuple(v.name for v in request.variables)
        self.on_evaluation = on_evaluation
        self.evaluation_count = 0
        self.simulation_count = 0
        self._cache: dict[tuple[float, ...], EvaluationMetrics | None] = {}

    def parameters(self, x: Sequence[float]) -> dict[str, float]:
        return {name: float(value) for name, value in zip(self.names, x, strict=True)}

    def vector(self, parameters: dict[str, float]) -> list[float]:
        return [float(parameters[name]) for name in self.names]

    def material_for(self, parameters: dict[str, float]) -> MaterialInput:
        # model_copy does not re-validate; optical sums are checked explicitly.
        # The candidate is a modified garment: drop library linkage.
        return self.request.base_material.model_copy(
            update={
                **parameters,
                "material_version_id": None,
                "parameter_sources": None,
                "source_type": "derived",
                "source_reference": "optimization candidate",
            }
        )

    @staticmethod
    def physically_valid(material: MaterialInput) -> bool:
        return (
            material.solar_reflectance + material.solar_transmittance <= 1.0 + OPTICAL_SUM_TOLERANCE
            and material.infrared_emissivity + material.infrared_transmittance
            <= 1.0 + OPTICAL_SUM_TOLERANCE
        )

    def evaluate(self, x: Sequence[float]) -> EvaluationMetrics | None:
        key = tuple(round(float(v), CACHE_DECIMALS) for v in x)
        if key in self._cache:
            return self._cache[key]

        material = self.material_for(self.parameters(key))
        if not self.physically_valid(material):
            self._cache[key] = None
            return None

        request = self.request
        pairs = []
        for sample in self.samples:
            candidate = simulate_material_with_interpolator(
                request.duration_minutes, request.output_interval_minutes,
                sample.interpolator, request.person, material,
            )
            pairs.append((sample.weight_days, sample.control, candidate))

        metrics = compute_metrics(
            pairs,
            skin_threshold_c=request.skin_threshold_c,
            core_threshold_c=request.core_threshold_c,
        )

        self._cache[key] = metrics
        self.evaluation_count += 1
        self.simulation_count += len(self.samples)

        if self.on_evaluation is not None:
            self.on_evaluation(self.evaluation_count)  # may raise (cancel / lease lost)

        return metrics