from django.urls import path
# from .views import appointment
from . import views
urlpatterns = [
     path('appointment/', views.appointment, name='appointment')
]