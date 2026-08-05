from pydantic import BaseModel, Field, model_validator

from datetime import datetime

from app.schemas.weather import WeatherTimeSeries

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
    met: float = Field(
        default=2.6,
        ge=0.7,
        le=10,
    )
    body_surface_area_m2: float = Field(
        default=1.8,
        ge=1.0,
        le=3.0,
    )
    initial_core_temperature_c: float = Field(
        default=36.8,
        ge=34,
        le=40,
    )
    initial_skin_temperature_c: float = Field(
        default=33.7,
        ge=20,
        le=40,
    )


class MaterialInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    clothing_insulation_clo: float = Field(
        default=0.5,
        ge=0,
        le=5,
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

    @model_validator(mode="after")
    def validate_optical_properties(self):
        total = self.solar_reflectance + self.solar_transmittance

        if total > 1.0 + 1e-6:
            raise ValueError(
                "solar_reflectance + solar_transmittance 不能大於 1"
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


class ScenarioResult(BaseModel):
    material_name: str
    time_series: list[TimeSeriesPoint]
    final_core_temperature_c: float
    final_skin_temperature_c: float
    peak_core_temperature_c: float
    peak_skin_temperature_c: float
    diagnostics: EnergyDiagnostics


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
    

    
class GaggeBenchmarkRequest(BaseModel):
    duration_minutes: int = Field(
        default=60,
        ge=1,
        le=240,
    )
    environment: EnvironmentInput
    person: PersonInput
    material: MaterialInput


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
    energy_residual_percent: float


class GaggeBenchmarkResponse(BaseModel):
    reference_model: str
    reference_library: str
    environment_note: str
    prototype: PrototypeBenchmarkOutput
    gagge: GaggeModelOutput
    difference_core_temperature_c: float
    difference_skin_temperature_c: float
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


class WeatherSimulationResponse(
    SimulationResponse
):
    weather: WeatherTimeSeries
    environment_model_note: str