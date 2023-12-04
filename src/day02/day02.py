import re
from dataclasses import dataclass

from src.aoc_solver import runifmain, AocSolver


@dataclass
class Game:
    id: int
    rounds: list


@dataclass
class CubeSet:
    blue: int
    red: int
    green: int


@runifmain(__name__)
class Day02(AocSolver):

    def __init__(self):
        super().__init__(__class__.__name__)

    def parse(self, input_data):
        """Parse input."""
        games = []
        lines = input_data.split('\n')
        matcher = re.compile(r"Game (\d+): (.+)")
        for line in lines:
            match = matcher.match(line)
            game_id, game_list = match.groups()
            game = Game(int(game_id), [])
            gamesstring = game_list.split(';')
            for gameline in gamesstring:
                color_names = gameline.split(',')
                cubeset = CubeSet(0, 0, 0)
                for color in color_names:
                    color_num_name = color.strip().split(' ')
                    if color_num_name[1] == "green":
                        cubeset.green = int(color_num_name[0])
                    if color_num_name[1] == "blue":
                        cubeset.blue = int(color_num_name[0])
                    if color_num_name[1] == "red":
                        cubeset.red = int(color_num_name[0])
                game.rounds.append(cubeset)
            games.append(game)
        return games

    def check_limit(self, games, red, green, blue):
        result = 0
        for game in games:
            valid_series = True
            for cubeset in game.rounds:
                if red < cubeset.red or green < cubeset.green or blue < cubeset.blue:
                    valid_series = False
                    break
            if valid_series:
                result += game.id
        return result

    def get_max_per_game_power_sum(self, games):
        powers = []
        for game in games:
            reds = map(lambda g: g.red, game.rounds)
            blues = map(lambda g: g.blue, game.rounds)
            greens = map(lambda g: g.green, game.rounds)
            powers.append(max(reds) * max(blues) * max(greens))
        return sum(powers)

    def part1(self, data):
        """Solve part 1."""
        return self.check_limit(data, 12, 13, 14)

    def part2(self, data):
        """Solve part 2."""
        return self.get_max_per_game_power_sum(data)
