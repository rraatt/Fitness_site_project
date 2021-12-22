from django import template
from examination.models import *

register = template.Library()

@register.simple_tag()
def get_examination():
    return Examination.objects.all()


@register.inclusion_tag('training/menu.html', name='menu')
def show_menu():
    menu = [{'title': 'Make an appointment', 'url_name': 'new_training'},
            {'title': 'Group trainings', 'url_name': 'group_schedule'},
            {'title': 'Examinations', 'url_name': 'examination'},
            {'title': 'About us', 'url_name': 'about'}]
    return {"menu": menu}