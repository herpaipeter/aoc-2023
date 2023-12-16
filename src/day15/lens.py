from enum import Enum


def get_char_hash(char: str, start_value: int) -> int:
    return ((start_value + ord(char)) * 17) % 256


def get_hash(text: str) -> int:
    value = 0
    for c in text:
        value = get_char_hash(c, value)
    return value


class LensOperation(Enum):
    ADD = 0
    REMOVE = 1


class LensCommand:

    def __init__(self, label: str, operation: LensOperation, value: int):
        self.label = label
        self.operation = operation
        self.value = value
        self.index: int = get_hash(label)

    def __eq__(self, other):
        if not isinstance(other, LensCommand):
            raise NotImplementedError
        return self.label == other.label and self.operation == other.operation and self.value == other.value

    def __repr__(self):
        return "[" + self.label + " " + str(self.value) + "]"
