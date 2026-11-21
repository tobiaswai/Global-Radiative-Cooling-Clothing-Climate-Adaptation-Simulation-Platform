"use client";

import dynamic from "next/dynamic";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { Suspense, useEffect, useState } from "react";
import type { Data } from "plotly.js";

import { SelectField } from "@/components/forms/select-field";
import { getCities, getSurrogateModel, listSurrogateModels, predictSurrogate } from "@/lib/api-client";
import { formatNumber } from "@/lib/format";
import { METRIC_LABELS, VARIABLE_LABELS } from "@/lib/optimization-labels";
import type { DecisionVariableName, MetricName } from "@/types/optimization";
import type { City } from "@/types/simulation";
import type { SurrogateModel, SurrogateModelDetail, SurrogatePredictResponse } from "@/types/surrogate";

const Plot = dynamic(() => import("react-plotly.js"), { ssr: false });
const SWEEP_POINTS = 41;
const DEBOUNCE_MS = 300;

function linspace(lower: number, upper: number, count: number): number[] {
  return Array.from({ length: count }, (_, i) => lower + ((upper - lower) * i) / (count - 1));
}

export default function SurrogateSweepPage() {
  return (
    <Suspense fallback={<main className="min-h-screen bg-slate-950 p-10 text-slate-400">Loading…</main>}>
      <SweepContent />
    </Suspense>
  );
}

function SweepContent() {
  const requestedModel = useSearchParams().get("model");
  const [models, setModels] = useState<SurrogateModel[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(requestedModel);
  const [detail, setDetail] = useState<SurrogateModelDetail | null>(null);
  const [cities, setCities] = useState<City[]>([]);
  const [cityId, setCityId] = useState("");
  const [sampleDate, setSampleDate] = useState("");
  const [parameters, setParameters] = useState<Record<string, number>>({});
  const [sweepVariable, setSweepVariable] = useState("");
  const [target, setTarget] = useState<MetricName>("mean_skin_cooling_c");
  const [prediction, setPrediction] = useState<{ key: string; data: SurrogatePredictResponse } | null>(null);
  const [verification, setVerification] = useState<{ key: string; data: SurrogatePredictResponse } | null>(null);
  const [verifying, setVerifying] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    let disposed = false;
    Promise.all([listSurrogateModels(), getCities()])
      .then(([modelList, cityList]) => {
        if (disposed) return;
        const usable = modelList.items.filter((m) => m.status === "completed");
        setModels(usable);
        setCities(cityList);
        setSelectedId((current) => current ?? usable.find((m) => m.accepted)?.id ?? usable[0]?.id ?? null);
      })
      .catch((caught: unknown) => { if (!disposed) setError(caught instanceof Error ? caught.message : "Unable to load"); });
    return () => { disposed = true; };
  }, []);

  useEffect(() => {
    if (!selectedId) return;
    let disposed = false;
    getSurrogateModel(selectedId)
      .then((d) => {
        if (disposed) return;
        setDetail(d);
        setParameters(d.base_parameters);
        setCityId(d.training_cities[0] ?? "");
        const month = d.months.includes(7) ? 7 : d.months[0];
        setSampleDate(`${d.year}-${String(month).padStart(2, "0")}-15`);
        setSweepVariable(d.variables[0]?.name ?? "");
        setTarget(d.targets[0]);
      })
      .catch((caught: unknown) => { if (!disposed) setError(caught instanceof Error ? caught.message : "Unable to load model"); });
    return () => { disposed = true; };
  }, [selectedId]);

  const requestKey = detail && cityId && sampleDate
    ? JSON.stringify({ model: detail.id, cityId, sampleDate, parameters, sweepVariable })
    : "";
  const pointKey = detail ? JSON.stringify({ model: detail.id, cityId, sampleDate, parameters }) : "";

  useEffect(() => {
    if (!detail || !requestKey) return;
    let disposed = false;
    const timer = window.setTimeout(() => {
      const variable = detail.variables.find((v) => v.name === sweepVariable);
      const sweep = variable
        ? linspace(variable.lower, variable.upper, SWEEP_POINTS).map((x) => ({ ...parameters, [variable.name]: x }))
        : [];
      predictSurrogate({
        model_id: detail.id, city_id: cityId, sample_date: sampleDate,
        materials: [parameters, ...sweep], mode: "surrogate", physics_fallback: false,
      })
        .then((data) => { if (!disposed) { setPrediction({ key: requestKey, data }); setError(""); } })
        .catch((caught: unknown) => { if (!disposed) setError(caught instanceof Error ? caught.message : "Prediction failed"); });
    }, DEBOUNCE_MS);
    return () => { disposed = true; window.clearTimeout(timer); };
  }, [detail, cityId, sampleDate, parameters, sweepVariable, requestKey]);

  async function verify() {
    if (!detail) return;
    setVerifying(true);
    try {
      const data = await predictSurrogate({
        model_id: detail.id, city_id: cityId, sample_date: sampleDate,
        materials: [parameters], mode: "both", physics_fallback: true,
      });
      setVerification({ key: pointKey, data });
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Physics verification failed");
    } finally {
      setVerifying(false);
    }
  }

  const current = prediction?.key === requestKey ? prediction.data : null;
  const point = current?.predictions[0] ?? null;
  const sweep = current?.predictions.slice(1) ?? [];
  const checked = verification?.key === pointKey ? verification.data.predictions[0] : null;
  const quantiles = detail ? `${detail.training.lower_quantile * 100}–${detail.training.upper_quantile * 100} %` : "";

  const xs = sweep.map((p) => p.parameters[sweepVariable]);
  const value = (i: number) => sweep[i].surrogate?.[target];
  const outside = sweep.map((p, i) => ({ p, i })).filter(({ p }) => !p.within_domain);
  const chart: Data[] = [
    { x: xs, y: sweep.map((_, i) => value(i)?.upper ?? null), type: "scatter", mode: "lines",
      line: { width: 0 }, showlegend: false, hoverinfo: "skip" },
    { x: xs, y: sweep.map((_, i) => value(i)?.lower ?? null), type: "scatter", mode: "lines",
      line: { width: 0 }, fill: "tonexty", fillcolor: "rgba(34,211,238,0.2)", name: `${quantiles} interval` },
    { x: xs, y: sweep.map((_, i) => value(i)?.value ?? null), type: "scatter", mode: "lines",
      name: "Surrogate", line: { color: "#22d3ee", width: 3 } },
    { x: outside.map(({ p }) => p.parameters[sweepVariable]), y: outside.map(({ i }) => value(i)?.value ?? null),
      type: "scatter", mode: "markers", name: "Outside training domain",
      marker: { color: "#f59e0b", symbol: "x", size: 9 } },
    ...(point?.surrogate?.[target] ? [{
      x: [parameters[sweepVariable]], y: [point.surrogate[target]!.value], type: "scatter" as const,
      mode: "markers" as const, name: "Current design", marker: { color: "#f8fafc", size: 12 } }] : []),
    ...(checked?.physics?.[target] !== undefined ? [{
      x: [parameters[sweepVariable]], y: [checked.physics![target]!], type: "scatter" as const,
      mode: "markers" as const, name: "Physics (verified)", marker: { color: "#10b981", size: 12, symbol: "diamond" as const} }] : []),
  ];

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl space-y-6 px-6 py-10">
        <nav className="text-sm text-slate-400">
          <Link href="/surrogate" className="hover:text-white">Surrogate models</Link> / <span className="text-slate-200">Quick sweep</span>
        </nav>
        <h1 className="text-3xl font-bold">Quick Material Sweep</h1>
        <p className="max-w-4xl text-slate-400">
          Surrogate predictions are approximations. Use &quot;Verify with physics&quot; before reporting a design;
          conclusions are based on physics results (ADR 0011).
        </p>

        {error && <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>}
        {current?.warnings.map((w) => (
          <div key={w} className="rounded-lg border border-amber-800 bg-amber-950/40 p-3 text-sm text-amber-200">{w}</div>
        ))}

        <section className="grid gap-5 rounded-2xl border border-slate-800 bg-slate-900 p-6 md:grid-cols-2 lg:grid-cols-4">
          <SelectField label="Model" value={selectedId ?? ""}
            options={models.map((m) => ({ value: m.id, label: `${m.name}${m.accepted ? "" : " (rejected)"}${m.stale ? " (stale)" : ""}` }))}
            onChange={setSelectedId} />
          <SelectField label="City" value={cityId}
            options={cities.map((c) => ({ value: c.id, label: `${c.name}${detail?.training_cities.includes(c.id) ? " · trained" : ""}` }))}
            onChange={setCityId} />
          <label className="block">
            <span className="mb-2 block text-sm text-slate-300">Date</span>
            <input type="date" value={sampleDate} onChange={(e) => setSampleDate(e.target.value)}
              className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2" />
          </label>
          {detail && (
            <SelectField<MetricName> label="Target" value={target}
              options={detail.targets.map((t) => ({ value: t, label: METRIC_LABELS[t] }))} onChange={setTarget} />
          )}
        </section>

        {detail && (
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Design</h2>
            <p className="mt-1 text-sm text-slate-400">
              Context fixed by the model: start {detail.local_start_hour}:00, {detail.duration_minutes} min exposure.
            </p>
            <div className="mt-5 grid gap-6 md:grid-cols-2">
              {detail.variables.map((v) => (
                <label key={v.name} className="block">
                  <span className="flex justify-between text-sm text-slate-300">
                    <span>{VARIABLE_LABELS[v.name as DecisionVariableName] ?? v.name}</span>
                    <span className="font-mono text-cyan-300">{formatNumber(parameters[v.name], 3)}</span>
                  </span>
                  <input type="range" min={v.lower} max={v.upper} step={(v.upper - v.lower) / 200}
                    value={parameters[v.name] ?? v.lower}
                    onChange={(e) => setParameters((p) => ({ ...p, [v.name]: Number(e.target.value) }))}
                    className="mt-2 w-full accent-cyan-400" />
                  <span className="mt-1 flex items-center gap-2 text-xs text-slate-500">
                    <input type="radio" name="sweep" checked={sweepVariable === v.name}
                      onChange={() => setSweepVariable(v.name)} className="accent-cyan-400" />
                    sweep this variable
                  </span>
                </label>
              ))}
            </div>
          </section>
        )}

        {point && detail && (
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <div className="flex flex-wrap items-center justify-between gap-4">
              <h2 className="text-xl font-semibold">Current design</h2>
              <div className="flex items-center gap-3 text-xs">
                <span className={`rounded-full px-2.5 py-1 ${point.within_domain ? "bg-emerald-950 text-emerald-300" : "bg-amber-950 text-amber-300"}`}>
                  {point.within_domain ? "inside training domain" : `outside domain: ${point.out_of_domain_features.join(", ")}`}
                </span>
                <span className="rounded-full bg-slate-800 px-2.5 py-1 text-slate-300">source: {point.source}</span>
                <span className="text-slate-500">{current?.elapsed_ms.toFixed(0)} ms</span>
                <button type="button" onClick={verify} disabled={verifying}
                  className="rounded-lg border border-emerald-700 px-3 py-1.5 text-emerald-300 disabled:opacity-50">
                  {verifying ? "Running physics…" : "Verify with physics"}
                </button>
              </div>
            </div>
            <table className="mt-4 w-full text-left text-sm">
              <thead className="border-b border-slate-700 text-slate-400">
                <tr><th className="px-3 py-2">Metric</th><th className="px-3 py-2">Surrogate</th>
                  <th className="px-3 py-2">{quantiles} interval</th><th className="px-3 py-2">Physics</th></tr>
              </thead>
              <tbody>
                {detail.targets.map((t) => {
                  const s = point.surrogate?.[t];
                  const physics = checked?.physics?.[t];
                  return (
                    <tr key={t} className="border-b border-slate-800">
                      <td className="px-3 py-2 text-slate-300">{METRIC_LABELS[t]}</td>
                      <td className="px-3 py-2 font-mono text-cyan-300">{formatNumber(s?.value, 4)}</td>
                      <td className="px-3 py-2 font-mono text-slate-400">{s ? `${s.lower.toFixed(4)} – ${s.upper.toFixed(4)}` : "—"}</td>
                      <td className="px-3 py-2 font-mono text-emerald-300">
                        {formatNumber(physics, 4)}
                        {s && physics !== undefined && (physics < s.lower || physics > s.upper) && (
                          <span className="ml-2 text-amber-300">outside interval</span>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </section>
        )}

        {sweep.length > 0 && detail && (
          <section className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
            <h2 className="mb-4 text-xl font-semibold">
              {METRIC_LABELS[target]} vs {VARIABLE_LABELS[sweepVariable as DecisionVariableName] ?? sweepVariable}
            </h2>
            <Plot data={chart}
              layout={{
                autosize: true, height: 420, paper_bgcolor: "#0f172a", plot_bgcolor: "#0f172a",
                font: { color: "#cbd5e1" }, margin: { l: 65, r: 30, t: 20, b: 55 },
                xaxis: { title: { text: VARIABLE_LABELS[sweepVariable as DecisionVariableName] ?? sweepVariable }, gridcolor: "#334155" },
                yaxis: { title: { text: METRIC_LABELS[target] }, gridcolor: "#334155" },
                legend: { orientation: "h", y: -0.25 }, hovermode: "x unified",
              }}
              config={{ responsive: true, displaylogo: false }} useResizeHandler style={{ width: "100%", height: "100%" }} />
          </section>
        )}
      </div>
    </main>
  );
}