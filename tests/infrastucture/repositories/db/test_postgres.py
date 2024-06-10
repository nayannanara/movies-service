from unittest.mock import AsyncMock
import pytest

from sqlalchemy.future import select
from app.infrastructure.models.base import CreateBaseModel
from app.infrastructure.repositories.db.postgres import PostgresRepository, Transaction
from app.infrastructure.schemas.query_params import QueryParams


class FakeModel(CreateBaseModel):
    __tablename__ = "fake"


class FakeRepository(PostgresRepository):
    model = FakeModel

    def __init__(self: "FakeRepository", session) -> None:
        self.session = session


@pytest.fixture
def mock_create_base_model():
    return FakeModel(id="a9cb35ee-5dc2-4073-8b71-2f8ffae27dc4")


async def test_postgres_repository_create_all(db_session, mock_create_base_model):
    repository = FakeRepository(session=db_session)

    await repository.create_all([mock_create_base_model])

    query = select(FakeRepository.model).where(
        FakeRepository.model.id == "a9cb35ee-5dc2-4073-8b71-2f8ffae27dc4"
    )
    result = await db_session.execute(query)

    item = result.scalar()

    assert item == mock_create_base_model
    assert item.id == "a9cb35ee-5dc2-4073-8b71-2f8ffae27dc4"


async def test_postgres_repository_detail(db_session, mock_create_base_model):
    repository = FakeRepository(session=db_session)
    await repository.create_all([mock_create_base_model])
    result = await repository.detail(
        filter={"id": "a9cb35ee-5dc2-4073-8b71-2f8ffae27dc4"}
    )

    assert result.id == "a9cb35ee-5dc2-4073-8b71-2f8ffae27dc4"


async def test_postgres_repository_query(db_session):
    data = [
        FakeModel(id="a9cb35ee-5dc2-4073-8b71-2f8ffae27dc4"),
        FakeModel(id="a9cb35ee-5dc2-4073-8b71-2f8ffae27dc4"),
        FakeModel(id="7f996af4-35f1-4ddf-8081-dee14d3c47ec"),
    ]
    repository = FakeRepository(session=db_session)
    await repository.create_all(data=data)

    query_params = QueryParams()
    result = await repository.query(query_params=query_params)

    assert isinstance(result, list)


async def test_transaction(db_session):
    async with Transaction(session=db_session):
        assert db_session.in_transaction()

    assert not db_session.in_transaction()


async def test_transaction_commit(db_session):
    commit_mock = AsyncMock()
    db_session.commit = commit_mock

    async with Transaction(db_session) as transaction:
        await transaction.__aexit__(None, None, None)
        commit_mock.assert_called_once()
