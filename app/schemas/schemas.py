from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class PlaceCreate(BaseModel):
    external_id: int

class PlaceUpdate(BaseModel):
    notes: Optional[str]
    visited: Optional[bool]

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str]
    start_date: Optional[date]
    places: Optional[List[PlaceCreate]] = []

class ProjectUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    start_date: Optional[date]