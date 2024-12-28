from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "profiles/profile_list.html", {"profiles": profiles})


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
        # Handle profile creation (we'll add form handling later)
        profile = Profile.objects.create(
            user=request.user,
            bio=request.POST.get("bio", ""),
            skills=request.POST.getlist("skills", []),
            interests=request.POST.getlist("interests", []),
        )
        messages.success(request, "Profile created successfully!")
        return redirect("profile_detail", pk=profile.pk)

    return render(request, "profiles/profile_form.html")


@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        # Handle profile update (we'll add form handling later)
        profile.bio = request.POST.get("bio", "")
        profile.skills = request.POST.getlist("skills", [])
        profile.interests = request.POST.getlist("interests", [])
        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile_detail", pk=profile.pk)

    return render(request, "profiles/profile_form.html", {"profile": profile})
