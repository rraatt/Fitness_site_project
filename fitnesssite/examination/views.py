from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from training.models import Training, Owner
from .models import *
from abonement.models import Client
from abonement.utils import DataMixin


class ExamInfo(DataMixin, LoginRequiredMixin, ListView):
    """Class for viewing information about examinations"""
    paginate_by = 10
    login_url = 'login'
    model = Examination
    template_name = 'training/examination.html'
    context_object_name = 'info'
    extra_context = {'title': 'Examinations'}

    def get_queryset(self):
        current_user = self.request.user
        current_client = Client.objects.get(user=current_user)
        return Examination.objects.filter(id_client=current_client)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Your examinations")
        return dict(list(context.items()) + list(c_def.items()))


class ResInfo(DataMixin, LoginRequiredMixin, ListView):
    """Class for viewing information about result of training"""
    paginate_by = 10
    login_url = 'login'
    model = Training
    template_name = 'training/results.html'
    context_object_name = 'info'
    extra_context = {'title': 'Results'}

    def get_queryset(self):
        current_user = self.request.user
        current_client = Client.objects.get(user=current_user)
        owner = Owner.objects.get(client=current_client)
        return Training.objects.filter(id_schedule__client_group=owner)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Your results")
        return dict(list(context.items()) + list(c_def.items()))
