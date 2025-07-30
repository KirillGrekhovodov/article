from django import forms
from django.contrib.auth import get_user_model
from django.forms import widgets

from webapp.models import Project
User = get_user_model()

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title',)


class AddUsersInProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['users'].queryset = User.objects.exclude(pk=user.pk)

    class Meta:
        model = Project
        fields = ('users',)
        widgets = {'users': widgets.CheckboxSelectMultiple}