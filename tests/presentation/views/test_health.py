from unittest.mock import AsyncMock, Mock
from fastapi import status


async def test_views_get_health_database_connected(client):
    response = await client.get("/health")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok", "database": "connected"}


async def test_views_get_health_database_disconnected(client, db_session):
    db_session.execute = AsyncMock(return_value=Mock(fetchone=Mock(return_value=None)))

    response = await client.get("/health")

    assert response.status_code == 503
    assert response.json() == {"detail": "503: Database connection failed"}


async def test_views_get_health_exception(client, db_session):
    db_session.execute = AsyncMock(side_effect=Exception("Database error"))

    response = await client.get("/health")

    assert response.status_code == 503
    assert response.json() == {"detail": "Database error"}
