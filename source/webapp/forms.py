from django import forms
from django.forms import widgets

from webapp.models import statuses, Tag


class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Title',
        widget=widgets.Input(attrs={"class": "form-control"}),
        error_messages={'required': 'Please enter title'},

    )
    author = forms.CharField(max_length=5, required=True, label='Author',
                             widget=widgets.Input(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": "20", "rows": "5", "class": "form-control"}),
                              required=True, label='Content')
    status = forms.ChoiceField(choices=statuses, widget=widgets.Select(attrs={"class": "form-control"}), )
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=widgets.SelectMultiple(attrs={"class": "form-control"}), required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        result = []
        if tags:
            tags = tags.split(',')
            for tag in tags:
                new_tag, _ = Tag.objects.get_or_create(title=tag.strip())
                result.append(new_tag)
        return result

    def set_initial_tags(self, tags):
        self.fields['tags'].initial = ", ".join([tag.title for tag in tags])
