import math
from dataclasses import dataclass
from enum import Enum


class Instruction(Enum):
    LEFT = 0
    RIGHT = 1

    def __repr__(self):
        return "L" if self == self.LEFT else "R"

    def __str__(self):
        return self.__repr__()


@dataclass
class Node:
    start: str
    left: str
    right: str


@dataclass
class Map:
    instructions: list[Instruction]
    nodes: list[Node]

    def get_next(self, start, direction):
        node = next(n for n in self.nodes if n.start == start)
        return node.left if direction == Instruction.LEFT else node.right

    def iterate(self, start, end):
        next_node = next(n.start for n in self.nodes if n.start == start)
        counter = 0
        while next_node != end:
            direction = self.instructions[counter % len(self.instructions)]
            next_node = self.get_next(next_node, direction)
            counter += 1
        return counter

    def iterate_last_char_end(self, start, end_last):
        next_node = next(n.start for n in self.nodes if n.start == start)
        counter = 0
        while next_node[2] != end_last:
            direction = self.instructions[counter % len(self.instructions)]
            next_node = self.get_next(next_node, direction)
            counter += 1
        return counter

    def iterate_parallel(self, start_last, end_last):
        next_nodes = list(map(lambda n: n.start, filter(lambda n: n.start[2] == start_last, self.nodes)))
        counters = list(map(lambda n: self.iterate_last_char_end(n, end_last), next_nodes))
        return math.lcm(*counters)