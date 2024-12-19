from unittest import TestCase, mock
from card import Card

class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card('Ace', 'Club')

    def test_init_valid(self):
        """Check that the object is initialized correctly"""
        self.assertEqual("Ace", self.card1.value)
        self.assertEqual('Club', self.card1.suite)

    def test_init_invalid_value_value(self):
        """Check the type of Card object value is from range 2-10"""
        with self.assertRaises(ValueError):
            card1 = Card("17", 'Club')

    def test_init_invalid_suite_value(self):
        """Check the type of Card object suite is correct"""
        with self.assertRaises(ValueError):
            card1 = Card("3", 'Flower')

    def test_init_invalid_value_type(self):
        """Check that value is from type string"""
        with self.assertRaises(TypeError):
         card1 = Card(3, 'Club')

    def test_init_invalid_suite_type(self):
        """Check that suite is from type string"""
        with self.assertRaises(TypeError):
            card1 = Card(3, 4)

    def test_translate_valid_number(self):
        """Check that str is translated correctly to int"""
        card2 = Card("5", 'Spade')
        self.assertEqual(card2.translate(), 5)

    def test_translate_valid_K_symbol(self):
        """Check that symbols are translated correctly"""
        card2 = Card("K", 'Spade')
        self.assertEqual(card2.translate(), 13)

    def test_translate_valid_J_symbol(self):
        """Check that symbols are translated correctly"""
        card2 = Card("J", 'Spade')
        self.assertEqual(card2.translate(), 11)

    def test_translate_valid_Q_symbol(self):
        """Check that symbols are translated correctly"""
        card2 = Card("Q", 'Spade')
        self.assertEqual(card2.translate(), 12)

    def test_translate_valid_Ace_symbol(self):
        """Check that symbols are translated correctly"""
        card2 = Card("Ace", 'Spade')
        self.assertEqual(card2.translate(), 14)

    def test__gt__valid_True(self):
        """Check if card is greater than another card"""
        card2 = Card('K', 'Spade')
        self.assertTrue(self.card1 > card2)

    def test__gt__valid_False(self):
        """Check if card is NOT greater than another card"""
        card1 = Card("3", 'Spade')
        card2 = Card('Ace', 'Heart')
        self.assertFalse(card1 > card2)

    def test__gt__valid_with_equal_values_True(self):
        """Check if card is greater than another card when their values are equals"""
        card1 = Card("Ace", 'Spade')
        card2 = Card('Ace', 'Heart')
        self.assertFalse(card1 > card2)

    def test__gt__invalid_card_type(self):
        """Check that the param is from type Card"""
        with self.assertRaises(TypeError):
            self.card1.__gt__(10)

    def test_eq_valid_True(self):
        """Check that the two cards are equal"""
        card2 = Card('Ace', 'Club')
        self.assertTrue(self.card1 == card2)

    def test_eq_valid_False(self):
        """Check that the two cards are NOT equal"""
        card2 = Card('K', 'Spade')
        self.assertFalse(self.card1 == card2)

    def test_eq_invalid_card_type(self):
        """Check that the param is from type Card"""
        with self.assertRaises(TypeError):
            self.card1.__eq__(10)

