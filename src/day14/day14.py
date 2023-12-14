from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.common.point import Point
from src.day14.rock import Rock, RockType, RockMap


def parse_line(line: str, row: int) -> list[Rock]:
    result = []
    for index, c in enumerate(line):
        if c == "O":
            result.append(Rock(RockType.ROUND, Point(row, index)))
        if c == "#":
            result.append(Rock(RockType.SQUARE, Point(row, index)))
    return result


def tilt_north(rocks: list[Rock]) -> list[Rock]:
    result = []
    rocks.sort()
    for r in rocks:
        if r.type == RockType.ROUND:
            rocks_above = list(map(lambda rock: rock.position.row,
                                   filter(lambda
                                              rock: rock.position.col == r.position.col and rock.position.row < r.position.row,
                                          result)))
            rocks_above.sort(reverse=True)
            row_pos = rocks_above[0] + 1 if 0 < len(rocks_above) else 0
            result.append(Rock(r.type, Point(row_pos, r.position.col)))
        else:
            result.append(r)
    return result


def tilt_west(rocks: list[Rock]) -> list[Rock]:
    result = []
    rocks.sort(key=lambda rock: [rock.position.col, rock.position.row])
    for r in rocks:
        if r.type == RockType.ROUND:
            rocks_above = list(map(lambda rock: rock.position.col,
                                   filter(lambda
                                              rock: rock.position.row == r.position.row and rock.position.col < r.position.col,
                                          result)))
            rocks_above.sort(reverse=True)
            col_pos = rocks_above[0] + 1 if 0 < len(rocks_above) else 0
            result.append(Rock(r.type, Point(r.position.row, col_pos)))
        else:
            result.append(r)
    return result


def tilt_south(rocks: list[Rock], rows_num: int) -> list[Rock]:
    result = []
    rocks.sort(reverse=True)
    for r in rocks:
        if r.type == RockType.ROUND:
            rocks_above = list(map(lambda rock: rock.position.row,
                                   filter(lambda
                                              rock: rock.position.col == r.position.col and rock.position.row > r.position.row,
                                          result)))
            rocks_above.sort()
            row_pos = rocks_above[0] - 1 if 0 < len(rocks_above) else rows_num - 1
            result.append(Rock(r.type, Point(row_pos, r.position.col)))
        else:
            result.append(r)
    return result


def tilt_east(rocks: list[Rock], col_nums: int) -> list[Rock]:
    result = []
    rocks.sort(key=lambda rock: [rock.position.col, rock.position.row], reverse=True)
    for r in rocks:
        if r.type == RockType.ROUND:
            rocks_above = list(map(lambda rock: rock.position.col,
                                   filter(lambda
                                              rock: rock.position.row == r.position.row and rock.position.col > r.position.col,
                                          result)))
            rocks_above.sort()
            col_pos = rocks_above[0] - 1 if 0 < len(rocks_above) else col_nums - 1
            result.append(Rock(r.type, Point(r.position.row, col_pos)))
        else:
            result.append(r)
    return result


def total_load(rock_map: RockMap) -> int:
    result = 0
    for r in rock_map.rocks:
        if r.type == RockType.ROUND:
            result += (rock_map.rows_num - r.position.row)
    return result


def spin_cycle(rock_map: RockMap) -> RockMap:
    tilted = tilt_north(rock_map.rocks)
    tilted = tilt_west(tilted)
    tilted = tilt_south(tilted, rock_map.rows_num)
    tilted = tilt_east(tilted, rock_map.cols_num)
    return RockMap(tilted, rock_map.rows_num, rock_map.cols_num)


@runifmain(__name__)
class Day14(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        enumerated = list(enumerate(input_data.split("\n")))
        rocks = list(map(lambda lineindex: parse_line(lineindex[1], lineindex[0]), enumerated))
        rocks = [j for i in rocks for j in i]
        rows_num = len(enumerated)
        cols_num = len(enumerated[0][1]) if 0 < len(enumerated) else 0
        return RockMap(rocks, rows_num, cols_num)

    def part1(self, data: RockMap) -> Any:
        moved = tilt_north(data.rocks)
        return total_load(RockMap(moved, data.rows_num, data.cols_num))

    def part2(self, data) -> Any:
        cycle = spin_cycle(data)
        cycles = [cycle]
        found_indexes = [-1]
        for i in range(1000000000):
            cycle = spin_cycle(cycle)
            try:
                ind = cycles.index(cycle)
                try:
                    found_indexes.index(ind)
                    break
                except:
                    pass
                found_indexes.append(ind)
            except:
                found_indexes.append(-1)
            cycles.append(cycle)
        no_repeat_start_len = len(list(filter(lambda ind: ind == -1, found_indexes)))
        repeat_pattern_len = len(list(filter(lambda ind: ind != -1, found_indexes)))
        cycle_at_billion = no_repeat_start_len + (1000000000 - no_repeat_start_len) % repeat_pattern_len - 1

        print("no_repeat_start_len", no_repeat_start_len)
        print("repeat_pattern_len", repeat_pattern_len)
        print("cycle_at_billion", cycle_at_billion)
        # example: cycle_at_billion = 9 + (1000000000 - 9) % 7 - 1
        # input: cycle_at_billion = 158 + (1000000000 - 158) % 65 - 1

        return total_load(cycles[cycle_at_billion])
