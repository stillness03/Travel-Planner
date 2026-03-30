from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.models import Project, Place
from app.repositories import project_repo, place_repo
from app.integrations.artic_validation import fetch_artwork


MAX_PLACES = 10


async def create_project(db: Session, payload):
    if payload.places and len(payload.places) > MAX_PLACES:
        raise HTTPException(400, "Max 10 places allowed")

    project = Project(
        name=payload.name,
        description=payload.description,
        start_date=payload.start_date
    )

    project_repo.create_project(db, project)

    for p in payload.places or []:
        artwork = await fetch_artwork(p.external_id)
        if not artwork:
            raise HTTPException(404, "Artwork not found")

        place = Place(
            project_id=project.id,
            external_id=p.external_id,
            title=artwork.get("title")
        )
        place_repo.create_place(db, place)

    db.commit()
    db.refresh(project)
    return project


def delete_project(db: Session, project_id: int):
    project = project_repo.get_project(db, project_id)

    if not project:
        raise HTTPException(404)

    if any(p.visited for p in project.places):
        raise HTTPException(400, "Cannot delete project with visited places")

    project_repo.delete_project(db, project)
    db.commit()


def update_project(db: Session, project_id: int, payload):
    project = project_repo.get_project(db, project_id)

    if not project:
        raise HTTPException(404)

    project_repo.update_project(
        db,
        project,
        payload.dict(exclude_unset=True)
    )

    db.commit()
    return project


def get_project(db: Session, project_id: int):
    project = project_repo.get_project(db, project_id)
    if not project:
        raise HTTPException(404)
    return project


def list_projects(db: Session):
    return project_repo.get_all_projects(db)