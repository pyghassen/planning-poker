"""
Task model test module.
"""
from django.test import TestCase

from polls.models import Task


class TaskModelTest(TestCase):
    """TaskModel test calss definition."""
    def test_string_representation(self):
        """Verifies calling the __str__ method returns the expected string."""
        task = Task(name="Task 1")
        self.assertEqual(str(task), task.name)
