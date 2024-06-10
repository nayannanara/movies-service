from app.infrastructure.models.base import CreateBaseModel
from app.infrastructure.repositories.base import Repository
import logging
from types import TracebackType
from typing import Any, List, Type, Union


from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.repositories.db.helpers import build_query
from app.infrastructure.schemas.query_params import QueryParams
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


class Transaction:
    def __init__(self: "Transaction", session: AsyncSession) -> None:
        self.session = session

    async def __aenter__(self: "Transaction") -> "Transaction":
        if not self.session.in_transaction():
            await self.session.begin()
        return self

    async def __aexit__(
        self: "Transaction",
        exc_t: Type[Exception] | None,
        exc_v: Exception | None,
        exc_tb: Union[TracebackType, None],
    ) -> None:
        try:
            if exc_v:
                await self.session.rollback()
            else:
                await self.session.commit()
        except SQLAlchemyError as exc:
            logger.error(f"Database error has occurred with exception: {exc}")
            await self.session.rollback()
            raise exc

    async def insert_all(self: "Transaction", models: list) -> Any:
        self.session.add_all(models)
        return models


class PostgresRepository(Repository):
    model: Any

    def __init__(self: "PostgresRepository", session: AsyncSession) -> None:
        self.session = session

    def transaction(self: "PostgresRepository") -> Transaction:
        return Transaction(session=self.session)

    async def create_all(self, data: List[CreateBaseModel]) -> None:
        async with self.transaction() as transaction:
            return await transaction.insert_all(models=data)

    async def detail(self: "PostgresRepository", filter: dict[str, Any]) -> Any:
        query = build_query(model=self.model, filter=filter)

        data = (await self.session.execute(query)).scalars().first()

        return data

    async def query(
        self: "PostgresRepository", query_params: QueryParams
    ) -> Union[list[Any], int]:
        filter_ = query_params.model_dump(exclude_none=True)
        limit = query_params.limit
        offset = query_params.offset

        query = build_query(model=self.model, filter=filter_)

        if limit:
            query = query.limit(limit=limit)

        if offset:
            query = query.offset(offset=offset)

        data = (await self.session.execute(query)).scalars().all()

        return data
