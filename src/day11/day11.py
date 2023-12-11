import time
from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.common.point import Point


def read_line(line_txt: str, row: int) -> list[Point]:
    return list(
        map(lambda col_char: Point(row, col_char[0]), filter(lambda col_char: col_char[1] == "#", enumerate(line_txt))))


def get_empty_rows(points: list[Point]) -> list[int]:
    result = []
    sorted_points = sorted(points, key=lambda p: p.row)
    if 1 < len(sorted_points):
        for i in range(len(sorted_points) - 1):
            for row in range(sorted_points[i].row + 1, sorted_points[i + 1].row):
                result.append(row)
    return result


def get_empty_cols(points: list[Point]) -> list[int]:
    result = []
    sorted_points = sorted(points, key=lambda p: p.col)
    if 1 < len(sorted_points):
        for i in range(len(sorted_points) - 1):
            for col in range(sorted_points[i].col + 1, sorted_points[i + 1].col):
                result.append(col)
    return result


def add_empty_rows(points: list[Point], empty_rows: list[int], multi: int = 2):
    sorted_points = sorted(points, key=lambda p: p.row)
    return list(map(lambda point: get_expanded_row_point(point, multi, empty_rows), sorted_points))


def get_expanded_row_point(point, multi, empty_rows):
    empties_below = len(list(filter(lambda r: r < point.row, empty_rows)))
    return Point(point.row + (multi - 1) * empties_below, point.col)


def add_empty_cols(points: list[Point], empty_cols: list[int], multi: int = 2):
    sorted_points = sorted(points, key=lambda p: p.col)
    return list(map(lambda point: get_expanded_col_point(point, multi, empty_cols), sorted_points))


def get_expanded_col_point(point, multi, empty_cols):
    empties_below = len(list(filter(lambda c: c < point.col, empty_cols)))
    return Point(point.row, point.col + (multi - 1) * empties_below)


@runifmain(__name__)
class Day11(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        result = []
        for row, line in enumerate(input_data.split("\n")):
            result += read_line(line, row)
        return result

    def part1(self, data, multi=2) -> Any:
        empty_rows = get_empty_rows(data)
        empty_cols = get_empty_cols(data)
        result = add_empty_rows(data, empty_rows, multi)
        result = add_empty_cols(result, empty_cols, multi)
        sum_dist = 0
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                sum_dist += result[i].m_dist(result[j])
        return sum_dist

    def part2(self, data, multi) -> Any:
        return self.part1(data, multi)

    def solve(self, input_data):
        """Solve the puzzle for the given input."""
        t_start = time.perf_counter_ns()
        data = self.parse(input_data)
        t_parse = time.perf_counter_ns()
        solution1 = self.part1(data)
        t_part1 = time.perf_counter_ns()
        solution2 = self.part2(data, 1_000_000)
        t_part2 = time.perf_counter_ns()

        self.logger.info("Parse execution time: %0.4f ms", (t_parse - t_start) / 1_000_000)
        self.logger.info("Part 1 execution time: %0.4f ms", (t_part1 - t_parse) / 1_000_000)
        self.logger.info("Part 2 execution time: %0.4f ms", (t_part2 - t_part1) / 1_000_000)

        return solution1, solution2
