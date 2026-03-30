from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import place_service
from app.schemas.schemas import PlaceCreate, PlaceUpdate

router = APIRouter(prefix="/projects/{project_id}/places", tags=["Places"])


@router.post("/")
async def add_place(project_id: int, payload: PlaceCreate, db: Session = Depends(get_db)):
    return await place_service.add_place(db, project_id, payload)


@router.get("/")
def list_places(project_id: int, db: Session = Depends(get_db)):
    return place_service.list_places(db, project_id)


@router.get("/{place_id}")
def get_place(project_id: int, place_id: int, db: Session = Depends(get_db)):
    return place_service.get_place(db, project_id, place_id)


@router.patch("/{place_id}")
def update_place(project_id: int, place_id: int, payload: PlaceUpdate, db: Session = Depends(get_db)):
    return place_service.update_place(db, project_id, place_id, payload)