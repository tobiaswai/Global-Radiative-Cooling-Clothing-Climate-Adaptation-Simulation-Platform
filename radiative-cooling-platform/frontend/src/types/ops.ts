export type WorkerStatus = {
  name: string;
  active_task_count: number;
  reserved_task_count: number;
};

export type LeaseSummary = {
  running_cities: number;
  queued_cities: number;
  live_leases: number;
  expired_leases: number;
  running_batches: number;
  cancelling_batches: number;
};

export type OpsStatus = {
  checked_at: string;
  broker_reachable: boolean;
  worker_count: number;
  workers: WorkerStatus[];
  leases: LeaseSummary;
  lease_ttl_seconds: number;
  heartbeat_interval_seconds: number;
  reaper_interval_seconds: number;
  worst_case_recovery_seconds: number;
};