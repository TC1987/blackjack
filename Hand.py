class Hand(object):
    def __init__(self):
        self.cards = []
        self.balance = 1000
        self.request_loan = 3

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        self.balance += amount
        print self.balance

    def get_loan(self):
        return self.request_loan

    def add_card(self, card):
        self.cards.append(card)

    def print_hand(self):
        print self.cards

    def get_score(self):
        total_score = 0

        for card in self.cards:
            total_score += card.value

        return total_score

    def is_busted(self):
        score = self.get_score()

        if score > 21:
            return True
        else:
            return False