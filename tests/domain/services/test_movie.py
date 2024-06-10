from unittest.mock import AsyncMock


async def test_services_create_should_return_success(movie_schema, movie_service):
    result = await movie_service.create_all(data=movie_schema)

    assert result is None


async def test_services_create_should_with_exists_return_success(
    movie_schema, movie_service
):
    movie_service.movie_repository.detail = AsyncMock(return_value=True)
    result = await movie_service.create_all(data=movie_schema)

    assert result is None
