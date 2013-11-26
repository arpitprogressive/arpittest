# -*- coding: utf-8 -*-
"""
    admin.views.occupational_standard

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from admin.models.occupational_standard import OccupationalStandard


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
