from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from pydantic import BaseModel
from typing import List


# Database setup
engine = create_engine("sqlite:///users.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Database Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    location = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

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


app = FastAPI(title="Users API integration with SQL")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()

# API EndPoints (CRUD Operation)
@app.get("/")
def root():
    return {"message": "Users API integration with SQl using SqlAlchemy!"}

@app.get("/users/", response_model=List[UserResponse])
def get_all_users(db:Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id:int , db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    
    return user

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db:Session = Depends(get_db)):
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

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id:int, user:UserCreate, db:Session = Depends(get_db)):
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

@app.delete("/users/{user_id}")
def delete_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    
    db.delete(user)
    db.commit()
    
    return {"mesage":"User deleted"}