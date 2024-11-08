from django.urls import path
from .views import *


urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
    path('forms/', forms, name='forms'), 
    path('alert/', alert, name='alert'),
    path('card/', card, name='card'),
    path('typography/',typography, name='typography'),
    path('icontabler/',icontabler, name='icontabler'), 
    path('buttons/',buttons, name='buttons'),
    path('samplepage/',samplepage, name='samplepage'),
    
]