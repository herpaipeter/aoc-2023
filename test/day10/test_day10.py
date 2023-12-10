import pathlib
import pytest

from src.common.point import Point
from src.day10 import day10
from src.day10.tiles import Tile, TileType

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_line():
    assert [] == day10.parse_line("")


def test_parse_line_dot():
    assert [Tile(Point(0, 0), Point(0, 0), ".", TileType.EMPTY)] == day10.parse_line(".")


def test_parse_line_north_south():
    assert [Tile(Point(1, 0), Point(-1, 0), "|", TileType.PIPE_VERTICAL)] == day10.parse_line("|")


def test_parse_line_east_west():
    assert [Tile(Point(0, 1), Point(0, -1), "-", TileType.PIPE)] == day10.parse_line("-")


def test_parse_line_north_east():
    assert [Tile(Point(-1, 0), Point(0, 1), "L", TileType.PIPE_VERTICAL)] == day10.parse_line("L")


def test_parse_line_north_west():
    assert [Tile(Point(-1, 0), Point(0, -1), "J", TileType.PIPE_VERTICAL)] == day10.parse_line("J")


def test_parse_line_south_west():
    assert [Tile(Point(1, 0), Point(0, -1), "7", TileType.PIPE_VERTICAL)] == day10.parse_line("7")


def test_parse_line_south_east():
    assert [Tile(Point(1, 0), Point(0, 1), "F", TileType.PIPE_VERTICAL)] == day10.parse_line("F")


def test_parse_line_start():
    assert [Tile(Point(0, 0), Point(0, 0), "S", TileType.START)] == day10.parse_line("S")


def test_parse_line_more():
    assert [Tile(Point(0, 1), Point(0, -1), "-", TileType.PIPE),
            Tile(Point(0, 1), Point(0, -1), "-", TileType.PIPE)] == day10.parse_line("--")


def test_parse_line_more_2():
    assert [Tile(Point(0, 1), Point(0, -1), "-", TileType.PIPE),
            Tile(Point(-1, 0), Point(0, -1), "J", TileType.PIPE_VERTICAL)] == day10.parse_line("-J")


def test_parse_find_start_example1(example1):
    assert Point(1, 1) == day10.find_start(example1)


def test_parse_find_start_example2(example2):
    assert Point(2, 0) == day10.find_start(example2)


def test_find_tiles_next_to_tile(example1):
    assert [Point(1, 3), Point(1, 1)] == day10.get_next_to(example1, Point(1, 2))


def test_find_tiles_next_to_tile_7(example1):
    assert [Point(2, 3), Point(1, 2)] == day10.get_next_to(example1, Point(1, 3))


def test_find_tiles_next_to_start_example1(example1):
    assert [Point(1, 2), Point(2, 1)] == day10.get_next_to(example1, Point(1, 1))


def test_find_tiles_next_to_star_example2(example2):
    assert [Point(2, 1), Point(3, 0)] == day10.get_next_to(example2, Point(2, 0))


def test_move_to_next(example1):
    assert Point(1, 3) == day10.move_to(example1, Point(1, 1), Point(1, 2))


def test_move_to_next_backward(example1):
    assert Point(3, 2) == day10.move_to(example1, Point(2, 3), Point(3, 3))


def test_simple_number_of_enclosed_0_when_no_intersection():
    assert 0 == day10.get_num_of_inside_points(day10.parse_line("."), [], 0)


def get_line_route(line, row):
    route = []
    for index, tile in enumerate(line):
        if tile.symbol != ".":
            route.append(Point(row, index))
    return route




def test_simple_number_of_enclosed_1_when_two_intersection():
    line = day10.parse_line(".|.|.")
    route = get_line_route(line, 0)
    assert 1 == day10.get_num_of_inside_points(line, route, 0)


def test_simple_number_of_enclosed_corners_1():
    line = day10.parse_line("L--J.L7...LJF7F-7L7.")
    route = get_line_route(line, 0)
    assert 3 == day10.get_num_of_inside_points(line, route, 0)


def test_simple_number_of_enclosed_corners_2():
    line = day10.parse_line("....F-J..F7FJ|L7L7L7")
    route = get_line_route(line, 0)
    assert 2 == day10.get_num_of_inside_points(line, route, 0)


def test_simple_number_of_enclosed_corners_3():
    line = day10.parse_line("....L7.F7||L7|.L7L7|")
    route = get_line_route(line, 0)
    assert 2 == day10.get_num_of_inside_points(line, route, 0)


def test_number_of_enclosed_0_when_no_intersection(example3):
    route = get_line_route(example3[0], 0)
    assert 0 == day10.get_num_of_inside_points(example3[0], route, 0)


def test_number_of_enclosed_0_when_continuous_line(example3):
    route = get_line_route(example3[1], 1)
    assert 0 == day10.get_num_of_inside_points(example3[1], route, 1)


def test_number_of_enclosed_0_when_no_empty_between_lines(example3):
    route = get_line_route(example3[2], 2)
    assert 0 == day10.get_num_of_inside_points(example3[2], route, 2)


def test_number_of_enclosed_0_when_only_even_crosses(example3):
    route = get_line_route(example3[3], 3)
    assert 0 == day10.get_num_of_inside_points(example3[3], route, 3)


# def test_number_of_enclosed_counting_empty_after_odd_crosses(example3):
#     assert 4 == day10.get_num_of_inside_points(example3[6])


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day10.Day10().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day10.Day10().parse(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return day10.Day10().parse(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return day10.Day10().parse(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().strip()
    return day10.Day10().parse(puzzle_input)

def test_part1_example1(example1):
    result = day10.Day10().part1(example1)
    assert result == 4


def test_part1_example2(example2):
    result = day10.Day10().part1(example2)
    assert result == 8


def test_part2_example3(example3):
    result = day10.Day10().part2(example3)
    assert result == 4


def test_part2_example4(example4):
    result = day10.Day10().part2(example4)
    assert result == 8


def test_part2_example5(example5):
    result = day10.Day10().part2(example5)
    assert result == 10
