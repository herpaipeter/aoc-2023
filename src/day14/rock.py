from dataclasses import dataclass
from enum import Enum

from src.common.point import Point


class RockType(Enum):
    ROUND = 0
    SQUARE = 1


@dataclass
class Rock:
    type: RockType
    position: Point

    def __lt__(self, other):
        if not isinstance(other, Rock):
            raise NotImplementedError
        return (self.position.row < other.position.row
                or self.position.row == other.position.row and self.position.col < other.position.col)


@dataclass
class RockMap:
    rocks: list[Rock]
    rows_num: int
    cols_num: int

    def __repr__(self):
        result = ""
        for row in range(self.rows_num):
            for col in range(self.cols_num):
                filtered = list(filter(lambda r: r.position.row == row and r.position.col == col, self.rocks))
                if 0 < len(filtered):
                    result += "O" if filtered[0].type == RockType.ROUND else "#"
                else:
                    result += "."
            result += "\n"
        return result

    def __eq__(self, other):
        if not isinstance(other, RockMap):
            raise NotImplementedError
        self.rocks.sort()
        other.rocks.sort()
        return self.rocks == other.rocks
