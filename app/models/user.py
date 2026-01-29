from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

# Database Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    location = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(String(100), nullable=False)
    hashed_pswd = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)