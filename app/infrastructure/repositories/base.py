from abc import ABC, abstractmethod
from typing import Any, List, Optional, TypeVar


from app.infrastructure.models.base import CreateBaseModel
from app.infrastructure.schemas.query_params import QueryParams

SessionT = TypeVar("SessionT")


class Repository(ABC):
    @abstractmethod
    async def create_all(self, data: List[CreateBaseModel]) -> None:
        raise NotImplementedError

    @abstractmethod
    async def query(
        self, query_params: QueryParams, ordering: str
    ) -> list[Optional[dict[str, Any]]]:
        raise NotImplementedError

    @abstractmethod
    async def detail(self, filters: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError
