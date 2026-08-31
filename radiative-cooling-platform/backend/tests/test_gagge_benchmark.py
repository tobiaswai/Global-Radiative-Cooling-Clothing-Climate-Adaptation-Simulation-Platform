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