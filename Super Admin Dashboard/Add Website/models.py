from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Website(Base):
    __tablename__ = "websites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)
    status = Column(String, default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)
