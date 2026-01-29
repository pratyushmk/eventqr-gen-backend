from pydantic import BaseModel

# Pydantic Models(Dataclass)
class UserCreate(BaseModel):
    name: str
    age: int
    location: str
    email: str
    role: str

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    location: str
    email: str
    role: str

    class Config:
        from_attributes = True