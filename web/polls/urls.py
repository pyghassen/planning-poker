"""
Poll app URL Configuration

The `urlpatterns` list routes URLs to views which will be included in the main
urls file.
"""
from django.urls import path

from polls.views import (
    TaskCreateView, TaskListView, TaskDetailView, VoteCreateView,
    TaskDeleteView
)


urlpatterns = [ # pylint: disable=C0103
    path('task/create', TaskCreateView.as_view(), name='task-create'),
    path('task/list', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>:', TaskDetailView.as_view(), name='task-detail'),
    path('task/delete/<int:pk>:', TaskDeleteView.as_view(), name='task-delete'),
    path('vote/create/<int:task_id>:', VoteCreateView.as_view(), name='vote-create'),
]
