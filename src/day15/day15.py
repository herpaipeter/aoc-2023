import re
from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.day15.lens import LensCommand, LensOperation, get_hash


def parse_lens_command(commmand_txt: str) -> LensCommand:
    texts = re.split("[=|-]", commmand_txt)
    eq_num = commmand_txt.count("=")
    return LensCommand(texts[0], LensOperation.ADD if 0 < eq_num else LensOperation.REMOVE,
                       int(texts[1]) if 0 < eq_num else 0)


@runifmain(__name__)
class Day15(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        return input_data.split(",")

    def part1(self, data) -> Any:
        return sum(map(get_hash, data))

    def part2(self, data) -> Any:
        commands = list(map(parse_lens_command, data))
        boxes = []
        for i in range(256):
            boxes.append([])
        for c in commands:
            if c.operation == LensOperation.REMOVE:
                del_index = list(map(lambda index_elem: index_elem[0],
                                     filter(lambda index_elem: index_elem[1].label == c.label,
                                            enumerate(boxes[c.index]))))
                if 0 < len(del_index):
                    del (boxes[c.index][del_index[0]])
                # try:
                #     boxes[c.index].remove(c)
                # except ValueError:
                #     pass
            else:
                found_index = list(map(lambda index_elem: index_elem[0],
                                       filter(lambda index_elem: index_elem[1].label == c.label,
                                              enumerate(boxes[c.index]))))
                if 0 < len(found_index):
                    boxes[c.index][found_index[0]].value = c.value
                else:
                    boxes[c.index].append(c)
                # try:
                #     c_in_box_index = boxes[c.index].index(c)
                #     boxes[c.index][c_in_box_index].value = c.value
                # except ValueError:
                #     boxes[c.index].append(c)
        result = 0
        for box_index, b in enumerate(boxes):
            for lens_index, l in enumerate(b):
                result += (box_index + 1) * (lens_index + 1) * l.value
        return result
