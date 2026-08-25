from fastapi import APIRouter, HTTPException

from app.schemas.simulation import (
    GaggeBenchmarkRequest,
    GaggeBenchmarkResponse,
)
from app.services.gagge_benchmark import (
    run_gagge_benchmark,
)


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
) -> GaggeBenchmarkResponse:
    try:
        return run_gagge_benchmark(request)
    except (ValueError, RuntimeError) as error:
        raise HTTPException(
            status_code=500,
            detail=f"Gagge benchmark calculation failed：{error}",
        ) from error