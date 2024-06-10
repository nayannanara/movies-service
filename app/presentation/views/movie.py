from fastapi import APIRouter, Depends, Request, status
from app.domain.services.movie import MovieServiceDependency
from app.infrastructure.schemas.movie import MovieQueryParams
from app.infrastructure.schemas.responses import CollectionResponse


router = APIRouter(tags=["movies"])


@router.get(
    "/movies",
    status_code=status.HTTP_200_OK,
)
async def query(
    request: Request,
    movie_service: MovieServiceDependency,
    query_params: MovieQueryParams = Depends(),
) -> CollectionResponse:
    data: CollectionResponse = await movie_service.query(
        query_params=query_params, request=request
    )

    return data
