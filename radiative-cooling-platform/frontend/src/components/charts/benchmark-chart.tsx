"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import type { BenchmarkSeriesPoint } from "@/types/benchmark";

const Plot = dynamic(() => import("react-plotly.js"), {
  ssr: false,
  loading: () => (
    <div className="flex h-96 items-center justify-center text-slate-400">
      Loading chart...
    </div>
  ),
});

type BenchmarkChartProps = {
  points: BenchmarkSeriesPoint[];
  referenceLabel: string;
};

export function BenchmarkChart({ points, referenceLabel }: BenchmarkChartProps) {
  const minutes = points.map((point) => point.minute);

  const data: Data[] = [
    {
      x: minutes,
      y: points.map((point) => point.prototype_core_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Prototype: Core",
      line: { color: "#ef4444", width: 3 },
    },
    {
      x: minutes,
      y: points.map((point) => point.reference_core_temperature_c),
      type: "scatter",
      mode: "lines",
      name: `${referenceLabel}: Core`,
      line: { color: "#fca5a5", width: 2, dash: "dash" },
    },
    {
      x: minutes,
      y: points.map((point) => point.prototype_skin_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Prototype: Skin",
      line: { color: "#22d3ee", width: 3 },
    },
    {
      x: minutes,
      y: points.map((point) => point.reference_skin_temperature_c),
      type: "scatter",
      mode: "lines",
      name: `${referenceLabel}: Skin`,
      line: { color: "#a5f3fc", width: 2, dash: "dash" },
    },
    {
      x: minutes,
      y: points.map((point) => point.prototype_evaporation_w_m2),
      type: "scatter",
      mode: "lines",
      name: "Prototype: Evaporation",
      line: { color: "#a3e635", width: 2 },
      yaxis: "y2",
      visible: "legendonly",
    },
    {
      x: minutes,
      y: points.map((point) => point.reference_evaporation_w_m2),
      type: "scatter",
      mode: "lines",
      name: `${referenceLabel}: Evaporation`,
      line: { color: "#d9f99d", width: 2, dash: "dash" },
      yaxis: "y2",
      visible: "legendonly",
    },
  ];

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">Trajectory Comparison</h2>

      <Plot
        data={data}
        layout={{
          autosize: true,
          height: 480,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" },
          margin: { l: 65, r: 70, t: 20, b: 60 },
          xaxis: { title: { text: "Time (min)" }, gridcolor: "#334155" },
          yaxis: { title: { text: "Temperature (°C)" }, gridcolor: "#334155" },
          yaxis2: {
            title: { text: "Evaporation (W/m²)" },
            overlaying: "y",
            side: "right",
            showgrid: false,
          },
          legend: { orientation: "h", y: -0.25 },
          hovermode: "x unified",
        }}
        config={{
          responsive: true,
          displaylogo: false,
          toImageButtonOptions: {
            format: "png",
            filename: "gagge-benchmark",
            scale: 2,
          },
        }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />

      <p className="mt-3 text-sm text-slate-400">
        Solid lines are the platform prototype; dashed lines are the reference
        model. Evaporation is on the right axis and hidden until toggled.
      </p>
    </div>
  );
}