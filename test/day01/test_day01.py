# test_aoc_template.py

import pathlib
import pytest
import src.day01.day01 as solution

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return solution.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return solution.parse(puzzle_input)


def test_empty_string_returns_none():
    value = solution.get_calibration_value("")
    assert value is None


def test_one_char_string_returns_none():
    value = solution.get_calibration_value("a")
    assert value is None


def test_one_number_string_returns_the_duplicated_num():
    value = solution.get_calibration_value("1")
    assert value == 11


def test_two_numbers_string_returns_the_the_same():
    value = solution.get_calibration_value("12")
    assert value == 12


def test_one_number_and_one_char_string_returns_the_number():
    value = solution.get_calibration_value("1a")
    assert value == 11


def test_only_one_number_returns_the_numer_duplicated():
    value = solution.get_calibration_value("ddweg1agfdt")
    assert value == 11


def test_more_numbers_returns_the_first_and_last():
    value = solution.get_calibration_value("dd4weg1agfd6t")
    assert value == 46


def test_sum():
    sum = solution.summa(['1abc2', 'pqr3stu8vwx'])
    assert sum == 50


def test_replace_empty_should_return_empty():
    replaced = solution.prefix_number_words_with_digit("")
    assert replaced == ""


def test_not_valid_word_should_return_empty():
    replaced = solution.prefix_number_words_with_digit("asdf")
    assert replaced == "asdf"


def test_word_one_should_return_1():
    replaced = solution.prefix_number_words_with_digit("one")
    assert replaced == "1one"


def test_word_two_should_return_2():
    replaced = solution.prefix_number_words_with_digit("two")
    assert replaced == "2two"


def test_words_replace_to_digit():
    replaced = solution.prefix_number_words_with_digit("onetwo")
    assert replaced == "1one2two"


def test_words_replace_if_inside():
    replaced = solution.prefix_number_words_with_digit("oneight")
    assert replaced == "1on8eight"


def test_words_replace_if_opposite_inside():
    replaced = solution.prefix_number_words_with_digit("eightwo")
    assert replaced == "8eigh2two"


def test_words_replace_if_inside_2():
    replaced = solution.prefix_number_words_with_digit("eightwothree")
    assert replaced == "8eigh2two3three"


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = solution.part1(example1)
    assert result == 142


def test_part2_example2(example2):
    """Test part 2 on example input."""
    result = solution.part2(example2)
    assert result == 281
