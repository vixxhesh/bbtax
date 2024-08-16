# appointments/forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'appointment_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 16px; border: 2px solid #343a40; padding: 10px; ',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 16px; border: 2px solid #343a40; padding: 10px;',
                'placeholder': 'Enter your email'
            }),
            'appointment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 16px; border: 2px solid #343a40; padding: 10px;',
                'type': 'date'
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'appointment_date': 'Appointment Date',
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'style': 'font-size: 16px; border: 2px solid #343a40; padding: 10px;',
            })
            field.label = field.label if field.label else field_name.capitalize()
