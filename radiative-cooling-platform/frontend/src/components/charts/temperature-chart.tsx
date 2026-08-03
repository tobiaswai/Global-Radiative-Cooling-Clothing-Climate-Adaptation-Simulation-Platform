"use client";

import dynamic from "next/dynamic";

import type { SimulationResponse } from "@/types/simulation";

const Plot = dynamic(
  () => import("react-plotly.js"),
  {
    ssr: false,
    loading: () => (
      <div className="flex h-96 items-center justify-center text-slate-400">
        正在載入圖表……
      </div>
    ),
  },
);

type TemperatureChartProps = {
  result: SimulationResponse;
};

export function TemperatureChart({
  result,
}: TemperatureChartProps) {
  const control =
    result.control.time_series;
  const rc =
    result.radiative_cooling.time_series;

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">
        人體溫度動態曲線
      </h2>

      <Plot
        data={[
          {
            x: control.map((point) => point.minute),
            y: control.map(
              (point) => point.skin_temperature_c,
            ),
            type: "scatter",
            mode: "lines",
            name: "普通服裝：皮膚溫度",
            line: {
              color: "#f97316",
              width: 3,
            },
          },
          {
            x: rc.map((point) => point.minute),
            y: rc.map(
              (point) => point.skin_temperature_c,
            ),
            type: "scatter",
            mode: "lines",
            name: "輻射製冷：皮膚溫度",
            line: {
              color: "#22d3ee",
              width: 3,
            },
          },
          {
            x: control.map((point) => point.minute),
            y: control.map(
              (point) => point.core_temperature_c,
            ),
            type: "scatter",
            mode: "lines",
            name: "普通服裝：核心溫度",
            line: {
              color: "#ef4444",
              width: 2,
              dash: "dot",
            },
          },
          {
            x: rc.map((point) => point.minute),
            y: rc.map(
              (point) => point.core_temperature_c,
            ),
            type: "scatter",
            mode: "lines",
            name: "輻射製冷：核心溫度",
            line: {
              color: "#3b82f6",
              width: 2,
              dash: "dot",
            },
          },
        ]}
        layout={{
          autosize: true,
          height: 480,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: {
            color: "#cbd5e1",
          },
          margin: {
            l: 65,
            r: 30,
            t: 20,
            b: 60,
          },
          xaxis: {
            title: {
              text: "時間（分鐘）",
            },
            gridcolor: "#334155",
          },
          yaxis: {
            title: {
              text: "溫度（°C）",
            },
            gridcolor: "#334155",
          },
          legend: {
            orientation: "h",
            y: -0.25,
          },
          hovermode: "x unified",
        }}
        config={{
          responsive: true,
          displaylogo: false,
          toImageButtonOptions: {
            format: "png",
            filename: "temperature-comparison",
            scale: 2,
          },
        }}
        useResizeHandler
        style={{
          width: "100%",
          height: "100%",
        }}
      />
    </div>
  );
}