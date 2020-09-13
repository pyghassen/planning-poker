from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from polls.models import Task
from poker_games.forms import PokerGameForm
from poker_games.models import PokerGame


class PokerGameCreateView(LoginRequiredMixin, CreateView):
    model = PokerGame
    success_url = reverse_lazy('poker-game-list')
    form_class = PokerGameForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                'user': self.request.user,
            }
        )
        return kwargs


class PokerGameListView(LoginRequiredMixin, ListView):
    model = PokerGame
    ordering = '-created_at'


class PokerGameDetailView(LoginRequiredMixin, DetailView):
    model = PokerGame

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.filter(poker_game_id=self.object.id)
        return context


class PokerGameDeleteView(LoginRequiredMixin, DeleteView):
    model = PokerGame
    success_url = reverse_lazy('poker-game-list')
