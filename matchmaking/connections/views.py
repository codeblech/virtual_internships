from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Connection
from users.models import CustomUser
from users.decorators import profile_required


@profile_required
@login_required
def connection_list(request):
    # Get all connections where user is mentor
    mentor_connections = Connection.objects.filter(mentor=request.user)
    mentor_pending_received = mentor_connections.filter(
        status="PENDING", mentor_initiated=False
    )
    mentor_pending_sent = mentor_connections.filter(
        status="PENDING", mentor_initiated=True
    )
    mentor_accepted = mentor_connections.filter(status="ACCEPTED")

    # Get all connections where user is mentee
    mentee_connections = Connection.objects.filter(mentee=request.user)
    mentee_pending_received = mentee_connections.filter(
        status="PENDING", mentee_initiated=False
    )
    mentee_pending_sent = mentee_connections.filter(
        status="PENDING", mentee_initiated=True
    )
    mentee_accepted = mentee_connections.filter(status="ACCEPTED")

    return render(
        request,
        "connections/connection_list.html",
        {
            "mentor_pending_received": mentor_pending_received,
            "mentor_pending_sent": mentor_pending_sent,
            "mentor_accepted": mentor_accepted,
            "mentee_pending_received": mentee_pending_received,
            "mentee_pending_sent": mentee_pending_sent,
            "mentee_accepted": mentee_accepted,
        },
    )


@profile_required
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
        Connection.objects.create(
            mentor=request.user, mentee=recipient, mentor_initiated=True
        )
    elif request.user.is_mentee and recipient.is_mentor:
        Connection.objects.create(
            mentor=recipient, mentee=request.user, mentee_initiated=True
        )
    else:
        messages.error(request, "Invalid mentor/mentee combination!")
        return redirect("profile_detail", pk=user_id)

    messages.success(request, "Connection request sent!")
    return redirect("connection_list")


@profile_required
@login_required
def accept_request(request, connection_id):
    connection = get_object_or_404(Connection, id=connection_id)
    # Check if the current user is the recipient of the request
    if connection.status == "PENDING":
        if (
            request.user.is_mentor
            and request.user == connection.mentor
            and not connection.mentor_initiated
        ) or (
            request.user.is_mentee
            and request.user == connection.mentee
            and not connection.mentee_initiated
        ):
            connection.status = "ACCEPTED"
            connection.save()
            messages.success(request, "Connection accepted!")
        else:
            messages.error(request, "You cannot accept a request you sent!")
    else:
        messages.error(request, "This connection cannot be accepted!")
    return redirect("connection_list")


@profile_required
@login_required
def reject_request(request, connection_id):
    connection = get_object_or_404(Connection, id=connection_id)
    # Check if the current user is the recipient of the request
    if connection.status == "PENDING":
        if (
            request.user.is_mentor
            and request.user == connection.mentor
            and not connection.mentor_initiated
        ) or (
            request.user.is_mentee
            and request.user == connection.mentee
            and not connection.mentee_initiated
        ):
            connection.status = "REJECTED"
            connection.save()
            messages.success(request, "Connection rejected!")
        else:
            messages.error(request, "You cannot reject a request you sent!")
    else:
        messages.error(request, "This connection cannot be rejected!")
    return redirect("connection_list")


@profile_required
@login_required
def cancel_request(request, connection_id):
    connection = get_object_or_404(Connection, id=connection_id)
    # Check if the current user is the sender of the request
    if connection.status == "PENDING":
        if (
            request.user.is_mentor
            and request.user == connection.mentor
            and connection.mentor_initiated
        ) or (
            request.user.is_mentee
            and request.user == connection.mentee
            and connection.mentee_initiated
        ):
            connection.delete()
            messages.success(request, "Connection request cancelled!")
        else:
            messages.error(request, "You can only cancel requests you sent!")
    else:
        messages.error(request, "This connection cannot be cancelled!")
    return redirect("connection_list")


@profile_required
@login_required
def terminate_connection(request, connection_id):
    connection = get_object_or_404(Connection, id=connection_id)
    # Check if the current user is part of the connection
    if connection.status == "ACCEPTED":
        if request.user == connection.mentor or request.user == connection.mentee:
            connection.delete()
            messages.success(request, "Connection terminated successfully!")
        else:
            messages.error(request, "You are not part of this connection!")
    else:
        messages.error(request, "Only accepted connections can be terminated!")
    return redirect("connection_list")
