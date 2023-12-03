import pathlib
import pytest
import src.day03.day03 as day03
from src.common.point import Point
from src.day03.engine_part import EngineNumber, EngineSymbol

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_point_eq():
    assert Point(1, 2) == Point(1, 2)


def test_empty_line_returns_empty():
    assert [] == day03.Day03().parseLine("", 0)


def test_one_dot_line_returns_empty():
    assert [] == day03.Day03().parseLine(".", 0)


def test_one_num_line_returns_one_num_with_0_position():
    result = day03.Day03().parseLine("1", 0)
    assert [EngineNumber(1, Point(0, 0), Point(0, 0))] == result


def test_one_num_and_dot_line_returns_one_num_with_0_position():
    result = day03.Day03().parseLine("1.", 0)
    assert [EngineNumber(1, Point(0, 0), Point(0, 0))] == result


def test_one_dot_and_num_line_returns_one_num_with_1_position():
    result = day03.Day03().parseLine(".1", 0)
    assert [EngineNumber(1, Point(0, 1), Point(0, 1))] == result


def test_two_digit_returns_one_num_with_two_diff_position():
    result = day03.Day03().parseLine("12", 0)
    assert [EngineNumber(12, Point(0, 0), Point(0, 1))] == result


def test_two_numbers_returns_two_enginenumber():
    result = day03.Day03().parseLine("467..114..", 0)
    assert [EngineNumber(467, Point(0, 0), Point(0, 2)),
            EngineNumber(114, Point(0, 5), Point(0, 7))] == result


def test_one_symbol_returns_one_enginesymbol():
    result = day03.Day03().parseLine("*", 0)
    assert [EngineSymbol("*", Point(0, 0))] == result


def test_parse_mixed_line():
    result = day03.Day03().parseLine("617+2.....", 1)
    assert [EngineNumber(617, Point(1, 0), Point(1, 2)),
            EngineSymbol("+", Point(1, 3)),
            EngineNumber(2, Point(1, 4), Point(1, 4))] == result


def test_check_near_symbol():
    assert day03.Day03().is_adjacent_to_any_symbol(EngineNumber(617, Point(1, 0), Point(1, 2)), []) is False


def test_after_symbol():
    symbols = [EngineSymbol("+", Point(1, 3))]
    assert day03.Day03().is_adjacent_to_any_symbol(EngineNumber(617, Point(1, 0), Point(1, 2)),
                                                   symbols) is True


def test_before_symbol():
    symbols = [EngineSymbol("+", Point(1, 0))]
    assert day03.Day03().is_adjacent_to_any_symbol(EngineNumber(617, Point(1, 1), Point(1, 3)),
                                                   symbols) is True


def test_not_next_to_because_of_rows():
    symbols = [EngineSymbol("+", Point(0, 0))]
    assert day03.Day03().is_adjacent_to_any_symbol(EngineNumber(617, Point(2, 1), Point(2, 3)),
                                                   symbols) is False


def test_next_to_in_previous_row():
    symbols = [EngineSymbol("+", Point(1, 0))]
    assert day03.Day03().is_adjacent_to_any_symbol(EngineNumber(617, Point(2, 1), Point(2, 3)),
                                                   symbols) is True


def test_next_to_in_next_row():
    symbols = [EngineSymbol("+", Point(3, 0))]
    assert day03.Day03().is_adjacent_to_any_symbol(EngineNumber(617, Point(2, 1), Point(2, 3)),
                                                   symbols) is True


def test_next_to_in_next_row_and_between():
    symbols = [EngineSymbol("+", Point(3, 1))]
    assert day03.Day03().is_adjacent_to_any_symbol(EngineNumber(617, Point(2, 1), Point(2, 3)),
                                                   symbols) is True


def test_next_to_in_next_row_and_between_upper():
    symbols = [EngineSymbol("+", Point(3, 3))]
    assert day03.Day03().is_adjacent_to_any_symbol(EngineNumber(617, Point(2, 1), Point(2, 3)),
                                                   symbols) is True


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day03.Day03().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day03.Day03().parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = day03.Day03().part1(example1)
    assert result == 4361


def test_part2_example2(example1):
    """Test part 2 on example input."""
    result = day03.Day03().part2(example1)
    assert result == 467835
