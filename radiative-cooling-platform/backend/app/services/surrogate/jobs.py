"""ORM -> response conversion for surrogate datasets and models."""

from __future__ import annotations

from app.models.surrogate import SurrogateDataset, SurrogateDatasetChunk, SurrogateModel
from app.schemas.surrogate import (
    SurrogateDatasetChunkResponse,
    SurrogateDatasetCreate,
    SurrogateDatasetDetail,
    SurrogateDatasetResponse,
    SurrogateModelDetail,
    SurrogateModelResponse,
    SurrogateTrainingCreate,
    ValidationReport,
)
from app.services.optimization.variables import variable_value
from app.services.surrogate.context import current_fingerprint
from app.services.two_node import MODEL_VERSION


def dataset_to_response(d: SurrogateDataset) -> SurrogateDatasetResponse:
    return SurrogateDatasetResponse(
        id=d.id, name=d.name, status=d.status, total_chunks=d.total_chunks,
        completed_chunks=d.completed_chunks, failed_chunks=d.failed_chunks, row_count=d.row_count,
        valid_material_count=d.valid_material_count, model_version=d.model_version,
        parameter_fingerprint=d.parameter_fingerprint, context_sha256=d.context_sha256,
        error_message=d.error_message, created_at=d.created_at, updated_at=d.updated_at,
        completed_at=d.completed_at,
    )


def chunk_to_response(c: SurrogateDatasetChunk) -> SurrogateDatasetChunkResponse:
    return SurrogateDatasetChunkResponse(
        id=c.id, city_id=c.city_id, month=c.month, status=c.status, attempt=c.attempt,
        row_count=c.row_count, skipped_sample_count=len(c.skipped_json or []),
        elapsed_seconds=c.elapsed_seconds, error_message=c.error_message,
    )


def dataset_to_detail(d: SurrogateDataset, chunks: list[SurrogateDatasetChunk]) -> SurrogateDatasetDetail:
    return SurrogateDatasetDetail(
        **dataset_to_response(d).model_dump(),
        spec=SurrogateDatasetCreate.model_validate(d.spec_json),
        chunks=[chunk_to_response(c) for c in sorted(chunks, key=lambda c: (c.city_id, c.month))],
    )


def model_is_stale(m: SurrogateModel) -> bool:
    if m.model_version != MODEL_VERSION:
        return True
    return m.parameter_fingerprint != current_fingerprint(SurrogateDatasetCreate.model_validate(m.spec_json))


def headline_mae(report_json: dict | None) -> dict[str, float]:
    for split in (report_json or {}).get("splits", []):
        if split["split"] == "leave_one_city":
            return {m["target"]: m["mae"] for m in split["metrics"]}
    return {}


def model_to_response(m: SurrogateModel) -> SurrogateModelResponse:
    return SurrogateModelResponse(
        id=m.id, name=m.name, dataset_id=m.dataset_id, status=m.status, accepted=m.accepted,
        targets=list(m.targets_json), model_version=m.model_version,
        parameter_fingerprint=m.parameter_fingerprint, stale=model_is_stale(m),
        headline_mae=headline_mae(m.report_json), error_message=m.error_message,
        created_at=m.created_at, updated_at=m.updated_at, completed_at=m.completed_at,
    )


def model_to_detail(m: SurrogateModel) -> SurrogateModelDetail:
    spec = SurrogateDatasetCreate.model_validate(m.spec_json)
    report = None if m.report_json is None else ValidationReport.model_validate(m.report_json)
    return SurrogateModelDetail(
        **model_to_response(m).model_dump(),
        training=SurrogateTrainingCreate.model_validate(m.training_spec_json),
        report=report,
        variables=spec.variables,
        base_parameters={n: variable_value(spec.base_material, n) for n in spec.variable_names},
        training_cities=report.training_cities if report else list(spec.city_ids),
        year=spec.year, months=spec.months,
        local_start_hour=spec.local_start_hour, duration_minutes=spec.duration_minutes,
    )