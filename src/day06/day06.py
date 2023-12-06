from typing import Any

from src.aoc_solver import runifmain, AocSolver


@runifmain(__name__)
class Day06(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data) -> Any:
        lines = input_data.split('\n')
        return list(map(lambda line: self.parseLine(line), lines))

    def part1(self, data) -> Any:
        result = 1
        for i in range(len(data[0])):
            result *= self.get_count_over_of_record(data[0][i], data[1][i])
        return result

    def part2(self, data) -> Any:
        max_time = int("".join(map(str, data[0])))
        record_distance = int("".join(map(str, data[1])))
        return self.get_count_over_of_record(max_time, record_distance)

    def parseLine(self, text):
        return list(map(int, filter(lambda t: 0 < len(t), text.split(":")[1].strip().split(" "))))

    def get_distance(self, push_time, max_race_time):
        speed = push_time
        remain = max_race_time - push_time
        return speed * remain

    def get_race_distances(self, max_time):
        result = []
        for i in range(max_time + 1):
            result.append(self.get_distance(i, max_time))
        return result

    def get_count_over_of_record(self, max_time, record_distance):
        return len(list(filter(lambda d: record_distance < d, self.get_race_distances(max_time))))
