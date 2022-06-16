from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "focus:outline-none",
                "style": "min-width:100%;max-width:100%",
                "placeholder": "demo@example.com",
            }
        ),
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "focus:outline-none",
                "style": "min-width:100%;max-width:100%",
                "placeholder": "johndoe",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "focus:outline-none",
                "style": "min-width:100%;max-width:100%",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "focus:outline-none",
                "style": "min-width:100%;max-width:100%",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
