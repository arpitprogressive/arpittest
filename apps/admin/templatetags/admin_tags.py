# -*- coding: utf-8 -*-
"""
    admin.templatetags.qp_tag

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db.models import Count
from admin.models.qualification_pack import QualificationPack
from admin.models.occupational_standard import OccupationalStandard
from django import template

register = template.Library()


@register.inclusion_tag('tags/list_qp.html', takes_context=True)
def list_qp(context):
    """
    Renders all the qualification packs.

    :param context: context
    """
    request = context['request']
    filter = {'is_draft': False}
    if request.GET.get('occupation'):
        filter['occupation__id__exact'] = request.GET.get('occupation')
    if request.GET.get('sub_sector'):
        filter['occupation__sub_sector__id__exact'] = \
            request.GET.get('sub_sector')
    if request.GET.get('occupation'):
        filter['occupation__id__exact'] = request.GET.get('occupation')

    qualification_packs = QualificationPack.objects.filter(**filter).annotate(
        Count('code')
    )
    return {
        'qualification_packs': qualification_packs,
        'request': request,
    }


@register.inclusion_tag('tags/list_os.html', takes_context=True)
def list_os(context):
    """
    Renders all the occupational standards.

    :param context: context
    """
    occupational_standards = OccupationalStandard.objects.filter(
        is_draft=False
    ).annotate(Count('code'))
    return {
        'occupational_standards': occupational_standards,
        'request': context['request'],
    }
