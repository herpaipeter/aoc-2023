from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.day08.nodes import Instruction, Node, Map


@runifmain(__name__)
class Day08(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        instructions_txt, nodes_txt = input_data.split('\n\n')
        nodes_lines = nodes_txt.split("\n")
        instructions = self.parseInstructions(instructions_txt)
        nodes = list(map(lambda n: self.parseNode(n), nodes_lines))
        return Map(instructions, nodes)

    def part1(self, data) -> Any:
        return data.iterate("AAA", "ZZZ")

    def part2(self, data) -> Any:
        return data.iterate_parallel("A", "Z")
        pass

    def parseInstructions(self, text):
        result = []
        for c in text:
            if c == "R":
                result.append(Instruction.RIGHT)
            elif c == "L":
                result.append(Instruction.LEFT)
        return result

    @classmethod
    def parseNode(cls, text):
        start, end = text.split("=")
        left, right = end.replace("(", "").replace(")", "").split(",")
        return Node(start.strip(), left.strip(), right.strip())
