from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name here'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email here'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email subject here'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
