"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";

import { ConvergenceChart } from "@/components/optimization/convergence-chart";
import { RequirementMapChart } from "@/components/optimization/requirement-map-chart";
import { LeaseBadge } from "@/components/global/lease-badge";
import { cancelOptimization, getOptimization } from "@/lib/api-client";
import { formatNumber } from "@/lib/format";
import { METRIC_LABELS, TERMINAL_OPTIMIZATION, VARIABLE_LABELS } from "@/lib/optimization-labels";
import type {
  CandidateEvaluation, DecisionVariableName, MetricName, OptimizationJobDetail, OptimizationResult,
} from "@/types/optimization";

export default function OptimizationDetailPage() {
  const { optimizationId } = useParams<{ optimizationId: string }>();
  const [job, setJob] = useState<OptimizationJobDetail | null>(null);
  const [error, setError] = useState("");
  const [revision, setRevision] = useState(0);
  const [cancelling, setCancelling] = useState(false);

  useEffect(() => {
    let disposed = false;
    let timer: number | null = null;

    async function load() {
      try {
        const detail = await getOptimization(optimizationId);
        if (disposed) return;
        setJob(detail);
        setError("");
        if (!TERMINAL_OPTIMIZATION.has(detail.status)) timer = window.setTimeout(load, 3000);
      } catch (caught) {
        if (disposed) return;
        setError(caught instanceof Error ? caught.message : "Unable to load optimization");
        timer = window.setTimeout(load, 5000);
      }
    }

    void load();
    return () => {
      disposed = true;
      if (timer !== null) window.clearTimeout(timer);
    };
  }, [optimizationId, revision]);

  async function handleCancel() {
    setCancelling(true);
    try {
      await cancelOptimization(optimizationId);
      setRevision((r) => r + 1);
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Unable to cancel");
    } finally {
      setCancelling(false);
    }
  }

  if (!job) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        {error ? <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>
               : <p className="text-slate-400">Loading…</p>}
      </main>
    );
  }

  const metric = job.request.objective.metric;
  const result = job.result;
  const terminal = TERMINAL_OPTIMIZATION.has(job.status);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl space-y-8 px-6 py-10">
        <nav className="text-sm text-slate-400">
          <Link href="/optimizations" className="hover:text-white">Inverse Design</Link> / <span className="text-slate-200">{job.name}</span>
        </nav>

        <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-start justify-between gap-4">
            <div>
              <h1 className="text-2xl font-bold">{job.name}</h1>
              <p className="mt-1 text-sm text-slate-400">
                {job.city_id} · months {job.request.months.join(", ")} · {job.request.variables.length} variable(s) ·
                objective: {job.request.objective.sense} {METRIC_LABELS[metric]}
              </p>
            </div>
            <div className="flex items-center gap-4">
              <LeaseBadge leaseState={job.lease_state} leaseOwner={job.lease_owner}
                lastHeartbeatAt={job.last_heartbeat_at} leaseExpiresAt={job.lease_expires_at} />
              {!terminal && (
                <button type="button" onClick={handleCancel} disabled={cancelling || job.status === "cancelling"}
                  className="rounded-lg border border-red-800 px-4 py-2 text-red-300 disabled:opacity-50">
                  {job.status === "cancelling" ? "Cancel requested…" : "Cancel"}
                </button>
              )}
            </div>
          </div>
          <div className="mt-5 h-3 overflow-hidden rounded-full bg-slate-800">
            <div className="h-full bg-cyan-400 transition-all" style={{ width: `${job.progress}%` }} />
          </div>
          <p className="mt-2 text-sm text-slate-400">
            {job.status} · {job.stage} · {job.evaluation_count} evaluations · {job.progress}%
          </p>
          {job.error_message && <p className="mt-3 text-sm text-red-300">{job.error_message}</p>}
          {error && <p className="mt-3 text-sm text-red-300">{error}</p>}
        </section>

        {result && <VerdictCard result={result} />}
        {job.history.length > 0 && <ConvergenceChart history={job.history} metric={metric} />}
        {result && <CandidateTable result={result} metric={metric} />}
        {result?.requirement_map && <RequirementMapChart map={result.requirement_map} metric={metric} />}
        {result && (
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6 text-sm text-slate-400">
            <h2 className="text-lg font-semibold text-slate-200">Run record</h2>
            <p className="mt-2">
              {result.sample_count} sample day(s), {result.skipped_samples.length} skipped ·
              {" "}{result.evaluation_count} garment evaluations · {result.simulation_count} thermal simulations ·
              {" "}{result.generations} generations · {result.elapsed_seconds.toFixed(1)} s
            </p>
            <p className="mt-1 font-mono text-xs">
              model {result.model_version} · fingerprint {result.parameter_fingerprint.slice(0, 16)}… · {result.algorithm_message}
            </p>
          </section>
        )}
      </div>
    </main>
  );
}

function VerdictCard({ result }: { result: OptimizationResult }) {
  const tone = result.verdict === "infeasible"
    ? "border-red-800 bg-red-950/40 text-red-200"
    : "border-emerald-800 bg-emerald-950/40 text-emerald-200";
  const map = result.requirement_map;

  return (
    <section className={`rounded-2xl border p-6 ${tone}`}>
      <p className="text-sm uppercase tracking-wide opacity-70">Verdict</p>
      <p className="mt-1 text-3xl font-bold">{result.verdict.toUpperCase()}</p>
      <p className="mt-3 max-w-4xl">{result.message}</p>
      {map && (
        <div className="mt-5 grid gap-4 sm:grid-cols-2">
          <Requirement label={`Minimum ${VARIABLE_LABELS[map.x_variable]}`}
            value={map.minimum_x_at_max_y}
            note={`when ${VARIABLE_LABELS[map.y_variable]} = ${map.y_values.at(-1)?.toFixed(2)}`} />
          <Requirement label={`Minimum ${VARIABLE_LABELS[map.y_variable]}`}
            value={map.minimum_y_at_max_x}
            note={`when ${VARIABLE_LABELS[map.x_variable]} = ${map.x_values.at(-1)?.toFixed(2)}`} />
        </div>
      )}
    </section>
  );
}

function Requirement({ label, value, note }: { label: string; value: number | null; note: string }) {
  return (
    <div className="rounded-xl border border-slate-700 bg-slate-950/60 p-4">
      <p className="text-sm text-slate-400">{label}</p>
      <p className="mt-1 text-2xl font-semibold text-white">{value === null ? "not reachable" : `≥ ${value.toFixed(2)}`}</p>
      <p className="mt-1 text-xs text-slate-500">{note} (grid resolution limits precision)</p>
    </div>
  );
}

function CandidateTable({ result, metric }: { result: OptimizationResult; metric: MetricName }) {
  const columns: [string, CandidateEvaluation | null][] = [
    ["Baseline candidate", result.baseline],
    ["Best found", result.best],
    ["Optical upper bound", result.optical_upper_bound],
  ];
  const parameterNames = Object.keys(result.best.parameters) as DecisionVariableName[];
  const metricNames = Object.keys(METRIC_LABELS) as MetricName[];

  return (
    <section className="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">Candidates</h2>
      <table className="mt-4 w-full min-w-[48rem] text-left text-sm">
        <thead className="border-b border-slate-700 text-slate-400">
          <tr>
            <th className="px-3 py-2">Quantity</th>
            {columns.map(([label]) => <th key={label} className="px-3 py-2">{label}</th>)}
          </tr>
        </thead>
        <tbody>
          {parameterNames.map((name) => (
            <tr key={name} className="border-b border-slate-800">
              <td className="px-3 py-2 text-slate-300">{VARIABLE_LABELS[name]}</td>
              {columns.map(([label, c]) => <td key={label} className="px-3 py-2 font-mono">{formatNumber(c?.parameters[name], 3)}</td>)}
            </tr>
          ))}
          {metricNames.map((name) => (
            <tr key={name} className={`border-b border-slate-800 ${name === metric ? "bg-cyan-950/30" : ""}`}>
              <td className="px-3 py-2 text-slate-300">{METRIC_LABELS[name]}</td>
              {columns.map(([label, c]) => <td key={label} className="px-3 py-2">{formatNumber(c?.metrics?.[name], 3)}</td>)}
            </tr>
          ))}
          <tr>
            <td className="px-3 py-2 text-slate-300">Constraints satisfied</td>
            {columns.map(([label, c]) => (
              <td key={label} className={`px-3 py-2 ${c?.feasible ? "text-emerald-300" : "text-red-300"}`}>
                {c ? (c.feasible ? "yes" : `no (violation ${formatNumber(c.constraint_violation, 4)})`) : "—"}
              </td>
            ))}
          </tr>
        </tbody>
      </table>
    </section>
  );
}