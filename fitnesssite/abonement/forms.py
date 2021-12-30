from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class BuyAbonement(forms.ModelForm):
    class Meta:
        model = Abonements
        fields = ['type_id', 'duration', 'num_of_trainings']

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration <= 0:
            raise ValidationError('Wrong abonement duration')
        return duration

    def clean_num_of_trainings(self):
        num = self.cleaned_data.get('num_of_trainings')
        if num <= 0:
            raise ValidationError('Wrong abonement number of trainings')
        return num


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'patronymic', 'birthday', 'sex', 'phone_number', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

