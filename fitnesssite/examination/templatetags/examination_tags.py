from django import template
from examination.models import *

register = template.Library()

@register.simple_tag()
def get_examination():
    return Examination.objects.all()