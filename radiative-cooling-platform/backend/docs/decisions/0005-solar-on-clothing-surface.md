# ADR 0005: absorbed solar enters the clothing surface balance

Context: since Stage 0 the solar radiation absorbed by the textile was
deposited on the skin node scaled by `absorbed_solar_to_body_fraction` (0.35,
`assumed`). ADR 0003 deferred moving it to the surface to Stage 4; Stage 4
did not do it.

Decision (Stage 5):
- The surface balance gains a source term:
  (T_sk - T_cl)/R_cl + S_abs = f_cl [h_c (T_cl - T_a) + (A_r/A_D) eps sigma (T_cl^4 - T_env^4)],
  S_abs = alpha_sol * I_body per unit A_D. The residual stays strictly
  decreasing and concave, so the Newton solver is unchanged.
- Solar transmitted through the textile (tau_sol * I_body) is deposited on
  the skin node (skin shortwave reflectance neglected; first-order).
- `TimeSeriesPoint.absorbed_solar_w_m2` now means "solar entering the
  clothing-body system" (= S_abs + S_trans). The skin storage equation keeps
  its form, so the energy diagnostics are unchanged.
- `absorbed_solar_to_body_fraction` is DEPRECATED: kept in MaterialInput,
  MaterialVersionCreate and the DB column so stored requests and versions
  keep loading; removed from MATERIAL_PHYSICAL_FIELD_ORDER, the field
  manifest, the participation test and library-conflict verification.
  Provenance keys naming it are still accepted.

Consequence: the share of absorbed solar that reaches the skin is now an
outcome (higher with low wind and dark textiles, lower with high wind), not a
fixed 35 %. Removes one `assumed` model input.