from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from abonement.utils import DataMixin
from django.urls import reverse_lazy
from abonement.forms import BuyAbonement, ClientForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client
from captcha.fields import CaptchaField


# Create your views here.

def index(request):
    return render(request, "abonement/index.html")


class AddAbonement(DataMixin, LoginRequiredMixin, CreateView):
    form_class = BuyAbonement
    template_name = 'abonement/buy.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def form_valid(self, form):
        cur_user = self.request.user
        cur_client = Client.objects.get(user=cur_user)
        form.instance.client_id = cur_client
        return super(AddAbonement, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Order abonement")
        return dict(list(context.items()) + list(c_def.items()))


class ShowProfile(DataMixin, LoginRequiredMixin, UpdateView):
    #instance = get_object_or_404(Client, id=id)
    model = Client
    form_class = ClientForm
    template_name = 'abonement/client.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    raise_exception = True
    #client_id

    def get_object(self, queryset=None):
        cur_user = self.request.user
        client_pk = Client.objects.get(user=cur_user).pk
        return get_object_or_404(Client, pk=client_pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #cur_user = self.request.user
        #client_pk = Client.objects.get(user=cur_user).pk
        c_def = self.get_user_context(title="Profile")#, client_id=client_pk)
        return dict(list(context.items()) + list(c_def.items()))


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

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
