from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def profile_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not hasattr(request.user, "profile"):
            messages.warning(request, "Please create your profile first.")
            return redirect("profile_create")
        return view_func(request, *args, **kwargs)

    return _wrapped_view
