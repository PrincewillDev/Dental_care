from django.urls import path
from core.views import index, appointment

urlpatterns = [
    path('', index, name='index'),
    path('appointment/', appointment, name='appointment'),
    # path('register/', register, name='register'),
]