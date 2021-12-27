from django.shortcuts import render,HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from abonement.models import Client
from abonement.utils import DataMixin


class ExamInfo(DataMixin, LoginRequiredMixin, ListView):
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
