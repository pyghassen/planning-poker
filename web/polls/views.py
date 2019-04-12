from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from polls.models import Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name']
    success_url = reverse_lazy('task-list')


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
