from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import AppointmentForms
from core.models import Appointment
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


def appointment(request):
    # Check if method is post
    if request.method == "POST":
        # Creating a form instance
        form = AppointmentForms(request.POST)
        print('Instance created')
        if form.is_valid():
            print('Validation check')
            try:
                print('testing1')
                form.save()
                print('testing2')
                messages.success(request, 'Appointment scheduled successfully!')
                return redirect('appointment')  # Redirect to empty form
            except:
                pass
        
    else:
        form = AppointmentForms()
    return render(request, 'appointment.html', {'form': form})
    
