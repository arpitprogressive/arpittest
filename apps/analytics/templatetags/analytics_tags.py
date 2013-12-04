# -*- coding: utf-8 -*-
"""
    analytics.templatetags.analytics_tags

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
import json

from django import template
from analytics.models import DemandData, SupplyBase, State
from analytics import views

register = template.Library()


# Source: http://stackoverflow.com/q/2566265
class DefineNode(template.Node):
    def __init__(self, var, name):
        self.var = var
        self.name = name

    def __repr__(self):
        return "<DefineNode>"

    def render(self, context):
        if self.name not in context:
            context[self.name] = self.var
        return ''


@register.tag
def demand_latest_year(parser, token):
    return DefineNode(views.get_latest_year('demand'), 'analytics_year')


@register.tag
def supply_latest_year(parser, token):
    return DefineNode(views.get_latest_year('supply'), 'analytics_year')


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
        'current': context.get('analytics_year', years[-1]),
        'years': years,
    })


@register.simple_tag(takes_context=True)
def get_latest_year(context, type):
    """
        Return latest year for analytics
    """
    return views.get_latest_year(type)


@register.simple_tag()
def get_states():
    """
        Return json for all states
    """
    return json.dumps({state.name: state.id for state in State.objects.all()})
