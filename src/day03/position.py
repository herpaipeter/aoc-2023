from src.common.point import Point


class NumberPosition:

    def __init__(self, number: int, pos_from: Point, pos_to: Point):
        self.number = number
        self.pos_from = pos_from
        self.pos_to = pos_to

    def __repr__(self):
        return str(self.number) + " @ " + str(self.pos_from) + "-" + str(self.pos_to)

    def __eq__(self, __o):
        if isinstance(__o, NumberPosition):
            return self.number == __o.number and self.pos_from == __o.pos_from and self.pos_to == __o.pos_to
        return NotImplemented


class SymbolPosition:

    def __init__(self, symbol: str, position):
        self.symbol = symbol
        self.position = position

    def __repr__(self):
        return str(self.symbol) + " @ " + str(self.position)

    def __eq__(self, __o):
        if isinstance(__o, SymbolPosition):
            return self.symbol == __o.symbol and self.position == __o.position
        return NotImplemented
