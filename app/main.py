from fastapi import FastAPI
from app.db import Base, engine
from app.api import users

# Create DB tables
Base.metadata.create_all(engine)

app = FastAPI(title="Users API integration with SQLLite using SQLAlchemy", 
              description="FastAPI Project to run User CRUD ops", 
              version="1.0.0")

# Register Routers
app.include_router(users.router)

