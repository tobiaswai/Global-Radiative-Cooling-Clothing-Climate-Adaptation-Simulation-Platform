from datetime import datetime
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator,
)


MaterialMode = Literal[
    "ordinary",
    "opaque_emitter",
    "infrared_transparent",
    "hybrid",
]

SpectrumType = Literal[
    "solar_reflectance",
    "solar_transmittance",
    "mir_emissivity",
    "mir_transmittance",
]


class MaterialVersionCreate(BaseModel):
    mode: MaterialMode = "opaque_emitter"

    clothing_insulation_clo: float = Field(
        default=0.5,
        ge=0,
        le=5,
    )

    evaporative_resistance_m2pa_w: float | None = Field(
        default=None,
        ge=0,
    )

    solar_reflectance: float = Field(
        default=0.5,
        ge=0,
        le=1,
    )

    solar_transmittance: float = Field(
        default=0,
        ge=0,
        le=1,
    )

    infrared_emissivity: float = Field(
        default=0.9,
        ge=0,
        le=1,
    )

    infrared_transmittance: float = Field(
        default=0,
        ge=0,
        le=1,
    )

    projected_solar_area_factor: float = Field(
        default=0.25,
        ge=0,
        le=1,
    )

    absorbed_solar_to_body_fraction: float = Field(
        default=0.35,
        ge=0,
        le=1,
    )

    areal_density_g_m2: float | None = Field(
        default=None,
        ge=0,
    )

    specific_heat_j_kgk: float | None = Field(
        default=None,
        ge=0,
    )

    source_type: str = Field(
        default="manual",
        max_length=50,
    )

    source_reference: str | None = None
    notes: str | None = None

    @model_validator(mode="after")
    def validate_optical_properties(self):
        if (
            self.solar_reflectance
            + self.solar_transmittance
            > 1.0 + 1e-6
        ):
            raise ValueError(
                "solar_reflectance + "
                "solar_transmittance 不能大於 1"
            )

        return self


class MaterialCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=200,
    )

    slug: str = Field(
        min_length=1,
        max_length=200,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )

    description: str | None = None
    institution: str | None = None

    initial_version: MaterialVersionCreate


class MaterialUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
    )

    description: str | None = None
    institution: str | None = None
    is_archived: bool | None = None


class SpectrumSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    spectrum_type: str
    wavelength_unit: str
    point_count: int
    minimum_wavelength_um: float
    maximum_wavelength_um: float
    original_filename: str
    file_checksum_sha256: str
    created_at: datetime


class MaterialVersionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    material_id: str
    version_number: int
    mode: str

    clothing_insulation_clo: float
    evaporative_resistance_m2pa_w: float | None

    solar_reflectance: float
    solar_transmittance: float
    infrared_emissivity: float
    infrared_transmittance: float

    projected_solar_area_factor: float
    absorbed_solar_to_body_fraction: float

    areal_density_g_m2: float | None
    specific_heat_j_kgk: float | None

    source_type: str
    source_reference: str | None
    notes: str | None

    created_at: datetime
    spectra: list[SpectrumSummary] = []


class MaterialResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    slug: str
    description: str | None
    institution: str | None
    is_archived: bool
    created_at: datetime
    updated_at: datetime

    versions: list[MaterialVersionResponse]


class MaterialListItem(BaseModel):
    id: str
    name: str
    slug: str
    institution: str | None
    is_archived: bool
    latest_version_number: int | None
    created_at: datetime


class MaterialListResponse(BaseModel):
    items: list[MaterialListItem]
    total: int
    limit: int
    offset: int


class SpectrumPoint(BaseModel):
    wavelength_um: float
    value: float


class SpectrumResponse(BaseModel):
    summary: SpectrumSummary
    points: list[SpectrumPoint]