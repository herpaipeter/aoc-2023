import sys
from typing import Any

from src.aoc_solver import runifmain, AocSolver
from src.day05.range import RangeMap, Range, Almanac, SeedRange


@runifmain(__name__)
class Day05(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        blocks = self.parseBlocks(input_data)
        return Almanac(self.parseSeeds(blocks[0]), self.parseMaps(blocks[1:]))

    def part1(self, data) -> Any:
        min_location = sys.maxsize
        for seed in data.seeds:
            mapped = seed
            for r_map in data.range_maps:
                mapped = r_map.map(mapped)
            if mapped < min_location:
                min_location = mapped
        return min_location


    def part2(self, data) -> Any:
        min_location = sys.maxsize
        merged_maps = data.merge_range_maps()
        merged_maps.ranges.sort(key = lambda n: n.map_to)
        seed_ranges = []
        for i in range(int(len(data.seeds) / 2)):
            seed_ranges.append(SeedRange(data.seeds[2 * i], data.seeds[2 * i] + data.seeds[2 * i + 1] - 1))
        for lr in merged_maps.ranges:
            local_min_location = sys.maxsize
            for sr in seed_ranges:
                if (sr.start <= lr.map_from <= sr.end):
                    local_min_location = lr.map_to
                    break
                elif (lr.map_from <= sr.start < lr.map_from + lr.length):
                    local_min_location = lr.map_to + sr.start - lr.map_from
                    break
            if local_min_location < min_location:
                min_location = local_min_location
        return min_location
        #too high: 36826209
        #not good: 1908646

    def parseBlocks(self, lines):
        return lines.split("\n\n")

    def parseSeeds(self, text):
        return list(map(int, text.split(":")[1].strip().split(" ")))

    def parseMap(self, lines):
        range_map = RangeMap([])
        for line in lines.split("\n")[1:]:
            range_values = list(map(int, line.split(" ")))
            range_map.ranges.append(Range(range_values[1], range_values[0], range_values[2]))
        #range_map.ranges.sort()
        return range_map

    def parseMaps(self, maps_list):
        return list(map(self.parseMap, maps_list))

