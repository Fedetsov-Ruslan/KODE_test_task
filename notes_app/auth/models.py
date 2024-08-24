import datetime

from sqlalchemy import Table, Integer, String, Column, TIMESTAMP, Boolean
from notes_app.database import metadata


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
