from django import forms
from .models import *


class BuyAbonement(forms.ModelForm):

    class Meta:
        model = Abonements
        fields = ['type_id', 'client_id', 'trainer_id', 'duration', 'num_of_trainings']


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name', 'surname', 'patronymic', 'birthday', 'sex', 'phone_number', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }