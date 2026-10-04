"use client";

import { LeaseBadge } from "@/components/global/lease-badge";
import type { BatchTransport } from "@/lib/use-global-batch";
import { formatRelativeTime } from "@/lib/relative-time";
import type { GlobalBatchDetail } from "@/types/global-batch";

type Props = {
  batch: GlobalBatchDetail;
  transport: BatchTransport;
};

export function BatchReliabilityPanel({ batch, transport }: Props) {
  const cities = batch.city_results;
  const live = cities.filter((c) => c.lease_state === "live").length;
  const expired = cities.filter((c) => c.lease_state === "expired").length;
  const resumed = cities.filter((c) => c.resumed_from_checkpoint).length;
  const retries = cities.reduce((sum, c) => sum + (c.retry_count ?? 0), 0);
  const checkpoints = cities.reduce((sum, c) => sum + (c.checkpoint_months?.length ?? 0), 0);

  return (
    <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-5">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <h2 className="text-xl font-semibold">Reliability</h2>
          <p className="mt-1 text-sm text-slate-400">
            Worker leases, heartbeats and durable monthly checkpoints (Stage 7).
          </p>
        </div>

        <span className="rounded-full border border-slate-700 px-3 py-1 text-xs text-slate-300">
          Updates via {transport === "sse" ? "server-sent events" : transport === "polling" ? "polling" : "—"}
        </span>
      </div>

      <dl className="mt-5 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-7">
        <Item label="Batch attempt" value={String(batch.attempt ?? 0)} />
        <Item label="Live leases" value={String(live)} tone={live > 0 ? "cyan" : undefined} />
        <Item label="Expired leases" value={String(expired)} tone={expired > 0 ? "red" : undefined} />
        <Item label="Cities resumed" value={String(resumed)} />
        <Item label="City retries" value={String(retries)} tone={retries > 0 ? "amber" : undefined} />
        <Item label="Checkpoints stored" value={String(checkpoints)} />
        <Item
          label="Cancel requested"
          value={batch.cancel_requested_at ? formatRelativeTime(batch.cancel_requested_at) : "No"}
          tone={batch.cancel_requested_at ? "amber" : undefined}
        />
      </dl>

      {expired > 0 && (
        <p className="mt-4 rounded-lg border border-red-900 bg-red-950/50 p-3 text-sm text-red-300">
          {expired} city lease(s) have expired. The lease reaper re-queues them within one
          reaper interval; if this persists, check <a href="/ops" className="underline">Operations</a>.
        </p>
      )}

      {batch.lease_owner && (
        <div className="mt-4">
          <LeaseBadge
            leaseState={batch.lease_expires_at && new Date(batch.lease_expires_at) > new Date() ? "live" : "expired"}
            leaseOwner={batch.lease_owner}
            lastHeartbeatAt={batch.last_heartbeat_at}
            leaseExpiresAt={batch.lease_expires_at}
          />
        </div>
      )}
    </section>
  );
}

function Item({ label, value, tone }: { label: string; value: string; tone?: "cyan" | "amber" | "red" }) {
  const color =
    tone === "red" ? "text-red-300" : tone === "amber" ? "text-amber-300" : tone === "cyan" ? "text-cyan-300" : "text-slate-100";
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950 p-4">
      <dt className="text-xs uppercase tracking-wide text-slate-500">{label}</dt>
      <dd className={`mt-2 text-lg font-semibold ${color}`}>{value}</dd>
    </div>
  );
}