from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    role: str
    status: str = "Active"

class UserUpdate(BaseModel):
    name: str
    role: str
    status: str

class UserResponse(BaseModel):
    id: int
    name: str
    role: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
