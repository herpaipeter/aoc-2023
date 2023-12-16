import pathlib
import pytest

from src.common.point import Point, Direction
from src.day16 import day16
from src.day16.cave import CaveTile, CaveTileType, BeamTile, Cave

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_line_empty():
    assert [] == day16.parse_line("", 0)


def test_parse_line_empty_space():
    assert [] == day16.parse_line(".", 0)


def test_parse_line_mirror_UL_BR():
    assert [CaveTile(Point(0, 0), CaveTileType.UL_BR_MIRROR)] == day16.parse_line("\\", 0)


def test_parse_line_mirror_BL_UR():
    assert [CaveTile(Point(0, 0), CaveTileType.BL_UR_MIRROR)] == day16.parse_line("/", 0)


def test_parse_line_v_splitter():
    assert [CaveTile(Point(0, 0), CaveTileType.V_SPLITTER)] == day16.parse_line("|", 0)


def test_parse_line_h_splitter():
    assert [CaveTile(Point(0, 0), CaveTileType.H_SPLITTER)] == day16.parse_line("-", 0)


def test_parse_line():
    assert [CaveTile(Point(0, 1), CaveTileType.V_SPLITTER),
            CaveTile(Point(0, 5), CaveTileType.UL_BR_MIRROR),
            CaveTile(Point(0, 7), CaveTileType.H_SPLITTER),
            CaveTile(Point(0, 10), CaveTileType.BL_UR_MIRROR)] == day16.parse_line(".|...\\.-../", 0)


def test_parse_line_fifth():
    assert [CaveTile(Point(5, 1), CaveTileType.V_SPLITTER),
            CaveTile(Point(5, 5), CaveTileType.UL_BR_MIRROR),
            CaveTile(Point(5, 7), CaveTileType.H_SPLITTER),
            CaveTile(Point(5, 10), CaveTileType.BL_UR_MIRROR)] == day16.parse_line(".|...\\.-../", 5)


def test_move_beam_on_empty_cave_tile():
    cave_tiles = day16.parse_line(".|...\\....", 0)
    assert [BeamTile(Point(0, 1), Direction.RIGHT)] == day16.move_beam(BeamTile(Point(0, 0), Direction.RIGHT),
                                                                       Cave(cave_tiles, 1, 10))


def test_move_beam_on_vertical_splitter_edge():
    cave_tiles = day16.parse_line(".|...\\....", 0)
    assert [BeamTile(Point(1, 1), Direction.DOWN)] == day16.move_beam(BeamTile(Point(0, 1), Direction.RIGHT),
                                                                      Cave(cave_tiles, 10, 10))


def test_move_beam_on_ul_br_mirror():
    cave_tiles = day16.parse_line(".|...\\....", 0)
    assert [BeamTile(Point(1, 5), Direction.DOWN)] == day16.move_beam(BeamTile(Point(0, 5), Direction.RIGHT),
                                                                      Cave(cave_tiles, 10, 10))


def test_move_beam_on_vertical_splitter_middle():
    cave_tiles = day16.parse_line(".|...\\....", 2)
    assert ([BeamTile(Point(1, 1), Direction.UP), BeamTile(Point(3, 1), Direction.DOWN)]
            == day16.move_beam(BeamTile(Point(2, 1), Direction.RIGHT), Cave(cave_tiles, 10, 10)))


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day16.Day16().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day16.Day16().parse(puzzle_input)


def test_part1_example1(example1):
    result = day16.Day16().part1(example1)
    assert result == 46


def test_part2_example1(example1):
    result = day16.Day16().part2(example1)
    assert result == 51
