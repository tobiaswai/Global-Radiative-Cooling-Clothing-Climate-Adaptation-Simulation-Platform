# Stage 8 acceptance: observability, frontend reliability surface, resume benchmark

## Stage 7 defects fixed first (Step 0)
1. Beat schedule pointed at a non-existent task name -> reaper never ran.
2. `from fastapi import logger` -> AttributeError on the city failure path.
3. `/cancel` registered twice; the live one never set `cancel_requested_at`.
4. `BatchStatus` lacked `partial_completed`; `derive_batch_status` disagreed
   with `refresh_batch_status`.
5. `load_resume_state` assumed `start_month == 1`.

## New surface
- `GET  /global-batches/{id}`                      lease_state, checkpoint_months, attempt, cancel_requested_at
- `GET  /global-batches/{id}/events`               SSE: progress / terminal (lightweight snapshot)
- `GET  /global-batches/{id}/cities/{cid}/checkpoints`  durable checkpoints + resume_from_month
- `GET  /ops/status`                               broker, workers, lease summary, recovery bound
- Frontend: Reliability panel, lease badges, checkpoint timeline, data-quality
  panel, durable checkpoint list, batch list page, Operations page.

## Manual drills (record outputs in drills.md)
1. Start a 12-month batch for 3 cities. Confirm the batch page shows
   "Updates via server-sent events" and per-city cells turn green monthly.
2. `kill -9` the worker. Within TTL + reaper interval the city shows
   "Lease expired" then "Lease live" with a new owner and the "Resumed" tag;
   `resume_from_month` on the checkpoint endpoint equals last green cell + 1.
3. Stop the API's reverse proxy SSE support (or block /events): the page
   switches to "Updates via polling" without losing state.
4. Cancel a running batch: button turns into "Cancel requested - finishing
   current month"; no new checkpoint rows appear after the request timestamp.
5. Stop Redis: /ops shows "Broker unreachable", API still answers 200.
6. `RECORD_BENCHMARK=1 pytest tests/test_stage_8_resume_benchmark.py`
   -> resume-benchmark.json with resumed_equals_full == true.

## Known limitation carried from Stage 7
Months restored from a checkpoint have no `monthly_weather_payload_sha256`
entry (no weather is fetched for them). The checkpoint row's own
`payload_sha256` (exposed in Stage 8) is the reproducibility anchor instead.