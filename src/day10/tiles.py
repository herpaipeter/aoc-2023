from dataclasses import dataclass
from enum import Enum

from src.common.point import Point

class TileType(Enum):
    EMPTY = 0
    START = 1
    PIPE = 2
    PIPE_VERTICAL = 3

@dataclass
class Tile:
    end1: Point
    end2: Point
    symbol: str
    type: TileType