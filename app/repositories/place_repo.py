from sqlalchemy.orm import Session
from app.models.models import Place


def create_place(db: Session, place: Place):
    db.add(place)
    return place


def get_place(db: Session, place_id: int):
    return db.get(Place, place_id)


def get_places_by_project(db: Session, project_id: int):
    return db.query(Place).filter_by(project_id=project_id).all()


def get_by_external_id(db: Session, project_id: int, external_id: int):
    return db.query(Place).filter_by(
        project_id=project_id,
        external_id=external_id
    ).first()