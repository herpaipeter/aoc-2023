import pathlib
import pytest
import src.day02.day02 as day02

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day02.Day02().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day02.Day02().parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = day02.Day02().part1(example1)
    assert result == 8


def test_part2_example2(example1):
    """Test part 2 on example input."""
    result = day02.Day02().part2(example1)
    assert result == 2286
