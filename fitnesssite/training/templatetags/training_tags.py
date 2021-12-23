from django import template
from training.models import *

register = template.Library()


@register.inclusion_tag('training/menu.html', name='menu')
def show_menu():
    menu = [{'title': 'Make an appointment', 'url_name': 'new_training'},
            {'title': 'Group trainings', 'url_name': 'group_schedule'},
            {'title': 'Examinations', 'url_name': 'examination'},
            {'title': 'About us', 'url_name': 'about'},
            {'title': 'Profile', 'url_name': 'profile'}]
    return {"menu": menu}
