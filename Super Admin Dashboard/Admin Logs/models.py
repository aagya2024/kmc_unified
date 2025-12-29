from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class AdminLog(Base):
    __tablename__ = "admin_logs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  
    status = Column(String, default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)
