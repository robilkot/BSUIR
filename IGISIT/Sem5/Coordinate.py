from dataclasses import dataclass


@dataclass
class Coordinate:
    lat: float
    lng: float

    def __hash__(self):
        return hash((self.lat, self.lng))
