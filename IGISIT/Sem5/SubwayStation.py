from dataclasses import dataclass

from Coordinate import Coordinate


@dataclass
class SubwayStation:
    name: str
    location: Coordinate

    def __hash__(self):
        return hash(self.name)
