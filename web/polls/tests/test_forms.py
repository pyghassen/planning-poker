from allauth.utils import get_user_model
from django.test import TestCase

from polls.forms import TaskForm, VoteForm
from polls.models import Task, PLANNING_CARDS


class TaskFormTest(TestCase):
    def test_create_task(self):
        """
        Verifies that the user instance is assigned to created_by field from
        the created Task model instance.
        """
        user_model_class = get_user_model()
        user = user_model_class.objects.create_user(
            username='testuser', password='testpass'
        )

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
        user_model_class = get_user_model()
        user = user_model_class.objects.create_user(
            username='testuser', password='testpass'
        )
        task = Task.objects.create(created_by=user, name='Task name 1')
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
