from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import AppointmentForms
from core.models import Appointment

# Create your views here.
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
                return HttpResponse('Success')
            except:
                pass
        
    else:
        form = AppointmentForms()
    return render(request, 'appointment.html', {'form': form})
    
