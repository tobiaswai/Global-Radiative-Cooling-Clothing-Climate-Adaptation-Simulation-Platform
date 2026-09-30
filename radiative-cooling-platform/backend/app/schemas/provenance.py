"""Provenance types shared by material inputs, the model parameter registry
and simulation responses (Stage 2), plus the material field manifest (Stage 4).
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


SourceType = Literal[
    "measured",      # measured on the actual sample
    "manufacturer",  # datasheet value
    "literature",    # published value, reference required
    "standard",      # ISO / ASHRAE / CODATA
    "derived",       # computed from other inputs by this platform
    "assumed",       # engineering assumption without measurement
    "manual",        # legacy default of the materials API
]

# Every MaterialInput field that enters the physics. Order is the display
# order used by the field manifest and by conflict reports.
MATERIAL_PHYSICAL_FIELD_ORDER: tuple[str, ...] = (
    "clothing_insulation_clo",
    "evaporative_resistance_m2pa_w",
    "clothing_area_factor",
    "solar_reflectance",
    "solar_transmittance",
    "infrared_emissivity",
    "infrared_transmittance",
    "projected_solar_area_factor",
    "absorbed_solar_to_body_fraction",
)

MATERIAL_PHYSICAL_FIELDS = frozenset(MATERIAL_PHYSICAL_FIELD_ORDER)


def validate_parameter_source_keys(
    sources: Mapping[str, object] | None,
) -> None:
    """Reject provenance entries that do not name a physical material field."""
    if not sources:
        return

    unknown = set(sources) - MATERIAL_PHYSICAL_FIELDS

    if unknown:
        raise ValueError(
            "parameter_sources refers to unknown material fields: "
            + ", ".join(sorted(unknown))
        )


class ParameterSource(BaseModel):
    """Provenance of one numeric input."""

    model_config = ConfigDict(extra="forbid")

    source_type: SourceType = "assumed"
    reference: str | None = Field(default=None, max_length=500)
    note: str | None = Field(default=None, max_length=1000)


class ModelParameter(BaseModel):
    """A physical constant used by the thermal model."""

    model_config = ConfigDict(frozen=True)

    name: str
    value: float
    unit: str
    description: str
    source_type: SourceType
    reference: str
    note: str | None = None


class ModelMetadata(BaseModel):
    """Written into every simulation response for traceability."""

    parameter_set_version: str
    parameter_set_sha256: str


class ModelParameterManifest(ModelMetadata):
    parameters: list[ModelParameter]


class MaterialFieldDescriptor(BaseModel):
    """Machine-readable description of one physical material field (Stage 4).

    Generated from ``MaterialInput`` so that the frontend can render forms and
    provenance editors without duplicating bounds, units or defaults.
    """

    model_config = ConfigDict(frozen=True)

    name: str
    unit: str
    description: str
    minimum: float | None
    maximum: float | None
    default: float | None
    nullable: bool
    derived_when_null: str | None = None


class MaterialFieldManifest(ModelMetadata):
    source_types: list[SourceType]
    fields: list[MaterialFieldDescriptor]