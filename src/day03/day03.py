from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.common.point import Point
from src.day03.position import NumberPosition, SymbolPosition


def append_number_and_reset(number, row, pos_end, pos_start, obj_list):
    if 0 < len(number):
        obj_list.append(NumberPosition(int(number), Point(row, pos_start), Point(row, pos_end)))
        number = ""
    return number


@runifmain(__name__)
class Day03(AocSolver):
    def parse(self, input_data) -> Any:
        lines = input_data.split('\n')
        result = []
        for row in range(len(lines)):
            result += self.parseLine(lines[row], row)
        return result

    def part1(self, data) -> Any:
        symbols = list(filter(lambda o: isinstance(o, SymbolPosition), data))
        numbers = list(filter(lambda o: isinstance(o, NumberPosition), data))
        result = 0
        for number in numbers:
            if self.is_next_to_symbols(number, symbols):
                result += number.number
        return result

    def part2(self, data) -> Any:
        symbols = list(filter(lambda o: isinstance(o, SymbolPosition) and o.symbol == "*", data))
        numbers = list(filter(lambda o: isinstance(o, NumberPosition), data))
        result = 0
        for symbol in symbols:
            next_numbers = self.get_next_numbers(symbol, numbers)
            if 2 == len(next_numbers):
                result += next_numbers[0].number * next_numbers[1].number
        return result

    def parseLine(self, param, row):
        result = []
        number = ""
        pos_start = 0
        pos_end = 0
        for i in range(len(param)):
            if str(param[i]).isdigit():
                number += param[i]
                pos_end = i
            elif param[i] == ".":
                number = append_number_and_reset(number, row, pos_end, pos_start, result)
                pos_start = i + 1
            else:
                number = append_number_and_reset(number, row, pos_end, pos_start, result)
                result.append(SymbolPosition(param[i], Point(row, i)))
                pos_start = i + 1
        append_number_and_reset(number, row, pos_end, pos_start, result)
        return result

    def is_next_to_symbols(self, number_pos, symbols) -> bool:
        for symbol in symbols:
            if self.is_next_to(number_pos, symbol):
                return True
        return False

    def get_next_numbers(self, symbol_pos, numbers) -> list:
        result = []
        for number in numbers:
            if self.is_next_to(number, symbol_pos):
                result.append(number)
        return result

    def is_next_to(self, number_pos: NumberPosition, symbol_pos: SymbolPosition) -> bool:
        if (number_pos.pos_to.row - 1 <= symbol_pos.position.row <= number_pos.pos_to.row + 1
                and number_pos.pos_from.col - 1 <= symbol_pos.position.col <= number_pos.pos_to.col + 1):
            return True
        return False
