from fastapi import APIRouter, status

from app.infrastructure.schemas.health import HealthOut

router = APIRouter(tags=["health"])


@router.get("/healthz", status_code=status.HTTP_200_OK)
@router.get("/readiness", status_code=status.HTTP_200_OK)
async def get_health() -> HealthOut:
    return HealthOut()
