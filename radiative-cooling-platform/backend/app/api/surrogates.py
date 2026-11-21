from celery import group
from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import PlainTextResponse
from sqlalchemy import func, select, update
from sqlalchemy.orm import Session

from app.core.cities import get_city
from app.core.time import utc_now
from app.db.session import get_db
from app.models.surrogate import SurrogateDataset, SurrogateDatasetChunk, SurrogateModel
from app.schemas.surrogate import (
    SurrogateDatasetCreate, SurrogateDatasetDetail, SurrogateDatasetEstimate,
    SurrogateDatasetListResponse, SurrogateDatasetResponse, SurrogateModelDetail,
    SurrogateModelListResponse, SurrogateModelResponse, SurrogatePredictRequest,
    SurrogatePredictResponse, SurrogateTrainingCreate, ValidationReport,
)
from app.services.material_resolution import resolve_request_materials
from app.services.surrogate.context import context_sha256, current_fingerprint
from app.services.surrogate.generation import estimate_dataset_cost
from app.services.surrogate.inference import SurrogateModelNotFoundError, run_prediction
from app.services.surrogate.jobs import dataset_to_detail, dataset_to_response, model_to_detail, model_to_response
from app.services.surrogate.registry import SurrogateArtifactError
from app.services.surrogate.report import render_validation_report
from app.services.surrogate.sampling import sample_materials
from app.services.two_node import MODEL_VERSION
from app.services.weather_quality import WeatherDataError
from app.worker.surrogate_tasks import SURROGATE_QUEUE, generate_dataset_chunk_task, train_surrogate_task

router = APIRouter(prefix="/api/v1/surrogate", tags=["surrogate"])
MATERIAL_FIELDS = ("control_material", "base_material")


def _resolved(session: Session, spec: SurrogateDatasetCreate) -> SurrogateDatasetCreate:
    spec = resolve_request_materials(session, spec, fields=MATERIAL_FIELDS)
    try:
        for city_id in spec.city_ids:
            get_city(city_id)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    return spec


@router.post("/datasets/estimate", response_model=SurrogateDatasetEstimate)
def estimate_dataset(spec: SurrogateDatasetCreate, session: Session = Depends(get_db)):
    return estimate_dataset_cost(_resolved(session, spec))


@router.post("/datasets", response_model=SurrogateDatasetResponse, status_code=status.HTTP_202_ACCEPTED)
def create_dataset(spec: SurrogateDatasetCreate, session: Session = Depends(get_db)):
    spec = _resolved(session, spec)
    materials, _ = sample_materials(spec)
    if not materials:
        raise HTTPException(status_code=422, detail="every sampled material is physically impossible")

    dataset = SurrogateDataset(
        name=spec.name, status="running", spec_json=spec.model_dump(mode="json"),
        context_sha256=context_sha256(spec), model_version=MODEL_VERSION,
        parameter_fingerprint=current_fingerprint(spec), total_chunks=len(spec.chunk_keys()),
        valid_material_count=len(materials),
    )
    session.add(dataset)
    session.flush()
    chunks = [SurrogateDatasetChunk(dataset_id=dataset.id, city_id=c, month=m, status="queued")
              for c, m in spec.chunk_keys()]
    session.add_all(chunks)
    session.commit()

    try:
        group(generate_dataset_chunk_task.s(c.id).set(queue=SURROGATE_QUEUE) for c in chunks).apply_async()
    except Exception as error:  # noqa: BLE001
        dataset.status, dataset.error_message = "failed", str(error)[:4000]
        session.commit()
        raise HTTPException(status_code=503, detail=f"Unable to submit chunks: {error}") from error

    session.refresh(dataset)
    return dataset_to_response(dataset)


@router.get("/datasets", response_model=SurrogateDatasetListResponse)
def list_datasets(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0),
                  session: Session = Depends(get_db)):
    total = session.scalar(select(func.count()).select_from(SurrogateDataset)) or 0
    items = session.scalars(select(SurrogateDataset).order_by(SurrogateDataset.created_at.desc())
                            .offset(offset).limit(limit)).all()
    return SurrogateDatasetListResponse(items=[dataset_to_response(d) for d in items],
                                        total=total, limit=limit, offset=offset)


@router.get("/datasets/{dataset_id}", response_model=SurrogateDatasetDetail)
def get_dataset(dataset_id: str, session: Session = Depends(get_db)):
    dataset = session.get(SurrogateDataset, dataset_id)
    if dataset is None:
        raise HTTPException(status_code=404, detail="Surrogate dataset not found")
    chunks = session.scalars(select(SurrogateDatasetChunk)
                             .where(SurrogateDatasetChunk.dataset_id == dataset_id)).all()
    return dataset_to_detail(dataset, list(chunks))


@router.post("/datasets/{dataset_id}/cancel", response_model=SurrogateDatasetResponse)
def cancel_dataset(dataset_id: str, session: Session = Depends(get_db)):
    dataset = session.get(SurrogateDataset, dataset_id)
    if dataset is None:
        raise HTTPException(status_code=404, detail="Surrogate dataset not found")
    if dataset.status != "running":
        raise HTTPException(status_code=409, detail=f"dataset is {dataset.status}")
    now = utc_now()
    dataset.status, dataset.cancel_requested_at, dataset.completed_at = "cancelled", now, now
    session.execute(update(SurrogateDatasetChunk)
                    .where(SurrogateDatasetChunk.dataset_id == dataset_id,
                           SurrogateDatasetChunk.status == "queued")
                    .values(status="cancelled", completed_at=now))
    session.commit()
    session.refresh(dataset)
    return dataset_to_response(dataset)


@router.post("/models", response_model=SurrogateModelResponse, status_code=status.HTTP_202_ACCEPTED)
def train_model(training: SurrogateTrainingCreate, session: Session = Depends(get_db)):
    dataset = session.get(SurrogateDataset, training.dataset_id)
    if dataset is None:
        raise HTTPException(status_code=404, detail="Surrogate dataset not found")
    if dataset.status not in ("completed", "partial_completed"):
        raise HTTPException(status_code=409, detail=f"dataset is {dataset.status}")
    spec = SurrogateDatasetCreate.model_validate(dataset.spec_json)
    if dataset.model_version != MODEL_VERSION or dataset.parameter_fingerprint != current_fingerprint(spec):
        raise HTTPException(status_code=409, detail="dataset is stale (physics changed); regenerate it")

    model = SurrogateModel(
        name=training.name, dataset_id=dataset.id, status="queued",
        training_spec_json=training.model_dump(mode="json"), spec_json=dataset.spec_json,
        targets_json=list(training.targets), context_sha256=dataset.context_sha256,
        model_version=MODEL_VERSION, parameter_fingerprint=dataset.parameter_fingerprint,
    )
    session.add(model)
    session.commit()
    try:
        train_surrogate_task.apply_async(args=[model.id], queue=SURROGATE_QUEUE)
    except Exception as error:  # noqa: BLE001
        model.status, model.error_message = "failed", str(error)[:4000]
        session.commit()
        raise HTTPException(status_code=503, detail=f"Unable to submit training: {error}") from error
    session.refresh(model)
    return model_to_response(model)


@router.get("/models", response_model=SurrogateModelListResponse)
def list_models(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0),
                session: Session = Depends(get_db)):
    total = session.scalar(select(func.count()).select_from(SurrogateModel)) or 0
    items = session.scalars(select(SurrogateModel).order_by(SurrogateModel.created_at.desc())
                            .offset(offset).limit(limit)).all()
    return SurrogateModelListResponse(items=[model_to_response(m) for m in items],
                                      total=total, limit=limit, offset=offset)


def _model_or_404(session: Session, model_id: str) -> SurrogateModel:
    model = session.get(SurrogateModel, model_id)
    if model is None:
        raise HTTPException(status_code=404, detail="Surrogate model not found")
    return model


@router.get("/models/{model_id}", response_model=SurrogateModelDetail)
def get_model(model_id: str, session: Session = Depends(get_db)):
    return model_to_detail(_model_or_404(session, model_id))


@router.get("/models/{model_id}/report.md", response_class=PlainTextResponse)
def get_model_report(model_id: str, session: Session = Depends(get_db)):
    model = _model_or_404(session, model_id)
    if model.report_json is None:
        raise HTTPException(status_code=409, detail=f"model is {model.status}")
    return render_validation_report(
        name=model.name, model_id=model.id, dataset_id=model.dataset_id,
        report=ValidationReport.model_validate(model.report_json),
        training=SurrogateTrainingCreate.model_validate(model.training_spec_json),
    )


@router.post("/predict", response_model=SurrogatePredictResponse)
async def predict(request: SurrogatePredictRequest, session: Session = Depends(get_db)):
    try:
        return await run_prediction(session, request)
    except SurrogateModelNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    except WeatherDataError as error:
        raise HTTPException(status_code=422, detail=error.to_detail()) from error
    except SurrogateArtifactError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    except RuntimeError as error:
        raise HTTPException(status_code=502, detail=str(error)) from error