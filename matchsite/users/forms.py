from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
import re

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

    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if not re.search(r"[A-Z]", password):
            raise ValidationError(
                "Password must contain at least one uppercase letter."
            )

        if not re.search(r"[a-z]", password):
            raise ValidationError(
                "Password must contain at least one lowercase letter."
            )

        if not re.search(r"[0-9]", password):
            raise ValidationError("Password must contain at least one number.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(
                "Password must contain at least one special character."
            )

        return password
