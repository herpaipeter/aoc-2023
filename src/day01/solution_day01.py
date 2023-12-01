# aoc_template.py

import pathlib
import sys

num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_calibration_value(param):
    filtered = ""
    for c in param:
        filtered += c if c.isdigit() else ''

    if 1 == len(filtered):
        if filtered[0].isdigit():
            return int(filtered[0] + filtered[0])
    if 1 < len(filtered):
        if filtered[0].isdigit() and filtered[-1].isdigit():
            return int(filtered[0] + filtered[-1])
    return None


def summa(str_list):
    result = 0
    for str_elem in str_list:
        result += get_calibration_value(str_elem)
    return result


def prefix_number_words_with_digit(text):
    result = ""
    for i in range(0, len(text)):
        wind = get_word_index_at_start(text[i:i + 5])
        if -1 < wind:
            result += str(wind + 1) + text[i]
        else:
            result += text[i]
    return result


def get_word_index_at_start(text):
    for word in num_words:
        if 0 == text.find(word):
            return num_words.index(word)
    return -1


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split('\n')


def part1(data):
    """Solve part 1."""
    return summa(data)


def part2(data):
    """Solve part 2."""
    result = []
    for elem in data:
        result.append(prefix_number_words_with_digit(elem))
    return summa(result)


def solve(p_input):
    """Solve the puzzle for the given input."""
    data = parse(p_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
