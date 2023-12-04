from dataclasses import dataclass
from typing import Any

from src.aoc_solver import runifmain, AocSolver


@dataclass
class Card:
    winning_numbers: list
    numbers: list

    def point(self) -> int:
        match = self.match()
        return 2 ** (match - 1) if 2 < match else match

    def match(self) -> int:
        return sum(map(lambda win_num: self.numbers.count(win_num), self.winning_numbers))


@runifmain(__name__)
class Day04(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        lines = input_data.split('\n')
        return list(map(lambda line: self.parseLine(line), lines))

    def part1(self, data) -> Any:
        return sum(map(lambda card: card.point(), data))

    def part2(self, data) -> Any:
        cards_count = [1] * len(data)
        for index, card in enumerate(data):
            for i in range(index + 1, index + 1 + card.match()):
                cards_count[i] += cards_count[index]
        return sum(cards_count)

    def parseLine(self, line) -> Card:
        wn_txt, n_txt = line.split(":")[1].split("|")
        wn_splitted = filter(lambda num: 0 < len(num), wn_txt.split(" "))
        n_splitted = filter(lambda num: 0 < len(num), n_txt.split(" "))
        wn = list(map(lambda num: int(num.strip()), wn_splitted))
        n = list(map(lambda num: int(num.strip()), n_splitted))
        return Card(wn, n)
