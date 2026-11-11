"use client";

import { buildCheckpointCells, type CheckpointCellState } from "@/lib/checkpoint-cells";

type Props = {
  startMonth: number;
  endMonth: number;
  checkpointMonths: readonly number[];
  status: string;
  compact?: boolean;
};

const MONTHS = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"];

const cellStyles: Record<CheckpointCellState, string> = {
  checkpointed: "bg-emerald-500 text-slate-950",
  running: "bg-cyan-400 text-slate-950 animate-pulse",
  pending: "bg-slate-800 text-slate-500",
  outside: "bg-transparent text-slate-700 border border-dashed border-slate-800",
};

const cellTitles: Record<CheckpointCellState, string> = {
  checkpointed: "Checkpoint saved",
  running: "In progress",
  pending: "Not started",
  outside: "Outside requested range",
};

export function CheckpointTimeline({
  startMonth,
  endMonth,
  checkpointMonths,
  status,
  compact = false,
}: Props) {
  const cells = buildCheckpointCells(startMonth, endMonth, checkpointMonths, status);
  const size = compact ? "h-4 w-4 text-[10px]" : "h-7 w-7 text-xs";

  return (
    <div
      className="flex gap-0.5"
      role="img"
      aria-label={`${checkpointMonths.length} of ${endMonth - startMonth + 1} months checkpointed`}
    >
      {cells.map((cell) => (
        <span
          key={cell.month}
          title={`${cell.month}: ${cellTitles[cell.state]}`}
          className={`flex items-center justify-center rounded ${size} ${cellStyles[cell.state]}`}
        >
          {compact ? "" : MONTHS[cell.month - 1]}
        </span>
      ))}
    </div>
  );
}