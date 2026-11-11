import type {
  EnvironmentInput,
  MaterialInput,
  PersonInput,
} from "@/types/simulation";

/** Acceptance thresholds on the maximum absolute trajectory difference. */
export type BenchmarkTolerances = {
  core_temperature_c: number;
  skin_temperature_c: number;
};

export type GaggeBenchmarkRequest = {
  duration_minutes: number;
  environment: EnvironmentInput;
  person: PersonInput;
  material: MaterialInput;
  tolerances: BenchmarkTolerances;
};

export type BenchmarkMetric = {
  final_difference_c: number;
  maximum_absolute_difference_c: number;
  root_mean_square_difference_c: number;
  tolerance_c: number;
  passed: boolean;
};

export type BenchmarkSeriesPoint = {
  minute: number;
  prototype_core_temperature_c: number;
  prototype_skin_temperature_c: number;
  prototype_evaporation_w_m2: number;
  reference_core_temperature_c: number;
  reference_skin_temperature_c: number;
  reference_evaporation_w_m2: number;
};

export type PrototypeBenchmarkOutput = {
  core_temperature_c: number;
  skin_temperature_c: number;
  evaporation_w_m2: number;
  skin_wettedness: number;
  skin_blood_flow_kg_h_m2: number;
  energy_residual_percent: number;
};

export type GaggeModelOutput = {
  core_temperature_c: number;
  skin_temperature_c: number;
  skin_evaporation_w_m2: number;
  skin_heat_loss_w_m2: number;
  respiratory_heat_loss_w_m2: number;
  skin_blood_flow_kg_h_m2: number;
  skin_wettedness: number;
  standard_effective_temperature_c: number;
};

/** Port vs. library after 60 minutes (the only duration the library runs). */
export type ReferencePortParity = {
  library_core_temperature_c: number;
  port_core_temperature_c: number;
  library_skin_temperature_c: number;
  port_skin_temperature_c: number;
  maximum_absolute_difference_c: number;
};

export type GaggeBenchmarkResponse = {
  reference_model: string;
  reference_library: string;
  reference_library_version: string;
  environment_note: string;
  alignment_applied: string[];
  prototype: PrototypeBenchmarkOutput;
  gagge: GaggeModelOutput;
  difference_core_temperature_c: number;
  difference_skin_temperature_c: number;
  core_temperature: BenchmarkMetric;
  skin_temperature: BenchmarkMetric;
  passed: boolean;
  time_series: BenchmarkSeriesPoint[];
  reference_port_parity: ReferencePortParity;
  warning: string;
};