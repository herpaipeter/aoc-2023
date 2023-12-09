import pathlib
import pytest

from src.day09 import day09

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_line():
    assert [0, 3, 6, 9, 12, 15] == day09.parse_line("0 3 6 9 12 15")


def test_diff_series():
    assert [3] == day09.get_diffs([0, 3])


def test_get_next():
    assert 18 == day09.get_next([0, 3, 6, 9, 12, 15])


def test_get_next_longer():
    assert 68 == day09.get_next([10, 13, 16, 21, 30, 45])


def test_get_prev():
    assert 5 == day09.get_prev([10, 13, 16, 21, 30, 45])


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day09.Day09().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day09.Day09().parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = day09.Day09().part1(example1)
    assert result == 114


def test_part2_example1(example1):
    """Test part 2 on example input."""
    result = day09.Day09().part2(example1)
    assert result == 2
