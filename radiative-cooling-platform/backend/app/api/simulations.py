from fastapi import APIRouter, HTTPException

from app.schemas.simulation import (
    SimulationRequest,
    SimulationResponse,
    SimulationSummary,
)
from app.services.two_node import simulate_material


router = APIRouter(
    prefix="/api/v1/simulations",
    tags=["simulations"],
)


@router.post(
    "/run",
    response_model=SimulationResponse,
)
def run_simulation(
    request: SimulationRequest,
) -> SimulationResponse:
    try:
        control_result = simulate_material(
            duration_minutes=request.duration_minutes,
            output_interval_minutes=(
                request.output_interval_minutes
            ),
            environment=request.environment,
            person=request.person,
            material=request.control_material,
        )

        rc_result = simulate_material(
            duration_minutes=request.duration_minutes,
            output_interval_minutes=(
                request.output_interval_minutes
            ),
            environment=request.environment,
            person=request.person,
            material=request.rc_material,
        )
    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error

    final_skin_improvement = (
        control_result.final_skin_temperature_c
        - rc_result.final_skin_temperature_c
    )

    final_core_improvement = (
        control_result.final_core_temperature_c
        - rc_result.final_core_temperature_c
    )

    control_skin_average = sum(
        point.skin_temperature_c
        for point in control_result.time_series
    ) / len(control_result.time_series)

    rc_skin_average = sum(
        point.skin_temperature_c
        for point in rc_result.time_series
    ) / len(rc_result.time_series)

    return SimulationResponse(
        model_name="RC transient two-node prototype",
        model_version="0.1.0",
        city=request.city,
        duration_minutes=request.duration_minutes,
        control=control_result,
        radiative_cooling=rc_result,
        summary=SimulationSummary(
            final_skin_temperature_improvement_c=round(
                final_skin_improvement,
                4,
            ),
            final_core_temperature_improvement_c=round(
                final_core_improvement,
                4,
            ),
            average_skin_temperature_improvement_c=round(
                control_skin_average - rc_skin_average,
                4,
            ),
        ),
        warning=(
            "本結果來自簡化瞬態原型，尚未完成熱人偶、"
            "人體實驗或 JOS-3 基準驗證，不可用於醫療、"
            "職業安全或產品認證。"
        ),
    )