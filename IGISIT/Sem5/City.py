from dataclasses import dataclass

from Bounds import Bounds
from Coordinate import Coordinate


@dataclass
class City:
    name: str
    bounds: Bounds
    location: Coordinate
