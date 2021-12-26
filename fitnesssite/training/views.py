from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from abonement.utils import DataMixin
from .models import *


# Create your views here.

class Home(DataMixin, TemplateView):
    template_name = 'training/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home")
        return dict(list(context.items()) + list(c_def.items()))


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


class PersonalSchedule(DataMixin, LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Schedule
    template_name = 'training/personal_schedule.html'
    context_object_name = 'info'

    def get_queryset(self):
        current_user = self.request.user
        cur_client = Client.objects.get(user=current_user)
        return Schedule.objects.filter(client_group__client=cur_client)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Your personal schedule")
        return dict(list(context.items()) + list(c_def.items()))


class PersonalGroup(DataMixin, LoginRequiredMixin, ListView):
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Your group schedule")
        return dict(list(context.items()) + list(c_def.items()))


class GroupSchedule(DataMixin, ListView):
    paginate_by = 3
    model = Schedule
    template_name = 'training/schedule.html'
    context_object_name = 'info'
    extra_context = {'title': 'Group trainings'}

    def get_queryset(self):
        return Schedule.objects.filter(client_group__group__isnull=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Group schedule")
        return dict(list(context.items()) + list(c_def.items()))


class NewTraining(DataMixin, LoginRequiredMixin, CreateView):
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Book a training")
        return dict(list(context.items()) + list(c_def.items()))
