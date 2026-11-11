import { describe, expect, it } from "vitest";

import { buildCheckpointCells, monthsFromCheckpoint } from "@/lib/checkpoint-cells";

describe("buildCheckpointCells", () => {
  it("marks outside, checkpointed, running and pending months", () => {
    const cells = buildCheckpointCells(7, 12, [7, 8], "running");
    const states = cells.map((c) => c.state);

    expect(states.slice(0, 6)).toEqual(Array(6).fill("outside"));
    expect(states[6]).toBe("checkpointed");
    expect(states[7]).toBe("checkpointed");
    expect(states[8]).toBe("running");
    expect(states.slice(9)).toEqual(["pending", "pending", "pending"]);
  });

  it("never shows a running cell for a non-running city", () => {
    const cells = buildCheckpointCells(1, 12, [1, 2, 3], "failed");
    expect(cells.filter((c) => c.state === "running")).toHaveLength(0);
    expect(cells.filter((c) => c.state === "pending")).toHaveLength(9);
  });

  it("always returns twelve cells", () => {
    expect(buildCheckpointCells(3, 3, [], "queued")).toHaveLength(12);
  });
});

describe("monthsFromCheckpoint", () => {
  it("splits restored and computed months", () => {
    expect(monthsFromCheckpoint([1, 2, 3], true, 12)).toEqual({ restored: 3, computed: 9 });
    expect(monthsFromCheckpoint([1, 2, 3], false, 12)).toEqual({ restored: 0, computed: 12 });
  });
});