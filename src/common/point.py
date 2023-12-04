from dataclasses import dataclass
from enum import Enum


@dataclass
class Point:
    row: int
    col: int

    def __repr__(self):
        return "[" + str(self.row) + "," + str(self.col) + "]"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.row + other.row, self.col + other.col)
        elif isinstance(other, Direction):
            return Point(self.row + other.value.row, self.col + other.value.col)
        elif isinstance(other, int):
            return Point(self.row + other, self.col + other)
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.row * other, self.col * other)
        raise NotImplementedError

    def __neg__(self):
        return Point(-self.row, -self.col)


class Direction(Enum):
    RIGHT = Point(0, 1)
    LEFT = Point(0, -1)
    UP = Point(-1, 0)
    DOWN = Point(1, 0)
