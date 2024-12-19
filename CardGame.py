from logging import raiseExceptions

from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, player_1_name, player_2_name, num_of_cards):
        if type(player_1_name) != str:
            raise TypeError("player_1_name must be str")
        if type(player_2_name) != str:
            raise TypeError("player_2_name must be str")
        if type(num_of_cards) != int:
            raise TypeError("num_of_cards must be int")
        self.num_of_cards = num_of_cards
        if num_of_cards<10 or num_of_cards>26:
            self.num_of_cards = 26
        self.game_packet = DeckOfCards()
        self.player_1 = Player(player_1_name, num_of_cards)
        self.player_2 = Player(player_2_name, num_of_cards)
        self.start_game = True  # True if the game has NOT started
        self.new_game()
        self.start_game = False  # False if the game has started

    def new_game(self):
        """The method initialize the game"""
        if self.start_game:  # Check if the game has already started
            self.game_packet.cards_shuffle()
            self.player_1.set_hand(self.game_packet)
            self.player_2.set_hand(self.game_packet)
        else:
            print("Cannot initialize during a game")
            return None

    def get_winner(self):
        """The method calculate who is the winner in the game"""
        if len(self.player_1.player_packet_cards)>len(self.player_2.player_packet_cards):
            return self.player_1
        elif len(self.player_2.player_packet_cards)>len(self.player_1.player_packet_cards):
            return self.player_2
        return None




