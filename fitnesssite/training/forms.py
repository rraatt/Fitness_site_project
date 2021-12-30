from django import forms
from .models import *


class NewAppointment(forms.ModelForm):
    """Form for a new personal traininga, contains checks for date"""
    class Meta:
        model = Schedule
        fields = ['id_trainer', 'date', 'time_start', 'time_end']

    def clean(self):
        cleaned_data = super(NewAppointment, self).clean()
        date = cleaned_data.get('date')
        if date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        if cleaned_data.get('time_start') > cleaned_data.get('time_end'):
            raise ValidationError('Training cannot end before it starts')
        return cleaned_data


