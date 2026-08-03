import pytest


@pytest.mark.integration
def test_health_endpoint(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["service"] == (
        "radiative-cooling-api"
    )


@pytest.mark.integration
def test_simulation_endpoint(
    client,
    simulation_request,
):
    response = client.post(
        "/api/v1/simulations/run",
        json=simulation_request.model_dump(),
    )

    assert response.status_code == 200

    body = response.json()

    assert body["city"] == "Dubai"
    assert "control" in body
    assert "radiative_cooling" in body
    assert "summary" in body

    assert len(
        body["control"]["time_series"]
    ) == 121

    assert (
        body["control"]["diagnostics"]
        ["normalized_residual_percent"]
        < 1.0
    )


@pytest.mark.integration
def test_invalid_material_is_rejected(
    client,
    simulation_request,
):
    payload = simulation_request.model_dump()

    payload["rc_material"][
        "solar_reflectance"
    ] = 0.8

    payload["rc_material"][
        "solar_transmittance"
    ] = 0.4

    response = client.post(
        "/api/v1/simulations/run",
        json=payload,
    )

    assert response.status_code == 422


@pytest.mark.integration
def test_identical_material_api_improvement_is_zero(
    client,
    simulation_request,
):
    payload = simulation_request.model_dump()

    payload["rc_material"] = payload[
        "control_material"
    ].copy()

    response = client.post(
        "/api/v1/simulations/run",
        json=payload,
    )

    assert response.status_code == 200

    summary = response.json()["summary"]

    assert abs(
        summary[
            "final_skin_temperature_improvement_c"
        ]
    ) < 1e-6

    assert abs(
        summary[
            "final_core_temperature_improvement_c"
        ]
    ) < 1e-6