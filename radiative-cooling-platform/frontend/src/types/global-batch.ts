import type {
  MaterialInput,
  PersonInput,
} from "@/types/simulation";


export type GlobalBatchStatus =
  | "queued"
  | "running"
  | "cancelling"
  | "cancelled"
  | "completed"
  | "partial_completed"
  | "failed";


export type GlobalCityStatus =
  | "queued"
  | "running"
  | "cancelled"
  | "completed"
  | "failed";


export type ExposureMatchMode =
  | "all"
  | "any";


export type AnalysisResolution =
  | "representative"
  | "daily";


export type ExecutionProfile =
  | "auto"
  | "standard"
  | "large";


export type GlobalCity = {
  id: string;
  name: string;
  country: string;
  latitude: number;
  longitude: number;
  elevation_m: number;
  timezone: string;
  climate_type: string;
};


export type GlobalBatchCreate = {
  name: string;
  city_ids: string[];

  year: number;
  start_month: number;
  end_month: number;

  analysis_resolution: AnalysisResolution;

  sample_days_per_month: number;
  daily_stride_days: number;

  execution_profile: ExecutionProfile;
  resume_from_checkpoint: boolean;

  enable_heatwave_analysis: boolean;
  heatwave_temperature_threshold_c: number;
  heatwave_minimum_consecutive_days: number;

  representative_day?: number | null;

  local_start_hour: number;
  duration_minutes: number;
  output_interval_minutes: number;

  minimum_skin_improvement_c: number;

  minimum_air_temperature_c:
    | number
    | null;

  minimum_solar_radiation_w_m2:
    | number
    | null;

  exposure_match_mode: ExposureMatchMode;

  person: PersonInput;
  control_material: MaterialInput;
  rc_material: MaterialInput;
};


export type DailyAdaptationResult = {
  sample_date_local: string;
  weight_days: number;

  mean_air_temperature_c: number;
  maximum_air_temperature_c: number;

  mean_solar_radiation_w_m2: number;
  maximum_solar_radiation_w_m2: number;

  exposure_eligible: boolean;
  beneficial: boolean;

  average_skin_improvement_c: number;
  final_skin_improvement_c: number;
  average_core_improvement_c: number;
  maximum_skin_improvement_c: number;

  weather_from_cache: boolean;
};


export type MonthlyAdaptationResult = {
  month: number;

  sampled_day_count: number;
  eligible_sample_count: number;

  total_weighted_days: number;
  evaluated_weighted_days: number;
  beneficial_weighted_days: number;

  exposure_coverage_percent: number;

  climate_adaptation_rate_percent:
    | number
    | null;

  average_skin_improvement_c:
    | number
    | null;

  average_core_improvement_c:
    | number
    | null;

  maximum_skin_improvement_c:
    | number
    | null;

  samples: DailyAdaptationResult[];

  representative_date_local?:
    | string
    | null;

  weight_days?:
    | number
    | null;

  final_skin_improvement_c?:
    | number
    | null;

  beneficial?:
    | boolean
    | null;
};


export type HeatwaveEvent = {
  start_date_local: string;
  end_date_local: string;

  duration_days: number;

  mean_maximum_air_temperature_c: number;
  peak_air_temperature_c: number;

  mean_skin_improvement_c: number;
  p90_skin_improvement_c: number;

  beneficial_day_count: number;
};


export type GlobalCityResult = {
  id: string;
  batch_id: string;
  celery_task_id: string | null;

  city_id: string;
  city_name: string;
  country: string;
  latitude: number;
  longitude: number;

  status: GlobalCityStatus;
  stage: string;
  progress: number;

  climate_adaptation_rate_percent:
    | number
    | null;

  exposure_coverage_percent:
    | number
    | null;

  annual_average_skin_improvement_c:
    | number
    | null;

  annual_average_core_improvement_c:
    | number
    | null;

  maximum_skin_improvement_c:
    | number
    | null;

  effective_cooling_hours:
    | number
    | null;

  sampled_day_count:
    | number
    | null;

  eligible_sample_count:
    | number
    | null;

  evaluated_weighted_days:
    | number
    | null;

  beneficial_weighted_days:
    | number
    | null;

  completed_month_count: number;

  last_checkpoint_month:
    | number
    | null;

  resumed_from_checkpoint: boolean;

  last_heartbeat_at:
    | string
    | null;

  skin_improvement_p50_c:
    | number
    | null;

  skin_improvement_p90_c:
    | number
    | null;

  skin_improvement_p95_c:
    | number
    | null;

  core_improvement_p50_c:
    | number
    | null;

  core_improvement_p90_c:
    | number
    | null;

  core_improvement_p95_c:
    | number
    | null;

  heatwave_event_count:
    | number
    | null;

  longest_heatwave_days:
    | number
    | null;

  heatwave_events:
    | HeatwaveEvent[]
    | null;

  retry_count: number;

  monthly_results:
    | MonthlyAdaptationResult[]
    | null;

  error_message: string | null;
  started_at: string | null;
  completed_at: string | null;
};


export type GlobalBatch = {
  id: string;
  celery_group_id: string | null;

  status: GlobalBatchStatus;
  stage: string;
  progress: number;

  total_city_count: number;
  completed_city_count: number;
  failed_city_count: number;
  cancelled_city_count: number;

  summary: Record<string, unknown> | null;
  error_message: string | null;

  created_at: string;
  updated_at: string;
  started_at: string | null;
  completed_at: string | null;
};


export type GlobalBatchDetail =
  GlobalBatch & {
    request: GlobalBatchCreate;
    city_results: GlobalCityResult[];
  };


export type GlobalBatchListResponse = {
  items: GlobalBatch[];
  total: number;
  limit: number;
  offset: number;
};


export type GlobalBatchEstimate = {
  city_count: number;
  month_count: number;

  samples_per_city: number;
  total_samples: number;

  thermal_simulation_count: number;
  estimated_weather_requests: number;

  analysis_resolution: AnalysisResolution;

  resolved_execution_profile:
    ExecutionProfile;

  resolved_queue: string;

  checkpoint_count_per_city: number;

  heatwave_analysis_available: boolean;
};


export type GeoJsonFeatureProperties = {
  city_id: string;
  city_name: string;
  country: string;

  status: string;

  climate_adaptation_rate_percent:
    | number
    | null;

  exposure_coverage_percent:
    | number
    | null;

  annual_average_skin_improvement_c:
    | number
    | null;

  annual_average_core_improvement_c:
    | number
    | null;

  maximum_skin_improvement_c:
    | number
    | null;

  effective_cooling_hours:
    | number
    | null;

  sampled_day_count:
    | number
    | null;

  eligible_sample_count:
    | number
    | null;

  evaluated_weighted_days:
    | number
    | null;

  beneficial_weighted_days:
    | number
    | null;

  skin_improvement_p50_c:
    | number
    | null;

  skin_improvement_p90_c:
    | number
    | null;

  skin_improvement_p95_c:
    | number
    | null;

  core_improvement_p50_c:
    | number
    | null;

  core_improvement_p90_c:
    | number
    | null;

  core_improvement_p95_c:
    | number
    | null;

  heatwave_event_count:
    | number
    | null;

  longest_heatwave_days:
    | number
    | null;
};


export type GeoJsonFeatureCollection = {
  type: "FeatureCollection";

  metadata: {
    batch_id?: string;
    status?: string;
    year?: number;
    method?: string;

    analysis_resolution?:
      AnalysisResolution;

    sample_days_per_month?: number;
    daily_stride_days?: number;

    execution_profile?:
      ExecutionProfile;

    heatwave_analysis_available?:
      boolean;

    [key: string]: unknown;
  };

  features: Array<{
    type: "Feature";

    geometry: {
      type: "Point";
      coordinates: [number, number];
    };

    properties: GeoJsonFeatureProperties;
  }>;
};