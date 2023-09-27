from django.contrib import admin

from .models import Anointment


@admin.register(Anointment)
class AnointmentAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "oils"]
