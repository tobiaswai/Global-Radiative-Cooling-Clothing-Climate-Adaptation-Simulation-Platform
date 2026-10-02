from datetime import datetime, timezone


def utc_now() -> datetime:
    """Timezone-aware UTC now. Shared by API layer and Celery tasks."""
    return datetime.now(timezone.utc)