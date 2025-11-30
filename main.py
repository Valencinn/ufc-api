from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated, Optional
from pydantic import BaseModel

import models
from db import SessionLocal, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dep = Annotated[Session, Depends(get_db)]


@app.get("/")
def root():
    return {"message": "running"}

@app.post("/fighters/", response_model=FighterResponse)
def create_fighter(fighter: FighterCreate, db: db_dep):
    db_f = models.Fighter(**fighter.dict())
    db.add(db_f)
    db.commit()
    db.refresh(db_f)
    return db_f

@app.get("/fighters/", response_model=list[FighterResponse])
def get_fighters(db: db_dep):
    return db.query(models.Fighter).all()