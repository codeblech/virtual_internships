from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile_list, name="profile_list"),
    path("create/", views.profile_create, name="profile_create"),
    path("edit/", views.profile_edit, name="profile_edit"),
    path("<int:pk>/", views.profile_detail, name="profile_detail"),
]
