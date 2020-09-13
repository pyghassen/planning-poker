from django.db import models
from django.contrib.auth.models import User


class PokerGame(models.Model):
    """PokerGame model definition."""

    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
