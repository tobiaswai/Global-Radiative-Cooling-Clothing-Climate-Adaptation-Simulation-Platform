# ADR 0004: material library references are resolved server-side and verified

Context: `MaterialInput.material_version_id` existed since Stage 2 but had no
effect; any client could claim a version while sending different numbers.

Decision (Stage 4, PR-4):
- Resolution happens once at the API boundary (`services/material_resolution`).
  Omitted physical fields are hydrated from the immutable version; supplied
  fields must match (rel/abs 1e-9) or the request fails with
  `MATERIAL_PARAMETER_CONFLICT`. Provenance fields are hydrated when omitted.
- The resolved request is what is persisted; workers never touch the library.
- `simulation_jobs` / `global_batch_jobs` record the version ids (FK, SET NULL)
  so a material version can list the simulations that used it.
- Every stored version must be a valid `MaterialInput`: write bounds and DB
  CHECK constraints now mirror the input schema.

Not changed: physics, `MODEL_PARAMETER_SET_VERSION` (3.0.0), golden fixture.