from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import AppointmentForms
from core.models import Appointment
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment scheduled successfully!')
            return redirect('appointment')
        else:
            print("Form errors:", form.errors)
            messages.error(request, 'There was an error with your submission. Please check all fields.')
    else:
        form = AppointmentForms()
    
    return render(request, 'appointment.html', {'form': form})
    
