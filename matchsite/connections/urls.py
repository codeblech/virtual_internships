from django.urls import path
from . import views

urlpatterns = [
    path("", views.connection_list, name="connection_list"),
    path("send/<int:user_id>/", views.send_request, name="send_request"),
    path("accept/<int:connection_id>/", views.accept_request, name="accept_request"),
    path("reject/<int:connection_id>/", views.reject_request, name="reject_request"),
    path("cancel/<int:connection_id>/", views.cancel_request, name="cancel_request"),
    path(
        "terminate/<int:connection_id>/",
        views.terminate_connection,
        name="terminate_connection",
    ),
]
