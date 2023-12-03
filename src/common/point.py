from dataclasses import dataclass


@dataclass
class Point:
    row: int
    col: int

    def __repr__(self):
        return "[" + str(self.row) + "," + str(self.col) + "]"
