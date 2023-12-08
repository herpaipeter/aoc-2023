from dataclasses import dataclass

JOKER_CARD = "J"
MAX_CARD_CATEGORY = 14
cards_wo_joker = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


class Hand:
    dejokerized: str = ""

    def __init__(self, cards, joker=False, dejokerize=True):
        self.cards = cards
        self.joker = joker
        self.dejokerized = self.replace_jokers() if self.joker and dejokerize else self.cards

    def __eq__(self, other):
        return self.cards == other.cards

    def __repr__(self):
        return self.cards + " " + str(self.joker)

    def __lt__(self, other):
        if not isinstance(other, Hand):
            raise NotImplementedError
        if self.get_category() < other.get_category():
            return True
        if self.get_category() == other.get_category():
            for i in range(len(self.cards)):
                if self.get_index(self.cards[i]) != other.get_index(other.cards[i]):
                    return self.get_index(self.cards[i]) < other.get_index(other.cards[i])
            return True
        return False

    def get_category(self):
        return self.get_category_for(self.dejokerized)

    def get_category_for(self, cards: str):
        counter = [0] * (MAX_CARD_CATEGORY + 1)
        for c in cards:
            counter[self.get_index(c)] += 1
        fives = counter.count(5)
        fours = counter.count(4)
        threes = counter.count(3)
        twos = counter.count(2)
        if 1 == fives:
            return 7
        elif 1 == fours:
            return 6
        elif 1 == threes and 1 == twos:
            return 5
        elif 1 == threes and 0 == twos:
            return 4
        elif 2 == twos:
            return 3
        elif 0 == threes and 1 == twos:
            return 2
        return 1

    def get_index(self, c):
        if "1" <= c <= "9":
            return int(c)
        elif "A" == c:
            return MAX_CARD_CATEGORY
        elif "K" == c:
            return MAX_CARD_CATEGORY - 1
        elif "Q" == c:
            return MAX_CARD_CATEGORY - 2
        elif "J" == c:
            return MAX_CARD_CATEGORY - 3 if not self.joker else 1
        elif "T" == c:
            return MAX_CARD_CATEGORY - 4

    def replace_jokers(self):
        if self.joker and 0 < self.cards.count(JOKER_CARD):
            possible_cards = list(filter(lambda c: 0 < self.cards.count(c), cards_wo_joker))
            max_cards = self.cards
            cards = max_cards
            for c0 in possible_cards:
                if self.cards[0] == JOKER_CARD:
                    cards = c0 + cards[1:]
                for c1 in possible_cards:
                    if self.cards[1] == JOKER_CARD:
                        cards = cards[:1] + c1 + cards[2:]
                    for c2 in possible_cards:
                        if self.cards[2] == JOKER_CARD:
                            cards = cards[:2] + c2 + cards[3:]
                        for c3 in possible_cards:
                            if self.cards[3] == JOKER_CARD:
                                cards = cards[:3] + c3 + cards[4:]
                            for c4 in possible_cards:
                                if self.cards[4] == JOKER_CARD:
                                    cards = cards[:4] + c4
                                if Hand(max_cards, True, False) < Hand(cards, True, False):
                                    max_cards = cards
            return max_cards
        else:
            return self.cards


@dataclass
class Bid:
    hand: Hand
    amount: int

    def __lt__(self, other):
        if not isinstance(other, Bid):
            raise NotImplementedError
        return self.hand < other.hand
