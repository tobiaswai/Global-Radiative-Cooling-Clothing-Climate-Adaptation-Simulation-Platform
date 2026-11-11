"use client";

import { formatRelativeTime, heartbeatHealth, shortOwner } from "@/lib/relative-time";
import type { LeaseState } from "@/types/global-batch";

type Props = {
  leaseState: LeaseState | undefined;
  leaseOwner: string | null | undefined;
  lastHeartbeatAt: string | null | undefined;
  leaseExpiresAt?: string | null;
  heartbeatIntervalSeconds?: number;
};

const DEFAULT_HEARTBEAT_SECONDS = 30; // mirrors settings.CITY_HEARTBEAT_SECONDS

const styles: Record<string, string> = {
  healthy: "border-emerald-800 bg-emerald-950 text-emerald-300",
  stale: "border-amber-800 bg-amber-950 text-amber-300",
  expired: "border-red-800 bg-red-950 text-red-300",
  none: "border-slate-700 bg-slate-900 text-slate-400",
};

const labels: Record<string, string> = {
  healthy: "Lease live",
  stale: "Heartbeat stale",
  expired: "Lease expired",
  none: "No lease",
};

export function LeaseBadge({
  leaseState,
  leaseOwner,
  lastHeartbeatAt,
  leaseExpiresAt,
  heartbeatIntervalSeconds = DEFAULT_HEARTBEAT_SECONDS,
}: Props) {
  const health = heartbeatHealth(leaseState, lastHeartbeatAt, heartbeatIntervalSeconds);

  const title = [
    leaseOwner ? `Owner: ${leaseOwner}` : null,
    lastHeartbeatAt ? `Heartbeat: ${new Date(lastHeartbeatAt).toLocaleString()}` : null,
    leaseExpiresAt ? `Expires: ${new Date(leaseExpiresAt).toLocaleString()}` : null,
  ]
    .filter(Boolean)
    .join("\n");

  return (
    <div className="space-y-1" title={title}>
      <span
        className={`inline-flex rounded-full border px-2.5 py-1 text-xs font-medium ${styles[health]}`}
      >
        {labels[health]}
      </span>

      {health !== "none" && (
        <p className="text-xs text-slate-500">
          <span className="font-mono">{shortOwner(leaseOwner)}</span>
          {" · "}
          {formatRelativeTime(lastHeartbeatAt)}
        </p>
      )}
    </div>
  );
}