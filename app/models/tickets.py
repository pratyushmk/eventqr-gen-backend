from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Enum
from sqlalchemy.orm import relationship

from datetime import datetime
from app.db import Base

import enum

class TicketStatus(str, enum.Enum):
    CHECKED_IN = "CHECKED_IN"
    NOT_CHECKED_IN = "NOT_CHECKED_IN"

class Ticket(Base):
    __tablename__ = "tickets"

    registration_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    ticket_type = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    qr_path = Column(String, nullable=False)
    status = Column(Enum(TicketStatus), default=TicketStatus.NOT_CHECKED_IN)
    created_at = Column(DateTime, nullable=False)
    checkin_time = Column(DateTime, nullable=False)
    checkin_count = Column(Integer, default=0)

    user = relationship("User", back_populates="tickets")
    event = relationship("Event", back_populates="tickets")

