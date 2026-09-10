from app.schemas.global_batch import (
    ExecutionProfile,
    GlobalBatchCreate,
)
from app.services.annual_sampling import (
    estimate_sample_count,
)


def resolve_execution_profile(
    request: GlobalBatchCreate,
) -> ExecutionProfile:
    if request.execution_profile != "auto":
        return request.execution_profile

    samples_per_city = estimate_sample_count(
        request
    )

    if (
        samples_per_city >= 180
        or len(request.city_ids) >= 20
    ):
        return "large"

    return "standard"


def resolve_queue_name(
    request: GlobalBatchCreate,
) -> str:
    profile = resolve_execution_profile(
        request
    )

    if profile == "large":
        return "global_large"

    return "global_standard"