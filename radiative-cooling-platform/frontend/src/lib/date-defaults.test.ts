import { describe, expect, it } from "vitest";

import {
  getDefaultSimulationDateTime,
  getPreviousCompleteYear,
} from "@/lib/date-defaults";

describe("date defaults", () => {
  it("uses the previous calendar year", () => {
    expect(getPreviousCompleteYear(new Date("2026-03-01T00:00:00"))).toBe(2025);
  });

  it("builds a datetime-local string for 15 July 10:00", () => {
    expect(getDefaultSimulationDateTime(new Date("2026-03-01T00:00:00"))).toBe(
      "2025-07-15T10:00",
    );
  });

  it("rejects invalid dates", () => {
    expect(() => getPreviousCompleteYear(new Date("nope"))).toThrow();
  });
  it("matches the datetime-local value format exactly", () => {
    expect(getDefaultSimulationDateTime(new Date("2026-03-01T00:00:00"))).toMatch(
      /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/,
    );
  });
});