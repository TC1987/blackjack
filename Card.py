class Card(object):
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number

        if number == 14:
            value = 1 or 11
        elif number > 10:
            value = 10
        else:
            value = number

        self.value = value

    def __repr__(self):
        return self.suite + " " + str(self.number) + " " + str(self.value)