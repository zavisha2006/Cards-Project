import random as r

class Cards():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.card = []
        self.card.append(suit)
        self.card.append(rank)
class Deck():
    def __init__(self):
        self.suits = ['hearts', 'spades', 'clovers', 'diamonds']
        self.ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.count = 0
        self.deck = []
    def shuffleDeck(self):
        r.shuffle(self.deck)
    def makeDeck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Cards(suit, rank))
                self.count += 1

current_deck = Deck()
current_deck.makeDeck()
current_deck.shuffleDeck()
print([cards.card for cards in current_deck.deck])