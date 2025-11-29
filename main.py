from fastapi import FastAPI
from routers import fighters, divisions, events, fights

app = FastAPI(
    title="UFC API",
    version="1.0",
    description="UFC API practice project using FastAPI + MySQL"
)

app.include_router(fighters.router)
app.include_router(divisions.router)
app.include_router(events.router)
app.include_router(fights.router)