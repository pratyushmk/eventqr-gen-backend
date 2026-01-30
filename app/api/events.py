from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas import EventCreate, EventResponse
from app.utils.dependencies import get_db
from app.services.event_service import get_events, get_event, create_event, update_event, delete_event

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=List[EventResponse])
def get_all_events_endpoint(db:Session = Depends(get_db)):
    return get_events(db)

@router.get("/{event_id}", response_model=EventResponse)
def get_event_endpoint(event_id:int, db:Session = Depends(get_db)):
    return get_event(event_id, db)

@router.post("/", response_model=EventResponse)
def create_event_endpoint(event:EventCreate, db:Session = Depends(get_db)):
    return create_event(event, db)

@router.put("/{event_id}", response_model=EventResponse)
def update_event_endpoint(event_id:int, event:EventCreate, db:Session = Depends(get_db)):
    return update_event(event_id, event, db)

@router.delete("/{event_id}")
def delete_event_endpoint(event_id:int, db:Session = Depends(get_db)):
    return delete_event(event_id, db)

