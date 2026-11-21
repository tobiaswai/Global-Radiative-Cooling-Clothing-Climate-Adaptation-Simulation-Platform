"""Surrogate dataset generation and training (Stage 13, ADR 0011).

Chunks are idempotent: the content of a (city, month) part is a deterministic
function of the spec, written atomically. Redelivery (acks_late) recomputes it.
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from time import perf_counter

from sqlalchemy import func, select, update

from app.core.time import utc_now
from app.db.session import SessionLocal
from app.models.surrogate import SurrogateDataset, SurrogateDatasetChunk, SurrogateModel
from app.schemas.surrogate import SurrogateDatasetCreate, SurrogateTrainingCreate
from app.services.surrogate.context import current_fingerprint
from app.services.surrogate.dataset_io import (
    chunk_path, dataset_directory, load_frame, model_artifact_path, write_frame, write_json,
)
from app.services.surrogate.generation import SurrogateCancelled, generate_chunk, materials_frame
from app.services.surrogate.registry import save_bundle
from app.services.surrogate.training import build_bundle, train_and_validate
from app.services.two_node import MODEL_VERSION
from app.worker.celery_app import celery_app

logger = logging.getLogger(__name__)

SURROGATE_QUEUE = "surrogate"
CHUNK_RETRY_COUNTDOWN_SECONDS = 30
TERMINAL_CHUNK = {"completed", "failed", "cancelled"}


@dataclass
class _Claim:
    dataset_id: str
    city_id: str
    month: int
    spec: SurrogateDatasetCreate | None
    outcome: str  # "run" | "cancelled" | "failed" | "skipped"


def _update_chunk(chunk_id: str, **values) -> None:
    with SessionLocal() as session:
        session.execute(update(SurrogateDatasetChunk).where(SurrogateDatasetChunk.id == chunk_id).values(**values))
        session.commit()


def _dataset_status(dataset_id: str) -> str | None:
    with SessionLocal() as session:
        return session.scalar(select(SurrogateDataset.status).where(SurrogateDataset.id == dataset_id))


def _claim_chunk(chunk_id: str) -> _Claim | None:
    with SessionLocal() as session:
        chunk = session.get(SurrogateDatasetChunk, chunk_id)
        if chunk is None:
            return None
        dataset = session.get(SurrogateDataset, chunk.dataset_id)
        claim = _Claim(chunk.dataset_id, chunk.city_id, chunk.month, None, "run")
        if chunk.status in TERMINAL_CHUNK:
            claim.outcome = "skipped"
        elif dataset.status == "cancelled":
            chunk.status, chunk.completed_at = "cancelled", utc_now()
            claim.outcome = "cancelled"
        elif dataset.model_version != MODEL_VERSION:
            chunk.status, chunk.completed_at = "failed", utc_now()
            chunk.error_message = f"physics changed since dataset creation ({dataset.model_version} -> {MODEL_VERSION})"
            claim.outcome = "failed"
        else:
            claim.spec = SurrogateDatasetCreate.model_validate(dataset.spec_json)
            chunk.status, chunk.started_at, chunk.error_message = "running", utc_now(), None
            chunk.attempt += 1
        session.commit()
        return claim


def finalize_dataset(dataset_id: str) -> None:
    with SessionLocal() as session:
        counts = dict(session.execute(
            select(SurrogateDatasetChunk.status, func.count())
            .where(SurrogateDatasetChunk.dataset_id == dataset_id)
            .group_by(SurrogateDatasetChunk.status)
        ).all())
        session.execute(update(SurrogateDataset).where(SurrogateDataset.id == dataset_id).values(
            completed_chunks=counts.get("completed", 0), failed_chunks=counts.get("failed", 0),
        ))
        session.commit()
        if counts.get("queued", 0) + counts.get("running", 0):
            return

        claimed = session.execute(
            update(SurrogateDataset)
            .where(SurrogateDataset.id == dataset_id, SurrogateDataset.status == "running")
            .values(status="finalizing")
            .returning(SurrogateDataset.id)
        ).scalar_one_or_none()
        session.commit()
        if claimed is None:
            return  # cancelled or already finalised

        dataset = session.get(SurrogateDataset, dataset_id)
        spec = SurrogateDatasetCreate.model_validate(dataset.spec_json)
        chunks = session.scalars(select(SurrogateDatasetChunk).where(
            SurrogateDatasetChunk.dataset_id == dataset_id, SurrogateDatasetChunk.status == "completed",
        )).all()
        rows = sum(c.row_count for c in chunks)

        directory = dataset_directory(dataset_id)
        write_frame(materials_frame(spec), directory / "materials.parquet")
        manifest_path = directory / "manifest.json"
        write_json(manifest_path, {
            "dataset_id": dataset_id, "spec": dataset.spec_json,
            "context_sha256": dataset.context_sha256, "model_version": dataset.model_version,
            "parameter_fingerprint": dataset.parameter_fingerprint, "row_count": rows,
            "materials_file": "materials.parquet",
            "chunks": [{"city_id": c.city_id, "month": c.month, "rows": c.row_count,
                        "file": c.file_path, "sha256": c.file_sha256,
                        "weather_payload_sha256": c.weather_payload_sha256,
                        "skipped_samples": len(c.skipped_json or [])} for c in chunks],
        })

        failed = counts.get("failed", 0)
        dataset.row_count = rows
        dataset.manifest_path = str(manifest_path)
        dataset.completed_at = utc_now()
        dataset.status = "failed" if rows == 0 else ("partial_completed" if failed else "completed")
        if rows == 0:
            dataset.error_message = "no rows were generated"
        session.commit()


@celery_app.task(bind=True, name="surrogate.generate_chunk", acks_late=True,
                 reject_on_worker_lost=True, max_retries=3)
def generate_dataset_chunk_task(self, chunk_id: str) -> dict:
    claim = _claim_chunk(chunk_id)
    if claim is None:
        return {"chunk_id": chunk_id, "status": "missing"}
    if claim.outcome != "run":
        finalize_dataset(claim.dataset_id)
        return {"chunk_id": chunk_id, "status": claim.outcome}

    started = perf_counter()
    try:
        output = asyncio.run(generate_chunk(
            claim.spec, claim.city_id, claim.month,
            should_cancel=lambda: _dataset_status(claim.dataset_id) == "cancelled",
        ))
        file_path = file_sha = None
        if not output.frame.empty:
            path = chunk_path(claim.dataset_id, claim.city_id, claim.month)
            file_sha, file_path = write_frame(output.frame, path), str(path)
    except SurrogateCancelled:
        _update_chunk(chunk_id, status="cancelled", completed_at=utc_now())
        finalize_dataset(claim.dataset_id)
        return {"chunk_id": chunk_id, "status": "cancelled"}
    except Exception as error:  # noqa: BLE001
        logger.exception("surrogate chunk %s failed", chunk_id)
        if self.request.retries < self.max_retries:
            _update_chunk(chunk_id, status="queued", error_message=str(error)[:4000])
            raise self.retry(exc=error, countdown=CHUNK_RETRY_COUNTDOWN_SECONDS, queue=SURROGATE_QUEUE)
        _update_chunk(chunk_id, status="failed", error_message=str(error)[:4000], completed_at=utc_now())
        finalize_dataset(claim.dataset_id)
        return {"chunk_id": chunk_id, "status": "failed"}

    _update_chunk(
        chunk_id, status="completed", row_count=len(output.frame),
        simulation_count=output.simulation_count, file_path=file_path, file_sha256=file_sha,
        weather_payload_sha256=output.weather_payload_sha256, skipped_json=output.skipped,
        elapsed_seconds=round(perf_counter() - started, 3), completed_at=utc_now(),
    )
    finalize_dataset(claim.dataset_id)
    return {"chunk_id": chunk_id, "status": "completed", "rows": len(output.frame)}


@celery_app.task(bind=True, name="surrogate.train", acks_late=True, reject_on_worker_lost=True)
def train_surrogate_task(self, model_id: str) -> dict:
    with SessionLocal() as session:
        claimed = session.execute(
            update(SurrogateModel)
            .where(SurrogateModel.id == model_id, SurrogateModel.status == "queued")
            .values(status="training", started_at=func.now())
            .returning(SurrogateModel.id)
        ).scalar_one_or_none()
        session.commit()
        if claimed is None:
            return {"model_id": model_id, "status": "skipped"}

        model = session.get(SurrogateModel, model_id)
        training = SurrogateTrainingCreate.model_validate(model.training_spec_json)
        spec = SurrogateDatasetCreate.model_validate(model.spec_json)
        chunks = session.scalars(select(SurrogateDatasetChunk).where(
            SurrogateDatasetChunk.dataset_id == model.dataset_id,
            SurrogateDatasetChunk.status == "completed",
            SurrogateDatasetChunk.file_path.is_not(None),
        )).all()
        files = [c.file_path for c in chunks]
        simulations = sum(c.simulation_count for c in chunks)
        seconds = sum(c.elapsed_seconds or 0.0 for c in chunks)
        dataset_id, fingerprint = model.dataset_id, model.parameter_fingerprint

        dataset_version = session.scalar(
            select(SurrogateDataset.model_version).where(SurrogateDataset.id == model.dataset_id)
        )

    def fail(message: str) -> dict:
        with SessionLocal() as session:
            session.execute(update(SurrogateModel).where(SurrogateModel.id == model_id).values(
                status="failed", error_message=message[:4000], completed_at=func.now()))
            session.commit()
        return {"model_id": model_id, "status": "failed"}

    if dataset_version != MODEL_VERSION or fingerprint != current_fingerprint(spec):
        return fail("dataset is stale: physics or parameters changed since generation")
    
    try:
        frame = load_frame(files)
        outcome = train_and_validate(
            frame, spec, training,
            physics_seconds_per_simulation=(round(seconds / simulations, 6) if simulations else None),
        )
        bundle = build_bundle(outcome, spec=spec, training=training, model_id=model_id, dataset_id=dataset_id)
        path = model_artifact_path(model_id)
        sha = save_bundle(bundle, path)
    except Exception as error:  # noqa: BLE001
        logger.exception("surrogate training %s failed", model_id)
        return fail(str(error))

    with SessionLocal() as session:
        session.execute(update(SurrogateModel).where(SurrogateModel.id == model_id).values(
            status="completed", accepted=outcome.report.passed,
            report_json=outcome.report.model_dump(mode="json"),
            artifact_path=str(path), artifact_sha256=sha, completed_at=func.now(), error_message=None,
        ))
        session.commit()
    return {"model_id": model_id, "status": "completed", "accepted": outcome.report.passed}
