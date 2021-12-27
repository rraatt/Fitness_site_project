from django import forms
from .models import *
from django.core.exceptions import ValidationError


class BuyAbonement(forms.ModelForm):

    class Meta:
        model = Abonements
        fields = ['type_id', 'trainer_id', 'duration', 'num_of_trainings']
        widgets = {
        }

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