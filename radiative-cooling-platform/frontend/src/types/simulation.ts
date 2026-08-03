export type EnvironmentInput = {
  air_temperature_c: number;
  mean_radiant_temperature_c: number;
  sky_temperature_c: number | null;
  relative_humidity_percent: number;
  wind_speed_m_s: number;
  solar_radiation_w_m2: number;
  sky_view_factor: number;
};

export type PersonInput = {
  met: number;
  body_surface_area_m2: number;
  initial_core_temperature_c: number;
  initial_skin_temperature_c: number;
};

export type MaterialInput = {
  name: string;
  clothing_insulation_clo: number;
  solar_reflectance: number;
  solar_transmittance: number;
  infrared_emissivity: number;
  projected_solar_area_factor: number;
  absorbed_solar_to_body_fraction: number;
};

export type SimulationRequest = {
  city: string;
  duration_minutes: number;
  output_interval_minutes: number;
  environment: EnvironmentInput;
  person: PersonInput;
  control_material: MaterialInput;
  rc_material: MaterialInput;
};

export type TimeSeriesPoint = {
  minute: number;
  core_temperature_c: number;
  skin_temperature_c: number;
  convection_w_m2: number;
  longwave_radiation_w_m2: number;
  evaporation_w_m2: number;
  absorbed_solar_w_m2: number;
  core_to_skin_w_m2: number;
};

export type ScenarioResult = {
  material_name: string;
  time_series: TimeSeriesPoint[];
  final_core_temperature_c: number;
  final_skin_temperature_c: number;
  peak_core_temperature_c: number;
  peak_skin_temperature_c: number;
};

export type SimulationResponse = {
  model_name: string;
  model_version: string;
  city: string;
  duration_minutes: number;
  control: ScenarioResult;
  radiative_cooling: ScenarioResult;
  summary: {
    final_skin_temperature_improvement_c: number;
    final_core_temperature_improvement_c: number;
    average_skin_temperature_improvement_c: number;
  };
  warning: string;
};