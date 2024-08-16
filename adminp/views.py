from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from contact.models import Contact

# View for the admin panel home page
@login_required
def admin_home(request):
    return render(request, 'adminp/admin_home.html')

# View for listing all appointments
@login_required
def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'adminp/list_appointments.html', {'appointments': appointments})

# View for listing all contacts
@login_required
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'adminp/list_contacts.html', {'contacts': contacts})

# Additional views for adding, modifying, and deleting entries
# For simplicity, here’s how you might handle deleting an appointment:

@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('list_appointments')

@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('list_contacts')
