# -*- coding: utf-8 -*-
"""
    analytics.templatetags.analytics_tags

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
import json

from django import template
from analytics.models import DemandData, SupplyBase

register = template.Library()


@register.simple_tag(takes_context=True)
def get_year(context, type):
    """
        Return year for analytics
    """
    Base = DemandData if type == 'demand' else SupplyBase

    years = sorted([
        k['year'] for k in Base.objects.values('year').distinct()
    ])
    return json.dumps({
        'current': context['request'].GET.get('year', years[-1]),
        'years': years,
    })
