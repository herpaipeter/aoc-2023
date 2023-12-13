from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.day13.pattern import Pattern


@runifmain(__name__)
class Day13(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        patterns = input_data.split("\n\n")
        return list(map(lambda p: Pattern(p), patterns))

    def part1(self, data: list[Pattern]) -> Any:
        count = 0
        for p in data:
            count += 100 * p.get_h_refl()
            count += p.get_v_refl()
        return count

    def part2(self, data: list[Pattern]) -> Any:
        count = 0
        for p in data:
            count += 100 * p.get_h_refl_smudge()
            count += p.get_v_refl_smudge()
        return count
