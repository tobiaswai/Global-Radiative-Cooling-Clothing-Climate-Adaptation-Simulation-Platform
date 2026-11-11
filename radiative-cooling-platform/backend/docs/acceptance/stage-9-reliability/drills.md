# Stage 9 reliability drills

Each drill is run against docker-compose with one API, one Celery worker on
`default,global_standard,global_large`, and beat. Record the raw command and
the observed values; a drill without a recorded value is not accepted.

| # | Drill | Expected | Observed (fill) |
|---|---|---|---|
| 1 | Submit a single job, `kill -9` the worker mid-run | within TTL + reaper interval (180 + 60 s) `/simulations/jobs/{id}` shows `lease_state: expired` then `queued`, then `running` with a new `lease_owner`; `attempt` == 2 | |
| 2 | Redeliver a completed job message (`celery call simulation.run_weather --args '["<id>"]'`) | task returns `{"status": "skipped", "reason": "lease_not_acquired"}`; row untouched | |
| 3 | Cancel a running single job | status `cancelling` -> `cancelled` within one heartbeat; no result file written | |
| 4 | 12-month, 3-city batch, `kill -9` the worker after month 4 | city shows `Lease expired` -> `Lease live` (new owner) with the `Resumed` tag; `/checkpoints` has `resume_from_month: 5`; all rows `provenance_matches_batch: true` | |
| 5 | Bump `MODEL_VERSION` locally, retry the batch from drill 4 | `/checkpoints` shows every row `not resumable`; `data_quality.checkpoints_discarded` lists 12 months; result recomputed from month 1 | |
| 6 | Retry with `resume_from_checkpoint: false` | checkpoint rows deleted before the worker starts; `resumed_from_checkpoint: false` | |
| 7 | Block `/events` at the reverse proxy | both pages switch to "Updates via polling" and stop polling at terminal status | |
| 8 | Stop Redis | `/ops/status` -> `broker_reachable: false`; `/simulations/run-weather` still 200 from cache | |
| 9 | `global_large` batch, force one city failure | re-queued task appears on `global_large`, not `global_standard` (`celery -A app.worker.celery_app inspect reserved`) | |