# -*- coding: utf-8 -*-
"""
    admin.filters

    Custom filters

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.core.exceptions import ObjectDoesNotExist
from admin.common import html2text
from django import template
from django.forms.fields import TypedChoiceField, DateField
from django.forms.models import ModelMultipleChoiceField

register = template.Library()


@register.filter
def get_description(page):
    '''
        Returns brief description of cms page
    '''
    placeholders = page.placeholders.filter(slot='content')
    if not placeholders:
        return ""
    placeholder, = placeholders
    plugins = placeholder.get_plugins().filter(plugin_type='TextPlugin')
    try:
        desc = ''.join([html2text(plugin.text.body) for plugin in plugins])
    except ObjectDoesNotExist:
        desc = ''
    desc = desc[:100] + ('...' if len(desc) > 100 else '')
    return desc


@register.filter
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)


@register.filter
def get_value(dict, key):
    """
        Returns the value from dict
    """
    if not dict:
        return None
    for k, v in dict:
        if k == key:
            return v
    return None


@register.filter()
def get_text(field):
    """
        Return display value of field
    """
    if type(field.field) is TypedChoiceField:
        for key, value in field.field.choices:
            if key == field.value():
                return value
    if type(field.field) is ModelMultipleChoiceField:
        out = ""
        for item in field.field.queryset.filter(id__in=field.value()).all():
            out += "<a href='%s'>%s</a><br>" % (item.get_absolute_url(), item)
        return out
    if type(field.field) is DateField and field.value():
        return field.value().strftime('%d-%m-%Y')

    return field.value()


@register.filter()
def mult(value, value2):
    return value * value2
