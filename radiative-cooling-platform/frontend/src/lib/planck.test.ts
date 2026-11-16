import { describe, expect, it } from "vitest";

import { bandFraction, blackbodyFraction, broadbandEmissivity, outsideWindowEmissivity } from "@/lib/planck";

describe("planck", () => {
  it("matches tabulated fractions", () => {
    expect(blackbodyFraction(2898)).toBeCloseTo(0.2501, 3);
    expect(blackbodyFraction(5000)).toBeCloseTo(0.6337, 3);
  });

  it("puts about a third of 300 K emission in the window", () => {
    expect(bandFraction(300)).toBeGreaterThan(0.31);
    expect(bandFraction(300)).toBeLessThan(0.33);
  });

  it("round-trips the band split", () => {
    expect(outsideWindowEmissivity(broadbandEmissivity(0.9, 0.3), 0.9)).toBeCloseTo(0.3, 10);
  });
});