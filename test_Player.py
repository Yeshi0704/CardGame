from unittest import TestCase, mock
from Player import Player
from DeckOfCards import DeckOfCards
from card import Card

class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player('Yeshi', 10)
        self.deck = DeckOfCards()

    def test_init_valid(self):
        """Check that the object configured correctly"""
        self.assertEqual('Yeshi', self.player.name)
        self.assertEqual(10, self.player.num_of_cards)

    def test_init_invalid_name_type(self):
        """Check that num_of_cards is from type str"""
        with self.assertRaises(TypeError):
            player1 = Player(123, 12)

    def test_init_invalid_number_of_card_type(self):
        """Check that num_of_cards is from type int"""
        with self.assertRaises(TypeError):
            player1 = Player("Yeshi", "12")

    def test_init_num_of_cards_above_the_range(self):
        """Check if num_of_cards is in the range 10-26"""
        player1 = Player("Yeshi", 27)  # bigger than 26
        self.assertEqual(player1.num_of_cards, 26)

    def test_init_num_of_cards_below_the_range(self):
        """Check if num_of_cards is in the range 10-26"""
        player1 = Player("Yeshi", 9)  # smaller than 26
        self.assertEqual(player1.num_of_cards, 26)

    def test_set_hand_invalid_deck_type(self):
        """Check that param for set_hand is from type DeckOfCards"""
        with self.assertRaises(TypeError):
            self.player.set_hand(11)

    @mock.patch("DeckOfCards.DeckOfCards.deal_one", return_value=Card("5","Club"))
    def test_set_hand_valid(self, mock):
        """Check that player gets the exact num of cards """
        self.player.set_hand(self.deck)
        self.assertIn(Card("5","Club"), self.player.player_packet_cards)

    def test_set_hand_len(self):
        """Check that player gets the exact num of cards """
        self.player.set_hand(self.deck)
        self.assertEqual(10, len(self.player.player_packet_cards))

    def test_set_hand_empty_deck(self):
        self.deck.cards = []
        self.assertEqual(self.player.set_hand(self.deck), None)

    def test_get_card_valid(self):
        """Check that player gets the correct card """
        self.player.set_hand(self.deck)
        card = self.player.get_card()
        self.assertNotIn(card, self.player.player_packet_cards)

    def test_get_card_len(self):
        """Check the player packet decrease"""
        self.player.set_hand(self.deck)
        self.assertEqual(len(self.player.player_packet_cards), 10)

    def test_get_card_card_not_in_game_deck(self):
        """Check that the card not in the player packet """
        card = self.player.get_card()
        self.assertNotIn(card, self.player.player_packet_cards)

    def test_get_card_invalid_empty_packet(self):
        """Check the method while the packet is empty"""
        self.player.player_packet_cards = []
        self.assertEqual(self.player.get_card(),None)

    def test_add_card_valid_card(self):
        """Add a card and check if exist in the player packet"""
        card = Card("3",'Heart')
        self.player.add_card(card)
        self.assertIn(card,self.player.player_packet_cards)

    def test_add_card_invalid_card_type(self):
        """Check that param for add_card is from type Card"""
        with self.assertRaises(TypeError):
            self.player.add_card(5)
