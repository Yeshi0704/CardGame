from unittest import TestCase, mock
from DeckOfCards import DeckOfCards
from card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_init_valid_52_cards(self):
        """Ensure there are 52 cards """
        self.assertEqual(len(self.deck.cards), 52)

    def test_init_valid_unique_cards(self):
        """Ensure all cards are unique"""
        self.assertEqual(len(self.deck.cards), len(set(str(card) for card in self.deck.cards)))

    def test_all_cards_are_card_objects(self):
        """Test that all items in the deck are instances of the Card class."""
        for card in self.deck.cards:
            self.assertIsInstance(card, Card)

    def test_cards_shuffle(self):
        """Check that after shuffle the order changes"""
        original_order = self.deck.cards.copy()
        self.deck.cards_shuffle()
        self.assertNotEqual(original_order, self.deck.cards)

    def test_deal_one_valid(self):
        """Check that the card removed from the deck"""
        card = self.deck.deal_one()
        self.assertNotIn(card, self.deck.cards)

    def test_deal_one_empty_deck(self):
        """Deal a card from an empty deck"""
        deck = DeckOfCards()
        deck.cards = []
        self.assertEqual(deck.deal_one(),None)

    def test_deal_one_deck_len(self):
        """Check the length of the deck decrease"""
        self.deck.deal_one()
        self.assertEqual(len(self.deck.cards), 51)









