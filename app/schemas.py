from pydantic import BaseModel
from typing import Optional

# Pydantic Models(Dataclass)
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