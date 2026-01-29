
from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1: {
        "name": "Prat",
        "age": 23,
        "location": "NC",
        "email": "prat@xyz.com"
    }
}

class User(BaseModel):
    name: str
    age: int
    location: str
    email: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    location: Optional[str] = None
    email: Optional[str] = None

# Root
@app.get("/")
def root():
    return "User's Landing Page!!!!"

# Get user
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User doesn't exist!!!")
    return users[user_id]

# Create user
@app.post("/users/{user_id}", status_code=201)
def create_user(user_id: int, user: User):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists!!")
    
    users[user_id] = user.dict()
    return user

# Update user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User doesn't exist!!")
    
    current_user = users[user_id]
    if user.name is not None:
        current_user["name"] = user.name
    
    if user.age is not None:
        current_user["age"] = user.age
    
    if user.location is not None:
        current_user["location"] = user.location
    
    if user.email is not None:
        current_user["email"] = user.email
    
    return current_user

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User doesn't exist!!")
    
    deleted_user = users.pop(user_id)
    return {"message": "User has been deleted", "deleted_user": deleted_user}

# Search User
@app.get("/users/search/")
def search_user_by_name(name: Optional[str] = None):
    if not name:
        return {"message": "Name is required"}
    
    for user in users.values():
        if user["name"] == name:
            return user
        
    raise HTTPException(status_code=404, detail="User not Found!!")