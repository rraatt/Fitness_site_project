from django import template
from training.models import *

register = template.Library()


@register.simple_tag()
def get_groups_schedule():
    return Schedule.objects.filter(content_type__model='group')


@register.inclusion_tag('training/menu.html', name='menu')
def show_menu():
    menu = [{'title': 'Make an appointment', 'url_name': 'new_training'},
            {'title': 'Group trainings', 'url_name': 'group_schedule'},
            {'title': 'About us', 'url_name': 'about'}]
    return {"menu": menu}