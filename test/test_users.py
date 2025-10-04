import pytest
from httpx import AsyncClient, ASGITransport
from backend.main import app

@pytest.mark.asyncio
async def test_create_user():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/users/", json={
            "name": "Greg",
            "email": "greg@test.com",
            "password": "1234"
        })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Greg"
    assert "id" in data
