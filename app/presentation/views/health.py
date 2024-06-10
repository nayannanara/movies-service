from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.infrastructure.repositories.db.session import get_db
from app.infrastructure.schemas.health import HealthOut

router = APIRouter(tags=["health"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def get_health(db: Annotated[AsyncSession, Depends(get_db)]) -> HealthOut:
    try:
        result = await db.execute(text("SELECT 1"))
        if result.fetchone() is not None:
            return HealthOut(status="ok", database="connected")
        else:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Database connection failed",
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e)
        )
