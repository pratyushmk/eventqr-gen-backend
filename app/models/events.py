from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db import Base

class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String(100), nullable=False)
    event_date = Column(String, nullable=False)
    event_location = Column(String(100), nullable=False)

    tickets = relationship("Ticket", back_populates="events")

