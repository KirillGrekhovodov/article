from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.utils import timezone

from webapp.models import statuses, Blog, Article


# def published_at_validate(value):
#     if value < timezone.now():
#         raise ValidationError("Published date must be in the future")


# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         required=True,
#         label='Title',
#         widget=widgets.Input(attrs={"class": "form-control"}),
#         error_messages={'required': 'Please enter title'},
#     )
#     author = forms.CharField(
#         max_length=5,
#         required=True,
#         label='Author',
#         widget=widgets.Input(attrs={"class": "form-control"})
#     )
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={"cols": "20", "rows": "5", "class": "form-control"}),
#         required=True,
#         label='Content'
#     )
#     status = forms.ChoiceField(
#         choices=statuses,
#         widget=widgets.Select(attrs={"class": "form-control"}),
#     )
#     blog = forms.ModelChoiceField(
#         queryset=Blog.objects.order_by("id"),
#         widget=widgets.Select(attrs={"class": "form-control"})
#     )
#
#     published_at = forms.DateTimeField(
#         widget=widgets.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
#         # validators=[published_at_validate, ]
#     )
#
#     def clean_published_at(self):
#         published_at = self.cleaned_data['published_at']
#         if published_at < timezone.now():
#             raise ValidationError("Published date must be in the future")
#         return published_at
#
#     def clean(self):
#         title = self.cleaned_data['title']
#         content = self.cleaned_data['content']
#         if title and content and title == content:
#             raise ValidationError("Название и контент не могут быть одинаковыми")
#         return super().clean()

class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Article
        # exclude = ['created_at', 'updated_at', ]
        fields = ['title', 'author', 'content', 'status', 'blog', 'published_at']
        widgets = {
            "published_at": widgets.DateTimeInput(attrs={"type": "datetime-local"}),
        }
        error_messages = {"title": {"required": "Please enter title"}}

    def clean_published_at(self):
        published_at = self.cleaned_data['published_at']
        if published_at < timezone.now():
            raise ValidationError("Published date must be in the future")
        return published_at

    def clean(self):
        title = self.cleaned_data['title']
        content = self.cleaned_data['content']
        if title and content and title == content:
            raise ValidationError("Название и контент не могут быть одинаковыми")
        return super().clean()
