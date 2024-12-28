from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from .forms import ProfileForm
from users.decorators import profile_required


@profile_required
@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "profiles/profile_list.html", {"profiles": profiles})


@profile_required
@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, "profiles/profile_detail.html", {"profile": profile})


@login_required
def profile_create(request):
    if hasattr(request.user, "profile"):
        messages.warning(request, "You already have a profile!")
        return redirect("profile_detail", pk=request.user.profile.pk)

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile created successfully!")
            return redirect("profile_detail", pk=profile.pk)
        else:
            # Add this to show form validation errors
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm()

    return render(request, "profiles/profile_form.html", {"form": form})


@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile_detail", pk=profile.pk)
    else:
        initial_data = {
            "bio": profile.bio,
            "skills": ", ".join(profile.skills),
            "interests": ", ".join(profile.interests),
        }
        form = ProfileForm(instance=profile, initial=initial_data)

    return render(
        request, "profiles/profile_form.html", {"form": form, "profile": profile}
    )
