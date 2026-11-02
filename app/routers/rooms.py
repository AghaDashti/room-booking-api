from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.room import Room
from app.schemas.room import RoomCreate, RoomRead

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.post("", response_model=RoomRead, status_code=201)
def create_room(data: RoomCreate, db: Session = Depends(get_db)):
    room = Room(name=data.name, capacity=data.capacity)
    db.add(room)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="A room with this name already exists")
    db.refresh(room)
    return room


@router.get("", response_model=list[RoomRead])
def list_rooms(db: Session = Depends(get_db)):
    return db.scalars(select(Room)).all()