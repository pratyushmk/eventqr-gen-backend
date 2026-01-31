from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.utils.security import verify_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token:str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    # print("Verifying token for current User!!!!")
    token_data = verify_token(token)
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise HTTPException(status_code=401,
                            detail="User does not exist",
                            headers={"WWW-Authenticate":"Bearer"}
                            )
    return user

def get_current_active_user(current_user:User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=404,
                            detail="Inactive User"
                            )
    return current_user

def get_admin_user(admin_user:User = Depends(get_current_active_user)):
    
    if not admin_user.role == 'Admin':
        raise HTTPException(status_code=401,
                            detail="You have to be an Admin to perform this operation"
                            )
    
    return admin_user