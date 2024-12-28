from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    is_mentor = forms.BooleanField(required=False)
    is_mentee = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "is_mentor",
            "is_mentee",
        )
