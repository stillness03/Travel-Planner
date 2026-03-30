from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(String, nullable=True)

    places = relationship('Place', back_populates='project', cascade='all, delete-orphan')


class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    external_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    visited = Column(Boolean, default=False)

    project = relationship('Project', back_populates='places')

