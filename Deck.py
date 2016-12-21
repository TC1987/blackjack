import random
from Card import Card

class Deck(object):
    def __init__(self):
        self.cards = []

        suites = ['S', 'C', 'D', 'H']

        for suite in suites:
            for number in xrange(2, 15):
                self.cards.append(Card(suite, number))

        self.shuffle_cards()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards[0]
        del self.cards[0]
        return card
