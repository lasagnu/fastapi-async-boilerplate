from typing import AsyncGenerator

import aiohttp
import fastapi
import fastapi.testclient
import pytest
import pytest_asyncio

import app
import tests.mock
import tests.mock.aiohttp


@pytest_asyncio.fixture(autouse=True)
async def client() -> AsyncGenerator[fastapi.testclient.TestClient, None]:
    test_client = fastapi.testclient.TestClient(app.app)
    yield test_client


@pytest.fixture(autouse=True)
def mock_aiohttp_session(monkeypatch):
    tests.mock.aiohttp.data_to_use = []
    tests.mock.aiohttp.next_status = [
        200,
    ]
    tests.mock.aiohttp.requests_done = []
    monkeypatch.setattr(aiohttp, 'ClientSession', lambda *args, **kwargs: tests.mock.aiohttp.MockSession())
