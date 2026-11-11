from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.simulation import (
    GaggeBenchmarkRequest,
    GaggeBenchmarkResponse,
)
from app.services.gagge_benchmark import run_gagge_benchmark
from app.services.material_resolution import resolve_request_materials


router = APIRouter(
    prefix="/api/v1/benchmarks",
    tags=["benchmarks"],
)


@router.post(
    "/gagge",
    response_model=GaggeBenchmarkResponse,
)
def compare_with_gagge(
    request: GaggeBenchmarkRequest,
    session: Session = Depends(get_db),
) -> GaggeBenchmarkResponse:
    request = resolve_request_materials(
        session, request, fields=("material",)
    )

    try:
        return run_gagge_benchmark(request)
    except (ValueError, RuntimeError) as error:
        raise HTTPException(
            status_code=500,
            detail=f"Gagge benchmark calculation failed：{error}",
        ) from error