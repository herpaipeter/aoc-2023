import pathlib
import pytest

from src.common.point import Point
from src.day14 import day14
from src.day14.rock import Rock, RockType, RockMap

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_line_empty():
    assert [] == day14.parse_line("", 0)


def test_parse_line_one_point():
    assert [] == day14.parse_line(".", 0)


def test_parse_line_one_round_rock():
    assert [Rock(RockType.ROUND, Point(0, 0))] == day14.parse_line("O", 0)


def test_parse_line_one_square_rock():
    assert [Rock(RockType.SQUARE, Point(0, 0))] == day14.parse_line("#", 0)


def test_parse_line_more_rock():
    assert [Rock(RockType.SQUARE, Point(0, 1)), Rock(RockType.ROUND, Point(0, 2))] == day14.parse_line(".#O", 0)


def test_parse_line_more_rock_not_first():
    assert [Rock(RockType.SQUARE, Point(3, 1)), Rock(RockType.ROUND, Point(3, 3)),
            Rock(RockType.SQUARE, Point(3, 4))] == day14.parse_line(".#.O#", 3)


def test_tilt_north_empty():
    rocks = day14.parse_line("", 0)
    assert [] == day14.tilt_north(rocks)


def test_tilt_north_square():
    rocks = day14.parse_line("#", 0)
    assert [Rock(RockType.SQUARE, Point(0, 0))] == day14.tilt_north(rocks)


def test_tilt_north_round():
    rocks = day14.parse_line("O", 0)
    assert [Rock(RockType.ROUND, Point(0, 0))] == day14.tilt_north(rocks)


def test_tilt_north_square_from_second_row():
    rocks = day14.parse_line("#", 1)
    assert [Rock(RockType.SQUARE, Point(1, 0))] == day14.tilt_north(rocks)


def test_tilt_north_round_from_second_row():
    rocks = day14.parse_line("O", 1)
    assert [Rock(RockType.ROUND, Point(0, 0))] == day14.tilt_north(rocks)


def test_dont_tilt_north_blocked_round():
    rocks = day14.parse_line("#", 0)
    rocks += day14.parse_line("O", 1)
    assert [Rock(RockType.SQUARE, Point(0, 0)), Rock(RockType.ROUND, Point(1, 0))] == day14.tilt_north(rocks)


def test_tilt_north_round_until_possible():
    rocks = day14.parse_line("#", 1)
    rocks += day14.parse_line("O", 5)
    assert [Rock(RockType.SQUARE, Point(1, 0)), Rock(RockType.ROUND, Point(2, 0))] == day14.tilt_north(rocks)


def test_total_load_empty():
    assert 0 == day14.total_load(RockMap([], 0, 0))


def test_total_load():
    rocks = day14.parse_line("#", 1)
    rocks += day14.parse_line("O", 5)
    assert 1 == day14.total_load(RockMap(rocks, 6, 1))


def test_tilt_west():
    rocks = day14.parse_line(".#", 1)
    rocks += day14.parse_line("...O", 5)
    assert [Rock(RockType.SQUARE, Point(1, 1)), Rock(RockType.ROUND, Point(5, 0))] == day14.tilt_west(rocks)


def test_tilt_south():
    rocks = day14.parse_line(".#", 1)
    rocks += day14.parse_line("...O", 5)
    assert [Rock(RockType.ROUND, Point(9, 3)), Rock(RockType.SQUARE, Point(1, 1))] == day14.tilt_south(rocks, 10)


def test_tilt_south_2():
    rocks = day14.parse_line(".#", 1)
    rocks += day14.parse_line("...O", 5)
    rocks += day14.parse_line("...#", 7)
    assert [Rock(RockType.SQUARE, Point(7, 3)), Rock(RockType.ROUND, Point(6, 3)),
            Rock(RockType.SQUARE, Point(1, 1))] == day14.tilt_south(rocks, 10)


def test_tilt_east():
    rocks = day14.parse_line(".#", 1)
    rocks += day14.parse_line("...O", 5)
    assert [Rock(RockType.ROUND, Point(5, 9)), Rock(RockType.SQUARE, Point(1, 1))] == day14.tilt_east(rocks, 10)


def test_tilt_east_2():
    rocks = day14.parse_line(".#", 1)
    rocks += day14.parse_line("...O..#", 5)
    assert [Rock(RockType.SQUARE, Point(5, 6)), Rock(RockType.ROUND, Point(5, 5)),
            Rock(RockType.SQUARE, Point(1, 1))] == day14.tilt_east(rocks, 10)


def test_cycle(example1, cycle_1, cycle_2, cycle_3):
    spin_1 = day14.spin_cycle(example1)
    assert cycle_1 == spin_1

    spin_2 = day14.spin_cycle(spin_1)
    assert cycle_2 == spin_2

    spin_3 = day14.spin_cycle(spin_2)
    assert cycle_3 == spin_3


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day14.Day14().parse(puzzle_input)


@pytest.fixture
def cycle_1():
    puzzle_input = (PUZZLE_DIR / "cycle_1.txt").read_text().strip()
    return day14.Day14().parse(puzzle_input)


@pytest.fixture
def cycle_2():
    puzzle_input = (PUZZLE_DIR / "cycle_2.txt").read_text().strip()
    return day14.Day14().parse(puzzle_input)


@pytest.fixture
def cycle_3():
    puzzle_input = (PUZZLE_DIR / "cycle_3.txt").read_text().strip()
    return day14.Day14().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day14.Day14().parse(puzzle_input)


def test_part1_example1(example1):
    result = day14.Day14().part1(example1)
    assert result == 136


def test_part2_example1(example1):
    result = day14.Day14().part2(example1)
    assert result == 64
