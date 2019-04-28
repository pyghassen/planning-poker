"""
Task views test modules.
"""
from django.test import TestCase
from django.urls import reverse

from allauth.utils import get_user_model

from polls.models import Task


class TaskCreateViewTest(TestCase):
    """
    Task create view test class definition.
    """
    def setUp(self):
        """
        Sets up required objects like creating a test user and login.
        """
        username = 'testuser'
        password = 'testpass'
        user_model_class = get_user_model()
        self.user = user_model_class.objects.create_user(
            username, password=password
        )
        self.client.login(username=username, password=password)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/task/create`.
        """
        response = self.client.get('/polls/task/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/task/create` while we use reverse function to get the URL.
        """
        response = self.client.get(reverse('task-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send request to `/polls/task/create` we use correct
        tempalte for the response.
        """
        response = self.client.get(reverse('task-create'))
        self.assertTemplateUsed(response, 'polls/task_form.html')

    def test_create_task_returns_task_list_page(self):
        """
        Verifies when we send request to `/polls/task/create` with valid task
        creation data we see `Task 1` tempalte for the response after
        redirecting to the task list view.
        """
        response = self.client.post(
            reverse('task-create'), {'name': 'Task 1'}, follow=True
        )
        self.assertTemplateUsed(response, 'polls/task_list.html')
        self.assertContains(response, 'Task 1')

    def test_create_task_fails_and_returns_task_create_page(self):
        """
        Verifies when we send request to `/polls/task/create` with invalid task
        creation data we see `Create Task` in the reponse while remaining in
        page and useing the same form.
        """
        response = self.client.post(reverse('task-create'), follow=True)
        self.assertTemplateUsed(response, 'polls/task_form.html')
        self.assertContains(response, 'Create Task')


class TaskListViewTest(TestCase):
    """
    Task create view test class definition.
    """
    def setUp(self):
        """
        Sets up required objects like creating a test user and login.
        """
        username = 'testuser'
        password = 'testpass'
        user_model_class = get_user_model()
        self.user = user_model_class.objects.create_user(
            username, password=password
        )
        self.client.login(username=username, password=password)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/task/list`.
        """
        response = self.client.get('/polls/task/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/task/list` while we use reverse function to get the URL.
        """
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send request to `/polls/task/list` we use correct
        tempalte for the response.
        """
        response = self.client.get(reverse('task-list'))
        self.assertTemplateUsed(response, 'polls/task_list.html')

    def test_list_task_returns_task_list(self):
        """
        Verifies when we send request to `/polls/task/list` we see `Task 1` and
        `Task 2` on the response.
        """
        Task.objects.create( # pylint: disable=E1101
            name='Task 1', created_by=self.user
        )
        Task.objects.create( # pylint: disable=E1101
            name='Task 2', created_by=self.user
        )
        response = self.client.get(reverse('task-list'))
        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Task 2')
        self.assertContains(response, self.user.username)

    def test_list_task_returns_emptytask_list(self):
        """
        Verifies when we send request to `/polls/task/list` we see
        `No tasks were created yet!` on the response.
        """
        response = self.client.get(reverse('task-list'))
        self.assertContains(response, 'No tasks were created yet!')


class TaskDetailViewTest(TestCase):
    """
    Task detail view test class definition.
    """
    def setUp(self):
        """
        Sets up required objects like creating a test usern test task and
        login.
        """
        username = 'testuser'
        password = 'testpass'
        user_model_class = get_user_model()
        self.user = user_model_class.objects.create_user(
            username, password=password
        )
        self.client.login(username=username, password=password)
        self.task = Task.objects.create( # pylint: disable=E1101
            name='Task 1', created_by=self.user
        )

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/task/<task.id>`.
        """
        response = self.client.get(f'/polls/task/{self.task.id}:')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/task/<task.id>` while we use reverse function to get the URL.
        """
        response = self.client.get(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send request to `/polls/task/<task.id>` we use correct
        tempalte for the response.
        """
        response = self.client.get(reverse('task-detail', args=[self.task.id]))
        self.assertTemplateUsed(response, 'polls/task_detail.html')

    def test_view_returns_task_detail(self):
        """
        Verifies when we send request to `/polls/task/<task.id>` we see
        `Task 1` on the response.
        """
        response = self.client.get(reverse('task-detail', args=[self.task.id]))
        self.assertContains(response, 'Task 1')
