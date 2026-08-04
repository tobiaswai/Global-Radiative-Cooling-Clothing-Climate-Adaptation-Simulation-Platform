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

import type {
  City,
  WeatherSimulationRequest,
  WeatherSimulationResponse,
  WeatherTimeSeries,
} from "@/types/simulation";

export async function getCities(): Promise<City[]> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/weather/cities`,
  );

  if (!response.ok) {
    throw new Error("無法取得城市列表");
  }

  return response.json();
}

export async function getWeatherHistory(
  cityId: string,
  startTimeLocal: string,
  durationMinutes: number,
): Promise<WeatherTimeSeries> {
  const parameters = new URLSearchParams({
    city_id: cityId,
    start_time_local: startTimeLocal,
    duration_minutes: String(durationMinutes),
  });

  const response = await fetch(
    `${API_BASE_URL}/api/v1/weather/history?${parameters}`,
  );

  if (!response.ok) {
    const body = await response.json().catch(
      () => null,
    );

    throw new Error(
      body?.detail ?? "無法取得歷史氣象資料",
    );
  }

  return response.json();
}

export async function runWeatherSimulation(
  request: WeatherSimulationRequest,
): Promise<WeatherSimulationResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/run-weather`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    const body = await response.json().catch(
      () => null,
    );

    throw new Error(
      body?.detail ??
        `氣象模擬失敗：HTTP ${response.status}`,
    );
  }

  return response.json();
}