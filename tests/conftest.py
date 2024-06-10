import asyncio
from typing import Callable

from fastapi import FastAPI
import pytest
from httpx import AsyncClient

from app.infrastructure.models.base import CreateBaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.repositories.db.session import async_session, engine, get_db
from app.domain.services.movie import MovieService
from app.infrastructure.repositories.movie import MovieRepository
from app.infrastructure.schemas.movie import MovieIn
from tests.factories import movies_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def db_session() -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(CreateBaseModel.metadata.drop_all)
        await connection.run_sync(CreateBaseModel.metadata.create_all)

        async with async_session(bind=connection) as session:
            yield session
            await session.flush()
            await session.rollback()


@pytest.fixture
def database(db_session: AsyncSession) -> Callable:
    async def _database():
        yield db_session

    return _database


@pytest.fixture
def app(database: Callable) -> FastAPI:
    from app.main import app

    app.dependency_overrides[get_db] = database

    return app


@pytest.fixture
async def client(app):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def movie_schema():
    return [MovieIn(**item) for item in movies_data()]


@pytest.fixture
async def movie_repository(db_session):
    return MovieRepository(session=db_session)


@pytest.fixture
async def movie_service(movie_repository):
    return MovieService(movie_repository=movie_repository)


@pytest.fixture
async def create_movies(movie_service, movie_schema):
    await movie_service.create_all(data=movie_schema)
