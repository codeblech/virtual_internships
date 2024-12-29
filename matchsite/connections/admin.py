from django.contrib import admin
from .models import Connection


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ["mentor", "mentee", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["mentor__username", "mentee__username"]
