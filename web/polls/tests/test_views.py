# from django.contrib.auth import get_user_model
#
# class HomePageTests(TestCase):
#
#     """Test whether our blog entries show up on the homepage"""
#
#     def setUp(self):
#         self.user = get_user_model().objects.create(username='some_user')
#
#     def test_one_entry(self):
#         Entry.objects.create(title='1-title', body='1-body', author=self.user)
#         response = self.client.get('/')
#         self.assertContains(response, '1-title')
#         self.assertContains(response, '1-body')
#
#     def test_two_entries(self):
#         Entry.objects.create(title='1-title', body='1-body', author=self.user)
#         Entry.objects.create(title='2-title', body='2-body', author=self.user)
#         response = self.client.get('/')
#         self.assertContains(response, '1-title')
#         self.assertContains(response, '1-body')
#         self.assertContains(response, '2-title')

from django.test import TestCase
from django.urls import reverse

from allauth.utils import get_user_model

from polls.models import Task


class TaskCreateViewTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        self.user = User.objects.create_user(username, password=password)
        self.client.login(username=username, password=password)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/polls/task/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('task-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('task-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/task_form.html')

    def test_create_task_returns_task_list_page(self):
        response = self.client.post(
            reverse('task-create'), {'name': 'Task 1'}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/task_list.html')
        self.assertContains(response, 'Task 1')

    def test_create_task_fails_and_returns_task_create_page(self):
        response = self.client.post(reverse('task-create'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/task_form.html')
        self.assertContains(response, 'Create Task')


class TaskListViewTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        self.user = User.objects.create_user(username, password=password)
        self.client.login(username=username, password=password)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/polls/task/list')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/task_list.html')

    def test_list_task_returns_task_list(self):
        Task.objects.create(name='Task 1')
        Task.objects.create(name='Task 2')
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/task_list.html')
        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Task 2')

    def test_list_task_returns_emptytask_list(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/task_list.html')
        self.assertContains(response, 'No tasks were created yet!')
