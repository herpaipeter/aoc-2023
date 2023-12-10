from concurrent.futures import ProcessPoolExecutor
from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.common.point import Point, Direction
from src.day10.tiles import Tile, TileType


def parse_line(line: str) -> list[Tile]:
    return list(map(lambda txt: get_tile(txt), line))


def get_tile(tile_txt: str) -> Tile:
    if tile_txt == ".":
        return Tile(Point(0, 0), Point(0, 0), ".", TileType.EMPTY)
    elif tile_txt == "S":
        return Tile(Point(0, 0), Point(0, 0), "S", TileType.START)
    elif tile_txt == "|":
        return Tile(Point(1, 0), Point(-1, 0), "|", TileType.PIPE_VERTICAL)
    elif tile_txt == "-":
        return Tile(Point(0, 1), Point(0, -1), "-", TileType.PIPE)
    elif tile_txt == "L":
        return Tile(Point(-1, 0), Point(0, 1), "L", TileType.PIPE_VERTICAL)
    elif tile_txt == "J":
        return Tile(Point(-1, 0), Point(0, -1), "J", TileType.PIPE_VERTICAL)
    elif tile_txt == "7":
        return Tile(Point(1, 0), Point(0, -1), "7", TileType.PIPE_VERTICAL)
    elif tile_txt == "F":
        return Tile(Point(1, 0), Point(0, 1), "F", TileType.PIPE_VERTICAL)


def find_start(tile_map: list[list[Tile]]) -> Point:
    for row in range(len(tile_map)):
        for col in range(len(tile_map[row])):
            if tile_map[row][col].type == TileType.START:
                return Point(row, col)
    return Point(-1, -1)


def get_start_original_symbol(tile_map: list[list[Tile]], start_pos: Point) -> str:
    points = get_next_to(tile_map, start_pos)
    directions = list(map(lambda p: Direction(p - start_pos), points))
    if 0 < directions.count(Direction.LEFT) and 0 < directions.count(Direction.DOWN):
        return "7"
    elif 0 < directions.count(Direction.RIGHT) and 0 < directions.count(Direction.DOWN):
        return "F"
    elif 0 < directions.count(Direction.LEFT) and 0 < directions.count(Direction.UP):
        return "J"
    elif 0 < directions.count(Direction.RIGHT) and 0 < directions.count(Direction.UP):
        return "L"
    raise AttributeError


def replace_start(tile_map: list[list[Tile]]):
    for row in range(len(tile_map)):
        for col in range(len(tile_map[row])):
            if tile_map[row][col].type == TileType.START:
                original = get_start_original_symbol(tile_map, Point(row, col))
                tile_map[row][col] = get_tile(original)


def has_route_to(tile_from: Tile, tile_from_pos: Point, tile_to_pos: Point) -> bool:
    return tile_from_pos + tile_from.end1 == tile_to_pos or tile_from_pos + tile_from.end2 == tile_to_pos


def get_tile_at(tile_map: list[list[Tile]], tile_pos: Point) -> Tile:
    if 0 <= tile_pos.row < len(tile_map) and 0 <= tile_pos.col < len(tile_map[tile_pos.row]):
        return tile_map[tile_pos.row][tile_pos.col]
    else:
        return Tile(Point(0, 0), Point(0, 0), ".", TileType.EMPTY)


def get_next_to(tile_map: list[list[Tile]], tile_pos: Point) -> list[Point]:
    tile = tile_map[tile_pos.row][tile_pos.col]
    if tile.type == TileType.EMPTY:
        return []
    elif tile.type == TileType.PIPE or tile.type == TileType.PIPE_VERTICAL:
        return [tile_pos + tile.end1, tile_pos + tile.end2]
    elif tile.type == TileType.START:
        return list(filter(lambda n: has_route_to(get_tile_at(tile_map, n), n, tile_pos),
                           map(lambda d: tile_pos + d, Direction)))


def move_to(tile_map: list[list[Tile]], prev: Point, at: Point) -> Point:
    next_positions = list(filter(lambda p: p != prev, get_next_to(tile_map, at)))
    if 0 < len(next_positions):
        return next_positions[0]
    return Point(-1, -1)


def get_num_of_inside_points(map_line: list[Tile], route: list[Point], row: int) -> int:
    inside_tiles = 0
    crosses = 0
    prev_vertical = ""
    for index, tile in enumerate(map_line):
        if next((True for point in route if point == Point(row, index)), False):
            if tile.type == TileType.PIPE_VERTICAL:
                if (prev_vertical == "L" and tile.symbol == "7"
                        or prev_vertical == "F" and tile.symbol == "J"
                        or tile.symbol == "|"):
                    crosses += 1
                prev_vertical = tile.symbol
        elif crosses % 2 == 1:
            inside_tiles += 1
    return inside_tiles


def get_route(tile_map: list[list[Tile]]) -> list[Point]:
    route1, route2 = get_routes_from_start(tile_map)
    return route1 + route2


def get_routes_from_start(tile_map) -> (list[Point], list[Point]):
    start = find_start(tile_map)
    next_to_start = get_next_to(tile_map, start)
    route1 = [start, next_to_start[0]]
    route2 = [start, next_to_start[1]]
    while route1[len(route1) - 1] != route2[len(route2) - 1]:
        route1.append(move_to(tile_map, route1[len(route1) - 2], route1[len(route1) - 1]))
        route2.append(move_to(tile_map, route2[len(route2) - 2], route2[len(route2) - 1]))
    return route1, route2


def get_num_of_inside_points_tupled(tuple, route):
    return get_num_of_inside_points(tuple[1], route, tuple[0])


@runifmain(__name__)
class Day10(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        return list(map(lambda line: parse_line(line), input_data.split("\n")))

    def part1(self, data) -> Any:
        route1, route2 = get_routes_from_start(data)
        return len(route1) - 1

    def part2(self, data) -> Any:
        route = get_route(data)
        replace_start(data)
        result = 0
        with ProcessPoolExecutor() as executor:
            for future in executor.map(get_num_of_inside_points_tupled, enumerate(data), [route] * len(data)):
                result += future
        return result
