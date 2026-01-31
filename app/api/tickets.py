from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.services.ticket_service import get_all_tickets, get_ticket, create_ticket
from app.utils.dependencies import get_db, get_current_active_user
from app.schemas import TicketCreate, TicketResponse
from app.models.user import User

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.get("/", response_model=List[TicketResponse])
def get_all_tickets_endpoints(user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return get_all_tickets(db)

@router.get("/{registration_id}", response_model=TicketResponse)
def get_ticket_endpoint(registration_id:str, user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    return get_ticket(registration_id, db)

@router.post("/", response_model=TicketResponse)
def create_ticket_endpoint(ticket:TicketCreate, user:User = Depends(get_current_active_user), db:Session = Depends(get_db)):
    user_id = user.id
    return create_ticket(ticket, user_id, db)

