class Hand(object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def print_hand(self):
        print self.cards

    def get_score(self):
        score = 0

        for card in self.cards:
            score += card.value

        return score

    def is_busted(self):
        score = self.get_score

        if score > 21:
            return true
        else:
            return false