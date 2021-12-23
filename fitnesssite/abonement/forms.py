from django import forms
from .models import *

class BuyAbonement(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.fields['type_id', 'client_id', 'trainer_id', 'duration', 'num_of_trainings'].empty_label = "not selected"

    class Meta:
        model = Abonements
        fields = ['type_id', 'client_id', 'trainer_id', 'duration', 'num_of_trainings']

