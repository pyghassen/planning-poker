from django import forms

from polls.models import Task, Vote

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name']


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        return super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.created_by=self.user
        return super().save(*args, **kwargs)


class VoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = ['value']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.task_id = kwargs.pop('task_id')
        return super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        vote, _ = Vote.objects.update_or_create(
            user=self.user,
            task_id=self.task_id,
            defaults={'value': self.instance.value}
        )
        return vote
