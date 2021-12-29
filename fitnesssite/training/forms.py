from django import forms
from .models import *


class NewAppointment(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['id_trainer', 'date', 'time_start', 'time_end']

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        if self.cleaned_data('time_start') > self.cleaned_data('time_end'):
            raise ValidationError("Training cannot end before beginning")
        return date

