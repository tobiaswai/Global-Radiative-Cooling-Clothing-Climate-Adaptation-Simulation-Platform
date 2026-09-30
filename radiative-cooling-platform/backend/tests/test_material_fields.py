import pytest
from pydantic import ValidationError

from app.schemas.provenance import MATERIAL_PHYSICAL_FIELD_ORDER
from app.schemas.simulation import MaterialInput
from app.services.material_fields import build_material_field_manifest


@pytest.mark.unit
def test_manifest_covers_every_physical_field_in_order():
    manifest = build_material_field_manifest()
    assert [f.name for f in manifest.fields] == list(MATERIAL_PHYSICAL_FIELD_ORDER)
    assert manifest.parameter_set_version == "4.0.0"
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

    # Sum constraints interfere for the optical pair; test the bound alone.
    base = {"name": "x", "solar_reflectance": 0.0, "infrared_emissivity": 0.0}
    MaterialInput(**{**base, name: descriptor.minimum})
    MaterialInput(**{**base, name: descriptor.maximum})

    with pytest.raises(ValidationError):
        MaterialInput(**{**base, name: descriptor.minimum - 1e-6})
    with pytest.raises(ValidationError):
        MaterialInput(**{**base, name: descriptor.maximum + 1e-6})


@pytest.mark.unit
def test_nullable_fields_declare_their_derivation():
    for field in build_material_field_manifest().fields:
        assert field.nullable == (field.derived_when_null is not None), field.name