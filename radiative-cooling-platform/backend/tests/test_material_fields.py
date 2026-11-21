import pytest
from pydantic import ValidationError

from app.schemas.provenance import MATERIAL_PHYSICAL_FIELD_ORDER
from app.schemas.simulation import MaterialInput
from app.services.material_fields import build_material_field_manifest
from app.services.planck import broadband_emissivity
from app.services import model_parameters as mp


@pytest.mark.unit
def test_manifest_covers_every_physical_field_in_order():
    manifest = build_material_field_manifest()
    assert [f.name for f in manifest.fields] == list(MATERIAL_PHYSICAL_FIELD_ORDER)
    assert manifest.parameter_set_version == mp.MODEL_PARAMETER_SET_VERSION
    assert "absorbed_solar_to_body_fraction" not in [f.name for f in manifest.fields]

@pytest.mark.unit
def test_deprecated_field_is_still_accepted_in_provenance():
    MaterialInput(
        name="legacy",
        parameter_sources={"absorbed_solar_to_body_fraction": {"source_type": "assumed"}},
    )

@pytest.mark.unit
@pytest.mark.parametrize("name", MATERIAL_PHYSICAL_FIELD_ORDER)
def test_manifest_bounds_match_validation(name):
    descriptor = next(f for f in build_material_field_manifest().fields if f.name == name)

    assert descriptor.unit
    assert descriptor.description
    assert descriptor.minimum is not None and descriptor.maximum is not None

    base = {"name": "x", "solar_reflectance": 0.0, "infrared_emissivity": 0.0}

    def with_value(value):
        payload = {**base, name: value}
        if name == "infrared_emissivity_window":
            # keep the implied eps_N at 0.5 so only the field's own bound is tested
            payload["infrared_emissivity"] = broadband_emissivity(min(max(value, 0.0), 1.0), 0.5)
        return payload

    MaterialInput(**with_value(descriptor.minimum))
    MaterialInput(**with_value(descriptor.maximum))
    with pytest.raises(ValidationError):
        MaterialInput(**with_value(descriptor.minimum - 1e-6))
    with pytest.raises(ValidationError):
        MaterialInput(**with_value(descriptor.maximum + 1e-6))


@pytest.mark.unit
def test_nullable_fields_declare_their_derivation():
    for field in build_material_field_manifest().fields:
        assert field.nullable == (field.derived_when_null is not None), field.name