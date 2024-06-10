from typing import Optional

from pydantic import BaseModel, Field


class HealthOut(BaseModel):
    status: Optional[str] = Field(default="OK")
