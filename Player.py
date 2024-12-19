import random
from DeckOfCards import DeckOfCards
from card import Card

class Player:
    def __init__(self,name, num_of_cards=26):
        if type(name) != str:
            raise TypeError("name must be str")
        if type(num_of_cards) != int:
            raise TypeError("num_of_cards must be int")
        self.name = name
        self.player_packet_cards = []
        self.num_of_cards = num_of_cards
        if num_of_cards<10 or num_of_cards>26:
            self.num_of_cards = 26

    def __repr__(self):
        return f"Player:{self.name} with {len(self.player_packet_cards)} cards"

    def set_hand(self, deck:DeckOfCards):
        """The method gets a random card from the packet and give it to the player"""
        if type(deck) != DeckOfCards:
            raise TypeError("deck must be from type DeckOfCards")
        if len(deck.cards) == 0:
            return None
        for i in range(self.num_of_cards):
            card = deck.deal_one()
            self.player_packet_cards.append(card)

    def get_card(self):
        """The method removes random card from the player packet"""
        if len(self.player_packet_cards) == 0: # Check if the player packet is empty
            return None
        card = random.choice(self.player_packet_cards)
        self.player_packet_cards.remove(card)
        return card

    def add_card(self, card:Card):
        """The method adds card to the player packet"""
        if type(card) != Card:
            raise TypeError("card must be from type Card")
        self.player_packet_cards.append(card)
