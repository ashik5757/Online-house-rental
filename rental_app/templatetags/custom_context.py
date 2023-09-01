# custom_context.py
from django import template
from django.contrib.auth.models import User
from rental_app.models import *

register = template.Library()

@register.simple_tag
def city_context():
    areaObj = Area.objects.all()
    return areaObj


@register.simple_tag
def district_context():
    distObj = District.objects.all()
    return distObj