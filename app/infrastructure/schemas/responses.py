from typing import Any, List

from fastapi import Request
from fastapi.datastructures import QueryParams
from pydantic import AnyHttpUrl, Field, NonNegativeInt

from app.infrastructure.schemas.base import BaseModel


class CollectionResponse(BaseModel):
    count: NonNegativeInt = Field()
    next_: AnyHttpUrl = Field(alias="next")
    previous: AnyHttpUrl = Field()
    results: list[Any] = Field()

    @classmethod
    def parse_collection(
        cls, request: Request, results: List[Any], query_params: QueryParams, count: int
    ) -> "CollectionResponse":
        previous_calc = query_params.offset - query_params.limit
        previous_offset = previous_calc if previous_calc > 0 else 0
        next_offset = query_params.offset + query_params.limit

        collection_response = {
            "count": count,
            "next": str(request.url.include_query_params(offset=next_offset)),
            "previous": str(request.url.include_query_params(offset=previous_offset)),
            "results": results,
        }

        return cls.model_validate(collection_response)
