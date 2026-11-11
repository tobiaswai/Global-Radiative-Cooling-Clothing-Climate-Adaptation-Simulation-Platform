from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.schemas.simulation import MaterialInput, WeatherSimulationRequest
from app.services.material_resolution import (
    MaterialParameterConflictError,
    MaterialVersionInvalidError,
    MaterialVersionNotFoundError,
    material_input_from_version,
    resolve_material_input,
    resolve_request_materials,
)


def make_version(**overrides) -> SimpleNamespace:
    values = dict(
        id="ver-1",
        version_number=2,
        material=SimpleNamespace(name="Cool Fabric"),
        clothing_insulation_clo=0.4,
        evaporative_resistance_m2pa_w=18.0,
        clothing_area_factor=None,
        solar_reflectance=0.92,
        solar_transmittance=0.0,
        infrared_emissivity=0.95,
        infrared_transmittance=0.0,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
        source_type="measured",
        source_reference="Lab report 12",
        parameter_sources_json={"solar_reflectance": {"source_type": "measured"}},
    )
    values.update(overrides)
    return SimpleNamespace(**values)


def make_session(version) -> Mock:
    session = Mock()
    session.scalar.return_value = version
    return session


@pytest.mark.unit
def test_input_without_version_id_is_returned_untouched():
    material = MaterialInput(name="Control")
    session = Mock()

    assert resolve_material_input(session, material) is material
    session.scalar.assert_not_called()


@pytest.mark.unit
def test_omitted_fields_are_hydrated_from_the_version():
    resolved = resolve_material_input(
        make_session(make_version()),
        MaterialInput(name="RC", material_version_id="ver-1"),
    )

    assert resolved.name == "RC"
    assert resolved.clothing_insulation_clo == 0.4
    assert resolved.evaporative_resistance_m2pa_w == 18.0
    assert resolved.solar_reflectance == 0.92
    assert resolved.source_type == "measured"
    assert resolved.source_reference == "Lab report 12"
    assert resolved.parameter_sources["solar_reflectance"].source_type == "measured"


@pytest.mark.unit
def test_matching_explicit_values_are_accepted():
    resolved = resolve_material_input(
        make_session(make_version()),
        MaterialInput(
            name="RC", material_version_id="ver-1",
            clothing_insulation_clo=0.4, solar_reflectance=0.92,
        ),
    )
    assert resolved.material_version_id == "ver-1"


@pytest.mark.unit
def test_conflicting_explicit_value_is_rejected():
    with pytest.raises(MaterialParameterConflictError) as error:
        resolve_material_input(
            make_session(make_version()),
            MaterialInput(name="RC", material_version_id="ver-1", solar_reflectance=0.5),
        )

    detail = error.value.to_detail()
    assert detail["code"] == "MATERIAL_PARAMETER_CONFLICT"
    assert detail["conflicts"][0]["field"] == "solar_reflectance"


@pytest.mark.unit
def test_explicit_null_against_stored_value_is_a_conflict():
    with pytest.raises(MaterialParameterConflictError):
        resolve_material_input(
            make_session(make_version()),
            MaterialInput(name="RC", material_version_id="ver-1", evaporative_resistance_m2pa_w=None),
        )


@pytest.mark.unit
def test_unknown_version_raises():
    with pytest.raises(MaterialVersionNotFoundError):
        resolve_material_input(make_session(None), MaterialInput(name="RC", material_version_id="ghost"))


@pytest.mark.unit
def test_legacy_version_outside_bounds_is_reported():
    with pytest.raises(MaterialVersionInvalidError, match="cannot be used"):
        material_input_from_version(make_version(evaporative_resistance_m2pa_w=5000.0))


@pytest.mark.unit
def test_display_name_is_truncated_to_input_limit():
    version = make_version(material=SimpleNamespace(name="x" * 150))
    assert len(material_input_from_version(version).name) == 100


@pytest.mark.unit
def test_request_level_resolution_only_replaces_linked_materials(person, control_material):
    request = WeatherSimulationRequest(
        start_time_local="2023-07-15T12:00:00",
        person=person,
        control_material=control_material,
        rc_material=MaterialInput(name="RC", material_version_id="ver-1"),
    )

    resolved = resolve_request_materials(make_session(make_version()), request)

    assert resolved is not request
    assert resolved.control_material is control_material
    assert resolved.rc_material.solar_reflectance == 0.92