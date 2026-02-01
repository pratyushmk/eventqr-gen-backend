from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.events import Event
from app.models.tickets import Ticket

from app.schemas import TicketCreate

from app.utils.id_generator import generate_registration_id
from app.utils.qrcode_generator import generate_qr

def get_all_tickets(db:Session):
    return db.query(Ticket).all()

def get_ticket(registration_id:str, db:Session):
    ticket = db.query(Ticket).filter(Ticket.registration_id == registration_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found!!")
    
    return ticket

def create_ticket(ticket:TicketCreate, user_id:int, db:Session):

    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    
    event = db.query(Event).filter(Event.id == ticket.event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Selected event is invalid!")
    

    reg_id = generate_registration_id()
    qrcode_path = generate_qr(reg_id, ticket.event_id)

    new_ticket = Ticket(registration_id = reg_id,
                        user_id = user_id,
                        event_id = ticket.event_id,
                        ticket_type = ticket.ticket_type,
                        quantity = ticket.quantity,
                        qr_path = qrcode_path
                        )
    
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


# def update_ticket(ticket_id:int, ticket:TicketCreate, db:Session):
#     if not db.query(Ticket).filter(Ticket.registration_id == ticket_id).first():
#         raise HTTPException(status_code=404, detail="Ticket not found!!")

# def delete_ticket(ticket_id:int, db:Session):
#     pass
