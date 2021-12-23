from django.shortcuts import render,HttpResponse
from django.views.generic import ListView

from .models import *
from abonement.models import Client



def examination(request):
    return render(request, 'training/examination.html', {'title': 'Examination'})

class ExamInfo(ListView):
    model = Examination
    template_name = 'training/examination.html'
    context_object_name = 'entry'
    extra_context = {'title': 'Examinations'}
    allow_empty = False

    def get_queryset(self):
        current_user = self.requests.user
        current_client = Client.object.get(user=current_user)
        return Examination.objects.filter(id_client=current_client)

class Examination_page(ListView):
    model = Examination
    template_name = 'training/examination.html'

def login(request):
    return render(request, 'training/login.html', {'title': 'Sign in'})

def register(request):
    return render(request, 'training/register.html', {'title': 'Sign up'})


