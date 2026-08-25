"use client";

import Link from "next/link";
import {
  useEffect,
  useState,
} from "react";

import {
  getSimulationJobs,
} from "@/lib/api-client";
import type {
  SimulationJob,
} from "@/types/simulation";


export default function SimulationJobsPage() {
  const [jobs, setJobs] =
    useState<SimulationJob[]>([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {
    async function loadJobs() {
      try {
        const response =
          await getSimulationJobs();

        setJobs(response.items);
      } finally {
        setLoading(false);
      }
    }

    void loadJobs();

    const timer = window.setInterval(
      loadJobs,
      5000,
    );

    return () => {
      window.clearInterval(timer);
    };
  }, []);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex items-center justify-between">
          <div>
            <p className="text-sm text-cyan-400">
              Simulation Jobs
            </p>

            <h1 className="mt-2 text-3xl font-bold">
              Simulation Jobs
            </h1>
          </div>

          <Link
            href="/simulations/weather"
            className="rounded-lg bg-cyan-400 px-5 py-2.5 font-semibold text-slate-950"
          >
            New Simulation
          </Link>
        </header>

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800">
          <table className="w-full text-left">
            <thead className="bg-slate-900 text-sm text-slate-400">
              <tr>
                <th className="px-5 py-4">
                  Job
                </th>
                <th className="px-5 py-4">
                  City
                </th>
                <th className="px-5 py-4">
                  Status
                </th>
                <th className="px-5 py-4">
                  Progress
                </th>
                <th className="px-5 py-4">
                  Created At
                </th>
              </tr>
            </thead>

            <tbody>
              {jobs.map((job) => (
                <tr
                  key={job.id}
                  className="border-t border-slate-800"
                >
                  <td className="px-5 py-4">
                    <Link
                      href={`/simulations/${job.id}`}
                      className="font-medium text-cyan-300 hover:underline"
                    >
                      {job.id.slice(0, 8)}
                    </Link>
                  </td>

                  <td className="px-5 py-4">
                    {job.city_id}
                  </td>

                  <td className="px-5 py-4">
                    <StatusBadge
                      status={job.status}
                    />
                  </td>

                  <td className="px-5 py-4">
                    {job.progress}%
                  </td>

                  <td className="px-5 py-4 text-sm text-slate-400">
                    {new Date(
                      job.created_at,
                    ).toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {loading && (
            <div className="p-10 text-center text-slate-400">
              Loading…
            </div>
          )}
        </section>
      </div>
    </main>
  );
}


function StatusBadge({
  status,
}: {
  status: string;
}) {
  const colors: Record<string, string> = {
    completed:
      "bg-emerald-950 text-emerald-300",
    running:
      "bg-cyan-950 text-cyan-300",
    queued:
      "bg-amber-950 text-amber-300",
    failed:
      "bg-red-950 text-red-300",
    cancelled:
      "bg-slate-800 text-slate-300",
  };

  return (
    <span
      className={`rounded-full px-3 py-1 text-xs font-medium ${
        colors[status]
        ?? "bg-slate-800 text-slate-300"
      }`}
    >
      {status}
    </span>
  );
}