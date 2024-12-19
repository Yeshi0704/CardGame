from unittest import TestCase,mock
from CardGame import CardGame
from Player import Player
from DeckOfCards import DeckOfCards
from card import Card

class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("niki","dani",10)

    def test_init_valid(self):
        """Check if the object is defined correctly"""
        self.assertEqual("niki", self.game.player_1.name)
        self.assertEqual("dani", self.game.player_2.name)
        self.assertEqual(10, self.game.num_of_cards)

    def test_init_invalid_player1_name_type(self):
        """Check if the player name type is correct"""
        with self.assertRaises(TypeError):
            game = CardGame(10, "dani", 10)

    def test_init_invalid_player2_name_type(self):
        """Check if the player name type is correct"""
        with self.assertRaises(TypeError):
            game = CardGame("niki", 10 , 10)

    def test_init_invalid_num_of_cards_type(self):
        """Check if num_of_cards type is correct"""
        with self.assertRaises(TypeError):
            game = CardGame("niki", "dani", "10")

    def test_init_num_of_cards_above_the_range(self):
        """Check if num_of_cards is in the range 10-26"""
        game = CardGame("niki", "dani", 27)  # Greater than 26
        self.assertEqual(game.num_of_cards, 26)

    def test_init_num_of_cards_under_the_range(self):
        """Check if num_of_cards is in the range 10-26"""
        game = CardGame("niki", "dani", 9)  # Less than 10
        self.assertEqual(game.num_of_cards, 26)

    @mock.patch("DeckOfCards.DeckOfCards.cards_shuffle")
    def test_new_game_valid_shuffle_cards(self,mock):
        """Check if the cards are shuffled correctly"""
        self.game.new_game()
        self.game.game_packet.cards_shuffle()
        mock.assert_called_once()

    def test_new_game_start_game_is_False(self):
        """Check if the param start_game is started"""
        self.assertEqual(self.game.start_game,False)

    def test_new_game_message(self):
        """Check if the exception message is printed when new game is called during the game"""
        game1 = CardGame("niki", "dani", 10)
        message = game1.new_game()
        self.assertEqual(message, None)

    def test_get_winner_player1_wins(self):
        """Test if Player 1 wins when they have more cards."""
        self.game.player_1.name = "Player1"
        self.game.player_2.name = "Player2"
        self.game.player_1.player_packet_cards = [Card("3", "Club"), Card("3", "Club")]
        self.game.player_2.player_packet_cards = [Card("3", "Club")]

        winner = self.game.get_winner()
        self.assertEqual(winner, self.game.player_1)

    def test_get_winner_player2_wins(self):
        """Test if Player 2 wins when they have more cards."""
        self.game.player_1.name = "Player1"
        self.game.player_2.name = "Player2"
        self.game.player_1.player_packet_cards = [Card("3", "Club")]
        self.game.player_2.player_packet_cards = [Card("3", "Club"), Card("3", "Club")]

        winner = self.game.get_winner()
        self.assertEqual(winner, self.game.player_2)

    def test_get_winner_draw(self):
        """Test if the result is None when both players have the same number of cards."""
        self.game.player_1.name = "Player1"
        self.game.player_2.name = "Player2"
        self.game.player_1.player_packet_cards = [Card("3", "Club"), Card("3", "Club")]
        self.game.player_2.player_packet_cards = [Card("3", "Club"), Card("3", "Club")]
        winner = self.game.get_winner()
        self.assertIsNone(winner)






