from pydantic import BaseModel, Field, model_validator

from datetime import datetime

from app.schemas.weather import WeatherTimeSeries

from app.schemas.environment import EnvironmentAssumptions

from app.schemas.provenance import (  # replace the existing provenance import
    MATERIAL_PHYSICAL_FIELD_ORDER,
    MATERIAL_PHYSICAL_FIELDS,
    ModelMetadata,
    ParameterSource,
    validate_parameter_source_keys,
)

__all__ = ["MATERIAL_PHYSICAL_FIELDS", "MATERIAL_PHYSICAL_FIELD_ORDER"]  # re-export

from typing import Literal

BodyPosition = Literal["standing", "sitting"]

class EnvironmentInput(BaseModel):
    air_temperature_c: float = Field(default=38.0, ge=-50, le=70)
    mean_radiant_temperature_c: float = Field(default=45.0, ge=-50, le=100)
    sky_temperature_c: float | None = Field(default=None, ge=-100, le=70)
    relative_humidity_percent: float = Field(default=40.0, ge=0, le=100)
    wind_speed_m_s: float = Field(default=1.5, ge=0, le=30)
    solar_radiation_w_m2: float = Field(
        default=800.0, ge=0, le=1500,
        description="Global horizontal irradiance (GHI)",
    )
    sky_view_factor: float = Field(default=0.5, ge=0, le=1)
    
    # Stage 5 (ADR 0006). Optional beam/diffuse split; supply both or neither.
    direct_normal_irradiance_w_m2: float | None = Field(
        default=None, ge=0, le=1500,
        description="Direct normal irradiance (DNI) on a plane facing the sun",
    )
    diffuse_horizontal_irradiance_w_m2: float | None = Field(
        default=None, ge=0, le=1500,
        description="Diffuse horizontal irradiance (DHI) from the sky vault",
    )
    ground_albedo: float = Field(
        default=0.2, ge=0, le=1,
        description="Shortwave reflectance of the ground (reflected-diffuse term)",
    )

    @model_validator(mode="after")
    def validate_solar_split(self):
        has_dni = self.direct_normal_irradiance_w_m2 is not None
        has_dhi = self.diffuse_horizontal_irradiance_w_m2 is not None

        if has_dni != has_dhi:
            raise ValueError(
                "direct_normal_irradiance_w_m2 and "
                "diffuse_horizontal_irradiance_w_m2 must be supplied together"
            )

        return self

    @property
    def has_solar_split(self) -> bool:
        return self.direct_normal_irradiance_w_m2 is not None

class PersonInput(BaseModel):
    met: float = Field(default=2.6, ge=0.7, le=10)
    body_surface_area_m2: float = Field(default=1.8, ge=1.0, le=3.0)
    body_mass_kg: float = Field(default=70.0, ge=30.0, le=200.0)
    initial_core_temperature_c: float = Field(default=36.8, ge=34, le=40)
    initial_skin_temperature_c: float = Field(default=33.7, ge=20, le=40)

    # Stage 5 (ADR 0006). Selects A_r/A_D for longwave and diffuse shortwave.
    position: BodyPosition = Field(
        default="standing",
        description="Posture; selects the effective radiation area ratio",
    )

class MaterialInput(BaseModel):
    """Garment parameters for one scenario.

    ``material_version_id`` links the input to an immutable material library
    version. When it is set, the API resolves it (Stage 4, PR-4):
    * physical fields that are omitted are filled from the stored version;
    * physical fields that are supplied must equal the stored version,
      otherwise the request is rejected with MATERIAL_PARAMETER_CONFLICT;
    * provenance fields are filled from the stored version when omitted.
    """

    name: str = Field(min_length=1, max_length=100)

    clothing_insulation_clo: float = Field(
        default=0.5, ge=0, le=5,
        description="Intrinsic dry thermal insulation of the garment",
        json_schema_extra={"unit": "clo"},
    )

    # Stage 2. Intrinsic clothing evaporative resistance Re,cl.
    evaporative_resistance_m2pa_w: float | None = Field(
        default=None, ge=0, le=1000,
        description="Intrinsic evaporative resistance Re,cl of the garment",
        json_schema_extra={
            "unit": "m^2 Pa/W",
            "derived_when_null": "R_cl / (LR * i_cl)",
        },
    )

    # Stage 3. Measured clothing area factor f_cl.
    clothing_area_factor: float | None = Field(
        default=None, ge=1.0, le=2.0,
        description="Clothing area factor f_cl = A_cl / A_D",
        json_schema_extra={
            "unit": "-",
            "derived_when_null": "1 + clothing_area_factor_slope * clo",
        },
    )

    solar_reflectance: float = Field(
        default=0.5, ge=0, le=1,
        description="Hemispherical solar reflectance (0.3-2.5 um)",
        json_schema_extra={"unit": "-"},
    )
    solar_transmittance: float = Field(
        default=0, ge=0, le=1,
        description="Hemispherical solar transmittance (0.3-2.5 um)",
        json_schema_extra={"unit": "-"},
    )
    infrared_emissivity: float = Field(
        default=0.9, ge=0, le=1,
        description="Longwave emissivity of the outer surface (8-13 um)",
        json_schema_extra={"unit": "-"},
    )

    # Stage 2. Longwave transmittance of the textile (IR-transparent designs).
    infrared_transmittance: float = Field(
        default=0.0, ge=0, le=1,
        description="Longwave transmittance of the textile (8-13 um)",
        json_schema_extra={"unit": "-"},
    )

    projected_solar_area_factor: float = Field(
        default=0.25, ge=0, le=1,
        description="Projected area factor A_p / A_D for direct solar radiation",
        json_schema_extra={"unit": "-"},
    )
    absorbed_solar_to_body_fraction: float = Field(
        default=0.35, ge=0, le=1,
        description=(
            "DEPRECATED since Stage 5 (ADR 0005): ignored by the physics. "
            "Kept so stored requests and library versions keep loading."
        ),
        json_schema_extra={"unit": "-", "deprecated": True},
    )

    # Provenance (no effect on the physics).
    material_version_id: str | None = Field(
        default=None,
        description="Material library version this input was taken from",
    )
    source_type: str | None = Field(default=None, max_length=50)
    source_reference: str | None = None
    # Stage 2. Per-parameter provenance keyed by field name.
    parameter_sources: dict[str, ParameterSource] | None = None

    @model_validator(mode="after")
    def validate_optical_properties(self):
        if self.solar_reflectance + self.solar_transmittance > 1.0 + 1e-6:
            raise ValueError(
                "solar_reflectance + solar_transmittance cannot be greater than 1"
            )

        if self.infrared_emissivity + self.infrared_transmittance > 1.0 + 1e-6:
            raise ValueError(
                "infrared_emissivity + infrared_transmittance cannot be greater than 1"
            )

        validate_parameter_source_keys(self.parameter_sources)

        return self


class SimulationRequest(BaseModel):
    city: str = Field(default="Dubai", min_length=1)
    duration_minutes: int = Field(
        default=120,
        ge=1,
        le=1440,
    )
    output_interval_minutes: int = Field(
        default=1,
        ge=1,
        le=60,
    )
    environment: EnvironmentInput
    person: PersonInput
    control_material: MaterialInput
    rc_material: MaterialInput

class EnergyDiagnostics(BaseModel):
    stored_energy_change_j_m2: float
    integrated_net_heat_j_m2: float
    energy_residual_j_m2: float
    normalized_residual_percent: float
    maximum_core_step_c: float
    maximum_skin_step_c: float
    solver_function_evaluations: int
    
class TimeSeriesPoint(BaseModel):
    minute: float
    core_temperature_c: float
    skin_temperature_c: float
    convection_w_m2: float
    longwave_radiation_w_m2: float
    evaporation_w_m2: float
    absorbed_solar_w_m2: float
    core_to_skin_w_m2: float
    # Stage 2 diagnostics. Optional so stored results still load.
    maximum_evaporation_w_m2: float | None = None
    skin_wettedness: float | None = None
    # Stage 3 diagnostics.
    clothing_surface_temperature_c: float | None = None
    skin_blood_flow_kg_h_m2: float | None = None
    # Stage 5 diagnostics.
    solar_incident_w_m2: float | None = None
    solar_absorbed_by_textile_w_m2: float | None = None
    solar_transmitted_w_m2: float | None = None

class ClothingSummary(BaseModel):
    """Resolved clothing quantities actually used by the solver."""

    dry_resistance_m2k_w: float
    evaporative_resistance_m2pa_w: float
    evaporative_resistance_source: Literal["material_input", "derived_from_clo"]
    infrared_transmittance: float
    # Stage 3
    clothing_area_factor: float | None = None
    clothing_area_factor_source: (
        Literal["material_input", "derived_from_clo"] | None
    ) = None

class BodyThermalSummary(BaseModel):
    """Heat capacities derived from PersonInput (Stage 3, ADR 0001)."""

    body_mass_kg: float
    body_surface_area_m2: float
    core_heat_capacity_j_m2k: float
    skin_heat_capacity_j_m2k: float
    # Stage 5
    position: BodyPosition | None = None
    effective_radiation_area_ratio: float | None = None

class ScenarioResult(BaseModel):
    material_name: str
    time_series: list[TimeSeriesPoint]
    final_core_temperature_c: float
    final_skin_temperature_c: float
    peak_core_temperature_c: float
    peak_skin_temperature_c: float
    diagnostics: EnergyDiagnostics
    # Stage 2
    clothing: ClothingSummary | None = None
    assumptions_applied: list[str] = Field(default_factory=list)
    # Stage 3
    body: BodyThermalSummary | None = None


class SimulationSummary(BaseModel):
    final_skin_temperature_improvement_c: float
    final_core_temperature_improvement_c: float
    average_skin_temperature_improvement_c: float


class SimulationResponse(BaseModel):
    model_name: str
    model_version: str
    city: str
    duration_minutes: int
    control: ScenarioResult
    radiative_cooling: ScenarioResult
    summary: SimulationSummary
    warning: str
    # Stage 2. Optional so previously stored results still load.
    model_metadata: ModelMetadata | None = None

class BenchmarkTolerances(BaseModel):
    """Acceptance thresholds on the maximum absolute trajectory difference."""

    core_temperature_c: float = Field(default=0.3, gt=0, le=5)
    skin_temperature_c: float = Field(default=1.0, gt=0, le=10)
    
class GaggeBenchmarkRequest(BaseModel):
    duration_minutes: int = Field(default=60, ge=1, le=240)
    environment: EnvironmentInput
    person: PersonInput
    material: MaterialInput
    tolerances: BenchmarkTolerances = Field(default_factory=BenchmarkTolerances)

class GaggeModelOutput(BaseModel):
    core_temperature_c: float
    skin_temperature_c: float
    skin_evaporation_w_m2: float
    skin_heat_loss_w_m2: float
    respiratory_heat_loss_w_m2: float
    skin_blood_flow_kg_h_m2: float
    skin_wettedness: float
    standard_effective_temperature_c: float


class PrototypeBenchmarkOutput(BaseModel):
    core_temperature_c: float
    skin_temperature_c: float
    evaporation_w_m2: float
    skin_wettedness: float
    skin_blood_flow_kg_h_m2: float
    energy_residual_percent: float

class BenchmarkSeriesPoint(BaseModel):
    minute: int
    prototype_core_temperature_c: float
    prototype_skin_temperature_c: float
    prototype_evaporation_w_m2: float
    reference_core_temperature_c: float
    reference_skin_temperature_c: float
    reference_evaporation_w_m2: float
    
class BenchmarkMetric(BaseModel):
    final_difference_c: float
    maximum_absolute_difference_c: float
    root_mean_square_difference_c: float
    tolerance_c: float
    passed: bool
    
class ReferencePortParity(BaseModel):
    """Port vs. library after 60 minutes (the only duration the library runs)."""

    library_core_temperature_c: float
    port_core_temperature_c: float
    library_skin_temperature_c: float
    port_skin_temperature_c: float
    maximum_absolute_difference_c: float
    
class GaggeBenchmarkResponse(BaseModel):
    reference_model: str
    reference_library: str
    reference_library_version: str
    environment_note: str
    alignment_applied: list[str]
    prototype: PrototypeBenchmarkOutput
    gagge: GaggeModelOutput
    # Kept for backward compatibility with Stage 2 clients.
    difference_core_temperature_c: float
    difference_skin_temperature_c: float
    # Stage 3
    core_temperature: BenchmarkMetric
    skin_temperature: BenchmarkMetric
    passed: bool
    time_series: list[BenchmarkSeriesPoint]
    reference_port_parity: ReferencePortParity
    warning: str
class WeatherSimulationRequest(BaseModel):
    city_id: str = Field(
        default="dubai",
        min_length=1,
    )
    start_time_local: datetime
    duration_minutes: int = Field(
        default=120,
        ge=1,
        le=1440,
    )
    output_interval_minutes: int = Field(
        default=1,
        ge=1,
        le=60,
    )
    person: PersonInput
    control_material: MaterialInput
    rc_material: MaterialInput
    environment_assumptions: EnvironmentAssumptions = Field(
        default_factory=EnvironmentAssumptions
    )

class WeatherSimulationResponse(
    SimulationResponse
):
    weather: WeatherTimeSeries
    environment_model_note: str
    environment_assumptions: EnvironmentAssumptions | None = None