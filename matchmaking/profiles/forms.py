from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    # Add string fields for skills and interests
    skills = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter skills separated by commas"}
        ),
    )
    interests = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter interests separated by commas"}
        ),
    )

    class Meta:
        model = Profile
        fields = ["bio", "skills", "interests"]

    def clean_skills(self):
        skills = self.cleaned_data.get("skills", "")
        return [s.strip() for s in skills.split(",")] if skills else []

    def clean_interests(self):
        interests = self.cleaned_data.get("interests", "")
        return [i.strip() for i in interests.split(",")] if interests else []
