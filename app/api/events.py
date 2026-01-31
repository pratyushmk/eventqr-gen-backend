from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas import EventCreate, EventResponse
from app.utils.dependencies import get_db, get_current_active_user, get_admin_user
from app.services.event_service import get_events, get_event, create_event, update_event, delete_event
from app.models.user import User

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=List[EventResponse])
def get_all_events_endpoint(user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return get_events(db)

@router.get("/{event_id}", response_model=EventResponse)
def get_event_endpoint(event_id:int, user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return get_event(event_id, db)

@router.post("/", response_model=EventResponse)
def create_event_endpoint(event:EventCreate, user:User = Depends(get_admin_user), db:Session = Depends(get_db)):
    return create_event(event, db)

@router.put("/{event_id}", response_model=EventResponse)
def update_event_endpoint(event_id:int, event:EventCreate, user:User = Depends(get_admin_user), db:Session = Depends(get_db)):
    return update_event(event_id, event, db)

@router.delete("/{event_id}")
def delete_event_endpoint(event_id:int, user:User = Depends(get_admin_user), db:Session = Depends(get_db)):
    return delete_event(event_id, db)

