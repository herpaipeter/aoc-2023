import pytest

from src.common.point import Point, Direction


def test_point_add_point():
    assert Point(3, 3) == Point(1, 1) + Point(2, 2)


def test_point_add_int():
    assert Point(3, 3) == Point(1, 1) + 2


def test_point_add_float():
    with pytest.raises(NotImplementedError):
        Point(1, 1) + 2.4


def test_point_multi_int():
    assert Point(2, 2) == Point(1, 1) * 2


def test_point_negate():
    assert Point(-1, -1) == -Point(1, 1)


def test_point_add_left_direction():
    assert Point(1, 1) == Point(1, 2) + Direction.LEFT


def test_point_add_right_direction():
    assert Point(1, 3) == Point(1, 2) + Direction.RIGHT


def test_point_add_up_direction():
    assert Point(0, 2) == Point(1, 2) + Direction.UP


def test_point_add_down_direction():
    assert Point(2, 2) == Point(1, 2) + Direction.DOWN


def test_point_minus_down_direction():
    assert Point(0, 2) == Point(1, 2) - Direction.DOWN


def test_manhattan_distance_0():
    assert 0 == Point(1, 1).m_dist(Point(1, 1))


def test_shortest_path_len_between_1():
    assert 1 == Point(1, 1).m_dist(Point(1, 2))


def test_shortest_path_len_between_more():
    assert 9 == Point(6, 1).m_dist(Point(11, 5))
