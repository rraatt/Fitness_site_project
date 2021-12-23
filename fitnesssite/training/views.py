from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from .models import *

# Create your views here.



def home(request):
    return render(request, 'training/home.html', {'title': 'Home page'})


def new_training(request):
    return render(request, 'training/new_training.html', {'title': 'Make an appointment'})


def about(request):
    return render(request, 'training/about.html', {'title': 'About'})


def enlist(request, group_id):
    current_user = request.user
    if current_user.is_authenticated:
        cur_client = Client.objects.get(user=current_user.id)
        cur_group = Group.objects.get(pk=group_id)
        cur_group.id_clients.add(cur_client)
        return HttpResponse(f'You`ve joined group {group_id}')
    else:
        return HttpResponse(f'Please authorize!')


class PersonalSchedule(ListView):
    model = Schedule
    extra_context = {'title': 'Your trainings'}
    template_name = 'training/personal_schedule'
    context_object_name = 'info'

    def get_queryset(self):
        current_user = self.request.user
        cur_client = Client.objects.get(user=current_user)
        return Schedule.objects.filter(client_group__client=cur_client)


class PersonalGroup(ListView):
    model = Schedule
    extra_context = {'title': 'Your group trainigs'}
    context_object_name = 'info'
    template_name = 'training/schdule.html'

    def get_queryset(self):
        current_user = self.request.user
        cur_client = Schedule.objects.get(user=current_user)
        cur_groups = Group.objects.filter(id_clients=cur_client)
        return Schedule.objects.filter(client_group__group__in=cur_groups)


class GroupSchedule(ListView):
    model = Schedule
    template_name = 'training/schedule.html'
    context_object_name = 'info'
    extra_context = {'title': 'Group trainings'}
    allow_empty = False

    def get_queryset(self):
        return Schedule.objects.filter(client_group__group__isnull=False)

