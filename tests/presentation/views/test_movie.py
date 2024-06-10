from fastapi import status
import pytest


@pytest.mark.usefixtures("create_movies")
async def test_views_should_return_success(client):
    response = await client.get("/movies")
    content = response.json()
    results = content.pop("results")

    item = results[0]

    del item["id"]
    del item["created_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "count": 3,
        "next": "http://test/movies?offset=100",
        "previous": "http://test/movies?offset=0",
    }
    assert item == {
        "title": "Batman & Robin",
        "release_date": "4 de julho de 1997",
        "duration": "2h 05min",
        "kinds": "Ação, Fantasia, Suspense",
        "directors": "Joel Schumacher",
        "cast": "George Clooney, Arnold Schwarzenegger, Chris O'Donnell",
        "original_title": None,
        "note": 2.0,
        "description": "A dupla dinâmica enfrenta uma terrível"
        " dupla de vilões: o gélido Mr. Freeze (Arnold Schwarzenegger)"
        "e a delicada botânica que, ao sofrer um acidente, "
        "transforma-se na perigosa e vingativa Hera Venenosa (Uma Thurman). "
        "Mas, para poder livrar Gotham City das garras dos vilões, "
        "Batman (George Clooney) e Robin (Chris O'Donnell) contam com uma nova ...",
    }
