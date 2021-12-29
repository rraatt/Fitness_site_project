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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from abonement.views import RegisterUser, LoginUser, AddAbonement, logout_user, ShowProfile
from training.views import Home, NewTraining, enlist, GroupSchedule, PersonalGroup, PersonalSchedule
from examination.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('groups', cache_page(60)(GroupSchedule.as_view()), name='group_schedule'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('Examination', cache_page(60)(ExamInfo.as_view()), name='examination'),
    path('appointment', NewTraining.as_view(), name='new_training'),
    path('groups/<int:group_id>/', enlist, name='join_group'),
    path('personal_trainings', cache_page(60)(PersonalSchedule.as_view()), name='view_personal'),
    path('personal_group', cache_page(60)(PersonalGroup.as_view()), name='personal_group'),
    path('groups/<int:group_id>/', enlist, name='join_group'),
    path('profile', ShowProfile.as_view(), name='profile'),
    path('buy', AddAbonement.as_view(), name='buy'),
    path('captcha', include('captcha.urls')),
    path('logout', logout_user, name='logout')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

