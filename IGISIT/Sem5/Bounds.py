from dataclasses import dataclass

from Coordinate import Coordinate


@dataclass
class Bounds:
    northeast: Coordinate
    southwest: Coordinate
