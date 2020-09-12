"""
Poker Game views test modules.
"""
from django.test import TestCase
from django.urls import reverse

from poker_games.models import PokerGame
from polls.tests.helpers import create_user


class PokerGameCreateViewTest(TestCase):
    """
    Poker Game create view test class definition.
    """
    @classmethod
    def setUpTestData(cls):
        """Sets up required objects like creating a test user."""
        cls.user = create_user()

    def setUp(self):
        """Sets up the user login step."""
        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to
        `/poker_games/poker-game/create`.
        """
        response = self.client.get('/poker_games/poker-game/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send request to
        `/poker_games/poker-game/create` while we use reverse function to get the URL.
        """
        response = self.client.get(reverse('poker-game-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send request to `/poker_games/poker-game/create` we use correct
        tempalte for the response.
        """
        response = self.client.get(reverse('poker-game-create'))
        self.assertTemplateUsed(response, 'poker_games/pokergame_form.html')

    def test_create_poker_game_returns_poker_game_list_page(self):
        """
        Verifies when we send request to `/poker_games/poker-game/create` with valid poker_game
        creation data we see `PokerGame 1` tempalte for the response after
        redirecting to the poker_game list view.
        """
        response = self.client.post(
            reverse('poker-game-create'), {'name': 'PokerGame 1'}, follow=True
        )
        self.assertTemplateUsed(response, 'poker_games/pokergame_list.html')
        self.assertContains(response, 'PokerGame 1')

    def test_create_poker_game_fails_and_returns_poker_game_create_page(self):
        """
        Verifies when we send request to `/poker_games/poker-game/create` with invalid poker_game
        creation data we see `Create PokerGame` in the reponse while remaining in
        page and using the same form.
        """
        response = self.client.post(reverse('poker-game-create'), follow=True)
        self.assertTemplateUsed(response, 'poker_games/pokergame_form.html')
        self.assertContains(response, '<h1>Create Poker Game</h1>')


class PokerGameListViewTest(TestCase):
    """
    PokerGame create view test class definition.
    """
    @classmethod
    def setUpTestData(cls):
        """Sets up required objects like creating a test user."""
        cls.user = create_user()

    def setUp(self):
        """Sets up the user login step."""
        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to
        `/poker_games/poker-game/list`.
        """
        response = self.client.get('/poker_games/poker-game/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send request to
        `/poker_games/poker-game/list` while we use reverse function to get the URL.
        """
        response = self.client.get(reverse('poker-game-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send request to `/poker_games/poker-game/list` we use correct
        tempalte for the response.
        """
        response = self.client.get(reverse('poker-game-list'))
        self.assertTemplateUsed(response, 'poker_games/pokergame_list.html')

    def test_list_poker_game_returns_poker_game_list(self):
        """
        Verifies when we send request to `/poker_games/poker-game/list` we see `PokerGame 1` and
        `PokerGame 2` on the response.
        """
        PokerGame.objects.create( # pylint: disable=E1101
            name='PokerGame 1', created_by=self.user
        )
        PokerGame.objects.create( # pylint: disable=E1101
            name='PokerGame 2', created_by=self.user
        )
        response = self.client.get(reverse('poker-game-list'))
        self.assertContains(response, 'PokerGame 1')
        self.assertContains(response, 'PokerGame 2')
        self.assertContains(response, self.user.username)

    def test_list_poker_game_returns_emptypoker_game_list(self):
        """
        Verifies when we send request to `/poker_games/poker-game/list` we see
        `No poker_games were created yet!` on the response.
        """
        response = self.client.get(reverse('poker-game-list'))
        self.assertContains(response, 'No poker_games were created yet!')


class PokerGameDeleteViewTest(TestCase):
    """
    PokerGame delete view test class definition.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Sets up required objects like creating a test user and poker_game object.
        """
        cls.user = create_user()
        cls.poker_game = PokerGame.objects.create( # pylint: disable=E1101
            name='PokerGame 1', created_by=cls.user
        )

    def setUp(self):
        """Sets up the user login step."""
        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send a GET request to
        `/poker_games/poker-game/delete/<poker_game_id>`.
        """
        response = self.client.get(f'/poker_games/poker-game/delete/{self.poker_game.id}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send a GET request to
        `/poker_games/poker-game/delete/<poker_game_id>` while we use reverse function to get the
        URL.
        """
        response = self.client.get(reverse('poker-game-delete', args=[self.poker_game.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send a GET request to `/poker_games/poker-game/delete/<poker_game_id>`
        we use correct tempalte for the response.
        """
        response = self.client.get(reverse('poker-game-delete', args=[self.poker_game.id]))
        self.assertTemplateUsed(response, 'poker_games/pokergame_confirm_delete.html')

    def test_delete_poker_game_returns_poker_game_list_page(self):
        """
        Verifies when we send a POST request to `/poker_games/poker-game/delete/<poker_game_id>`
        it redirecting to the poker_game list view and the deleted poker_game wont't show up
        anymore.
        """
        response = self.client.post(
            reverse('poker-game-delete', args=[self.poker_game.id]), follow=True
        )
        self.assertTemplateUsed(response, 'poker_games/pokergame_list.html')
        self.assertNotContains(response, self.poker_game.name)


class PokerGameDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up required objects like creating a test user and a poker_game object.
        """
        cls.user = create_user()
        cls.poker_game = PokerGame.objects.create( # pylint: disable=E1101
            name='PokerGame 1', created_by=cls.user
        )

    def setUp(self):
        """Sets up the user login step."""
        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to
        `/poker_games/poker-game/<poker_game.id>`.
        """
        response = self.client.get(f'/poker_games/poker-game/{self.poker_game.id}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send request to
        `/poker_games/poker-game/<poker_game.id>` while we use reverse function to get the URL.
        """
        response = self.client.get(reverse('poker-game-detail', args=[self.poker_game.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send request to `/poker_games/poker-game/<poker_game.id>` we use correct
        tempalte for the response.
        """
        response = self.client.get(reverse('poker-game-detail', args=[self.poker_game.id]))
        self.assertTemplateUsed(response, 'poker_games/pokergame_detail.html')

    def test_view_returns_poker_game_detail(self):
        """
        Verifies when we send request to `/poker_games/poker-game/<poker_game.id>` we see
        `PokerGame 1` on the response.
        """
        response = self.client.get(reverse('poker-game-detail', args=[self.poker_game.id]))
        self.assertContains(response, 'PokerGame 1')
