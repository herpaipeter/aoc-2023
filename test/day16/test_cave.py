from src.common.point import Point, Direction
from src.day16.cave import CaveTile, CaveTileType, BeamTile


def test_next_tile_from_empty_direction_right():
    assert [BeamTile(Point(1, 2), Direction.RIGHT)] == CaveTile(Point(1, 1), CaveTileType.EMPTY).next_tiles(
        Direction.RIGHT)


def test_next_tile_from_empty_direction_left():
    assert [BeamTile(Point(1, 0), Direction.LEFT)] == CaveTile(Point(1, 1), CaveTileType.EMPTY).next_tiles(
        Direction.LEFT)


def test_next_tile_from_empty_direction_up():
    assert [BeamTile(Point(0, 1), Direction.UP)] == CaveTile(Point(1, 1), CaveTileType.EMPTY).next_tiles(Direction.UP)


def test_next_tile_from_empty_direction_down():
    assert [BeamTile(Point(2, 1), Direction.DOWN)] == CaveTile(Point(1, 1), CaveTileType.EMPTY).next_tiles(
        Direction.DOWN)


def test_next_tile_from_h_splitter_direction_right():
    assert [BeamTile(Point(1, 2), Direction.RIGHT)] == CaveTile(Point(1, 1), CaveTileType.H_SPLITTER).next_tiles(
        Direction.RIGHT)


def test_next_tile_from_h_splitter_direction_left():
    assert [BeamTile(Point(1, 0), Direction.LEFT)] == CaveTile(Point(1, 1), CaveTileType.H_SPLITTER).next_tiles(
        Direction.LEFT)


def test_next_tile_from_h_splitter_direction_up():
    assert [BeamTile(Point(1, 0), Direction.LEFT), BeamTile(Point(1, 2), Direction.RIGHT)] == CaveTile(Point(1, 1),
                                                                                                       CaveTileType.H_SPLITTER).next_tiles(
        Direction.UP)


def test_next_tile_from_h_splitter_direction_down():
    assert [BeamTile(Point(1, 0), Direction.LEFT), BeamTile(Point(1, 2), Direction.RIGHT)] == CaveTile(Point(1, 1),
                                                                                                       CaveTileType.H_SPLITTER).next_tiles(
        Direction.DOWN)


def test_next_tile_from_v_splitter_direction_right():
    assert [BeamTile(Point(0, 1), Direction.UP), BeamTile(Point(2, 1), Direction.DOWN)] == CaveTile(Point(1, 1),
                                                                                                    CaveTileType.V_SPLITTER).next_tiles(
        Direction.RIGHT)


def test_next_tile_from_v_splitter_direction_left():
    assert [BeamTile(Point(0, 1), Direction.UP), BeamTile(Point(2, 1), Direction.DOWN)] == CaveTile(Point(1, 1),
                                                                                                    CaveTileType.V_SPLITTER).next_tiles(
        Direction.LEFT)


def test_next_tile_from_v_splitter_direction_up():
    assert [BeamTile(Point(0, 1), Direction.UP)] == CaveTile(Point(1, 1), CaveTileType.V_SPLITTER).next_tiles(
        Direction.UP)


def test_next_tile_from_v_splitter_direction_down():
    assert [BeamTile(Point(2, 1), Direction.DOWN)] == CaveTile(Point(1, 1), CaveTileType.V_SPLITTER).next_tiles(
        Direction.DOWN)


def test_next_tile_from_ul_br_mirror_direction_right():
    assert [BeamTile(Point(2, 1), Direction.DOWN)] == CaveTile(Point(1, 1), CaveTileType.UL_BR_MIRROR).next_tiles(
        Direction.RIGHT)


def test_next_tile_from_ul_br_mirror_direction_left():
    assert [BeamTile(Point(0, 1), Direction.UP)] == CaveTile(Point(1, 1), CaveTileType.UL_BR_MIRROR).next_tiles(
        Direction.LEFT)


def test_next_tile_from_ul_br_mirror_direction_down():
    assert [BeamTile(Point(1, 2), Direction.RIGHT)] == CaveTile(Point(1, 1), CaveTileType.UL_BR_MIRROR).next_tiles(
        Direction.DOWN)


def test_next_tile_from_ul_br_mirror_direction_up():
    assert [BeamTile(Point(1, 0), Direction.LEFT)] == CaveTile(Point(1, 1), CaveTileType.UL_BR_MIRROR).next_tiles(
        Direction.UP)


def test_next_tile_from_bl_ur_mirror_direction_right():
    assert [BeamTile(Point(0, 1), Direction.UP)] == CaveTile(Point(1, 1), CaveTileType.BL_UR_MIRROR).next_tiles(
        Direction.RIGHT)


def test_next_tile_from_bl_ur_mirror_direction_left():
    assert [BeamTile(Point(2, 1), Direction.DOWN)] == CaveTile(Point(1, 1), CaveTileType.BL_UR_MIRROR).next_tiles(
        Direction.LEFT)


def test_next_tile_from_bl_ur_mirror_direction_down():
    assert [BeamTile(Point(1, 0), Direction.LEFT)] == CaveTile(Point(1, 1), CaveTileType.BL_UR_MIRROR).next_tiles(
        Direction.DOWN)


def test_next_tile_from_bl_ur_mirror_direction_up():
    assert [BeamTile(Point(1, 2), Direction.RIGHT)] == CaveTile(Point(1, 1), CaveTileType.BL_UR_MIRROR).next_tiles(
        Direction.UP)


def test_beam_tile_equals():
    assert BeamTile(Point(3, 6), Direction.DOWN) == BeamTile(Point(3, 6), Direction.DOWN)


def test_beam_tile_not_equals_direction():
    assert BeamTile(Point(3, 6), Direction.DOWN) != BeamTile(Point(3, 6), Direction.UP)


def test_beam_tile_not_equals_position():
    assert BeamTile(Point(3, 4), Direction.DOWN) != BeamTile(Point(3, 6), Direction.DOWN)
