import type { DecisionVariable, MetricName } from "@/types/optimization";

export type SurrogateDatasetStatus =
  | "running" | "finalizing" | "completed" | "partial_completed" | "failed" | "cancelled";
export type SurrogateModelStatus = "queued" | "training" | "completed" | "failed";
export type PredictionSource = "surrogate" | "physics" | "none";

export type SurrogateDataset = {
  id: string; name: string; status: SurrogateDatasetStatus;
  total_chunks: number; completed_chunks: number; failed_chunks: number;
  row_count: number; valid_material_count: number;
  model_version: string; parameter_fingerprint: string; context_sha256: string;
  error_message: string | null; created_at: string; updated_at: string; completed_at: string | null;
};

export type SurrogateModel = {
  id: string; name: string; dataset_id: string | null; status: SurrogateModelStatus;
  accepted: boolean; targets: MetricName[]; model_version: string; parameter_fingerprint: string;
  stale: boolean; headline_mae: Partial<Record<MetricName, number>>;
  error_message: string | null; created_at: string; updated_at: string; completed_at: string | null;
};

export type TargetMetrics = {
  target: MetricName; count: number; mae: number; rmse: number; r2: number | null;
  interval_coverage: number; mean_interval_width: number;
};

export type ValidationReport = {
  row_count: number; feature_columns: string[]; targets: MetricName[]; training_cities: string[];
  splits: { split: string; fold_count: number; metrics: TargetMetrics[]; group_mae: Record<string, Record<string, number>> }[];
  acceptance: { split: string; target: string; mae: number; mae_threshold: number;
                interval_coverage: number; minimum_coverage: number; passed: boolean }[];
  passed: boolean; nominal_interval_coverage: number; training_seconds: number;
  prediction_microseconds_per_row: number; physics_seconds_per_simulation: number | null;
  sklearn_version: string;
};

export type SurrogateModelDetail = SurrogateModel & {
  training: { lower_quantile: number; upper_quantile: number; targets: MetricName[] };
  report: ValidationReport | null;
  variables: DecisionVariable[];
  base_parameters: Record<string, number>;
  training_cities: string[];
  year: number; months: number[]; local_start_hour: number; duration_minutes: number;
};

export type SurrogatePredictRequest = {
  model_id?: string | null; city_id: string; sample_date: string;
  materials: Record<string, number>[];
  mode?: "surrogate" | "physics" | "both"; physics_fallback?: boolean;
};

export type TargetPrediction = { value: number; lower: number; upper: number };

export type MaterialPrediction = {
  parameters: Record<string, number>; valid: boolean; within_domain: boolean;
  out_of_domain_features: string[]; source: PredictionSource;
  surrogate: Partial<Record<MetricName, TargetPrediction>> | null;
  physics: Partial<Record<MetricName, number>> | null;
  message: string | null;
};

export type SurrogatePredictResponse = {
  model_id: string; model_name: string; accepted: boolean; stale: boolean;
  city_id: string; sample_date: string; city_in_training: boolean;
  start_time_local: string; duration_minutes: number;
  weather_features: Record<string, number | null>; weather_payload_sha256: string | null;
  predictions: MaterialPrediction[]; physics_evaluations: number; physics_limit: number;
  elapsed_ms: number; warnings: string[];
};

export type Paged<T> = { items: T[]; total: number; limit: number; offset: number };