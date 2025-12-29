from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    websites = relationship("UserWebsite", back_populates="user")


class Website(Base):
    __tablename__ = "websites"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class UserWebsite(Base):
    __tablename__ = "user_websites"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    website_id = Column(Integer, ForeignKey("websites.id"))

    user = relationship("User", back_populates="websites")
    website = relationship("Website")
