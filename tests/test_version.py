from httpx import AsyncClient
from app.main import app

import pytest

@pytest.mark.asyncio
async def test_version():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/api/v1/version")
    assert resp.status_code == 200
    assert "version" in resp.json()
