import pathlib
import pytest
import src.day05.day05 as day05
from src.day05.range import RangeMap, Range

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_blocks():
    result = day05.Day05().parseBlocks("a\nb\n\nc\nd\n\ne")
    assert result == ["a\nb", "c\nd", "e"]


def test_parse_seeds():
    result = day05.Day05().parseSeeds("seeds: 79 14 55 13")
    assert result == [79, 14, 55, 13]


@pytest.mark.skip
def test_parse_map():
    result = day05.Day05().parseMap("seed-to-soil map:\n50 98 2\n52 50 48")
    assert result == RangeMap([Range(50, 52, 48), Range(98, 50, 2)])


@pytest.mark.skip
def test_parse_maps():
    result = day05.Day05().parseMaps(
        ["seed-to-soil map:\n50 98 2\n52 50 48", "soil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15"])
    assert result == [RangeMap([Range(50, 52, 48), Range(98, 50, 2)]),
                      RangeMap([Range(0, 39, 15), Range(15, 0, 37), Range(52, 37, 2)])]


def test_range_contains():
    assert Range(1, 2, 1).contains(1) is True


def test_range_not_contains():
    assert Range(1, 2, 1).contains(2) is False


def test_range_map_value():
    assert Range(1, 2, 1).map(1) == 2


def test_range_map_wrong_value():
    with pytest.raises(KeyError):
        Range(1, 2, 1).map(2)


def test_range_map_not_first_value():
    assert Range(1, 3, 5).map(4) == 6


def test_range_map_mapping_first():
    range_map = RangeMap([Range(98, 50, 2), Range(50, 52, 48)])
    assert range_map.map(98) == 50


def test_range_map_mapping_not_first():
    range_map = RangeMap([Range(98, 50, 2), Range(50, 52, 48)])
    assert range_map.map(99) == 51


def test_range_map_mapping_second_range():
    range_map = RangeMap([Range(98, 50, 2), Range(50, 52, 48)])
    assert range_map.map(60) == 62


def test_range_map_mapping_second_range_upper():
    range_map = RangeMap([Range(98, 50, 2), Range(50, 52, 48)])
    assert range_map.map(97) == 99


def test_range_map_mapping_out_of_ranges():
    range_map = RangeMap([Range(98, 50, 2), Range(50, 52, 48)])
    assert range_map.map(1) == 1


def test_merge_range_no_intersection():
    range1 = Range(1, 2, 3)
    range2 = Range(11, 12, 13)
    assert ([range1], [range2], []) == range1.merge(range2)


def test_merge_range_simple_intersection():
    range1 = Range(1, 2, 5)
    range2 = Range(4, 12, 13)
    assert ([Range(1, 2, 2)], [Range(7, 15, 10)], [Range(3, 12, 3)]) == range1.merge(range2)


def test_merge_range_simple_intersection_empty_self_result():
    range1 = Range(1, 2, 5)
    range2 = Range(2, 12, 13)
    assert ([], [Range(7, 17, 8)], [Range(1, 12, 5)]) == range1.merge(range2)


def test_merge_range_only_first_ranges():
    range1 = Range(2, 12, 13)
    range2 = Range(15, 3, 5)
    assert ([Range(2, 12, 3), Range(10, 20, 5)], [], [Range(5, 3, 5)]) == range1.merge(range2)


def test_merge_range_only_second_ranges():
    range1 = Range(12, 7, 5)
    range2 = Range(4, 10, 16)
    assert ([], [Range(4, 10, 3), Range(12, 18, 8)], [Range(12, 13, 5)]) == range1.merge(range2)


def test_merge_to_range_map():
    range_map = RangeMap([Range(98, 50, 2), Range(50, 52, 48)])
    range_right = Range(1, 2, 10)
    result = range_map.merge(range_right)
    assert result == [Range(98, 50, 2), Range(50, 52, 48), Range(1, 2, 10)]


def test_merge_to_range_map_intersect():
    range_map = RangeMap([Range(98, 50, 2), Range(50, 52, 48)])
    range_right = Range(40, 60, 20)
    result = range_map.merge(range_right)
    assert sorted(result) == sorted([Range(map_from=98, map_to=70, length=2),
                      Range(map_from=58, map_to=60, length=40),
                      Range(map_from=50, map_to=72, length=8),
                      Range(map_from=40, map_to=60, length=10)])


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day05.Day05().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day05.Day05().parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = day05.Day05().part1(example1)
    assert result == 35


def test_part2_example2(example1):
    """Test part 2 on example input."""
    result = day05.Day05().part2(example1)
    assert result == 46
