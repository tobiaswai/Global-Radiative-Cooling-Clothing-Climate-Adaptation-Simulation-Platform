from pydantic import BaseModel, Field, model_validator

from datetime import datetime

from app.schemas.weather import WeatherTimeSeries

from app.schemas.environment import EnvironmentAssumptions

from app.schemas.provenance import ModelMetadata, ParameterSource

from typing import Literal

class EnvironmentInput(BaseModel):
    air_temperature_c: float = Field(
        default=38.0,
        ge=-50,
        le=70,
    )
    mean_radiant_temperature_c: float = Field(
        default=45.0,
        ge=-50,
        le=100,
    )
    sky_temperature_c: float | None = Field(
        default=None,
        ge=-100,
        le=70,
    )
    relative_humidity_percent: float = Field(
        default=40.0,
        ge=0,
        le=100,
    )
    wind_speed_m_s: float = Field(
        default=1.5,
        ge=0,
        le=30,
    )
    solar_radiation_w_m2: float = Field(
        default=800.0,
        ge=0,
        le=1500,
    )
    sky_view_factor: float = Field(
        default=0.5,
        ge=0,
        le=1,
    )


class PersonInput(BaseModel):
    met: float = Field(default=2.6, ge=0.7, le=10)

    body_surface_area_m2: float = Field(default=1.8, ge=1.0, le=3.0)

    # Stage 3. Heat capacities are derived from body mass (ADR 0001).
    # 70 kg / 1.8 m^2 reproduces the Gagge two-node lumped value.
    body_mass_kg: float = Field(default=70.0, ge=30.0, le=200.0)

    initial_core_temperature_c: float = Field(default=36.8, ge=34, le=40)
    initial_skin_temperature_c: float = Field(default=33.7, ge=20, le=40)

MATERIAL_PHYSICAL_FIELDS = frozenset(
    {
        "clothing_insulation_clo",
        "evaporative_resistance_m2pa_w",
        "clothing_area_factor",
        "solar_reflectance",
        "solar_transmittance",
        "infrared_emissivity",
        "infrared_transmittance",
        "projected_solar_area_factor",
        "absorbed_solar_to_body_fraction",
    }
)

class MaterialInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)

    clothing_insulation_clo: float = Field(default=0.5, ge=0, le=5)

    # Stage 2. Intrinsic clothing evaporative resistance Re,cl.
    # None -> derived from clo (clothing.derive_evaporative_resistance_m2pa_w)
    # and reported in ScenarioResult.assumptions_applied.
    evaporative_resistance_m2pa_w: float | None = Field(
        default=None, ge=0, le=1000
    )
    clothing_area_factor: float | None = Field(default=None, ge=1.0, le=2.0)


    solar_reflectance: float = Field(default=0.5, ge=0, le=1)
    solar_transmittance: float = Field(default=0, ge=0, le=1)
    infrared_emissivity: float = Field(default=0.9, ge=0, le=1)

    # Stage 2. Longwave transmittance of the textile (IR-transparent designs).
    infrared_transmittance: float = Field(default=0.0, ge=0, le=1)

    projected_solar_area_factor: float = Field(default=0.25, ge=0, le=1)
    absorbed_solar_to_body_fraction: float = Field(default=0.35, ge=0, le=1)

    # Provenance (no effect on the physics).
    material_version_id: str | None = None
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

        if self.parameter_sources:
            unknown = set(self.parameter_sources) - MATERIAL_PHYSICAL_FIELDS
            if unknown:
                raise ValueError(
                    "parameter_sources refers to unknown material fields: "
                    + ", ".join(sorted(unknown))
                )

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