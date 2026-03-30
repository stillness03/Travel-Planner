from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import project_service
from app.schemas.schemas import ProjectCreate, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
async def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    return await project_service.create_project(db, payload)


@router.get("/")
def list_projects(db: Session = Depends(get_db)):
    return project_service.list_projects(db)


@router.get("/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    return project_service.get_project(db, project_id)


@router.put("/{project_id}")
def update_project(project_id: int, payload: ProjectUpdate, db: Session = Depends(get_db)):
    return project_service.update_project(db, project_id, payload)


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project_service.delete_project(db, project_id)
    return {"message": "Deleted"}