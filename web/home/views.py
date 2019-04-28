"""
The home view module.
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    """
    HomeView class definition, it uses the LoginRequiredMixin to require
    authentication to access the view, and it returns a TemplateView
    """
    template_name = 'home.html'
