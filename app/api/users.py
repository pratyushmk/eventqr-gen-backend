from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas import UserCreate, UserResponse
from app.services.user_service import get_user, get_all_users, create_user, update_user, delete_user
from app.utils.dependencies import get_db, get_current_active_user

router = APIRouter(prefix="/users", tags=["users"])

# API EndPoints (CRUD Operation)
@router.get("/", response_model=List[UserResponse])
def get_all_users_endpoint(current_user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_endpoint(user_id:int, current_user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return get_user(user_id, db)

@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, current_user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return create_user(user, db)

@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id:int, user:UserCreate, current_user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return update_user(user_id, user, db)

@router.delete("/{user_id}")
def delete_user_endpoint(user_id:int, current_user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return delete_user(user_id, current_user, db)