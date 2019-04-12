from django.db import models

from django.contrib.auth.models import User


PLANNING_CARDS = (
    ('0', '0'),
    ('1/2', '1/2'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('5', '5'),
    ('8', '8'),
    ('13', '13'),
)

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    value = models.CharField(
        max_length=3,
        choices=PLANNING_CARDS,
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.task} - {self.value} - {self.user}'
