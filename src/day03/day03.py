from functools import reduce
from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.common.point import Point
from src.day03.engine_part import EngineNumber, EngineSymbol


def append_number_and_reset(number, row, pos_end, pos_start, obj_list):
    if 0 < len(number):
        obj_list.append(EngineNumber(int(number), Point(row, pos_start), Point(row, pos_end)))
        number = ""
    return number


@runifmain(__name__)
class Day03(AocSolver):
    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        lines = input_data.split('\n')
        numbers_symbols_lines = [self.parseLine(line, row) for row, line in enumerate(lines)]
        return reduce(lambda list1, list2: list1 + list2, numbers_symbols_lines)

    def part1(self, data) -> Any:
        symbols = list(filter(lambda o: isinstance(o, EngineSymbol), data))
        numbers = list(filter(lambda o: isinstance(o, EngineNumber), data))
        adjacent_numbers = filter(lambda n: self.is_adjacent_to_any_symbol(n, symbols), numbers)
        return sum(map(lambda n: n.number, adjacent_numbers))

    def part2(self, data) -> Any:
        symbols = list(filter(lambda o: isinstance(o, EngineSymbol) and o.symbol == "*", data))
        numbers = list(filter(lambda o: isinstance(o, EngineNumber), data))
        result = 0
        for symbol in symbols:
            next_numbers = self.get_adjacent_numbers(symbol, numbers)
            if 2 == len(next_numbers):
                result += next_numbers[0].number * next_numbers[1].number
        return result

    def parseLine(self, line, row):
        result = []
        number = ""
        number_start_col = 0
        number_end_col = 0
        for i in range(len(line)):
            if str(line[i]).isdigit():
                number += line[i]
                number_end_col = i
            elif line[i] == ".":
                number = append_number_and_reset(number, row, number_end_col, number_start_col, result)
                number_start_col = i + 1
            else:
                number = append_number_and_reset(number, row, number_end_col, number_start_col, result)
                result.append(EngineSymbol(line[i], Point(row, i)))
                number_start_col = i + 1
        append_number_and_reset(number, row, number_end_col, number_start_col, result)
        return result

    def is_adjacent_to_any_symbol(self, number, symbols) -> bool:
        return any(self.is_adjacent(number, s) for s in symbols)

    def get_adjacent_numbers(self, symbol, numbers) -> list:
        return list(filter(lambda number: self.is_adjacent(number, symbol), numbers))

    def is_adjacent(self, number: EngineNumber, symbol: EngineSymbol) -> bool:
        return (number.end.row - 1 <= symbol.position.row <= number.end.row + 1
                and number.start.col - 1 <= symbol.position.col <= number.end.col + 1)
