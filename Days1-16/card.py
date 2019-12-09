import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck():
    suits = "hearts diamonds spades clubs".split()
    ranks = [ str(rank) for rank in range(2, 11) ] + list("JQKA")

    def __init__(self):

        self._cards = [
            Card(rank, suit) for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


f = FrenchDeck()
# print(f"Is this your card: {choice(f)}")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    # why are we multiplying by the len of suit values
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(f, key=spades_high):
    print(card)
