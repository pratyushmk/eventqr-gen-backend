from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas import UserCreate

def get_user(user_id:int , db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    
    return user

def get_all_users(db:Session):
    
    return db.query(User).all()

def create_user(user:UserCreate, db:Session):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="User already exists!")
    
    # Create new user
    new_user = User(name=user.name,
                   age=user.age,
                   location=user.location, 
                   email = user.email, 
                   role=user.role)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(user_id:int, user:UserCreate, db:Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="User doesn't exist!!")
    
    # Update User
    db_user.name = user.name
    db_user.age = user.age
    db_user.email = user.email
    db_user.role = user.role

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(user_id:int, db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    
    db.delete(user)
    db.commit()
    
    return {"mesage":"User deleted"}
