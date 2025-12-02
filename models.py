from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from db import Base

#el formato para crear las clases es completar los campos IDENTICAMENTE a como están en la base de datos, mismos nombres y tipos de datos

class Fighter(Base):
    __tablename__ = "fighters"

    fighter_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    nickname = Column(String, index=True)
    gender = Column(String, index=True)
    weight_class_id = Column(Integer, index=True)
    country = Column(String, index=True)

class Divisions(Base):
    __tablename__ = "divisions"

    weight_class_id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, index=True)
    gender = Column(String, index=True)

class Events(Base):
    __tablename__ = "events"

    edition_number = Column(Integer, primary_key=True, index=True)
    event_name = Column(String(255))
    event_date = Column(Date)
    location_name = Column(String(255))  # Nota: en el modelo anterior era 'location'

class Fight(Base):
    __tablename__ = "fights"

    fight_id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    fighter_red = Column(Integer, ForeignKey("fighters.fighter_id"), nullable=False)
    fighter_blue = Column(Integer, ForeignKey("fighters.fighter_id"), nullable=False)
    winner = Column(Integer, ForeignKey("fighters.fighter_id"), nullable=True)
    method = Column(String(80))
    round_number = Column(Integer)
    notes = Column(String(255))