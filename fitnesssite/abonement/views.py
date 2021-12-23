from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from abonement.utils import DataMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def index(request):
    return render(request, "abonement/index.html")

class AddAbonement(CreateView):
    pass


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'abonement/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authentication")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'abonement/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))
