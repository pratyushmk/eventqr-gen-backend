import jwt

from fastapi import HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

from app.utils.config import SECRET_KEY, ALGORITHM
from app.schemas import TokenData

# Password Hashing
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def get_pwd_hash(password:str) -> str:
    return pwd_context.hash(password)

def verify_pwd(plain_pwd: str, hashed_pwd:str) -> bool:
    return pwd_context.verify(plain_pwd, hashed_pwd)

def create_access_token(data:dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_token(token:str) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        
        if email is None:
            raise credentials_exception()

        return TokenData(email=email)
    
    except jwt.PyJWTError:
        raise credentials_exception()

def credentials_exception():
    return HTTPException(
        status_code=401,
        detail="Could not verify credentials",
        headers={"WWW-Authenticate":"Bearer"}
        )