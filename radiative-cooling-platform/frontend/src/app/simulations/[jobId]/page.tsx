"use client";

import { useParams } from "next/navigation";
import { useState } from "react";

import { HeatFluxChart } from "@/components/charts/heat-flux-chart";
import { PhysiologyChart } from "@/components/charts/physiology-chart";
import { TemperatureChart } from "@/components/charts/temperature-chart";
import { WeatherChart } from "@/components/charts/weather-chart";
import { LeaseBadge } from "@/components/global/lease-badge";
import { ModelProvenancePanel } from "@/components/simulation/model-provenance-panel";
import { ModelQualityPanel } from "@/components/simulation/model-quality-panel";
import { WeatherQualityPanel } from "@/components/simulation/weather-quality-panel";
import { getSimulationExportUrl } from "@/lib/api-client";
import { isTerminalJobStatus, useSimulationJob } from "@/lib/use-simulation-job";

const stageLabels: Record<string, string> = {
  queued: "Waiting for computing resources",
  retry_scheduled: "Re-queued after a worker failure",
  initializing: "Initializing model",
  downloading_weather: "Downloading historical weather data",
  running_control_simulation: "Running control simulation",
  running_radiative_cooling_simulation: "Running radiative cooling simulation",
  generating_summary: "Generating summary",
  saving_result: "Saving result",
  completed: "Simulation completed",
  failed: "Simulation failed",
  cancelling: "Cancelling simulation",
  waiting_for_cooperative_cancel: "Waiting for cooperative cancel",
  cancelled: "Cancelled",
};

export default function SimulationJobPage() {
  const { jobId } = useParams<{ jobId: string }>();
  const { job, result, error, resultError, transport, cancel, retryResult } = useSimulationJob(jobId);
  const [cancelling, setCancelling] = useState(false);
  const [cancelError, setCancelError] = useState("");

  async function handleCancel() {
    if (cancelling) return;
    setCancelling(true);
    setCancelError("");
    try {
      await cancel();
    } catch (caught) {
      setCancelError(caught instanceof Error ? caught.message : "Failed to cancel simulation job");
    } finally {
      setCancelling(false);
    }
  }

  if (!job) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="mx-auto max-w-4xl">
          {error ? (
            <div role="alert" className="rounded-xl border border-red-900 bg-red-950 p-5 text-red-300">{error}</div>
          ) : (
            <p className="text-slate-400">Loading simulation job…</p>
          )}
        </div>
      </main>
    );
  }

  const isTerminal = isTerminalJobStatus(job.status);
  const progress = Math.min(100, Math.max(0, job.progress));

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex flex-wrap items-start justify-between gap-4">
          <div>
            <p className="text-sm font-medium text-cyan-400">Simulation Job</p>
            <h1 className="mt-2 text-3xl font-bold">Simulation Job</h1>
            <p className="mt-2 break-all text-sm text-slate-400">{job.id}</p>
          </div>
          <span className="rounded-full border border-slate-700 px-3 py-1 text-xs text-slate-300">
            Updates via {transport === "sse" ? "server-sent events" : transport === "polling" ? "polling" : "—"}
          </span>
        </header>

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p className="text-sm text-slate-400">Current Stage</p>
              <p className="mt-1 text-xl font-semibold">{stageLabels[job.stage] ?? job.stage}</p>
            </div>

            <div className="flex items-center gap-4">
              <LeaseBadge
                leaseState={job.lease_state}
                leaseOwner={job.lease_owner}
                lastHeartbeatAt={job.last_heartbeat_at}
                leaseExpiresAt={job.lease_expires_at}
              />
              {!isTerminal && (
                <button
                  type="button"
                  onClick={handleCancel}
                  disabled={cancelling || job.status === "cancelling"}
                  className="rounded-lg border border-red-800 px-4 py-2 text-red-300 transition hover:bg-red-950 disabled:cursor-not-allowed disabled:opacity-50"
                >
                  {job.status === "cancelling" ? "Cancel requested…" : cancelling ? "Cancelling…" : "Cancel Job"}
                </button>
              )}
            </div>
          </div>

          <div className="mt-6 h-3 overflow-hidden rounded-full bg-slate-800">
            <div className="h-full bg-cyan-400 transition-all duration-500" style={{ width: `${progress}%` }} />
          </div>
          <div className="mt-2 flex justify-between text-sm text-slate-400">
            <span>{job.status}{(job.attempt ?? 0) > 1 ? ` · attempt ${job.attempt}` : ""}</span>
            <span>{progress}%</span>
          </div>

          <dl className="mt-6 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
            <Field label="City" value={job.city_id} />
            <Field label="Created At" value={new Date(job.created_at).toLocaleString()} />
            <Field label="Started At" value={job.started_at ? new Date(job.started_at).toLocaleString() : "Not started"} />
            <Field label="Completed At" value={job.completed_at ? new Date(job.completed_at).toLocaleString() : "Not completed"} />
          </dl>

          {(job.control_material_version_id || job.rc_material_version_id) && (
            <dl className="mt-5 grid gap-4 text-sm sm:grid-cols-2">
              <Field label="Control material version" value={job.control_material_version_id ?? "manual values"} mono />
              <Field label="RC material version" value={job.rc_material_version_id ?? "manual values"} mono />
            </dl>
          )}

          {job.error_message && <Alert>{job.error_message}</Alert>}
          {error && <Alert>{error}</Alert>}
          {cancelError && <Alert>{cancelError}</Alert>}
        </section>

        {job.status === "completed" && !result && (
          <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
            {resultError ? (
              <div className="flex flex-wrap items-center justify-between gap-4">
                <p className="text-red-300">{resultError}</p>
                <button
                  type="button"
                  onClick={() => void retryResult()}
                  className="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-200 hover:bg-slate-800"
                >
                  Retry loading result
                </button>
              </div>
            ) : (
              <p className="text-slate-400">Loading complete simulation results…</p>
            )}
          </section>
        )}

        {result && (
          <section className="mt-10 space-y-8">
            <div className="grid gap-4 md:grid-cols-3">
              <SummaryCard label="final skin temperature improvement" value={result.summary.final_skin_temperature_improvement_c} />
              <SummaryCard label="average skin temperature improvement" value={result.summary.average_skin_temperature_improvement_c} hint={result.summary.averaging_method ?? undefined} />
              <SummaryCard label="final core temperature improvement" value={result.summary.final_core_temperature_improvement_c} />
            </div>

            <div className="rounded-xl border border-amber-800 bg-amber-950/50 p-4 text-amber-200">
              <p>{result.warning}</p>
              <p className="mt-2 text-sm">{result.environment_model_note}</p>
            </div>

            <WeatherChart weather={result.weather} />
            <WeatherQualityPanel weather={result.weather} />
            <TemperatureChart result={result} />
            <HeatFluxChart result={result} />
            <PhysiologyChart result={result} />
            <ModelQualityPanel result={result} />
            <ModelProvenancePanel result={result} />

            <div className="flex flex-wrap gap-3">
              <a href={getSimulationExportUrl(jobId, "csv")} className="rounded-lg bg-cyan-400 px-5 py-2 font-semibold text-slate-950">Export CSV</a>
              <a href={getSimulationExportUrl(jobId, "json")} className="rounded-lg border border-slate-700 px-5 py-2">Export JSON</a>
            </div>
          </section>
        )}
      </div>
    </main>
  );
}

function Field({ label, value, mono = false }: { label: string; value: string; mono?: boolean }) {
  return (
    <div>
      <dt className="text-slate-500">{label}</dt>
      <dd className={`mt-1 ${mono ? "font-mono text-xs text-slate-300" : ""}`}>{value}</dd>
    </div>
  );
}

function Alert({ children }: { children: React.ReactNode }) {
  return (
    <div role="alert" className="mt-5 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{children}</div>
  );
}

function SummaryCard({ label, value, hint }: { label: string; value: number; hint?: string }) {
  return (
    <article className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-sm text-slate-400">{label}</p>
      <p className="mt-2 text-3xl font-bold text-cyan-300">
        {value.toFixed(3)}<span className="ml-1 text-base font-normal">°C</span>
      </p>
      {hint && <p className="mt-1 font-mono text-xs text-slate-500">{hint}</p>}
    </article>
  );
}