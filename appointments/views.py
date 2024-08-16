# appointments/views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save the appointment to the database
            appointment = form.save()

            # Send email to admin

            return redirect('appointment_success')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/schedule_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')
