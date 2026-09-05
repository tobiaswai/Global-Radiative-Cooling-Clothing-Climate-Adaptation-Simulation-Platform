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
  representative_day: number;
  local_start_hour: number;
  duration_minutes: number;
  output_interval_minutes: number;
  minimum_skin_improvement_c: number;
  person: PersonInput;
  control_material: MaterialInput;
  rc_material: MaterialInput;
};


export type MonthlyAdaptationResult = {
  month: number;
  representative_date_local: string;
  weight_days: number;
  average_skin_improvement_c: number;
  final_skin_improvement_c: number;
  average_core_improvement_c: number;
  maximum_skin_improvement_c: number;
  beneficial: boolean;
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

  evaluated_weighted_days:
    | number
    | null;

  beneficial_weighted_days:
    | number
    | null;

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


export type GeoJsonFeatureCollection = {
  type: "FeatureCollection";
  metadata: Record<string, unknown>;
  features: Array<{
    type: "Feature";
    geometry: {
      type: "Point";
      coordinates: [number, number];
    };
    properties: {
      city_id: string;
      city_name: string;
      country: string;
      status: string;
      climate_adaptation_rate_percent:
        number;
      annual_average_skin_improvement_c:
        number;
      annual_average_core_improvement_c:
        number;
      maximum_skin_improvement_c:
        number;
      effective_cooling_hours:
        number;
    };
  }>;
};