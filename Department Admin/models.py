from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, default="Active")
    created_at = Column(DateTime, default=datetime.now)

    websites = relationship(
        "UserWebsite",
        back_populates="user",
        cascade="all, delete"
    )


class Website(Base):
    __tablename__ = "websites"

    id = Column(Integer, primary_key=True)
    website_name = Column(String, unique=True)


class UserWebsite(Base):
    __tablename__ = "user_websites"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    website_id = Column(Integer, ForeignKey("websites.id"))

    user = relationship("User", back_populates="websites")
