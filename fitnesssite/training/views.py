from django.shortcuts import render
from .models import *

# Create your views here.
menu = ['Home', 'Make an appointment', 'About us']


def home(request):
    return render(request, 'training/home.html', {'title': 'Home page', 'menu': menu})


def schedule(request):
    info = Schedule.objects.all()
    return render(request, 'training/schedule.html', {'title': 'Schedule info', 'menu': menu, 'info': info})
