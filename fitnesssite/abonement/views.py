from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from abonement.utils import DataMixin
from django.urls import reverse_lazy
from abonement.forms import BuyAbonement, ClientForm, RegisterUserForm, LoginUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client, Abonements


class AddAbonement(DataMixin, LoginRequiredMixin, CreateView):
    """View class for buying abonements"""
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
    """View class for showing client's profile"""
    model = Client
    form_class = ClientForm
    template_name = 'abonement/client.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_object(self, queryset=None):
        cur_user = self.request.user
        client_pk = Client.objects.get(user=cur_user).pk
        return get_object_or_404(Client, pk=client_pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Profile")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    """View class for registration """
    form_class = RegisterUserForm
    template_name = 'abonement/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authentication")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    """View class for authorisation"""
    form_class = LoginUserForm
    template_name = 'abonement/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    """View method for logging out"""
    logout(request)
    return redirect('login')


class ShowAbonements(DataMixin, ListView):
    """View class for displaying abonements"""
    model = Abonements
    template_name = 'abonement/showabonements.html'
    context_object_name = 'abons'

    def get_queryset(self):
        date = self.request.GET.get('date')
        cur_user = self.request.user
        client_pk = Client.objects.get(user=cur_user).pk
        object_list = Abonements.objects.filter(client_id=client_pk).prefetch_related('client_id')
        if date:
            object_list = object_list.filter(purchase_date__gte=date)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Your abonements")
        return dict(list(context.items()) + list(c_def.items()))
