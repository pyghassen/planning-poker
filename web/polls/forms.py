from django import forms

from polls.models import Task

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
