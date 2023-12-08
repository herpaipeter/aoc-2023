import pathlib

import pytest

import src.day07.day07 as day07
from src.day07.card import Bid, Hand

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_line():
    assert Bid(Hand("448J8"), 748) == day07.Day07().parseLine("448J8 748")


def test_hand_five_of_a_kind_has_category_7():
    assert 7 == Hand("AAAAA").get_category()


def test_hand_four_of_a_kind_has_category_6():
    assert 6 == Hand("AA8AA").get_category()


def test_hand_full_house_has_category_5():
    assert 5 == Hand("23332").get_category()


def test_hand_Three_of_a_kind_has_category_4():
    assert 4 == Hand("TTT98").get_category()


def test_hand_Two_pair_has_category_3():
    assert 3 == Hand("23432").get_category()


def test_hand_One_pair_has_category_2():
    assert 2 == Hand("A23A4").get_category()


def test_hand_high_pair_has_category_1():
    assert 1 == Hand("23456").get_category()


def test_hands_order_by_different_category():
    assert Hand("AA8AA") < Hand("AAAAA")


def test_hands_same_category_different_first_pos():
    assert Hand("2AAAA") < Hand("33332")


def test_hands_same_category_different_third_pos():
    assert Hand("77788") < Hand("77888")


def test_hands_same_category_different_last_pos():
    assert Hand("77778") < Hand("77779")


def test_hands_with_jokers():
    assert 6 == Hand("KTJJT", True).get_category()


def test_hands_with_jokers_spec1():
    assert Hand("JJJJJ", True) < Hand("AAAJJ", True)


def test_hands_with_jokers_spec2():
    assert Hand("J345A", True) < Hand("2345J", True)


def test_hands_with_jokers_spec3():
    assert Hand("2345J", True) < Hand("32T3K", True)


def test_hands_with_jokers_spec4():
    assert Hand("JJJJJ", True) < Hand("JJJJ2", True)


def test_hands_with_jokers_spec5():
    assert Hand("JAAAA", True) < Hand("2JJJJ", True)


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day07.Day07().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day07.Day07().parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = day07.Day07().part1(example1)
    assert result == 6440


def test_part2_example1(example1):
    """Test part 2 on example input."""
    result = day07.Day07().part2(example1)
    assert result == 5905


def test_part2_example2(example2):
    """Test part 2 on example input."""
    result = day07.Day07().part2(example2)
    assert result == 3667
