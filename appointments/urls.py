# appointments/urls.py
from django.urls import path
from .views import schedule_appointment, appointment_success

urlpatterns = [
    path('schedule/', schedule_appointment, name='schedule_appointment'),
    path('success/', appointment_success, name='appointment_success'),
]
