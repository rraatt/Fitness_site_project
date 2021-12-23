from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


# Create your views here.


def home(request):
    return render(request, 'training/home.html', {'title': 'Home page'})


def enlist(request, group_id):
    current_user = request.user
    if current_user.is_authenticated:
        cur_client = Client.objects.get(user=current_user.id)
        cur_group_owner = Owner.objects.get(pk=group_id)
        cur_group = Group.objects.get(owner=cur_group_owner)
        cur_group.id_clients.add(cur_client)
        return redirect('personal_group')
    else:
        return redirect('login')


class PersonalSchedule(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Schedule
    extra_context = {'title': 'Your trainings'}
    template_name = 'training/personal_schedule.html'
    context_object_name = 'info'

    def get_queryset(self):
        current_user = self.request.user
        cur_client = Client.objects.get(user=current_user)
        return Schedule.objects.filter(client_group__client=cur_client)


class PersonalGroup(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Schedule
    extra_context = {'title': 'Your group trainings'}
    context_object_name = 'info'
    template_name = 'training/schedule_pers_group.html'

    def get_queryset(self):
        current_user = self.request.user
        cur_client = Client.objects.get(user=current_user)
        cur_groups = Group.objects.filter(id_clients=cur_client)
        return Schedule.objects.filter(client_group__group__in=cur_groups)


class GroupSchedule(ListView):
    model = Schedule
    template_name = 'training/schedule.html'
    context_object_name = 'info'
    extra_context = {'title': 'Group trainings'}

    def get_queryset(self):
        return Schedule.objects.filter(client_group__group__isnull=False)


class NewTraining(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Schedule
    fields = ('id_trainer', 'date', 'time_start', 'time_end')
    success_url = 'personal_trainings'
    template_name = 'training/new_training.html'

    def form_valid(self, form):
        cur_user = self.request.user
        cur_client = Client.objects.get(user=cur_user)
        try:
            form.instance.client_group = Owner.objects.get(client=cur_client)
        except Owner.DoesNotExist:
            form.instance.client_group = Owner.objects.create(client=cur_client)
        return super(NewTraining, self).form_valid(form)
