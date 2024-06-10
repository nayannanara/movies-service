from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.application.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


DatabaseDependency = Annotated[AsyncSession, Depends(get_db)]
