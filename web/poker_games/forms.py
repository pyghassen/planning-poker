"""
Forms module contains the PokerGameForm and the class definition.
"""
from django import forms

from poker_games.models import PokerGame


class PokerGameForm(forms.ModelForm):
    """PokerGame form class definition."""
    class Meta: # pylint: disable=R0903,C0111
        model = PokerGame
        fields = ['name']


    def __init__(self, *args, **kwargs):
        """
        Gets the `user` instance from the kwargs and assigns it it the `user`
        class attribue.
        """
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Gets the `user` class attribute value to assign it to the `created_by`
        `PokerGame` model field when saving to the database.
        """
        self.instance.created_by = self.user
        return super().save()
