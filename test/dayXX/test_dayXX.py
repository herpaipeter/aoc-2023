import pathlib
import pytest

from src.dayXX import dayXX

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return dayXX.DayXX().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return dayXX.DayXX().parse(puzzle_input)


def test_part1_example1(example1):
    result = dayXX.DayXX().part1(example1)
    assert result == None


def test_part2_example1(example1):
    result = dayXX.DayXX().part2(example1)
    assert result == None
