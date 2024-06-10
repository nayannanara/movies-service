from typing import Annotated

from fastapi import Depends
from app.infrastructure.models.movie import MovieModel
from app.infrastructure.repositories.db.postgres import PostgresRepository

from app.infrastructure.repositories.db.session import DatabaseDependency


class MovieRepository(PostgresRepository):
    model = MovieModel

    def __init__(self: "MovieRepository", session: DatabaseDependency) -> None:
        self.session = session


MovieRepositoryDependency = Annotated[MovieRepository, Depends()]
