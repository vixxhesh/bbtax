# appointments/admin.py
from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'appointment_date', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('appointment_date', 'created_at')

    def delete_model(self, request, obj):
        # handle any related deletions here if necessary
        obj.delete()

admin.site.register(Appointment, AppointmentAdmin)
