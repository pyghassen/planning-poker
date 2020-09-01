from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from polls.forms import TaskForm, VoteForm
from polls.models import Task, Vote


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('task-list')
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                'user': self.request.user,
            }
        )
        return kwargs


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    ordering = '-created_at'


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['vote_list'] = Vote.objects.filter(task_id=self.object.id)
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')


class VoteCreateView(LoginRequiredMixin, CreateView):
    model = Vote
    form_class = VoteForm

    def get_success_url(self):
        return reverse_lazy('task-detail', args=[self.kwargs['task_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_id'] = context['form'].task_id
        return context


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                'user': self.request.user,
                'task_id': self.kwargs['task_id']
            }
        )
        return kwargs
