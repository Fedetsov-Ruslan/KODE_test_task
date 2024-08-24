
from fastapi_users import FastAPIUsers
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from src.database import get_async_session
from src.notes.models import  record
from src.auth.manager import get_user_manager
from src.auth.auth import auth_backend
from src.auth.models import User
from src.notes.schemas import RecordSchema

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
async def create_record( content:str, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = insert(record).values(auther=current_user.id, content=content)
    await session.execute(query)
    await session.commit()

    return {"status": "record add"}