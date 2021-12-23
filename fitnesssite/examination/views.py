from django.shortcuts import render,HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from abonement.models import Client



class ExamInfo(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Examination
    template_name = 'training/examination.html'
    context_object_name = 'info'
    extra_context = {'title': 'Examinations'}

    def get_queryset(self):
        current_user = self.request.user
        current_client = Client.objects.get(user=current_user)
        return Examination.objects.filter(id_client=current_client)
