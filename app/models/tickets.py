from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from datetime import datetime
from app.db import Base

from enum import Enum

class TicketStatus(str, Enum):
    CHECKED_IN = "CHECKED_IN"
    NOT_CHECKED_IN = "NOT_CHECKED_IN"

class Ticket(Base):
    __tablename__ = "tickets"

    registration_id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"))
    ticket_type = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    qr_path = Column(String, nullable=False)
    status = Column(String, default=TicketStatus.NOT_CHECKED_IN.value)
    created_at = Column(String, default=lambda: datetime.utcnow().isoformat())
    checkin_time = Column(String, nullable=True)
    checkin_count = Column(Integer, default=0)

    user = relationship("User", back_populates="tickets")
    event = relationship("Event", back_populates="tickets")

