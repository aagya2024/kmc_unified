from pydantic import BaseModel
from typing import List
from datetime import datetime

class WebsiteBase(BaseModel):
    website_name: str

class UserCreate(BaseModel):
    name: str
    websites: List[WebsiteBase]

class UserUpdate(BaseModel):
    name: str
    is_active: bool
    websites: List[WebsiteBase]

class UserResponse(BaseModel):
    id: int
    name: str
    access_details: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
