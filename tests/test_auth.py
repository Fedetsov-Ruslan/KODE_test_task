import pytest

from httpx import AsyncClient

from src.auth.models import User
from tests.conftest import client, async_session_marker



def test_register():
  responce =  client.post("/auth/register", json={
  "email": "root@gmail.com",
  "password": "root",
  "is_active": True,
  "is_superuser": False,
  "is_verified": False,
  "username": "root"
})

  assert responce.status_code == 201

async def test_login(ac: AsyncClient):
    responce =  await ac.post("/auth/jwt/login", data={
  "username": "root@gmail.com",
  "password": "root"
})
    assert responce.status_code == 204


def test_register2():
  responce =  client.post("/auth/register", json={
  "email": "user@gmail.com",
  "password": "user",
  "is_active": True,
  "is_superuser": False,
  "is_verified": False,
  "username": "user"
})

  assert responce.status_code == 201


