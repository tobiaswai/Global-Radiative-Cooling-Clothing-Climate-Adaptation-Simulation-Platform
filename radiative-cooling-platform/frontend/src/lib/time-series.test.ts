import { describe, expect, it } from "vitest";

import { hasOptionalSeries, pluckOptionalSeries } from "@/lib/time-series";
import type { TimeSeriesPoint } from "@/types/simulation";

function point(overrides: Partial<TimeSeriesPoint> = {}): TimeSeriesPoint {
  return {
    minute: 0,
    core_temperature_c: 36.8,
    skin_temperature_c: 33.7,
    convection_w_m2: 0,
    longwave_radiation_w_m2: 0,
    evaporation_w_m2: 0,
    absorbed_solar_w_m2: 0,
    core_to_skin_w_m2: 0,
    ...overrides,
  };
}

describe("hasOptionalSeries", () => {
  it("is false when every value is absent or null", () => {
    const points = [point(), point({ skin_wettedness: null })];
    expect(hasOptionalSeries(points, "skin_wettedness")).toBe(false);
  });

  it("is true when at least one numeric value exists", () => {
    const points = [point(), point({ skin_wettedness: 0.2 })];
    expect(hasOptionalSeries(points, "skin_wettedness")).toBe(true);
  });
});

describe("pluckOptionalSeries", () => {
  it("maps missing and non-finite values to null", () => {
    const points = [
      point({ clothing_surface_temperature_c: 35.1 }),
      point({ clothing_surface_temperature_c: null }),
      point(),
      point({ clothing_surface_temperature_c: Number.NaN }),
    ];

    expect(
      pluckOptionalSeries(points, "clothing_surface_temperature_c"),
    ).toEqual([35.1, null, null, null]);
  });
});