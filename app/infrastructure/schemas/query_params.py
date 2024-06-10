from typing import Optional

from fastapi import Query
from pydantic import BaseModel, NonNegativeInt


class QueryParams(BaseModel):
    offset: Optional[NonNegativeInt] = Query(
        0, description="Number of data to offset for pagination", exclude=True
    )
    limit: Optional[NonNegativeInt] = Query(
        100, description="Maximum number of data to return", exclude=True
    )
