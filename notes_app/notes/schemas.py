from pydantic import BaseModel
from datetime import datetime


class record(BaseModel):
    id: int
    auther: int
    content: str
    created_at: datetime