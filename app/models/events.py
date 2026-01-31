from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from app.db import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String(100), nullable=False)

    tickets = relationship("Ticket", back_populates="event", cascade="all, delete-orphan", passive_deletes=True)

