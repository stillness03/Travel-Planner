from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.models import Place
from app.repositories import place_repo, project_repo
from app.integrations.artic_validation import fetch_artwork

MAX_PLACES = 10


async def add_place(db: Session, project_id: int, payload):
    project = project_repo.get_project(db, project_id)

    if not project:
        raise HTTPException(404)

    if len(project.places) >= MAX_PLACES:
        raise HTTPException(400, "Max 10 places per project")

    exists = place_repo.get_by_external_id(
        db, project_id, payload.external_id
    )
    if exists:
        raise HTTPException(400, "Place already exists")

    artwork = await fetch_artwork(payload.external_id)
    if not artwork:
        raise HTTPException(404)

    place = Place(
        project_id=project_id,
        external_id=payload.external_id,
        title=artwork.get("title")
    )

    place_repo.create_place(db, place)
    db.commit()
    return place


def update_place(db: Session, project_id: int, place_id: int, payload):
    place = place_repo.get_place(db, place_id)

    if not place or place.project_id != project_id:
        raise HTTPException(404)

    for key, value in payload.dict(exclude_unset=True).items():
        setattr(place, key, value)

    db.commit()
    return place


def list_places(db: Session, project_id: int):
    return place_repo.get_places_by_project(db, project_id)


def get_place(db: Session, project_id: int, place_id: int):
    place = place_repo.get_place(db, place_id)

    if not place or place.project_id != project_id:
        raise HTTPException(404)

    return place