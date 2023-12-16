import pathlib
import pytest

from src.day15 import day15, lens
from src.day15.lens import LensCommand, LensOperation

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_get_value_for_H_char():
    assert 200 == lens.get_char_hash("H", 0)


def test_get_value_for_A_char():
    assert 153 == lens.get_char_hash("A", 200)


def test_get_value_for_S_char():
    assert 172 == lens.get_char_hash("S", 153)


def test_get_value_for_H_char_2():
    assert 52 == lens.get_char_hash("H", 172)


def test_hash_for_string_HASH():
    assert 52 == lens.get_hash("HASH")


def test_hash_for_string_rneq1():
    assert 30 == lens.get_hash("rn=1")


def test_hash_for_string_cmmin():
    assert 253 == lens.get_hash("cm-")


def test_parse_lense_command_add():
    command = day15.parse_lens_command("rn=1")
    assert LensCommand("rn", LensOperation.ADD, 1) == command
    assert 0 == command.index


def test_parse_lense_command_remove():
    command = day15.parse_lens_command("cm-")
    assert LensCommand("cm", LensOperation.REMOVE, 0) == command
    assert 0 == command.index


def test_parse_lense_command_remove_third_box_index():
    command = day15.parse_lens_command("pc=4")
    assert LensCommand("pc", LensOperation.ADD, 4) == command
    assert 3 == command.index


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day15.Day15().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day15.Day15().parse(puzzle_input)


def test_part1_example1(example1):
    result = day15.Day15().part1(example1)
    assert result == 1320


def test_part2_example1(example1):
    result = day15.Day15().part2(example1)
    assert result == 145
