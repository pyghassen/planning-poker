"""Task views test modules."""
from django.test import TestCase
from django.urls import reverse

from polls.forms import VoteForm
from polls.models import Task, Vote
from polls.tests.helpers import create_user
from polls.views import VoteCreateView


class TaskCreateViewTest(TestCase):
    """
    Task create view test class definition.
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
        page and using the same form.
        """
        response = self.client.post(reverse('task-create'), follow=True)
        self.assertTemplateUsed(response, 'polls/task_form.html')
        self.assertContains(response, '<h1>Create Task</h1>')


class TaskListViewTest(TestCase):
    """
    Task create view test class definition.
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


class TaskDeleteViewTest(TestCase):
    """
    Task delete view test class definition.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Sets up required objects like creating a test user and task object.
        """
        cls.user = create_user()
        cls.task = Task.objects.create( # pylint: disable=E1101
            name='Task 1', created_by=cls.user
        )

    def setUp(self):
        """Sets up the user login step."""
        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send a GET request to
        `/polls/task/delete/<task_id>`.
        """
        response = self.client.get(f'/polls/task/delete/{self.task.id}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send a GET request to
        `/polls/task/delete/<task_id>` while we use reverse function to get the
        URL.
        """
        response = self.client.get(reverse('task-delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send a GET request to `/polls/task/delete/<task_id>`
        we use correct tempalte for the response.
        """
        response = self.client.get(reverse('task-delete', args=[self.task.id]))
        self.assertTemplateUsed(response, 'polls/task_confirm_delete.html')

    def test_delete_task_returns_task_list_page(self):
        """
        Verifies when we send a POST request to `/polls/task/delete/<task_id>`
        it redirecting to the task list view and the deleted task wont't show up
        anymore.
        """
        response = self.client.post(
            reverse('task-delete', args=[self.task.id]), follow=True
        )
        self.assertTemplateUsed(response, 'polls/task_list.html')
        self.assertNotContains(response, self.task.name)


class TaskDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up required objects like creating a test user and a task object.
        """
        cls.user = create_user()
        cls.task = Task.objects.create( # pylint: disable=E1101
            name='Task 1', created_by=cls.user
        )

    def setUp(self):
        """Sets up the user login step."""
        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/task/<task.id>`.
        """
        response = self.client.get(f'/polls/task/{self.task.id}')
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


class VoteCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up required objects like creating a test user and a task object.
        """
        cls.user = create_user()
        cls.task = Task.objects.create( # pylint: disable=E1101
            name='Task 1', created_by=cls.user
        )

    def setUp(self):
        """Sets up the user login step."""
        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/vote/create/<task_id>`.
        """
        response = self.client.get(f'/polls/vote/create/{self.task.id}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Verifies getting 200 as status code when we send request to
        `/polls/vote/create/<task_id>` while we use reverse function to get the
        URL.
        """
        response = self.client.get(reverse('vote-create', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Verifies when we send request to `/polls/vote/create/<task_id>` we use
        correct tempalte for the response.
        """
        response = self.client.get(reverse('vote-create', args=[self.task.id]))
        self.assertTemplateUsed(response, 'polls/vote_form.html')

    def test_view_uses_correct_context_data(self):
        """
        Verifies when we send request to `/polls/vote/create/<task_id>` we use
        correct context data.
        """
        response = self.client.get(reverse('vote-create', args=[self.task.id]))
        self.assertEqual(response.context_data['task_id'], self.task.id)
        self.assertIsInstance(response.context_data['form'], VoteForm)
        self.assertIsInstance(response.context_data['view'], VoteCreateView)

    def test_view_returns_task_detail(self):
        """
        Verifies when we send request to `/polls/vote/create/<task_id>` we see
        `Task 1` on the response.
        """
        url = reverse('vote-create', args=[self.task.id])
        value = '3'
        response = self.client.post(url, {'value': value}, follow=True)
        self.assertContains(response, '<h2>Task name: Task 1</h2>')
        self.assertContains(response, f'<td>{self.user}</td>')
        self.assertContains(response, f'<td>{value}</td>')
        self.assertTrue(
            Vote.objects.filter(
                task=self.task, user=self.user, value=value
            ).exists()
        )
