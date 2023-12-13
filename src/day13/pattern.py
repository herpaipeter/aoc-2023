class Pattern:

    def __init__(self, pattern: str):
        self.rows = pattern.split("\n")
        self.cols = []
        if 0 < len(self.rows):
            for i in range(len(self.rows[0])):
                col = ""
                for r in self.rows:
                    col += r[i]
                self.cols.append(col)

    def get_h_refl(self):
        return self.get_refl(self.rows)

    def get_v_refl(self):
        return self.get_refl(self.cols)

    def get_refl(self, pattern: list[str]) -> int:
        result = 0
        if 1 < len(pattern):
            for i in range(len(pattern) - 1):
                if pattern[i] == pattern[i + 1]:
                    result = max(result, self.get_refl_value(pattern, i))
        return result

    def get_refl_value(self, pattern: list[str], i: int) -> int:
        for j in range(i + 1):
            if (0 <= i - j and i + 1 + j <= len(pattern) - 1
                    and pattern[i - j] != pattern[i + 1 + j]):
                return 0
        return i + 1

    def get_h_refl_smudge(self):
        return self.get_refl_smudge(self.rows)

    def get_v_refl_smudge(self):
        return self.get_refl_smudge(self.cols)

    def get_refl_smudge(self, pattern: list[str]) -> int:
        result = 0
        if 1 < len(pattern):
            for i in range(len(pattern) - 1):
                pattern_diffs = len([x for x, y in zip(pattern[i], pattern[i + 1]) if x != y])
                if pattern_diffs <= 1:
                    result = max(result, self.get_refl_value_smudge(pattern, i))
        return result

    def get_refl_value_smudge(self, pattern: list[str], i: int) -> int:
        found_diffs = 0
        j = 0
        for j in range(i + 1):
            if 0 <= i - j and i + 1 + j <= len(pattern) - 1:
                found_diffs += len([x for x, y in zip(pattern[i - j], pattern[i + 1 + j]) if x != y])
        return i + 1 if found_diffs == 1 and (i - j == 0 or i + 1 + j == len(pattern) - 1) else 0
