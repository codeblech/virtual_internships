from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Connection
from users.models import CustomUser


@login_required
def connection_list(request):
    mentor_connections = Connection.objects.filter(mentor=request.user)
    mentee_connections = Connection.objects.filter(mentee=request.user)
    return render(
        request,
        "connections/connection_list.html",
        {
            "mentor_connections": mentor_connections,
            "mentee_connections": mentee_connections,
        },
    )


@login_required
def send_request(request, user_id):
    recipient = get_object_or_404(CustomUser, id=user_id)

    # Check if connection already exists
    existing_connection = (
        Connection.objects.filter(mentor=request.user, mentee=recipient).exists()
        or Connection.objects.filter(mentor=recipient, mentee=request.user).exists()
    )

    if existing_connection:
        messages.warning(request, "Connection already exists!")
        return redirect("profile_detail", pk=user_id)

    if request.user.is_mentor and recipient.is_mentee:
        Connection.objects.create(mentor=request.user, mentee=recipient)
    elif request.user.is_mentee and recipient.is_mentor:
        Connection.objects.create(mentor=recipient, mentee=request.user)
    else:
        messages.error(request, "Invalid mentor/mentee combination!")
        return redirect("profile_detail", pk=user_id)

    messages.success(request, "Connection request sent!")
    return redirect("connection_list")


@login_required
def accept_request(request, connection_id):
    connection = get_object_or_404(Connection, id=connection_id)
    if request.user == connection.mentor or request.user == connection.mentee:
        connection.status = "ACCEPTED"
        connection.save()
        messages.success(request, "Connection accepted!")
    return redirect("connection_list")


@login_required
def reject_request(request, connection_id):
    connection = get_object_or_404(Connection, id=connection_id)
    if request.user == connection.mentor or request.user == connection.mentee:
        connection.status = "REJECTED"
        connection.save()
        messages.success(request, "Connection rejected!")
    return redirect("connection_list")
