from unittest.mock import Mock, patch
import pytest
import requests

from app.scraper.base import MovieScraper


@pytest.fixture
def scraper():
    return MovieScraper()


@pytest.mark.parametrize("number_of_pages", [1, 2])
def test_run_scraper(scraper, number_of_pages):
    scraper.get_number_of_pages = Mock(return_value=number_of_pages)
    result = scraper.run()
    item = result[0]

    assert len(result) > 1
    assert item.get("title") is not None


def test_get_number_of_pages(scraper):
    response = requests.get(scraper.url)
    html_content = response.content
    result = scraper.get_number_of_pages(html_content=html_content)

    assert isinstance(result, int)


def test_get_html_content_with_statuscode_different_200(scraper):
    with patch("requests.get") as mock_get:
        mock_get.status_code = 400
        scraper.get_html_content(url=scraper.url)
