import pathlib

import pytest

import src.day06.day06 as day06

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_line():
    assert [7, 15, 30] == day06.Day06().parseLine("Time:      7  15   30")


def test_parse_input():
    assert [[7, 15, 30], [9, 40, 200]] == day06.Day06().parse("Time:      7  15   30\nDistance:  9  40  200")


def test_get_travel_distance_zero():
    assert 0 == day06.Day06().get_distance(0, 7)


def test_get_travel_distance_one():
    assert 6 == day06.Day06().get_distance(1, 7)


def test_get_travel_distance_two():
    assert 10 == day06.Day06().get_distance(2, 7)


def test_get_possible_race_times():
    assert [0, 6, 10, 12, 12, 10, 6, 0] == day06.Day06().get_race_distances(7)


def test_get_number_of_better_than_record():
    assert 4 == day06.Day06().get_count_over_of_record(7, 9)

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day06.Day06().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day06.Day06().parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = day06.Day06().part1(example1)
    assert result == 288


def test_part2_example2(example1):
    """Test part 2 on example input."""
    result = day06.Day06().part2(example1)
    assert result == 71503
