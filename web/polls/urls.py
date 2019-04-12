from django.urls import path
from polls.views import TaskCreateView, TaskListView, TaskDetailView

urlpatterns = [
    path('task/create', TaskCreateView.as_view(), name='task-create'),
    path('task/list', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>:', TaskDetailView.as_view(), name='task-detail'),
]
