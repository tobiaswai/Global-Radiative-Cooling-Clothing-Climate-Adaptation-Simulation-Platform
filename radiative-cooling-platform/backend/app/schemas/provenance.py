"""Provenance types shared by material inputs, the model parameter registry
and simulation responses (Stage 2)."""

from __future__ import annotations

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