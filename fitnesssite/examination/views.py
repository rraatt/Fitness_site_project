from django.shortcuts import render,HttpResponse
from .models import *

def home(request):
    return render(request, 'examination/home.html', {'title': 'Home page'})

def about(request):
    return render(request, 'examination/about.html', {'title': 'About'})

