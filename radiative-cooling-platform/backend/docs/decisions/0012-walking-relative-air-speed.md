# ADR 0012: walking speed enters the relative air speed

## Context
The project brief asks for street-walking scenarios (e.g. two hours in Dubai).
Until Stage 12 only `met` described activity; the body saw the ambient wind only,
although walking at 1.1 m/s in still air roughly triples h_c relative to 3.1 W/(m^2 K).

## Decision
- `PersonInput.walking_speed_m_s` (default 0, <= 2.5 m/s).
- Relative air speed v_rel = sqrt(v_wind^2 + v_walk^2): the RMS relative speed for a
  walking direction uniformly distributed against the wind. It replaces the wind in
  h_c, Re,a (through h_c) and w_max. The ground balance keeps the ambient wind.
- Activity presets (standing, slow/moderate/brisk walk) set met and walking speed
  together; values from ISO 8996:2004 Annex B (to be verified against the standard).
- Zero walking returns the wind speed exactly, so existing results are bit-identical.

## Consequences
- MODEL_VERSION 0.11.0; parameter registry unchanged (6.0.0 after the Stage 13 version fix).
- Checkpoints of earlier versions are not resumable (model_version differs).
- Must precede the surrogate dataset (ADR 0011).

## Limitations
- Clothing pumping (reduced insulation and evaporative resistance when walking),
  body-segment swing and solar-geometry changes with heading are not modelled.
- A fixed heading against the wind would give |v_wind - v_walk|; the RMS form is a
  direction-averaged approximation.