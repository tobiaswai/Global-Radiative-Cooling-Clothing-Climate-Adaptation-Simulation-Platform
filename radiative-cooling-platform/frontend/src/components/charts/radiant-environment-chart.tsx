"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import { hasOptionalSeries, pluckOptionalSeries } from "@/lib/time-series";
import type { SimulationResponse } from "@/types/simulation";

const Plot = dynamic(() => import("react-plotly.js"), { ssr: false });

/** Longwave boundary temperatures actually used, plus clothing surfaces (Stage 11). */
export function RadiantEnvironmentChart({ result }: { result: SimulationResponse }) {
  const rc = result.radiative_cooling.time_series;
  const control = result.control.time_series;
  if (!hasOptionalSeries(rc, "sky_temperature_c")) return null;

  const minutes = rc.map((p) => p.minute);
  const data: Data[] = [
    { x: minutes, y: pluckOptionalSeries(rc, "sky_temperature_c"), type: "scatter", mode: "lines",
      name: "Sky (effective)", line: { color: "#60a5fa", width: 3 } },
    { x: minutes, y: pluckOptionalSeries(rc, "surround_temperature_c"), type: "scatter", mode: "lines",
      name: "Non-sky surroundings", line: { color: "#f97316", width: 3 } },
    { x: control.map((p) => p.minute), y: pluckOptionalSeries(control, "clothing_surface_temperature_c"),
      type: "scatter", mode: "lines", name: "Control clothing surface", line: { color: "#fdba74", dash: "dot" } },
    { x: minutes, y: pluckOptionalSeries(rc, "clothing_surface_temperature_c"),
      type: "scatter", mode: "lines", name: "RC clothing surface", line: { color: "#67e8f9", dash: "dot" } },
  ];

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">Radiant Environment</h2>
      <Plot
        data={data}
        layout={{
          autosize: true, height: 380, paper_bgcolor: "#0f172a", plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" }, margin: { l: 65, r: 30, t: 20, b: 55 },
          xaxis: { title: { text: "Time (min)" }, gridcolor: "#334155" },
          yaxis: { title: { text: "Temperature (°C)" }, gridcolor: "#334155" },
          legend: { orientation: "h", y: -0.25 }, hovermode: "x unified",
        }}
        config={{ responsive: true, displaylogo: false }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />
      <p className="mt-2 text-sm text-slate-400">
        A garment surface below the surroundings temperature gains longwave heat from them; a low
        emissivity then helps. Whether that happens depends on how the surroundings are modelled.
      </p>
    </div>
  );
}