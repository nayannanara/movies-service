from unittest.mock import patch

import httpx
import pytest
from app.flows.main import start
from tests.flows.factories import response_movies
from prefect.client.schemas.objects import StateType


@patch("app.flows.main.fetch_all_data", return_value=response_movies()["results"])
def test_start(mocker):
    result = start()
    assert result[0].type == StateType.COMPLETED


@patch(
    "app.flows.main.fetch_all_data",
    side_effect=httpx.RequestError("Erro ao buscar os dados"),
)
def test_fetch_all_data_exception(mocker):
    with pytest.raises(httpx.RequestError):
        start()
