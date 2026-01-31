from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User Pydantic Models(Dataclass)
class UserCreate(BaseModel):
    name: str
    age: int
    location: str
    email: str
    role: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    location: str
    email: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True

# Authentication PyDantic Models
class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Events PyDantic Models
class EventCreate(BaseModel):
    name: str
    date: datetime
    location: str

class EventResponse(BaseModel):
    id: int
    name: str
    date: datetime
    location: str

    class Config:
        from_attributes = True

# Tickets PyDantic Models
class TicketCreate(BaseModel):
    event_id: int
    ticket_type: str
    quantity: int

class TicketResponse(BaseModel):
    registration_id: str
    event_id: int
    ticket_type: str
    quantity: int
    status: str

    class Config:
        from_attributes = True

class CheckInRequest(BaseModel):
    registration_id: str