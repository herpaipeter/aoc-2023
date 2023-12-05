from dataclasses import dataclass


@dataclass
class Range:
    map_from: int
    map_to: int
    length: int

    def __lt__(self, other):
        if not isinstance(other, Range):
            raise TypeError
        return self.map_from < other.map_from

    def __repr__(self):
        return ("[" + "(" + str(self.map_from) + ":" + str(self.map_from + self.length - 1) + ")->" +
                "(" + str(self.map_to) + ":" + str(self.map_to + self.length - 1) + ")" +"]")

    def contains(self, number):
        return self.map_from <= number < self.map_from + self.length

    def map(self, number):
        if not self.contains(number):
            raise KeyError
        return self.map_to + (number - self.map_from)

    def merge(self, other):
        if not isinstance(other, Range):
            raise TypeError
        if self.is_disjunct(other):
            return [self], [other], []

        lower_min = min(self.map_to, other.map_from)
        lower_max = max(self.map_to, other.map_from)
        upper_min = min(self.map_to + self.length, other.map_from + other.length)
        upper_max = max(self.map_to + self.length, other.map_from + other.length)
        lower_length = lower_max - lower_min
        middle_length = upper_min - lower_max
        upper_length = upper_max - upper_min

        ranges_self = []
        ranges_other = []
        ranges_new = []
        if lower_min == self.map_to:
            if 0 < lower_length:
                ranges_self.append(Range(self.map_from, self.map_to, lower_length))
            ranges_new.append(Range(self.map_from + lower_length, other.map_to, middle_length))
        elif lower_min == other.map_from:
            if 0 < lower_length:
                ranges_other.append(Range(other.map_from, other.map_to, lower_length))
            ranges_new.append(Range(self.map_from, other.map_to + lower_length, middle_length))

        if upper_max == self.map_to + self.length and 0 < upper_length:
            ranges_self.append(
                Range(self.map_from + self.length - upper_length, self.map_to + self.length - upper_length,
                      upper_length))
        elif upper_max == other.map_from + other.length and 0 < upper_length:
            ranges_other.append(
                Range(other.map_from + other.length - upper_length, other.map_to + other.length - upper_length,
                      upper_length))

        return ranges_self, ranges_other, ranges_new

    def is_disjunct(self, other):
        return self.map_to + self.length - 1 < other.map_from \
            or other.map_from + other.length - 1 < self.map_to

    def is_empty(self):
        return self.length < 1


@dataclass
class RangeMap:
    ranges: list[Range]

    def map(self, number):
        for r in self.ranges:
            if r.contains(number):
                return r.map(number)
        return number

    def merge(self, other: Range):
        self.ranges.sort(key=lambda n: n.map_to)
        lefts = []
        rights = [other]
        for l in self.ranges:
            new_rights = []
            l_changed = False
            for r in rights:
                if not l.is_disjunct(r):
                    left, right, new = l.merge(r)
                    lefts += left
                    lefts += new
                    new_rights += right
                    l_changed = True
                else:
                    new_rights.append(r)
            rights = new_rights
            if not l_changed:
                lefts.append(l)
        return lefts + rights


@dataclass
class Almanac:
    seeds: list
    range_maps: list[RangeMap]

    def merge_range_maps(self) -> RangeMap:
        merged = self.range_maps[0]
        for i in range(1, len(self.range_maps)):
            for m in self.range_maps[i].ranges:
                merged = RangeMap(merged.merge(m))
        return merged


@dataclass
class SeedRange:
    start: int
    end: int
