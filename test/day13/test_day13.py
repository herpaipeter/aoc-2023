import pathlib
import pytest

from src.day13 import day13
from src.day13.pattern import Pattern

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_read_get_horizontal_reflection_on_empty():
    assert 0 == Pattern("").get_h_refl()


def test_read_get_horizontal_reflection_one_line():
    assert 0 == Pattern("#.#").get_h_refl()


def test_read_get_horizontal_reflection_after_first_line():
    assert 1 == Pattern("#.#\n#.#").get_h_refl()


def test_read_get_horizontal_reflection_no():
    assert 0 == Pattern("#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.").get_h_refl()


def test_read_get_horizontal_reflection():
    assert 4 == Pattern("#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#").get_h_refl()


def test_read_get_vertical_reflection_on_empty():
    assert 0 == Pattern("").get_v_refl()


def test_read_get_vertical_reflection_one_line():
    assert 0 == Pattern("#.#").get_v_refl()


def test_read_get_vertical_reflection_one_line_reflects():
    assert 2 == Pattern("#..#").get_v_refl()


def test_read_get_vertical_reflection():
    assert 5 == Pattern("#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.").get_v_refl()


def test_read_get_vertical_reflection_no():
    assert 0 == Pattern("#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#").get_v_refl()


def test_read_get_vertical_reflection_smudge_no_1():
    assert 0 == Pattern(
        "#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.").get_v_refl_smudge()


def test_read_get_vertical_reflection_smudge_no_2():
    assert 0 == Pattern(
        "#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#").get_v_refl_smudge()


def test_read_get_horizontal_reflection_smudge_1():
    assert 3 == Pattern(
        "#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.").get_h_refl_smudge()


def test_read_get_horizontal_reflection_smudge_2():
    assert 1 == Pattern(
        "#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#").get_h_refl_smudge()


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return day13.Day13().parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return day13.Day13().parse(puzzle_input)


def test_part1_example1(example1):
    result = day13.Day13().part1(example1)
    assert result == 405


def test_part1_example2(example2):
    result = day13.Day13().part1(example2)
    assert result == 1200


def test_part2_example1(example1):
    result = day13.Day13().part2(example1)
    assert result == 400


def test_part2_example2(example2):
    result = day13.Day13().part2(example2)
    assert result == 0
