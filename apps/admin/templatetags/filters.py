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
