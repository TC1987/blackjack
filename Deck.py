import random
from Card import Card

class Deck(object):
    def __init__(self):
        print 'New Deck Created'
        self.cards = []

        suites = ['S', 'C', 'D', 'H']

        for suite in suites:
            for number in xrange(2, 15):
                self.cards.append(Card(suite, number))

    def shuffle_cards(self):
        print 'Shuffled'
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards[0]
        del self.cards[0]
        return card

new_deck = Deck()
new_deck.shuffle_cards()
# new_deck.draw_card()





# from Card import Card
# from random import shuffle
#
# class Deck(object):
#
#     def __init__(self):
#         # list of 52 cards, with 1 of each rank and suite
#         self.cards = []
#
#         for i in xrange(1,14):
#             new_card = Card("S", i)
#             self.cards.append(new_card)
#
#         for i in xrange(1,14):
#             new_card = Card("C", i)
#             self.cards.append(new_card)
#
#         for i in xrange(1,14):
#             new_card = Card("D", i)
#             self.cards.append(new_card)
#
#         for i in xrange(1,14):
#             new_card = Card("H", i)
#             self.cards.append(new_card)
#
#         shuffle(self.cards)
#
#     def draw_card(self):
#         card = self.cards[0]
#         del self.cards[0]
#         return card