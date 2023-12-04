import abc
import logging
import pathlib
import sys
import time
from abc import ABC
from typing import Any

logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
                    datefmt='%H:%M:%S')


class AocSolver(ABC):

    def __init__(self, classname):
        self.logger = logging.getLogger(classname)
        self.logger.setLevel(logging.DEBUG)

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
        t_start = time.perf_counter_ns()
        data = self.parse(input_data)
        t_parse = time.perf_counter_ns()
        solution1 = self.part1(data)
        t_part1 = time.perf_counter_ns()
        solution2 = self.part2(data)
        t_part2 = time.perf_counter_ns()

        self.logger.info("Parse execution time: %0.4f ms", (t_parse - t_start) / 1_000_000)
        self.logger.info("Part 1 execution time: %0.4f ms", (t_part1 - t_parse) / 1_000_000)
        self.logger.info("Part 2 execution time: %0.4f ms", (t_part2 - t_part1) / 1_000_000)

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
