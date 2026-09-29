# ADR 0001: body_surface_area_m2 is currently informational

Finding (Stage 2): heat capacities are fixed per m² (245 + 35 kJ/(m²·K)), so
`PersonInput.body_surface_area_m2` has no effect on results. The lumped
value is also ~2× the Gagge two-node value for 70 kg / 1.8 m².

Decision: do not change in Stage 2 (would invalidate the golden case and the
Gagge benchmark simultaneously). Add `body_mass_kg` in Stage 3 and derive
C_core, C_skin = m·c_p·(1−α)/A_D, m·c_p·α/A_D with c_p = 3490 J/(kg·K),
α = 0.1 (Gagge 1986), validated against `benchmarks/gagge`.
Until then `test_body_surface_area_participates` is `xfail(strict=True)`.