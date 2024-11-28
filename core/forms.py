from django import forms
from core.models import Appointment
from django.forms import fields

# ModelForm automatically creates a form from the specified model
class AppointmentForms(forms.ModelForm):
    # ModelForm automatically creates a form from the specified model
    class Meta:
        # Specify which model to use for creating the form
        model = Appointment
        # "__all__" means include all fields from the model
        fields = "__all__"
        
        # Define custom widgets for specific fields
        widgets = {
            # Custom widget for date input
            'preferred_date': forms.DateInput(
                attrs={
                    'type': 'date',     # HTML5 date picker
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white'
                }
            ),
            # Custom widget for time input
            'preferred_time': forms.TimeInput(
                attrs={
                    'type': 'time',     # HTML5 time picker
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white'
                }
            ),
            # Add styling for other fields if they exist
            'name': forms.TextInput(
                attrs={
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                    'placeholder': 'Enter your name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                    'placeholder': 'Enter your email'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                    'placeholder': 'Enter your phone number'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                    'placeholder': 'Any additional information',
                    'rows': 4
                }
            ),
        }
        
        # Define custom labels for form fields
        labels = {
            'preferred_date': 'Preferred Date',  # Display name for date field
            'preferred_time': 'Preferred Time',  # Display name for time field
        }