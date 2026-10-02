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


def load_resume_state(db: Session, city_result_id: str) -> tuple[int, list[dict]]:
    """回傳 (下一個要跑的月份, 已完成月份的 payload 依月份排序)。"""
    rows = db.execute(
        select(GlobalCityCheckpoint.month, GlobalCityCheckpoint.payload_json)
        .where(GlobalCityCheckpoint.city_result_id == city_result_id)
        .order_by(GlobalCityCheckpoint.month)
    ).all()
    if not rows:
        return 1, []
    months = [m for m, _ in rows]
    # 只信任連續前綴，中間有洞就從洞開始
    next_month = 1
    for m in months:
        if m == next_month:
            next_month += 1
        else:
            break
    return next_month, [p for m, p in rows if m < next_month]