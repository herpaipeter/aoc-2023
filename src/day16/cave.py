from dataclasses import dataclass
from enum import Enum

from src.common.point import Point, Direction


class CaveTileType(Enum):
    EMPTY = "."
    V_SPLITTER = "|"
    H_SPLITTER = "-"
    UL_BR_MIRROR = "\\"
    BL_UR_MIRROR = "/"


@dataclass(frozen=True)
class BeamTile:
    position: Point
    direction: Direction


@dataclass
class CaveTile:
    position: Point
    type: CaveTileType

    def next_tiles(self, direction: Direction) -> list[BeamTile]:
        if self.type == CaveTileType.H_SPLITTER:
            if direction == Direction.RIGHT or direction == Direction.LEFT:
                return [BeamTile(self.position + direction, direction)]
            else:
                return [BeamTile(self.position + Direction.LEFT, Direction.LEFT), BeamTile(self.position + Direction.RIGHT, Direction.RIGHT)]
        elif self.type == CaveTileType.V_SPLITTER:
            if direction == Direction.UP or direction == Direction.DOWN:
                return [BeamTile(self.position + direction, direction)]
            else:
                return [BeamTile(self.position + Direction.UP, Direction.UP), BeamTile(self.position + Direction.DOWN, Direction.DOWN)]
        elif self.type == CaveTileType.UL_BR_MIRROR:
            if direction == Direction.RIGHT:
                return [BeamTile(self.position+ Direction.DOWN, Direction.DOWN)]
            elif direction == Direction.LEFT:
                return [BeamTile(self.position+ Direction.UP, Direction.UP)]
            elif direction == Direction.DOWN:
                return [BeamTile(self.position+ Direction.RIGHT, Direction.RIGHT)]
            elif direction == Direction.UP:
                return [BeamTile(self.position+ Direction.LEFT, Direction.LEFT)]
        elif self.type == CaveTileType.BL_UR_MIRROR:
            if direction == Direction.RIGHT:
                return [BeamTile(self.position+ Direction.UP, Direction.UP)]
            elif direction == Direction.LEFT:
                return [BeamTile(self.position+ Direction.DOWN, Direction.DOWN)]
            elif direction == Direction.DOWN:
                return [BeamTile(self.position+ Direction.LEFT, Direction.LEFT)]
            elif direction == Direction.UP:
                return [BeamTile(self.position+ Direction.RIGHT, Direction.RIGHT)]
        return [BeamTile(self.position + direction, direction)]

@dataclass
class Cave:
    tiles: list[CaveTile]
    rows: int
    cols: int