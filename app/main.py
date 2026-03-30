from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import project_router, place_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(project_router.router)
app.include_router(place_router.router)