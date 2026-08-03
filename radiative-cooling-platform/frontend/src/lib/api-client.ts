import type {
  SimulationRequest,
  SimulationResponse,
} from "@/types/simulation";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ??
  "http://localhost:8000";

export async function runSimulation(
  request: SimulationRequest,
): Promise<SimulationResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/run`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    const errorBody = await response
      .json()
      .catch(() => null);

    const detail =
      errorBody?.detail ??
      `模擬請求失敗：HTTP ${response.status}`;

    throw new Error(
      typeof detail === "string"
        ? detail
        : JSON.stringify(detail),
    );
  }

  return response.json();
}