"""
Polls models test module.
"""
from allauth.utils import get_user_model
from django.test import TestCase

from polls.models import Task, Vote


class TaskModelTest(TestCase):
    """Task model test calss definition."""
    def setUp(self):
        """
        Creates object requirements.
        """
        username = 'testuser'
        password = 'testpass'
        user_model_class = get_user_model()
        self.user = user_model_class.objects.create_user(
            username, password=password
        )

    def test_string_representation(self):
        """Verifies calling the __str__ method returns the expected string."""
        task = Task(name="Task 1")
        self.assertEqual(str(task), task.name)

    def test_create_task_model(self):
        """
        Verifies that the task instance is created and task fetch by id is the
        same.
        """
        created_task = Task.objects.create( # pylint: disable=E1101
            name='Task 1', created_by=self.user
        )
        fetched_task = Task.objects.get( # pylint: disable=E1101
            id=created_task.id
        )
        self.assertEqual(created_task, fetched_task)



class VoteModelTest(TestCase):
    """Vote model test calss definition."""
    def setUp(self):
        """
        Creates object requirements.
        """
        username = 'testuser'
        password = 'testpass'
        user_model_class = get_user_model()
        self.user = user_model_class.objects.create_user(
            username, password=password
        )
        self.task = Task.objects.create( # pylint: disable=E1101
            name="Task 1", created_by=self.user
        )


    def test_string_representation(self):
        """Verifies calling the __str__ method returns the expected string."""
        task = Vote(value="5", user=self.user, task=self.task)
        self.assertEqual(str(task), 'Task 1 - 5 - testuser')

    def test_create_vote_model(self):
        """
        Verifies that the vote instance is created and vote fetch by id is the
        same.
        """
        created_vote = Vote.objects.create( # pylint: disable=E1101
            value='5', user=self.user, task=self.task
        )
        fetched_vote = Vote.objects.get( # pylint: disable=E1101
            id=created_vote.id
        )
        self.assertEqual(created_vote, fetched_vote)
