import re

import pytest

from app.services import model_parameters as mp


@pytest.mark.unit
def test_every_parameter_has_unit_and_reference():
    for parameter in mp.list_model_parameters():
        assert parameter.unit, parameter.name
        assert parameter.reference, parameter.name


@pytest.mark.unit
def test_manifest_sha_is_stable_and_hex():
    first = mp.model_parameter_set_sha256()
    assert re.fullmatch(r"[0-9a-f]{64}", first)
    assert first == mp.model_parameter_set_sha256()


@pytest.mark.unit
def test_unknown_parameter_raises():
    with pytest.raises(KeyError, match="Unknown model parameter"):
        mp.get_parameter_value("does_not_exist")


@pytest.mark.api
def test_model_parameter_endpoint(client):
    response = client.get("/api/v1/model/parameters")
    assert response.status_code == 200
    body = response.json()
    assert body["parameter_set_version"] == mp.MODEL_PARAMETER_SET_VERSION
    assert len(body["parameters"]) == len(mp.MODEL_PARAMETERS)


@pytest.mark.api
def test_default_assumptions_endpoint(client):
    response = client.get("/api/v1/model/environment-assumptions/defaults")
    assert response.status_code == 200
    assert response.json()["sky_view_factor"] == 0.5
    
@pytest.mark.api
def test_model_metadata_endpoint(client):
    body = client.get("/api/v1/model/metadata").json()
    assert body["parameter_set_version"] == mp.MODEL_PARAMETER_SET_VERSION
    assert body["parameter_set_sha256"] == mp.model_parameter_set_sha256()


@pytest.mark.api
def test_single_parameter_endpoint(client):
    assert client.get("/api/v1/model/parameters/clo_to_si").json()["value"] == 0.155
    assert client.get("/api/v1/model/parameters/nope").status_code == 404


@pytest.mark.api
def test_material_fields_endpoint(client):
    body = client.get("/api/v1/model/material-fields").json()
    names = [f["name"] for f in body["fields"]]
    assert "evaporative_resistance_m2pa_w" in names
    assert body["fields"][0]["unit"] == "clo"