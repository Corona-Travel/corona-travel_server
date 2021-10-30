from typing import List
from pydantic import BaseModel


class Position(BaseModel):
    lat: float
    lng: float


class Marker(BaseModel):
    name: str
    pos: Position
    place_id: str

Markers = List[Marker]
