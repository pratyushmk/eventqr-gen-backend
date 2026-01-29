from fastapi import Depends
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas import UserCreate, UserResponse, Token
from app.services.auth_service import register_user, login_for_access_token, get_profile, verify_token
from app.utils.dependencies import get_db, get_current_active_user

router = APIRouter(prefix="/users", tags=["token"])

@router.post("/register", response_model=UserResponse)
def register_user_endpoint(user:UserCreate, db:Session = Depends(get_db)):
    return register_user(user, db)

@router.post("/login", response_model=Token)
def get_access_token_endpoint(form_data:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    return login_for_access_token(form_data, db)

@router.get("/profile", response_model=UserResponse)
def get_profile_endpoint(current_user:User = Depends(get_current_active_user)):
    return get_profile(current_user)

@router.get("/verify-token")
def verify_token_endpoint(current_user:User = Depends(get_current_active_user)):
    return verify_token(current_user)
