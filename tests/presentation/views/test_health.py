from fastapi import status


async def test_hould_return_ok(client):
    response = await client.get("/health")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok", "database": "connected"}
