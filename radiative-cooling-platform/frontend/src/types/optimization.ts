import type { EnvironmentAssumptions, MaterialInput, PersonInput, LeaseState } from "@/types/simulation";

export type DecisionVariableName =
  | "solar_reflectance" | "solar_transmittance" | "infrared_emissivity"
  | "infrared_transmittance" | "clothing_insulation_clo" | "evaporative_resistance_m2pa_w";

export type MetricName =
  | "mean_skin_temperature_c" | "peak_skin_temperature_c" | "peak_core_temperature_c"
  | "skin_exceedance_fraction" | "core_exceedance_fraction"
  | "mean_skin_cooling_c" | "mean_core_cooling_c";

export type DecisionVariable = { name: DecisionVariableName; lower: number; upper: number };
export type MetricConstraint = { metric: MetricName; operator: "<=" | ">="; threshold: number };
export type OptimizationObjective = { metric: MetricName; sense: "minimize" | "maximize" };
export type RequirementMapSpec = { x_variable: DecisionVariableName; y_variable: DecisionVariableName; resolution: number };

export type OptimizationCreate = {
  name: string;
  city_id: string;
  year: number;
  months: number[];
  sample_days_per_month: number;
  local_start_hour: number;
  duration_minutes: number;
  output_interval_minutes: number;
  skin_threshold_c: number;
  core_threshold_c: number;
  person: PersonInput;
  control_material: MaterialInput;
  base_material: MaterialInput;
  environment_assumptions?: EnvironmentAssumptions;
  variables: DecisionVariable[];
  objective: OptimizationObjective;
  constraints: MetricConstraint[];
  algorithm: "differential_evolution";
  population_multiplier: number;
  max_generations: number;
  seed: number | null;
  requirement_map: RequirementMapSpec | null;
};

export type OptimizationEstimate = {
  variable_count: number;
  population_size: number;
  optimizer_evaluation_budget: number;
  requirement_map_evaluations: number;
  sample_count: number;
  thermal_simulation_budget: number;
  weather_requests: number;
};

export type EvaluationMetrics = { sample_count: number } & Record<MetricName, number>;

export type CandidateEvaluation = {
  parameters: Record<string, number>;
  metrics: EvaluationMetrics | null;
  objective_value: number | null;
  constraint_violation: number | null;
  feasible: boolean;
};

export type GenerationRecord = {
  generation: number;
  penalised_objective: number;
  best_parameters: Record<string, number>;
  best_metric_value: number | null;
  best_feasible: boolean;
  evaluation_count: number;
};

export type RequirementCell = { x: number; y: number; metric_value: number; constraint_violation: number; feasible: boolean };

export type RequirementMapResult = {
  x_variable: DecisionVariableName;
  y_variable: DecisionVariableName;
  x_values: number[];
  y_values: number[];
  cells: (RequirementCell | null)[][];
  frontier: { y: number; minimum_x: number | null }[];
  minimum_x_at_max_y: number | null;
  minimum_y_at_max_x: number | null;
  fixed_parameters: Record<string, number>;
};

export type OptimizationResult = {
  verdict: "feasible" | "infeasible" | "unconstrained";
  message: string;
  objective: OptimizationObjective;
  constraints: MetricConstraint[];
  best: CandidateEvaluation;
  baseline: CandidateEvaluation;
  optical_upper_bound: CandidateEvaluation | null;
  requirement_map: RequirementMapResult | null;
  sample_count: number;
  skipped_samples: { sample_date_local: string; reason_code: string; message: string }[];
  weather_payload_sha256: Record<string, string | null>;
  evaluation_count: number;
  simulation_count: number;
  generations: number;
  algorithm: string;
  algorithm_message: string;
  elapsed_seconds: number;
  model_version: string;
  parameter_fingerprint: string;
};

export type OptimizationStatus = "queued" | "running" | "cancelling" | "cancelled" | "completed" | "failed";

export type OptimizationJob = {
  id: string;
  celery_task_id: string | null;
  name: string;
  city_id: string;
  status: OptimizationStatus;
  stage: string;
  progress: number;
  evaluation_count: number;
  error_message: string | null;
  created_at: string;
  updated_at: string;
  started_at: string | null;
  completed_at: string | null;
  attempt: number;
  lease_owner: string | null;
  lease_expires_at: string | null;
  last_heartbeat_at: string | null;
  lease_state: LeaseState;
  cancel_requested_at: string | null;
};

export type OptimizationJobDetail = OptimizationJob & {
  request: OptimizationCreate;
  history: GenerationRecord[];
  result: OptimizationResult | null;
};

export type OptimizationJobList = { items: OptimizationJob[]; total: number; limit: number; offset: number };