from src.common.point import Point


class EngineNumber:

    def __init__(self, number: int, start: Point, end: Point):
        self.number = number
        self.start = start
        self.end = end

    def __repr__(self):
        return str(self.number) + " @ " + str(self.start) + "-" + str(self.end)

    def __eq__(self, __o):
        if isinstance(__o, EngineNumber):
            return self.number == __o.number and self.start == __o.start and self.end == __o.end
        raise NotImplementedError


class EngineSymbol:

    def __init__(self, symbol: str, position: Point):
        self.symbol = symbol
        self.position = position

    def __repr__(self):
        return str(self.symbol) + " @ " + str(self.position)

    def __eq__(self, __o):
        if isinstance(__o, EngineSymbol):
            return self.symbol == __o.symbol and self.position == __o.position
        raise NotImplementedError
