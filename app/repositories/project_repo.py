from sqlalchemy.orm import Session
from app.models.models import Project


def create_project(db: Session, project: Project):
    db.add(project)
    db.flush()
    return project

def get_project(db: Session, project_id: int):
    return db.get(Project, project_id)

def get_all_projects(db: Session):
    return db.query(Project).all()

def delete_project(db: Session, project_id: int):
    db.delete(get_project(db, project_id))

def update_project(db: Session, project: Project, data: dict):
    for key, value in data.items():
        setattr(project, key, value)
    return project
