"""
Poker Game models test module.
"""
from django.test import TestCase

from poker_games.models import PokerGame
from polls.tests.helpers import create_user


class PokerGameModelTest(TestCase):
    """Poker Game model test calss definition."""
    @classmethod
    def setUpTestData(cls):
        """
        Creates object requirements.
        """
        cls.user = create_user()

    def test_string_representation(self):
        """Verifies calling the __str__ method returns the expected string."""
        poker_game = PokerGame(name="PokerGame 1")
        self.assertEqual(str(poker_game), poker_game.name)

    def test_create_poker_game_model(self):
        """
        Verifies that the poker_game instance is created and poker_game fetch by id is the
        same.
        """
        created_poker_game = PokerGame.objects.create( # pylint: disable=E1101
            name='PokerGame 1', created_by=self.user
        )
        fetched_poker_game = PokerGame.objects.get( # pylint: disable=E1101
            id=created_poker_game.id
        )
        self.assertEqual(created_poker_game, fetched_poker_game)
