from django.test import TestCase

from polls.models import Task


class TaskModelTest(TestCase):

    def test_string_representation(self):
        task = Task(name="Task 1")
        self.assertEqual(str(task), task.name)
