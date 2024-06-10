from fastapi import FastAPI

from app.application.core.config import settings
from app.presentation.views.health import router as health_router
from app.presentation.views.movie import router as movie_router


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            title=settings.PROJECT_NAME,
            version="0.0.1",
            root_path=settings.ROOT_PATH
        )
        self._include_routers()

    def _include_routers(self):
        self.include_router(health_router)
        self.include_router(movie_router)


app = App()
