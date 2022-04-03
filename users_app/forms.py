from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    fullname = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'fullname', 'username', 'password1', 'password2']
