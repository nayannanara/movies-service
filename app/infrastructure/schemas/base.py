from datetime import datetime
from pydantic import UUID4, BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True


class OutSchema(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
