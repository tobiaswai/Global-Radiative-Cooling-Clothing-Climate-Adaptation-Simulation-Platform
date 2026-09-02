"""Dynamic application date defaults."""

from __future__ import annotations

from datetime import date, datetime


def get_previous_complete_year(
    today: date | None = None,
) -> int:
    """Return the year before the current calendar year."""
    current_date = today or date.today()
    return current_date.year - 1


def get_default_simulation_datetime(
    now: datetime | None = None,
) -> datetime:
    """Return the representative datetime in the previous year."""
    current_datetime = now or datetime.now().astimezone()

    return datetime(
        year=current_datetime.year - 1,
        month=7,
        day=15,
        hour=10,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=current_datetime.tzinfo,
    )