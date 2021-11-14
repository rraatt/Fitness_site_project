from django.shortcuts import render

# Create your views here.
menu = ['Home', 'Make an appointment', 'About us']


def home(request):
    return render(request, 'training/home.html', {'title': 'Home page', 'menu': menu})
