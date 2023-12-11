import pathlib
import pytest

from src.common.point import Point
from src.day11 import day11

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_read_empty_line():
    assert [] == day11.read_line("", 0)


def test_read_line_with_one_galaxy():
    assert [Point(0, 0)] == day11.read_line("#", 0)


def test_read_line_with_one_galaxy_and_empty_space():
    assert [Point(0, 1)] == day11.read_line(".#", 0)


def test_read_line_with_more_galaxy():
    assert [Point(0, 1), Point(0, 4), Point(0, 8)] == day11.read_line(".#..#...#", 0)


def test_read_line_with_given_row_number():
    assert [Point(3, 1), Point(3, 4), Point(3, 8)] == day11.read_line(".#..#...#", 3)


def test_find_empty_rows_in_empty_list():
    assert [] == day11.get_empty_rows([])


def test_find_empty_rows_in_one_point_list():
    assert [] == day11.get_empty_rows([Point(1, 1)])


def test_find_empty_rows_in_two_points_list():
    assert [] == day11.get_empty_rows([Point(1, 1), Point(2, 1)])


def test_find_empty_rows_in_two_points_list_with_distance():
    assert [2] == day11.get_empty_rows([Point(1, 1), Point(3, 1)])


def test_find_empty_rows_in_two_points_list_with_more_rows_distance():
    assert [2, 3, 4] == day11.get_empty_rows([Point(1, 1), Point(5, 1)])


def test_find_empty_rows_in_more_points_list_with_more_rows_distance():
    assert [2, 3, 4, 6, 7, 8, 9] == day11.get_empty_rows([Point(1, 1), Point(5, 1), Point(10, 1)])


def test_find_empty_rows_in_more_points_list_with_more_rows_distance_mixed():
    assert [2, 4] == day11.get_empty_rows([Point(1, 1), Point(5, 1), Point(3, 2)])


def test_find_empty_cols_in_more_points_list_with_more_rows_distance():
    assert [2, 4, 5, 6, 7] == day11.get_empty_cols([Point(1, 1), Point(5, 3), Point(10, 8)])


def test_find_empty_cols_in_more_points_list_with_more_rows_distance_mixed():
    assert [2, 4, 5] == day11.get_empty_cols([Point(1, 1), Point(5, 6), Point(10, 3)])


def test_add_empty_rows_between_0_if_no_between():
    assert [Point(1, 1), Point(2, 1)] == day11.add_empty_rows([Point(1, 1), Point(2, 1)], [])


def test_add_empty_rows_between_with_one_row():
    assert [Point(1, 1), Point(4, 1)] == day11.add_empty_rows([Point(1, 1), Point(3, 1)], [2])


def test_add_empty_rows_between_with_more_empty_rows():
    assert [Point(1, 1), Point(6, 4), Point(11, 2)] == day11.add_empty_rows([Point(1, 1), Point(4, 4), Point(7, 2)],
                                                                            [2, 3, 5, 6])


def test_add_empty_cols_between_with_more_empty_cols():
    assert [Point(1, 1), Point(7, 4), Point(4, 13)] == day11.add_empty_cols([Point(1, 1), Point(4, 8), Point(7, 3)],
                                                                            [2, 4, 5, 6, 7])


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day11.Day11().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day11.Day11().parse(puzzle_input)


def test_part1_example1(example1):
    result = day11.Day11().part1(example1)
    assert result == 374


def test_part2_example1_multi_10(example1):
    result = day11.Day11().part2(example1, 10)
    assert result == 1030


def test_part2_example1_multi_100(example1):
    result = day11.Day11().part2(example1, 100)
    assert result == 8410
