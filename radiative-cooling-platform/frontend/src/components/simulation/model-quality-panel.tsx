import type {
  SimulationResponse,
} from "@/types/simulation";

type ModelQualityPanelProps = {
  result: SimulationResponse;
};

function residualColor(value: number): string {
  if (value < 0.5) {
    return "text-emerald-300";
  }

  if (value < 2.0) {
    return "text-amber-300";
  }

  return "text-red-300";
}

export function ModelQualityPanel({
  result,
}: ModelQualityPanelProps) {
  const control =
    result.control.diagnostics;

  const rc =
    result.radiative_cooling.diagnostics;

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">
        數值計算品質
      </h2>

      <p className="mt-2 text-sm text-slate-400">
        能量殘差越接近 0%，表示積分熱流與人體儲能變化越一致。
      </p>

      <div className="mt-5 overflow-x-auto">
        <table className="w-full min-w-[700px] text-left text-sm">
          <thead className="border-b border-slate-700 text-slate-400">
            <tr>
              <th className="px-3 py-3">
                情景
              </th>
              <th className="px-3 py-3">
                能量殘差
              </th>
              <th className="px-3 py-3">
                儲能變化
              </th>
              <th className="px-3 py-3">
                積分淨熱量
              </th>
              <th className="px-3 py-3">
                求值次數
              </th>
            </tr>
          </thead>

          <tbody>
            {[
              {
                name: result.control.material_name,
                diagnostics: control,
              },
              {
                name:
                  result.radiative_cooling
                    .material_name,
                diagnostics: rc,
              },
            ].map((item) => (
              <tr
                key={item.name}
                className="border-b border-slate-800"
              >
                <td className="px-3 py-4">
                  {item.name}
                </td>

                <td
                  className={`px-3 py-4 font-semibold ${residualColor(
                    item.diagnostics
                      .normalized_residual_percent,
                  )}`}
                >
                  {item.diagnostics
                    .normalized_residual_percent
                    .toFixed(4)}
                  %
                </td>

                <td className="px-3 py-4">
                  {item.diagnostics
                    .stored_energy_change_j_m2
                    .toFixed(1)}
                  {" J/m²"}
                </td>

                <td className="px-3 py-4">
                  {item.diagnostics
                    .integrated_net_heat_j_m2
                    .toFixed(1)}
                  {" J/m²"}
                </td>

                <td className="px-3 py-4">
                  {
                    item.diagnostics
                      .solver_function_evaluations
                  }
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}