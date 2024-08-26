import requests

from fastapi_users import FastAPIUsers
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.notes.models import  record
from src.auth.manager import get_user_manager
from src.auth.auth import auth_backend
from src.auth.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)
current_user = fastapi_users.current_user()

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)

def check_spelling(content:str):
    url = "https://speller.yandex.net/services/spellservice.json/checkText"
    params = {
        "text": content,
        "lang": "ru, en",
        "options" : 6
    }
    responce = requests.post(url, data=params)
    for res in responce.json():
        x = content.replace(res['word'], res['s'][0], 1)
        content = x
    return content

@router.get("/")
async def get_records(current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(record).where(record.c.auther == current_user.id)
    result = await session.execute(query)
    recodrds =  result.all()
    return [{
        "id": rec.id,
        "auther": rec.auther,
        "content": rec.content,
        "created_at": rec.created_at
    } for rec in recodrds]

@router.post("/")
async def create_record(content:str, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    new_content = check_spelling(content)
    query = insert(record).values(auther=current_user.id, content=new_content)
    await session.execute(query)
    await session.commit()

    return {"status": "record add"}