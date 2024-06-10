import asyncio
from app.domain.services.movie import MovieService
from app.infrastructure.repositories.movie import MovieRepository
from app.infrastructure.schemas.movie import MovieIn
from app.scraper.base import MovieScraper
from app.infrastructure.repositories.db.session import async_session


class MoviesSpider:
    def __init__(self) -> None:
        self.scraper = MovieScraper()

    async def start(self):
        movies = self.scraper.run()
        await self.create_movies(movies=movies)

    async def create_movies(self, movies):
        async with async_session() as session:
            movie_service = MovieService(
                movie_repository=MovieRepository(session=session)
            )
            await movie_service.create_all(data=[MovieIn(**item) for item in movies])


if __name__ == "__main__":
    movie = MoviesSpider()
    asyncio.run(movie.start())
