from typing import List, Optional
from pydantic import Field, TypeAdapter
from app.infrastructure.schemas.base import BaseSchema, OutSchema
from app.infrastructure.schemas.query_params import QueryParams


class MovieBase(BaseSchema):
    title: str = Field(..., description="Movie title")
    release_date: str = Field(..., description="Movie date")
    duration: Optional[str] = Field(None, description="Movie duration")
    kinds: str = Field(..., description="Movie kinds")
    directors: Optional[str] = Field(None, description="Movie directors")
    cast: Optional[str] = Field(None, description="Movie cast")
    original_title: Optional[str] = Field(None, description="Movie original title")
    note: Optional[float] = Field(None, description="Movie note")
    description: str = Field(..., description="Movie description")


class MovieIn(MovieBase):
    ...


class MovieOut(MovieIn, OutSchema):
    ...


class MovieQueryParams(QueryParams):
    ...


MovieCollectionOut = TypeAdapter(List[MovieOut])
