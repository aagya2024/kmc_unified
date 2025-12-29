from pydantic import BaseModel

class WebsiteResponse(BaseModel):
    name: str

    class Config:
        orm_mode = True
