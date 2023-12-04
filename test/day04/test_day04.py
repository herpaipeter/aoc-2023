import pathlib
import pytest
import src.day04.day04 as day04

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_input_parseLine():
    card = day04.Day04().parseLine("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card.winning_numbers == [41, 48, 83, 86, 17]
    assert card.numbers == [83, 86, 6, 31, 17, 9, 48, 53]


def test_card_no_points():
    card = day04.Card([], [])
    assert card.point() == 0


def test_card_one_point():
    card = day04.Card([1], [1])
    assert card.point() == 1


def test_card_no_match_zero_point():
    card = day04.Card([1], [2])
    assert card.point() == 0
    assert card.match() == 0


def test_card_match_but_not_first():
    card = day04.Card([1], [2, 1])
    assert card.point() == 1
    assert card.match() == 1


def test_card_multimatch():
    card = day04.Card([1, 2], [2, 1])
    assert card.point() == 2
    assert card.match() == 2


def test_card_multimatch_but_power():
    card = day04.Card([1, 2, 3], [3, 2, 1])
    assert card.point() == 4
    assert card.match() == 3


def test_card_multimatch_but_power_more():
    card = day04.Card([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])
    assert card.point() == 8
    assert card.match() == 4


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day04.Day04().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day04.Day04().parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = day04.Day04().part1(example1)
    assert result == 13


def test_part2_example2(example1):
    """Test part 2 on example input."""
    result = day04.Day04().part2(example1)
    assert result == 30
