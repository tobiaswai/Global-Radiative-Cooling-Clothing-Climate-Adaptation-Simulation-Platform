"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import { listOptimizations } from "@/lib/api-client";
import { TERMINAL_OPTIMIZATION } from "@/lib/optimization-labels";
import { formatRelativeTime } from "@/lib/relative-time";
import type { OptimizationJob } from "@/types/optimization";

export default function OptimizationListPage() {
  const [items, setItems] = useState<OptimizationJob[]>([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let disposed = false;
    let timer: number | null = null;

    async function load() {
      try {
        const response = await listOptimizations();
        if (disposed) return;
        setItems(response.items);
        setError("");
        if (response.items.some((job) => !TERMINAL_OPTIMIZATION.has(job.status))) {
          timer = window.setTimeout(load, 5000);
        }
      } catch (caught) {
        if (!disposed) setError(caught instanceof Error ? caught.message : "Unable to load optimizations");
      } finally {
        if (!disposed) setLoading(false);
      }
    }

    void load();
    return () => {
      disposed = true;
      if (timer !== null) window.clearTimeout(timer);
    };
  }, []);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <p className="text-sm text-cyan-400">Inverse Design</p>
            <h1 className="mt-2 text-3xl font-bold">Material Requirement Searches</h1>
          </div>
          <Link href="/optimizations/new" className="rounded-lg bg-cyan-400 px-5 py-2.5 font-semibold text-slate-950">
            New Search
          </Link>
        </header>

        {error && <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>}

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800">
          <table className="w-full text-left text-sm">
            <thead className="bg-slate-900 text-xs uppercase tracking-wide text-slate-500">
              <tr>
                <th className="px-5 py-4">Name</th>
                <th className="px-5 py-4">City</th>
                <th className="px-5 py-4">Status</th>
                <th className="px-5 py-4">Progress</th>
                <th className="px-5 py-4">Evaluations</th>
                <th className="px-5 py-4">Created</th>
              </tr>
            </thead>
            <tbody>
              {items.map((job) => (
                <tr key={job.id} className="border-t border-slate-800">
                  <td className="px-5 py-4">
                    <Link href={`/optimizations/${job.id}`} className="text-cyan-300 hover:underline">{job.name}</Link>
                    <p className="font-mono text-xs text-slate-500">{job.id.slice(0, 8)}</p>
                  </td>
                  <td className="px-5 py-4">{job.city_id}</td>
                  <td className="px-5 py-4">{job.status}</td>
                  <td className="px-5 py-4">{job.progress}%</td>
                  <td className="px-5 py-4">{job.evaluation_count}</td>
                  <td className="px-5 py-4 text-slate-400">{formatRelativeTime(job.created_at)}</td>
                </tr>
              ))}
            </tbody>
          </table>
          {loading && <div className="p-10 text-center text-slate-400">Loading…</div>}
          {!loading && items.length === 0 && <div className="p-10 text-center text-slate-400">No searches yet.</div>}
        </section>
      </div>
    </main>
  );
}