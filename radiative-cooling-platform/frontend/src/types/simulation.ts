export type ParameterSourceType =
  | "measured"
  | "manufacturer"
  | "literature"
  | "standard"
  | "derived"
  | "assumed"
  | "manual";

export type ParameterSource = {
  source_type: ParameterSourceType;
  reference?: string | null;
  note?: string | null;
};

/** How the solver obtained a resolved clothing quantity. */
export type ResolvedParameterSource = "material_input" | "derived_from_clo";

export type EnvironmentInput = {
  air_temperature_c: number;
  mean_radiant_temperature_c: number;
  /** `null` lets the backend derive the sky temperature. */
  sky_temperature_c: number | null;
  relative_humidity_percent: number;
  wind_speed_m_s: number;
  solar_radiation_w_m2: number;
  sky_view_factor: number;
};

export type PersonInput = {
  met: number;
  /** Stage 3 (ADR 0001): drives core/skin heat capacities. Backend default 70 kg. */
  body_mass_kg: number;
  body_surface_area_m2: number;
  initial_core_temperature_c: number;
  initial_skin_temperature_c: number;
};

export type MaterialInput = {
  name: string;
  clothing_insulation_clo: number;
  /** Stage 3: f_cl in [1, 2]. `null` lets the backend derive it from clo. */
  clothing_area_factor: number | null;
  evaporative_resistance_m2pa_w?: number | null;
  solar_reflectance: number;
  solar_transmittance: number;
  infrared_emissivity: number;
  infrared_transmittance?: number;
  projected_solar_area_factor: number;
  absorbed_solar_to_body_fraction: number;
  material_version_id?: string | null;
  parameter_sources?: Record<string, ParameterSource> | null;
  source_type?: string | null;
  source_reference?: string | null;
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

/**
 * Optional members are nullable on the wire and may be absent entirely on
 * results persisted before Stage 3. Always read them defensively.
 */
export type TimeSeriesPoint = {
  minute: number;
  core_temperature_c: number;
  skin_temperature_c: number;
  convection_w_m2: number;
  longwave_radiation_w_m2: number;
  evaporation_w_m2: number;
  absorbed_solar_w_m2: number;
  core_to_skin_w_m2: number;
  maximum_evaporation_w_m2?: number | null;
  skin_wettedness?: number | null;
  /** Stage 3 */
  clothing_surface_temperature_c?: number | null;
  /** Stage 3 */
  skin_blood_flow_kg_h_m2?: number | null;
};

export type EnergyDiagnostics = {
  stored_energy_change_j_m2: number;
  integrated_net_heat_j_m2: number;
  energy_residual_j_m2: number;
  normalized_residual_percent: number;
  maximum_core_step_c: number;
  maximum_skin_step_c: number;
  solver_function_evaluations: number;
};

export type ClothingSummary = {
  dry_resistance_m2k_w: number;
  evaporative_resistance_m2pa_w: number;
  evaporative_resistance_source: ResolvedParameterSource;
  infrared_transmittance: number;
  /** Stage 3 */
  clothing_area_factor?: number | null;
  /** Stage 3 */
  clothing_area_factor_source?: ResolvedParameterSource | null;
};

/** Stage 3 (ADR 0001): heat capacities derived from PersonInput. */
export type BodyThermalSummary = {
  body_mass_kg: number;
  body_surface_area_m2: number;
  core_heat_capacity_j_m2k: number;
  skin_heat_capacity_j_m2k: number;
};

export type ScenarioResult = {
  material_name: string;
  time_series: TimeSeriesPoint[];
  final_core_temperature_c: number;
  final_skin_temperature_c: number;
  peak_core_temperature_c: number;
  peak_skin_temperature_c: number;
  diagnostics: EnergyDiagnostics;
  assumptions_applied?: string[];
  clothing?: ClothingSummary | null;
  /** Stage 3 */
  body?: BodyThermalSummary | null;
};

export type ModelMetadata = {
  parameter_set_version: string;
  parameter_set_sha256: string;
};

export type SimulationSummary = {
  final_skin_temperature_improvement_c: number;
  final_core_temperature_improvement_c: number;
  average_skin_temperature_improvement_c: number;
};

export type SimulationResponse = {
  model_name: string;
  model_version: string;
  model_metadata?: ModelMetadata | null;
  city: string;
  duration_minutes: number;
  control: ScenarioResult;
  radiative_cooling: ScenarioResult;
  summary: SimulationSummary;
  warning: string;
};

export type City = {
  id: string;
  name: string;
  country: string;
  latitude: number;
  longitude: number;
  elevation_m: number;
  timezone: string;
  climate_type: string;
};

export type WeatherPoint = {
  timestamp: string;
  air_temperature_c: number;
  relative_humidity_percent: number;
  wind_speed_m_s: number;
  ghi_w_m2: number;
  direct_radiation_w_m2: number;
  diffuse_radiation_w_m2: number;
  dni_w_m2: number;
};

export type WeatherTimeSeries = {
  city: City;
  requested_start_time: string;
  requested_end_time: string;
  points: WeatherPoint[];
  source: {
    provider: string;
    dataset: string;
    model: string;
    latitude: number;
    longitude: number;
    elevation_m: number;
    timezone: string;
    downloaded_at: string;
    from_cache: boolean;
    attribution: string;
  };
};

export type WeatherSimulationRequest = {
  city_id: string;
  start_time_local: string;
  duration_minutes: number;
  output_interval_minutes: number;
  person: PersonInput;
  control_material: MaterialInput;
  rc_material: MaterialInput;
};

export type WeatherSimulationResponse = SimulationResponse & {
  weather: WeatherTimeSeries;
  environment_model_note: string;
};

export type SimulationJobStatus =
  | "queued"
  | "running"
  | "cancelling"
  | "cancelled"
  | "completed"
  | "failed";

export type SimulationJob = {
  id: string;
  celery_task_id: string | null;
  status: SimulationJobStatus;
  stage: string;
  progress: number;
  city_id: string;
  summary: Record<string, number> | null;
  error_message: string | null;
  created_at: string;
  updated_at: string;
  started_at: string | null;
  completed_at: string | null;
};

export type SimulationJobDetail = SimulationJob & {
  request: WeatherSimulationRequest;
};

export type SimulationJobList = {
  items: SimulationJob[];
  total: number;
  limit: number;
  offset: number;
};