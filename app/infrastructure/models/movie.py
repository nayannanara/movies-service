from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, String, DateTime

from app.infrastructure.models.base import CreateBaseModel


class MovieModel(CreateBaseModel):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(String, nullable=False)
    release_date: Mapped[str] = mapped_column(String, nullable=False)
    duration: Mapped[str] = mapped_column(String, nullable=True)
    kinds: Mapped[str] = mapped_column(String, nullable=False)
    directors: Mapped[str] = mapped_column(String, nullable=True)
    cast: Mapped[DateTime] = mapped_column(String, nullable=True)
    original_title: Mapped[str] = mapped_column(String, nullable=True)
    note: Mapped[float] = mapped_column(Float, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
