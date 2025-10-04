# test/test_iot.py
import pytest
from httpx import AsyncClient, ASGITransport
from backend.main import app

@pytest.mark.asyncio
async def test_create_iot():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/iot/", json={
            "id": 1,
            "device": "Sensor-01",
            "type": "temperature",
            "value": 22.5,
            "unit": "C"
        })
    assert response.status_code == 200
    data = response.json()
    assert data["device"] == "Sensor-01"
    assert data["type"] == "temperature"


@pytest.mark.asyncio
async def test_list_iot():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/iot/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.asyncio
async def test_get_iot():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/iot/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["device"] == "Sensor-01"


@pytest.mark.asyncio
async def test_update_iot():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.put("/iot/1", json={
            "id": 1,
            "device": "Sensor-01",
            "type": "humidity",
            "value": 55.0,
            "unit": "%"
        })
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "humidity"
    assert data["value"] == 55.0


@pytest.mark.asyncio
async def test_delete_iot():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.delete("/iot/1")
    assert response.status_code == 200
    data = response.json()
    assert "deleted" in data["message"]
