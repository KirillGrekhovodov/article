from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.validators import FileExtensionValidator

from accounts.models import Profile

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    avatar = forms.ImageField(
        required=False,
        # validators=[FileExtensionValidator(['jpg'], 'Можно загружать только jpg')]
    )

    class Meta:
        model = Profile
        fields = ['birth_date', 'avatar']

    #
    # def clean_avatar(self):
    #     avatar = self.cleaned_data.get("avatar")
    #     if avatar and avatar.size > 5000:
    #         from django.core.exceptions import ValidationError
    #         raise ValidationError("Файл больше чем 600 байт")
    #     return avatar
