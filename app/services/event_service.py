from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.events import Event
from app.schemas import EventCreate, EventResponse

def get_events(db:Session) -> List[Event]:
    return db.query(Event).all()

def get_event(event_id:int, db:Session) -> Event:
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Requested event doesn't exist!")
    
    return event

def create_event(event:EventCreate, db:Session):
    if db.query(Event).filter(Event.name == event.name).first():
        raise HTTPException(status_code=400, detail="Event already created!!")
    
    new_event = Event(name=event.name, 
                      date=event.date, 
                      location=event.location)
    
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    
    return EventResponse.model_validate(new_event)

def update_event(event_id:int, event:EventCreate, db:Session) -> Event:
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Requested event doesn't exist!")
    

    db_event.name = event.name
    db_event.date = event.date
    db_event.location = event.location

    db.commit()
    db.refresh(db_event)

    return db_event

def delete_event(event_id:int, db:Session) -> dict:
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event doesn't exist!")
    
    db.delete(db_event)
    db.commit()
    
    return {"message": "Event deleted"}