from django.test import TestCase

from polls.forms import TaskForm, VoteForm
from polls.models import Task, PLANNING_CARDS
from polls.tests.helpers import create_user


class TaskFormTest(TestCase):
    def test_create_task(self):
        """
        Verifies that the user instance is assigned to created_by field from
        the created Task model instance.
        """
        user = create_user()

        task_form = TaskForm(user=user, data={'name':'Task name 1'})
        self.assertEqual(task_form.user, user)
        self.assertTrue(task_form.is_valid())

        task = task_form.save()
        self.assertEqual(task.created_by, user)


class VoteFormTest(TestCase):
    def test_create_vote(self):
        """
        Verifies that the user instance, and the task_id were assigned to
        correctly to the Vote model instance.
        """
        user = create_user()
        task = Task.objects.create(created_by=user, name='Task name 1') # pylint: disable=E1101
        # Picking up the first value from Planning cards values tuple.
        value = PLANNING_CARDS[0][0]

        vote_form = VoteForm(user=user, task_id=task.id, data={'value': value})
        self.assertEqual(vote_form.user, user)
        self.assertEqual(vote_form.task_id, task.id)
        self.assertTrue(vote_form.is_valid())

        vote = vote_form.save()
        self.assertEqual(vote.user, user)
        self.assertEqual(vote.task, task)
        self.assertEqual(vote.value, value)
