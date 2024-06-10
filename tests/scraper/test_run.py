from unittest.mock import Mock
import pytest
from app.scraper.run import MoviesSpider
from tests.factories import movies_data


@pytest.fixture
def spider():
    return MoviesSpider()


async def test_start_spider(spider):
    spider.scraper = Mock(run=Mock(return_value=movies_data()))
    await spider.start()


async def test_create_movies(spider):
    await spider.create_movies(movies=movies_data())
