from typing import Any

from src.aoc_solver import runifmain, AocSolver


def parse_line(line):
    return list(map(int, line.strip().split(" ")))


def get_diffs(series):
    result = []
    if 1 < len(series):
        for i in range(len(series) - 1):
            result.append(series[i + 1] - series[i])
    return result


def append_last_to_list(last_elements, series):
    last_elements.append(series[len(series) - 1])
    return series


def append_first_to_list(first_elements, series):
    first_elements.append(series[0])
    return series


def get_prev(series):
    first_elements = []
    diffs = append_first_to_list(first_elements, series)
    while 0 != diffs[len(diffs) - 1]:
        diffs = append_first_to_list(first_elements, get_diffs(diffs))
    first_elements.reverse()
    actual = 0
    for number in first_elements:
        actual = number - actual
    return actual


def get_next(series):
    last_elements = []
    diffs = append_last_to_list(last_elements, series)
    while 0 != diffs[len(diffs) - 1]:
        diffs = append_last_to_list(last_elements, get_diffs(diffs))
    return sum(last_elements)


@runifmain(__name__)
class Day09(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        lines = input_data.strip().split("\n")
        return list(map(lambda line: parse_line(line), lines))

    def part1(self, data) -> Any:
        return sum(map(lambda n: get_next(n), data))

    def part2(self, data) -> Any:
        return sum(map(lambda n: get_prev(n), data))
        pass
