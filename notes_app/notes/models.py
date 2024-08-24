import datetime

from sqlalchemy import Table, Integer, String, Column, TIMESTAMP, Boolean, ForeignKey
from notes_app.database import metadata


record = Table(
    "record",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('auther', Integer, ForeignKey("user.id")),
    Column('content', String, nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.datetime.utcnow),
)