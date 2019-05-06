from django.contrib import admin
from core.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'appointment_date', 'last_modified')
    search_fields = ("user", )
