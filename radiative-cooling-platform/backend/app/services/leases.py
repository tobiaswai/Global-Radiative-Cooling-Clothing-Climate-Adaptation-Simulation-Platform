from datetime import timedelta
from sqlalchemy import update, func, or_
from sqlalchemy.orm import Session
from app.core.time import utc_now

from app.core.config import settings
from app.models.global_batch import GlobalCityResult
from app.services.job_state import CityStatus


def acquire_city_lease(db: Session, city_result_id: str, owner: str) -> bool:
    ttl = timedelta(seconds=settings.CITY_LEASE_TTL_SECONDS)
    stmt = (
        update(GlobalCityResult)
        .where(
            GlobalCityResult.id == city_result_id,
            GlobalCityResult.status.in_([CityStatus.QUEUED, CityStatus.RUNNING]),
            or_(
                GlobalCityResult.lease_owner.is_(None),
                GlobalCityResult.lease_expires_at < func.now(),
                GlobalCityResult.lease_owner == owner,     # 同一 owner 重入
            ),
        )
        .values(
            lease_owner=owner,
            lease_expires_at=func.now() + ttl,
            last_heartbeat_at=func.now(),
            status=CityStatus.RUNNING,
            started_at=func.coalesce(GlobalCityResult.started_at, func.now()),
        )
        .returning(GlobalCityResult.id)
    )
    got = db.execute(stmt).scalar_one_or_none()
    db.commit()
    return got is not None


def heartbeat_city_lease(session, city_result_id, owner, **values) -> bool:
    now = utc_now()
    payload = {
        "last_heartbeat_at": now,
        "lease_expires_at": now + timedelta(seconds=settings.CITY_LEASE_TTL_SECONDS),
    }
    payload.update(values)          # 呼叫方的值優先
    result = session.execute(
        update(GlobalCityResult)
        .where(GlobalCityResult.id == city_result_id,
               GlobalCityResult.lease_owner == owner)
        .values(**payload)
    )
    session.commit()
    return result.rowcount == 1


def release_city_lease(db: Session, city_result_id: str, owner: str) -> None:
    db.execute(
        update(GlobalCityResult)
        .where(GlobalCityResult.id == city_result_id, GlobalCityResult.lease_owner == owner)
        .values(lease_owner=None, lease_expires_at=None)
    )
    db.commit()