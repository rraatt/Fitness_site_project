from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

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




class GroupSchedule(ListView):
    model = Schedule
    template_name = 'training/schedule.html'
    context_object_name = 'info'
    extra_context = {'title': 'Group trainings'}
    allow_empty = False

    def get_queryset(self):
        return Schedule.objects.filter(client_group__group__isnull=False)

