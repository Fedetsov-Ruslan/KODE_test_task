from pydantic import BaseModel
from datetime import datetime


class RecordSchema(BaseModel):
    id: int
    auther: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True