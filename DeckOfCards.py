from card import Card
import random


class DeckOfCards:
    def __init__(self):
        """Create a list of 52 uniq cards"""
        suits = {'Diamond': 1, 'Spade': 2, 'Heart': 3, 'Club': 4}
        num_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.cards = []
        for key in suits:
            for num_value in num_values:
                card = Card(num_value, key)
                self.cards.append(card)

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)

    def cards_shuffle(self):
        """The method shuffles cards"""
        random.shuffle(self.cards)

    def deal_one(self):
        """The method remove random card from the game deck"""
        if len(self.cards) == 0:
            return None
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card



