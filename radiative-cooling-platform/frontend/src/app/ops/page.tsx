"use client";

import { useEffect, useState } from "react";

import { getOpsStatus } from "@/lib/api-client";
import { formatRelativeTime } from "@/lib/relative-time";
import type { OpsStatus } from "@/types/ops";

const REFRESH_MS = 10000;

export default function OperationsPage() {
  const [status, setStatus] = useState<OpsStatus | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    let disposed = false;

    async function load() {
      try {
        const response = await getOpsStatus();
        if (!disposed) {
          setStatus(response);
          setError("");
        }
      } catch (caught) {
        if (!disposed) setError(caught instanceof Error ? caught.message : "Unable to load status.");
      }
    }

    void load();
    const timer = window.setInterval(load, REFRESH_MS);

    return () => {
      disposed = true;
      window.clearInterval(timer);
    };
  }, []);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-6xl px-6 py-10">
        <header>
          <p className="text-sm text-cyan-400">Operations</p>
          <h1 className="mt-2 text-3xl font-bold">Pipeline Health</h1>
          <p className="mt-3 max-w-3xl text-slate-400">
            Celery workers, lease state and recovery bounds for the global analysis pipeline.
            Refreshes every {REFRESH_MS / 1000} seconds.
          </p>
        </header>

        {error && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>
        )}

        {!status ? (
          <p className="mt-8 text-slate-400">Loading…</p>
        ) : (
          <>
            <section className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
              <Card
                label="Broker"
                value={status.broker_reachable ? "Reachable" : "Unreachable"}
                tone={status.broker_reachable ? "emerald" : "red"}
              />
              <Card
                label="Workers"
                value={String(status.worker_count)}
                tone={status.worker_count > 0 ? "emerald" : "red"}
              />
              <Card
                label="Expired leases"
                value={String(status.leases.expired_leases)}
                tone={status.leases.expired_leases > 0 ? "red" : "slate"}
              />
              <Card label="Live leases" value={String(status.leases.live_leases)} tone="cyan" />
              <Card label="Running cities" value={String(status.leases.running_cities)} />
              <Card label="Queued cities" value={String(status.leases.queued_cities)} />
              <Card label="Running batches" value={String(status.leases.running_batches)} />
              <Card
                label="Cancelling batches"
                value={String(status.leases.cancelling_batches)}
                tone={status.leases.cancelling_batches > 0 ? "amber" : "slate"}
              />
            </section>

            <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
              <h2 className="text-xl font-semibold">Recovery Bounds</h2>
              <dl className="mt-4 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
                <Pair label="Lease TTL" value={`${status.lease_ttl_seconds} s`} />
                <Pair label="Heartbeat interval" value={`${status.heartbeat_interval_seconds} s`} />
                <Pair label="Reaper interval" value={`${status.reaper_interval_seconds} s`} />
                <Pair
                  label="Worst-case recovery after kill -9"
                  value={`${status.worst_case_recovery_seconds} s`}
                />
              </dl>
              <p className="mt-4 text-xs text-slate-500">
                A city whose worker dies is re-queued no later than lease TTL + reaper interval
                after its last heartbeat, and resumes from its last durable monthly checkpoint.
              </p>
            </section>

            <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
              <div className="flex items-baseline justify-between">
                <h2 className="text-xl font-semibold">Workers</h2>
                <span className="text-xs text-slate-500">checked {formatRelativeTime(status.checked_at)}</span>
              </div>

              {status.workers.length === 0 ? (
                <p className="mt-4 text-sm text-red-300">
                  No worker answered the ping. Jobs will stay queued; expired leases will not be reaped
                  until a worker consuming the <span className="font-mono">default</span> queue is up.
                </p>
              ) : (
                <table className="mt-4 w-full text-left text-sm">
                  <thead className="border-b border-slate-700 text-slate-400">
                    <tr>
                      <th className="px-3 py-2">Worker</th>
                      <th className="px-3 py-2">Active</th>
                      <th className="px-3 py-2">Reserved</th>
                    </tr>
                  </thead>
                  <tbody>
                    {status.workers.map((worker) => (
                      <tr key={worker.name} className="border-b border-slate-800">
                        <td className="px-3 py-2 font-mono text-slate-200">{worker.name}</td>
                        <td className="px-3 py-2">{worker.active_task_count}</td>
                        <td className="px-3 py-2">{worker.reserved_task_count}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </section>
          </>
        )}
      </div>
    </main>
  );
}

function Card({
  label,
  value,
  tone = "slate",
}: {
  label: string;
  value: string;
  tone?: "slate" | "emerald" | "cyan" | "amber" | "red";
}) {
  const color = {
    slate: "text-slate-100",
    emerald: "text-emerald-300",
    cyan: "text-cyan-300",
    amber: "text-amber-300",
    red: "text-red-300",
  }[tone];

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-sm text-slate-400">{label}</p>
      <p className={`mt-2 text-2xl font-semibold ${color}`}>{value}</p>
    </div>
  );
}

function Pair({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-slate-500">{label}</dt>
      <dd className="mt-1 font-mono text-slate-200">{value}</dd>
    </div>
  );
}