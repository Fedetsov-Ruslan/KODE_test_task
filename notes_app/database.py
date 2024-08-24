from typing import AsyncGenerator

from sqlalchemy import Column, String, Integer,  MetaData, ForeignKey
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.orm import DeclarativeMeta, declarative_base, Mapped, sessionmaker

from notes_app.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
Base: DeclarativeMeta = declarative_base()

metadata = MetaData()

class User(SQLAlchemyBaseUserTableUUID, Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True)
    auther = Column(ForeignKey("users.id"), nullable=False)
    content = Column(String(255), nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_marker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_marker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

