"""
Polls models test module.
"""
from django.contrib.auth.models import User
from django.test import TestCase

from polls.tests.helpers import create_user


class TaskModelTest(TestCase):
    """Task model test calss definition."""
    def test_create_user(self):
        """
        Creates object requirements.
        """
        user = create_user()
        self.assertIsInstance(user, User)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass'))
