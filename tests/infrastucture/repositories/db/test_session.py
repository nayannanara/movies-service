from app.infrastructure.repositories.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession


async def test_get_db():
    async for session in get_db():
        assert isinstance(session, AsyncSession)
