import pathlib
import pytest

from src.day08.nodes import Instruction, Node, Map

from src.day08 import day08

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_instruction_right():
    assert [Instruction.RIGHT] == day08.Day08().parseInstructions("R")


def test_parse_instruction_left():
    assert [Instruction.LEFT] == day08.Day08().parseInstructions("L")


def test_parse_instruction_left_right():
    assert [Instruction.LEFT, Instruction.RIGHT] == day08.Day08().parseInstructions("LR")


def test_parse_node_line():
    assert Node("AAA", "BBB", "CCC") == day08.Day08.parseNode("AAA = (BBB, CCC)")


def test_map_move_left():
    d_map = Map([Instruction.LEFT, Instruction.RIGHT], [Node("AAA", "BBB", "CCC"), Node("BBB", "DDD", "EEE")])
    assert "BBB" == d_map.get_next("AAA", Instruction.LEFT)


def test_map_move_right():
    d_map = Map([Instruction.LEFT, Instruction.RIGHT], [Node("AAA", "BBB", "CCC"), Node("BBB", "DDD", "EEE")])
    assert "EEE" == d_map.get_next("BBB", Instruction.RIGHT)


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day08.Day08().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day08.Day08().parse(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return day08.Day08().parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = day08.Day08().part1(example1)
    assert result == 2


def test_part1_example2(example2):
    """Test part 1 on example input."""
    result = day08.Day08().part1(example2)
    assert result == 6


def test_part2_example3(example3):
    """Test part 2 on example input."""
    result = day08.Day08().part2(example3)
    assert result == 6
