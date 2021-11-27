from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.



def home(request):
    return render(request, 'training/home.html', {'title': 'Home page'})


def new_training(request):
    return render(request, 'training/new_training.html', {'title': 'Make an appointment'})


def about(request):
    return render(request, 'training/about.html', {'title': 'About'})


def enlist(request, group_id):
    return HttpResponse(f'You`ve joined group {group_id}')


def group_schedule(request):
    return render(request, 'training/schedule.html', {'title': 'Schedule info'})
