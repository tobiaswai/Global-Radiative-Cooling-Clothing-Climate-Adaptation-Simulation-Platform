"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import { METRIC_LABELS } from "@/lib/optimization-labels";
import type { GenerationRecord, MetricName } from "@/types/optimization";

const Plot = dynamic(() => import("react-plotly.js"), { ssr: false });

export function ConvergenceChart({ history, metric }: { history: GenerationRecord[]; metric: MetricName }) {
  const data: Data[] = [
    {
      x: history.map((r) => r.generation),
      y: history.map((r) => r.best_metric_value),
      type: "scatter",
      mode: "lines+markers",
      name: METRIC_LABELS[metric],
      line: { color: "#22d3ee", width: 3 },
      marker: { size: 8, color: history.map((r) => (r.best_feasible ? "#10b981" : "#ef4444")) },
    },
    {
      x: history.map((r) => r.generation),
      y: history.map((r) => r.evaluation_count),
      type: "scatter",
      mode: "lines",
      name: "Cumulative evaluations",
      yaxis: "y2",
      line: { color: "#94a3b8", dash: "dot" },
    },
  ];

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">Convergence</h2>
      <Plot
        data={data}
        layout={{
          autosize: true, height: 380, paper_bgcolor: "#0f172a", plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" }, margin: { l: 65, r: 70, t: 20, b: 55 },
          xaxis: { title: { text: "Generation" }, gridcolor: "#334155" },
          yaxis: { title: { text: "Best objective metric" }, gridcolor: "#334155" },
          yaxis2: { title: { text: "Evaluations" }, overlaying: "y", side: "right", showgrid: false },
          legend: { orientation: "h", y: -0.25 }, hovermode: "x unified",
        }}
        config={{ responsive: true, displaylogo: false }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />
      <p className="mt-2 text-sm text-slate-400">Green markers: best member satisfies all constraints; red: it does not.</p>
    </div>
  );
}