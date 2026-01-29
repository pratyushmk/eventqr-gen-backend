from fastapi import FastAPI
from app.db import Base, engine
from app.api import users, auth

# Create DB tables
Base.metadata.create_all(engine)

app = FastAPI(title="Authenticated User API", 
              description="FastAPI based implementation to authenticate, verify, login and perform CRUD operations on users", 
              version="1.1.0")

# Register Routers
app.include_router(users.router)
app.include_router(auth.router)

