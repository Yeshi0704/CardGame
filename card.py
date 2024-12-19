
class Card:
    def __init__(self, value, suite):
        self.suits = {'Diamond': 1, 'Spade': 2, 'Heart': 3, 'Club': 4}
        self.values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        if type(suite) != str:
            raise TypeError('suite must be string')
        if type(value) != str:
            raise TypeError('value must be string')
        if suite in self.suits:
            self.suite = suite
        else:
            raise ValueError('Invalid suite')

        if value in self.values:
            self.value = value
        else:
            raise ValueError('Invalid value')

    def __repr__(self):
        return f"{self.value} Of {self.suite}"

    def translate(self):
        """This method translates the string into an int value for comparison"""
        if self.value == 'Ace':
            return 14
        if self.value == 'J':
            return 11
        if self.value == 'Q':
            return 12
        if self.value == 'K':
            return 13
        else:
            return int(self.value)

    def __gt__(self, other):
        """Check if a Card object is bigger than another"""
        if type(other) != Card:
            raise TypeError("Other must be type Card")
        other_value = other.translate()
        self_value = self.translate()
        if self_value > other_value:
            return True
        if self_value == other_value:
            return self.suits[self.suite] > self.suits[other.suite]
        else:
            return False

    def __eq__(self,other):
        """Check if a Card object is equal to another"""
        if type(other) != Card:
            raise TypeError("Other must be type Card")
        return self.value == other.value and self.suite == other.suite
