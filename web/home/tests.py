"""
Test home view module.
"""
from django.test import TestCase
from django.urls import reverse

from allauth.utils import get_user_model


class HomeViewTest(TestCase):
    """HomeView test class."""
    def setUp(self):
        username = 'testuser'
        password = 'testpass'
        user_model_class = get_user_model()
        user_model_class.objects.create_user(username, password=password)
        self.client.login(username=username, password=password)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to `/`.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send request to `/` while
        we use reverse function to get the URL.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send request to `/` while we use reverse function to
        get the URL and make sure we use correct tempalte for the response.
        """
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
