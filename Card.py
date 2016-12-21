class Card(object):
    def __init__(self, suite, number):
        self.suite = suite

        face = ['J', 'Q', 'K']

        if number == 14:
            value = 1 or 11
            num = 'A'
        elif number > 10:
            value = 10
            num = face[number - 11]
        else:
            value = number
            num = number

        self.value = value
        self.num = num

    def __repr__(self):
        return self.suite + str(self.num)