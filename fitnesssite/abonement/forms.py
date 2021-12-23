from django import forms
from .models import *

class BuyAbonement(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.fields['type_id', 'client_id', 'trainer_id', 'duration', 'num_of_trainings'].empty_label = "not selected"

    class Meta:
        model = Abonements
        fields = ['type_id', 'client_id', 'trainer_id', 'duration', 'num_of_trainings']


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.fields['name', 'surname', 'patronymic', 'birthday', 'sex', 'phone_number', 'description'].empty_label = "not selected"

    class Meta:
        model = Abonements
        fields = ['name', 'surname', 'patronymic', 'birthday', 'sex', 'phone_number', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }