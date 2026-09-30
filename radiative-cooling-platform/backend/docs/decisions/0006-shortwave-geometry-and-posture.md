# ADR 0006: beam/diffuse split for body-incident shortwave; posture

Context: ERA5 supplies GHI, DNI, DHI. Stages 0-4 used GHI only and applied
the projected area factor f_p (a beam quantity) to it, which is geometrically
inconsistent. A_r/A_D was fixed at the standing value.

Decision (Stage 5):
- I_body = f_p * DNI + 0.5 f_eff F_sky DHI + 0.5 f_eff rho_g GHI
  (ASHRAE 55-2020 Appendix C geometry; measured DHI instead of 0.2 I_dir;
  sky view factor limits the sky-diffuse term; f_bes = 1).
- Fallback without DNI/DHI: I_body = f_p * GHI (legacy). Recorded in
  `assumptions_applied`. `EnvironmentInput` rejects a partial split.
- `EnvironmentAssumptions.ground_albedo` (0.2, assumed) feeds the reflected term.
- `PersonInput.position` in {standing, sitting} selects
  `effective_radiation_area_ratio_{standing,sitting}` (0.73 / 0.70) for both
  longwave exchange and the diffuse shortwave terms. The Gagge reference and
  library receive the same posture.

Not done (Stage 6): f_p as a function of solar altitude and posture
(ASHRAE 55 Table C-1; requires solar position from lat/lon/time, which the
weather series already carries); f_bes < 1 for partial shade; spectral
weighting of rho_sol / eps_IR from uploaded spectra.

MODEL_PARAMETER_SET_VERSION 3.0.0 -> 4.0.0; MODEL_VERSION 0.5.0 -> 0.6.0.