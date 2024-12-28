from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Connection
from users.models import CustomUser
from users.decorators import profile_required


@profile_required
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
    if connection.status == "PENDING":
        if (request.user.is_mentor and request.user == connection.mentor) or (
            request.user.is_mentee and request.user == connection.mentee
        ):
            connection.delete()
            messages.success(request, "Connection request cancelled!")
        else:
            messages.error(request, "You don't have permission to cancel this request!")
    else:
        messages.error(request, "This connection cannot be cancelled!")
    return redirect("connection_list")


@profile_required
@login_required
def terminate_connection(request, connection_id):
    connection = get_object_or_404(Connection, id=connection_id)
    if connection.status == "ACCEPTED":
        if request.user in [connection.mentor, connection.mentee]:
            connection.status = "TERMINATED"
            connection.save()
            messages.success(request, "Connection terminated!")
        else:
            messages.error(
                request, "You don't have permission to terminate this connection!"
            )
    else:
        messages.error(request, "This connection cannot be terminated!")
    return redirect("connection_list")
