import type { GlobalCityStatus } from "@/types/global-batch";

export type CheckpointCellState = "outside" | "checkpointed" | "running" | "pending";

export type CheckpointCell = {
  month: number;
  state: CheckpointCellState;
};

/**
 * Twelve cells, one per calendar month. Months outside [startMonth, endMonth]
 * are "outside"; months with a durable checkpoint are "checkpointed"; for a
 * running city the first missing month is "running"; the rest are "pending".
 */
export function buildCheckpointCells(
  startMonth: number,
  endMonth: number,
  checkpointMonths: readonly number[],
  status: GlobalCityStatus | string,
): CheckpointCell[] {
  const done = new Set(checkpointMonths);
  let runningAssigned = false;

  return Array.from({ length: 12 }, (_, index) => {
    const month = index + 1;

    if (month < startMonth || month > endMonth) {
      return { month, state: "outside" as const };
    }
    if (done.has(month)) {
      return { month, state: "checkpointed" as const };
    }
    if (status === "running" && !runningAssigned) {
      runningAssigned = true;
      return { month, state: "running" as const };
    }
    return { month, state: "pending" as const };
  });
}

export function monthsFromCheckpoint(
  checkpointMonths: readonly number[],
  resumedFromCheckpoint: boolean,
  completedMonthCount: number,
): { restored: number; computed: number } {
  if (!resumedFromCheckpoint) return { restored: 0, computed: completedMonthCount };
  const restored = Math.min(checkpointMonths.length, completedMonthCount);
  return { restored, computed: Math.max(0, completedMonthCount - restored) };
}