from django import forms
from core.models import Appointment
from django.forms import fields

class AppointmentForms(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
        
        # widgets = {
        #     'preferred_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        # }
        
        # labels = {
        #     'preferred_date': 'Preferred date',
        # }