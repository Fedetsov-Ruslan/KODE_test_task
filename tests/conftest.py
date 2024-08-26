import asyncio
import pytest
from typing import AsyncGenerator
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.database import get_async_session
from src.database import metadata
from src.config import DB_TEST_HOST, DB_TEST_PORT, DB_TEST_NAME, DB_TEST_USER, DB_TEST_PASS
from src.main import app

DATABASE_TEST_URL = f'postgresql+asyncpg://{DB_TEST_USER}:{DB_TEST_PASS}@{DB_TEST_HOST}/{DB_TEST_NAME}'

engine_test = create_async_engine(DATABASE_TEST_URL, poolclass=NullPool)
async_session_marker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine_test

async def  override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_marker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope="session")
async def prepare_database() -> AsyncGenerator[None, None]:
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

client = TestClient(app)

@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        yield ac
