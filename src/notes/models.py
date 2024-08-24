import datetime

from sqlalchemy import Table, Integer, String, Column, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeMeta, declarative_base

from src.database import metadata

Base: DeclarativeMeta = declarative_base()


record = Table(
    "record",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('auther', Integer, ForeignKey("user.id")),
    Column('content', String, nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.datetime.utcnow),
)

# class Record(Base):
#     __tablename__ = "record"

#     id = Column(Integer, primary_key=True)
#     auther = Column(ForeignKey("users.id"), nullable=False)
#     content = Column(String(255), nullable=False)
#     created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)