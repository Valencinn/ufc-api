from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from datetime import date

import models
from db import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# -----------------------------------------------------------------------------
# Pydantic Schemas, para crear los schemas tiene que ser igual a los modelos de la base de datos, mismos nombres y tipos de datos
# -----------------------------------------------------------------------------

class FighterCreate(BaseModel): #esquema para la creación de fighters
    first_name: str
    last_name: str
    nickname: str | None = None
    gender: str
    weight_class_id: int

class FighterResponse(BaseModel): # Esquema para la respuesta de fighters
    fighter_id: int
    first_name: str
    last_name: str
    nickname: str | None
    gender: str
    weight_class_id: int

    model_config = {
        "from_attributes": True
    }

class EventResponse(BaseModel):
    edition_number: int
    event_name: str
    event_date: date | None
    location_name: str

    model_config = {
        "from_attributes": True
    }

# -----------------------------------------------------------------------------
# conexion a la base de datos
# -----------------------------------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dep = Annotated[Session, Depends(get_db)]

# -----------------------------------------------------------------------------
# ENDPOINTS
# -----------------------------------------------------------------------------

#endpoint de creación de fighters
@app.post("/fighters/", response_model=FighterResponse, status_code=status.HTTP_201_CREATED)
async def create_fighter(fighter: FighterCreate, db: db_dep):
    db_fighter = models.Fighter(
        first_name=fighter.first_name,
        last_name=fighter.last_name,
        nickname=fighter.nickname,
        gender=fighter.gender,
        weight_class_id=fighter.weight_class_id,
    )

    db.add(db_fighter)
    db.commit()
    db.refresh(db_fighter)
    return db_fighter

#endpoint de fighters
@app.get("/fighters/", response_model=list[FighterResponse])
def get_all_fighters(db: db_dep):
    fighters = db.query(models.Fighter).all()
    return fighters


#endpoint de eventos
@app.get("/events/", response_model=list[EventResponse])
def get_events(db: db_dep):
    events = db.query(models.Events).all()
    return events
