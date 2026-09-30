import math

import pytest

from app.schemas.simulation import (
    GaggeBenchmarkRequest,
)
from app.services.gagge_benchmark import (
    run_gagge_benchmark,
)


@pytest.mark.benchmark
def test_gagge_benchmark_returns_finite_values(
    environment,
    person,
    control_material,
):
    request = GaggeBenchmarkRequest(
        duration_minutes=60,
        environment=environment,
        person=person,
        material=control_material,
    )

    result = run_gagge_benchmark(request)

    assert math.isfinite(
        result.gagge.core_temperature_c
    )

    assert math.isfinite(
        result.gagge.skin_temperature_c
    )

    assert math.isfinite(
        result.prototype.core_temperature_c
    )

    assert math.isfinite(
        result.prototype.skin_temperature_c
    )


@pytest.mark.benchmark
def test_gagge_output_is_in_broad_range(
    environment,
    person,
    control_material,
):
    request = GaggeBenchmarkRequest(
        duration_minutes=60,
        environment=environment,
        person=person,
        material=control_material,
    )

    result = run_gagge_benchmark(request)

    assert (
        34.0
        < result.gagge.core_temperature_c
        < 42.0
    )

    assert (
        15.0
        < result.gagge.skin_temperature_c
        < 45.0
    )

    assert result.gagge.skin_evaporation_w_m2 >= 0


@pytest.mark.integration
def test_gagge_benchmark_api(
    client,
    environment,
    person,
    control_material,
):
    response = client.post(
        "/api/v1/benchmarks/gagge",
        json={
            "duration_minutes": 60,
            "environment": (
                environment.model_dump()
            ),
            "person": person.model_dump(),
            "material": (
                control_material.model_dump()
            ),
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["reference_model"] == (
        "Gagge Two-Node"
    )

    assert "prototype" in body
    assert "gagge" in body

import pytest
from fastapi import HTTPException

from app.api import benchmarks


@pytest.mark.unit
def test_gagge_api_converts_service_error_to_500(
    monkeypatch,
):
    def fake_run_gagge_benchmark(request):
        raise ValueError(
            "invalid benchmark input"
        )

    monkeypatch.setattr(
        benchmarks,
        "run_gagge_benchmark",
        fake_run_gagge_benchmark,
    )

    with pytest.raises(
        HTTPException,
    ) as error:
        benchmarks.compare_with_gagge(
            object()
        )

    assert error.value.status_code == 500
    assert (
        "invalid benchmark input"
        in error.value.detail
    )
    
@pytest.mark.benchmark
def test_benchmark_returns_aligned_transient_series(environment, person, control_material):
    request = GaggeBenchmarkRequest(
        duration_minutes=90, environment=environment, person=person, material=control_material
    )

    result = run_gagge_benchmark(request)

    assert len(result.time_series) == 91
    assert result.time_series[0].minute == 0
    assert result.time_series[-1].minute == 90
    assert result.core_temperature.maximum_absolute_difference_c >= abs(
        result.core_temperature.final_difference_c
    )
    assert result.reference_port_parity.maximum_absolute_difference_c < 0.05
    assert any("solar_radiation" in note for note in result.alignment_applied)


@pytest.mark.benchmark
def test_default_case_is_within_stage_3_tolerances(environment, person, control_material):
    """Acceptance criterion of Stage 3 for the reference scenario."""
    result = run_gagge_benchmark(
        GaggeBenchmarkRequest(environment=environment, person=person, material=control_material)
    )

    assert result.core_temperature.passed, result.core_temperature
    assert result.skin_temperature.passed, result.skin_temperature
    assert result.passed
    
@pytest.mark.benchmark
def test_sitting_posture_runs_and_reports_seated_area_ratio(
    environment, person, control_material
):
    result = run_gagge_benchmark(
        GaggeBenchmarkRequest(
            environment=environment,
            person=person.model_copy(update={"position": "sitting"}),
            material=control_material,
        )
    )
    assert result.reference_port_parity.maximum_absolute_difference_c < 0.05