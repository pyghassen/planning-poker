"""
Forms module contains the TaskForm and the VoteForm classes definition.
"""
from django import forms


from polls.models import Task, Vote

class TaskForm(forms.ModelForm):
    """Task form class definition."""
    class Meta: # pylint: disable=R0903,C0111
        model = Task
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
        `Task` model field when saving to the database.
        """
        self.instance.created_by = self.user
        return super().save()


class VoteForm(forms.ModelForm):
    """Vote form class definition."""
    class Meta: # pylint: disable=R0903,C0111
        model = Vote
        fields = ['value']
        widgets = {'value': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        """
        Gets the `user` instance and `task_id` from the kwargs and assigns them
        as class attribue.
        """
        self.user = kwargs.pop('user')
        self.task_id = kwargs.pop('task_id')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Gets the `user` and the `task_id` class attribute value to assign it to
        the `user`, `task_id` in the `Vote` model fields when saving to the
        database.

        The `update_or_create` method was used to prevent creating object every
        time, which is the default behaviour, but update the Vote if exists.
        """
        vote, _ = Vote.objects.update_or_create( # pylint: disable=E1101
            user=self.user,
            task_id=self.task_id,
            defaults={'value': self.instance.value}
        )

        return vote
