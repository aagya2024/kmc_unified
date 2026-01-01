from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AdminCreate(BaseModel):
    name: str
    role: str        # Ward Admin / Department Admin
    status: str = "Active"

class AdminUpdate(BaseModel):
    name: str
    role: str
    status: str

class AdminResponse(BaseModel):
    id: int
    name: str
    role: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
