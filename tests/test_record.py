from httpx import AsyncClient

records_root = ['first_record', 'second_record', 'third_record', 'fourth_record']
records_user = ['1_record', '2_record', '3_record']

async def test_add_record_for_root(ac: AsyncClient):
    responce =  await ac.post("/auth/jwt/login", data={
    "username": "root@gmail.com",
    "password": "root"
    })  
    coockes = responce.cookies
    bounds = coockes.get("bounds")
    if responce.status_code == 204:
        for record in records_root:
            response = await ac.post(f"/notes/?content={record}",
            cookies={"bounds": bounds}  
            )
            assert response.status_code == 200

async def test_get_records_for_root(ac: AsyncClient):
    responce =  await ac.post("/auth/jwt/login", data={
  "username": "root@gmail.com",
  "password": "root"
})
    coockes = responce.cookies
    bounds = coockes.get("bounds")
    if responce.status_code == 204:
        response = await ac.get("/notes/",
                                cookies={"bounds": bounds})
        print(response.json())
        assert response.status_code == 200 and len(response.json()) == 4

async def test_add_record_for_user(ac: AsyncClient):
    responce =  await ac.post("/auth/jwt/login", data={
    "username": "user@gmail.com",
    "password": "user"
    })  
    coockes = responce.cookies
    bounds = coockes.get("bounds")
    if responce.status_code == 204:
      for record in records_user:
            response = await ac.post(
            f"/notes/?content={record}",
            cookies={"bounds": bounds}  
            )
            assert response.status_code == 200 

async def test_get_records_for_user(ac: AsyncClient):
    responce =  await ac.post("/auth/jwt/login", data={
  "username": "user@gmail.com",
  "password": "user"
})
    coockes = responce.cookies
    bounds = coockes.get("bounds")
    if responce.status_code == 204:
        response = await ac.get("/notes/",
                                cookies={"bounds": bounds})
        print(response.json())
        assert response.status_code == 200 and len(response.json()) == 3