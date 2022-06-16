from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(max_length=15, required=True)
    password2 = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
