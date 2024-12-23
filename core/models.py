from django.db import models
# from django.contrib.auth.models import AbstractUser
import uuid

# Custom User model

# Appointment model remains unchanged
class Appointment(models.Model):
    GENERAL_CHECK_UP = 'general_check-up'
    TEETH_CLEANING = 'teeth_cleaning'
    TEETH_WHITENING = 'teeth_whitening'
    DENTAL_IMPLANTS = 'dental_implants'
    ROOT_CANAL = 'root_canal'
    OTHER = 'other'  
    
    SERVICE_TYPE_CHOICES = [
        (GENERAL_CHECK_UP, 'general_check-up'),
        (TEETH_CLEANING, 'teeth_cleaning'),
        (TEETH_WHITENING, 'teeth_whitening'),
        (DENTAL_IMPLANTS, 'dental_implants'),
        (ROOT_CANAL, 'root_canal'),
        (OTHER, 'other'), 
    ]
    
    aid = models.UUIDField(primary_key=True, max_length=10, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False, null=False, max_length=70)
    firstname = models.CharField(blank=False, null=False, max_length=70)
    lastname = models.CharField(blank=False, null=False, max_length=70)
    phonenumber = models.CharField(blank=False, null=False, max_length=20)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    service_type = models.CharField(max_length=60, choices=SERVICE_TYPE_CHOICES, default=GENERAL_CHECK_UP, blank=False, null=False)
    additional_note = models.TextField()