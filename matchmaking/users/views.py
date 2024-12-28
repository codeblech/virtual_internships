from django.shortcuts import render, redirect
from form import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(request, "myapp/register_done.html", {"new_user": new_user})
    else:
        form = UserRegistrationForm()
    return render(request, "myapp/register.html", {"form": form})
