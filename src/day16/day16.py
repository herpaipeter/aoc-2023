import sys
from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.common.point import Point, Direction
from src.day16.cave import CaveTile, CaveTileType, BeamTile, Cave


def parse_line(line_txt: str, row: int) -> list[CaveTile]:
    result = []
    for index, c in enumerate(line_txt):
        if c == "\\":
            result.append(CaveTile(Point(row, index), CaveTileType.UL_BR_MIRROR))
        elif c == "/":
            result.append(CaveTile(Point(row, index), CaveTileType.BL_UR_MIRROR))
        elif c == "-":
            result.append(CaveTile(Point(row, index), CaveTileType.H_SPLITTER))
        elif c == "|":
            result.append(CaveTile(Point(row, index), CaveTileType.V_SPLITTER))
    return result


def move_beam(beam: BeamTile, cave: Cave) -> list[BeamTile]:
    result = []
    cave_tile_at_beam = list(filter(lambda ct: ct.position == beam.position, cave.tiles))
    if 0 < len(cave_tile_at_beam):
        next_tiles = cave_tile_at_beam[0].next_tiles(beam.direction)
        for tile in next_tiles:
            if 0 <= tile.position.row < cave.rows and 0 <= tile.position.col < cave.cols:
                result.append(tile)
    else:
        new_beam_position = beam.position + beam.direction
        if 0 <= new_beam_position.row < cave.rows and 0 <= new_beam_position.col < cave.cols:
            result.append(BeamTile(new_beam_position, beam.direction))
    return result


def find_and_add_new_beams(beams: set[BeamTile], beam: BeamTile, cave: Cave):
    new_beams = move_beam(beam, cave)
    disjoint_beams = set()
    for b in new_beams:
        if beams.isdisjoint({b}):
            disjoint_beams.add(b)
        beams.add(b)
    for b in disjoint_beams:
        find_and_add_new_beams(beams, b, cave)


def get_start_beams(cave: Cave):
    start_beams = []
    for row in range(cave.rows):
        start_beams.append(BeamTile(Point(row, 0), Direction.RIGHT))
        start_beams.append(BeamTile(Point(row, cave.cols - 1), Direction.LEFT))
    for col in range(cave.cols):
        start_beams.append(BeamTile(Point(0, col), Direction.DOWN))
        start_beams.append(BeamTile(Point(cave.rows - 1, col), Direction.UP))
    return start_beams

@runifmain(__name__)
class Day16(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        cave_tiles = []
        lines_txt = input_data.split("\n")
        for index, line in enumerate(lines_txt):
            cave_tiles += parse_line(line, index)
        return Cave(cave_tiles, len(lines_txt), len(lines_txt[0]) if 0 < len(lines_txt) else 0)

    def part1(self, data: Cave) -> Any:
        sys.setrecursionlimit(3000)
        return self.get_energizes_tiles(data, BeamTile(Point(0, 0), Direction.RIGHT))

    def get_energizes_tiles(self, cave: Cave, start_beam: BeamTile):
        beams = {start_beam}
        find_and_add_new_beams(beams, start_beam, cave)
        beam_positions = set(map(lambda beam: beam.position, beams))
        return len(beam_positions)

    def part2(self, data: Cave) -> Any:
        start_beams = get_start_beams(data)
        energized_tiles = []
        for b in start_beams:
            print("get_energizes_tiles for ", b)
            energized_tiles.append(self.get_energizes_tiles(data, b))
        return max(energized_tiles)
