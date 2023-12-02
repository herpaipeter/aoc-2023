import abc
import pathlib
import sys
from abc import ABC
from typing import Any


class AocSolver(ABC):

    @abc.abstractmethod
    def parse(self, input_data) -> Any:
        """Parse input."""

    @abc.abstractmethod
    def part1(self, data) -> Any:
        """Solve part 1."""

    @abc.abstractmethod
    def part2(self, data) -> Any:
        """Solve part 2."""

    def solve(self, input_data):
        """Solve the puzzle for the given input."""
        data = self.parse(input_data)
        solution1 = self.part1(data)
        solution2 = self.part2(data)

        return solution1, solution2


def runifmain(mainname):
    def deco(clas):
        if mainname == '__main__':
            for path in sys.argv[1:]:
                print(f"{path}:")
                puzzle_input = pathlib.Path(path).read_text().strip()
                solutions = clas().solve(puzzle_input)
                print("\n".join(str(solution) for solution in solutions))
        return clas

    return deco

# if __name__ == "__main__":
#     for path in sys.argv[1:]:
#         print(f"{path}:")
#         puzzle_input = pathlib.Path(path).read_text().strip()
#         solutions = AocSolver().solve(puzzle_input)
#         print("\n".join(str(solution) for solution in solutions))
