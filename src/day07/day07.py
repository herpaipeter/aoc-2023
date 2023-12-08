from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.day07.card import Bid, Hand


@runifmain(__name__)
class Day07(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        lines = input_data.split('\n')
        return list(map(lambda line: self.parseLine(line), lines))

    def part1(self, data) -> Any:
        data.sort()
        result = 0
        for i, bid in enumerate(data):
            result += bid.amount * (i + 1)
        return result

    def part2(self, data) -> Any:
        jokerized = list(map(lambda bid: Bid(Hand(bid.hand.cards, True), bid.amount), data))
        return self.part1(jokerized)

    def parseLine(self, text):
        hand, bid = text.split(" ")
        return Bid(Hand(hand), int(bid))
