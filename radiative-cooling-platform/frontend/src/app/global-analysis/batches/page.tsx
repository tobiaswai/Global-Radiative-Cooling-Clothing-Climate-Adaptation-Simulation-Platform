"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import { listGlobalBatches } from "@/lib/api-client";
import { isTerminalBatchStatus } from "@/lib/global-batch-progress";
import { formatRelativeTime } from "@/lib/relative-time";
import type { GlobalBatch } from "@/types/global-batch";

const PAGE_SIZE = 20;
const REFRESH_MS = 10000;

export default function GlobalBatchListPage() {
  const [items, setItems] = useState<GlobalBatch[]>([]);
  const [total, setTotal] = useState(0);
  const [offset, setOffset] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let disposed = false;
    let timer: number | null = null;

    async function load() {
      try {
        const response = await listGlobalBatches(PAGE_SIZE, offset);
        if (disposed) return;
        setItems(response.items);
        setTotal(response.total);
        setError("");
        // Keep refreshing while anything on this page is still running.
        if (response.items.some((batch) => !isTerminalBatchStatus(batch.status))) {
          timer = window.setTimeout(load, REFRESH_MS);
        }
      } catch (caught) {
        if (!disposed) setError(caught instanceof Error ? caught.message : "Unable to load batches.");
      } finally {
        if (!disposed) setLoading(false);
      }
    }

    void load();

    return () => {
      disposed = true;
      if (timer !== null) window.clearTimeout(timer);
    };
  }, [offset]);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <p className="text-sm text-cyan-400">Global Analysis</p>
            <h1 className="mt-2 text-3xl font-bold">Analysis Batches</h1>
          </div>
          <Link
            href="/global-analysis"
            className="rounded-lg bg-cyan-400 px-5 py-2.5 font-semibold text-slate-950"
          >
            New Batch
          </Link>
        </header>

        {error && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>
        )}

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800">
          <table className="w-full text-left text-sm">
            <thead className="bg-slate-900 text-xs uppercase tracking-wide text-slate-500">
              <tr>
                <th className="px-5 py-4">Batch</th>
                <th className="px-5 py-4">Status</th>
                <th className="px-5 py-4">Progress</th>
                <th className="px-5 py-4">Cities</th>
                <th className="px-5 py-4">Attempt</th>
                <th className="px-5 py-4">Created</th>
                <th className="px-5 py-4">Updated</th>
              </tr>
            </thead>
            <tbody>
              {items.map((batch) => (
                <tr key={batch.id} className="border-t border-slate-800 bg-slate-950">
                  <td className="px-5 py-4">
                    <Link
                      href={`/global-analysis/${batch.id}`}
                      className="font-mono text-cyan-300 hover:underline"
                    >
                      {batch.id.slice(0, 8)}
                    </Link>
                    {batch.cancel_requested_at && (
                      <p className="mt-1 text-xs text-amber-300">cancel requested</p>
                    )}
                  </td>
                  <td className="px-5 py-4">
                    <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusClass(batch.status)}`}>
                      {batch.status.replace("_", " ")}
                    </span>
                  </td>
                  <td className="px-5 py-4">
                    <div className="h-2 w-32 overflow-hidden rounded-full bg-slate-800">
                      <div className="h-full bg-cyan-400" style={{ width: `${batch.progress}%` }} />
                    </div>
                    <p className="mt-1 text-xs text-slate-500">{batch.progress}%</p>
                  </td>
                  <td className="px-5 py-4 text-slate-300">
                    {batch.completed_city_count} / {batch.total_city_count}
                    {batch.failed_city_count > 0 && (
                      <span className="ml-2 text-red-300">{batch.failed_city_count} failed</span>
                    )}
                  </td>
                  <td className="px-5 py-4">{batch.attempt ?? 0}</td>
                  <td className="px-5 py-4 text-slate-400">{formatRelativeTime(batch.created_at)}</td>
                  <td className="px-5 py-4 text-slate-400">{formatRelativeTime(batch.updated_at)}</td>
                </tr>
              ))}
            </tbody>
          </table>

          {loading && <div className="p-10 text-center text-slate-400">Loading…</div>}
          {!loading && items.length === 0 && (
            <div className="p-10 text-center text-slate-400">No batches yet.</div>
          )}
        </section>

        <div className="mt-6 flex items-center justify-between text-sm text-slate-400">
          <span>
            {total === 0 ? "0" : `${offset + 1}–${Math.min(offset + PAGE_SIZE, total)}`} of {total}
          </span>
          <div className="flex gap-3">
            <button
              type="button"
              disabled={offset === 0}
              onClick={() => setOffset(Math.max(0, offset - PAGE_SIZE))}
              className="rounded-lg border border-slate-700 px-4 py-2 disabled:cursor-not-allowed disabled:opacity-50"
            >
              Previous
            </button>
            <button
              type="button"
              disabled={offset + PAGE_SIZE >= total}
              onClick={() => setOffset(offset + PAGE_SIZE)}
              className="rounded-lg border border-slate-700 px-4 py-2 disabled:cursor-not-allowed disabled:opacity-50"
            >
              Next
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}

function statusClass(status: string): string {
  switch (status) {
    case "completed":
      return "bg-emerald-950 text-emerald-300";
    case "partial_completed":
      return "bg-amber-950 text-amber-300";
    case "running":
      return "bg-cyan-950 text-cyan-300";
    case "cancelling":
      return "bg-amber-950 text-amber-300";
    case "failed":
      return "bg-red-950 text-red-300";
    case "cancelled":
      return "bg-slate-800 text-slate-300";
    default:
      return "bg-slate-800 text-slate-300";
  }
}