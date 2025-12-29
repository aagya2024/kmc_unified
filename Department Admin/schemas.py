from pydantic import BaseModel
from typing import List
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    website_ids: List[int]

class UserUpdate(BaseModel):
    website_ids: List[int] | None = None
    status: str | None = None

class UserResponse(BaseModel):
    id: int
    name: str
    access_details: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
