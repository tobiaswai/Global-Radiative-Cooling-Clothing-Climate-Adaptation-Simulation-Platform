const DEFAULT_SIMULATION_MONTH = 7;
const DEFAULT_SIMULATION_DAY = 15;
const DEFAULT_SIMULATION_HOUR = 10;
const DEFAULT_SIMULATION_MINUTE = 0;

function padTwoDigits(value: number): string {
  return value.toString().padStart(2, "0");
}

export function getPreviousCompleteYear(
  now: Date = new Date(),
): number {
  if (Number.isNaN(now.getTime())) {
    throw new Error("A valid date is required.");
  }

  return now.getFullYear() - 1;
}

export function getDefaultSimulationDateTime(
  now: Date = new Date(),
): string {
  const year = getPreviousCompleteYear(now);

  return [
    `${year}-${padTwoDigits(DEFAULT_SIMULATION_MONTH)}`,
    `${padTwoDigits(DEFAULT_SIMULATION_DAY)}T`,
    `${padTwoDigits(DEFAULT_SIMULATION_HOUR)}:`,
    padTwoDigits(DEFAULT_SIMULATION_MINUTE),
  ].join("");
}