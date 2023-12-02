from src.aoc_solver import AocSolver, runifmain


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


@runifmain(__name__)
class Day01(AocSolver):
    num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def prefix_number_words_with_digit(self, text):
        result = ""
        for i in range(0, len(text)):
            wind = self.get_word_index_at_start(text[i:i + 5])
            if -1 < wind:
                result += str(wind + 1) + text[i]
            else:
                result += text[i]
        return result

    def get_word_index_at_start(self, text):
        for word in self.num_words:
            if 0 == text.find(word):
                return self.num_words.index(word)
        return -1

    def parse(self, input_data):
        """Parse input."""
        return input_data.split('\n')

    def part1(self, data):
        """Solve part 1."""
        return summa(data)

    def part2(self, data):
        """Solve part 2."""
        result = []
        for elem in data:
            result.append(self.prefix_number_words_with_digit(elem))
        return summa(result)
