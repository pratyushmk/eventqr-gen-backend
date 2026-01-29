from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.utils.security import get_pwd_hash, verify_pwd, create_access_token
from app.models.user import User
from app.schemas import UserCreate
from app.utils.config import TOKEN_EXPIRES

def register_user(user:UserCreate, db:Session):
    if db.query(User.email == user.email).first():
        raise HTTPException(status_code=404,
                            detail="User already created"
                            )
    
    hashed_pswd = get_pwd_hash(user.password)
    
    db_user = User(name=user.name,
                   age=user.age,
                   location=user.location, 
                   email = user.email, 
                   role=user.role,
                   hashed_pswd=hashed_pswd)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def login_for_access_token(form_data:OAuth2PasswordRequestForm, db:Session):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_pwd(form_data.password, user.hashed_pswd):
        raise HTTPException(status_code=404,
                            detail="Invalid credentials!"
                            )

    if not user.is_active:
        raise HTTPException(status_code=404,
                            detail="Inactive User"
                            )
    
    access_token_expires = timedelta(minutes=TOKEN_EXPIRES)
    access_token = create_access_token(data={'sub': user.email}, 
                                       expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

def get_profile(current_user:User):
    return current_user

def verify_token(current_user:User):
    return {
        "valid": True,
        "user": {
            "id": current_user.id,
            "name": current_user.name,
            "age": current_user.age,
            "location": current_user.location,
            "email": current_user.email,
            "role": current_user.role
        }
    }
