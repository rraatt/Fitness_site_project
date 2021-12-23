"""fitnesssite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from abonement.views import index, RegisterUser, LoginUser
from training.views import home, NewTraining, enlist, GroupSchedule, PersonalGroup, PersonalSchedule
from examination.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('abonement', index),
    path('groups', GroupSchedule.as_view(), name='group_schedule'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('Examination', Examination_page.as_view(), name='examination'),
    path('appointment', NewTraining.as_view(), name='new_training'),
    path('groups/<int:group_id>/', enlist, name='join_group'),
    path('personal_trainings', PersonalSchedule.as_view(), name='view_personal'),
    path('personal_group', PersonalGroup.as_view(), name='personal_group'),
    path('groups/<int:group_id>/', enlist, name='join_group'),
    path('profile', index, name='profile')
]
