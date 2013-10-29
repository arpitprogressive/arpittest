# -*- coding: utf-8 -*-
"""
    admin.views.occupational_standard

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.db.models import Count
from admin.models.occupational_standard import OccupationalStandard


def view_occupational_standards(request):
    """
    Renders all the occupational standards.

    :param request: request object
    """
    occupational_standards = OccupationalStandard.objects.filter(
        is_draft=False
    ).annotate(Count('code'))
    return render_to_response(
        'admin/occupational_standards.html',
        {'occupational_standards': occupational_standards},
        context_instance=RequestContext(request)
    )


def view_occupational_standard(request, code, version=None):
    """
    Render Occupational Standard

    :param request: request object
    :param code: occupational standard code
    :param version: version of occupational standard
    """
    filter = {'code': code, 'is_draft': False}
    if version:
        filter['version'] = version
    occupational_standards = OccupationalStandard.objects.filter(**filter)
    if occupational_standards:
        return render_to_response(
            'admin/occupational_standard.html',
            {'occupational_standard': occupational_standards.latest('version')},
            context_instance=RequestContext(request),
        )
    raise Http404
