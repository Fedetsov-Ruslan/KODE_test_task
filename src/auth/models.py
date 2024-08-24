import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import DeclarativeMeta, declarative_base
from sqlalchemy import Table, Integer, String, Column, TIMESTAMP, Boolean
from src.database import metadata

Base: DeclarativeMeta = declarative_base()
user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.datetime.utcnow),
    Column('is_active', Boolean, default=True),
    Column('is_superuser', Boolean,  default=False),
    Column('is_verified', Boolean,  default=False),
)

class User(SQLAlchemyBaseUserTableUUID, Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)