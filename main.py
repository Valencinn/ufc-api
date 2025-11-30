from fastapi import FastAPI, HTTPException, Depends, status #de fastapi importas FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session #sqlalchemy importas Session que hace que puedas interactuar con la base de datos
from typing import Annotated, Optional #typing importas Annotated y Optional que te permiten definir tipos de datos como en typescript
from pydantic import BaseModel #pydantic importas BaseModel que te permite definir modelos de datos para validacion y serializacion

import models #models que contiene las columnas de la base de datos
from db import SessionLocal, engine #el motor y la sesion de la base de datos

#creas tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#validacion de datos con BaseModel de pydantic
class FighterCreate(BaseModel):
    first_name: str
    last_name: str
    nickname: str
    gender: str
    weight_class_id: int
    country: Optional[str] = None

class FighterResponse(FighterCreate):
    fighter_id: int
    nickname: Optional[str] = None
    country: Optional[str] = None

    class Config:
        from_attributes = True

#dependencia para obtener la sesion de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dep = Annotated[Session, Depends(get_db)] #esto significa que db_dep es una sesion de la base de datos que se obtiene a traves de la dependencia get_db

#para crear rutas en fastapi
@app.get("/")
def root():
    return {"message": "running"}

#endpoint para crear un luchador
@app.post("/fighters/", response_model=FighterResponse)
def create_fighter(fighter: FighterCreate, db: db_dep):
    db_f = models.Fighter(**fighter.dict())
    db.add(db_f)
    db.commit()
    db.refresh(db_f)
    return db_f

#endpoint para obtener todos los luchadores
@app.get("/fighters/", response_model=list[FighterResponse])
def get_fighters(db: db_dep):
    return db.query(models.Fighter).all()