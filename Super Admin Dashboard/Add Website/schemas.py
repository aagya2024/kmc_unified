from pydantic import BaseModel
from datetime import datetime

class WebsiteCreate(BaseModel):
    name: str
    url: str
    status: str = "Active"

class WebsiteUpdate(BaseModel):
    name: str
    url: str
    status: str

class WebsiteResponse(BaseModel):
    id: int
    name: str
    url: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
