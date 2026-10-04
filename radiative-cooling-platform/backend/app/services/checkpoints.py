from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

from app.models.global_batch import GlobalCityResult, GlobalCityCheckpoint


def upsert_month_checkpoint(db, city_result_id: str, month: int, attempt: int, payload: dict) -> None:
    db.execute(
        pg_insert(GlobalCityCheckpoint)
        .values(city_result_id=city_result_id, month=month, attempt=attempt, payload_json=payload)
        .on_conflict_do_update(
            constraint="uq_global_city_checkpoint_month",
            set_={"payload_json": payload, "attempt": attempt},
        )
    )


def load_resume_state(
    db: Session,
    city_result_id: str,
    *,
    start_month: int = 1,
) -> tuple[int, list[dict]]:
    """Return (next month to run, payloads of the contiguous completed prefix).

    Only the contiguous prefix starting at ``start_month`` is trusted. A hole
    (e.g. months 7, 8, 10) resumes from the hole (9) and discards 10.
    """
    rows = db.execute(
        select(GlobalCityCheckpoint.month, GlobalCityCheckpoint.payload_json)
        .where(GlobalCityCheckpoint.city_result_id == city_result_id)
        .order_by(GlobalCityCheckpoint.month)
    ).all()

    next_month = start_month
    for month, _ in rows:
        if month == next_month:
            next_month += 1
        elif month > next_month:
            break

    return next_month, [payload for month, payload in rows if start_month <= month < next_month]