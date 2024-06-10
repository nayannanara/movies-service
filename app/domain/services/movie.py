from typing import Annotated, List

from fastapi import Depends, Request

from app.infrastructure.models.movie import MovieModel
from app.infrastructure.repositories.movie import MovieRepositoryDependency
from app.infrastructure.schemas.movie import MovieCollectionOut, MovieIn, MovieOut
from app.infrastructure.schemas.query_params import QueryParams
from app.infrastructure.schemas.responses import CollectionResponse
from app.application.core.logging import logger


class MovieService:
    def __init__(
        self: "MovieService", movie_repository: MovieRepositoryDependency
    ) -> None:
        self.movie_repository: MovieRepositoryDependency = movie_repository

    async def create_all(self, data: List[MovieIn]) -> List[MovieOut]:
        movies_models = []
        for item in data:
            movie = await self.movie_repository.detail(filter={"title": item.title})
            if movie:
                continue
            movies_models.append(MovieModel(**item.model_dump()))
        await self.movie_repository.create_all(data=movies_models)
        logger.info("Dados inseridos com sucesso")

    async def query(
        self, query_params: QueryParams, request: Request
    ) -> CollectionResponse:
        async with self.movie_repository.transaction():
            movies_model = await self.movie_repository.query(query_params=query_params)

            movies = MovieCollectionOut.validate_python(movies_model)

            return CollectionResponse.parse_collection(
                request=request,
                results=movies,
                query_params=query_params,
                count=len(movies),
            )


MovieServiceDependency = Annotated[MovieService, Depends()]
