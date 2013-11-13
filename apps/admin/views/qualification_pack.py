# -*- coding: utf-8 -*-
"""
    admin.views.qualification_pack

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.db.models import Count
from admin.models.qualification_pack import QualificationPack


def view_qualification_packs(request):
    """
    Renders all the qualification packs.

    :param request: request object
    """
    qualification_packs = QualificationPack.objects.filter(
        is_draft=False
    ).annotate(Count('code'))
    return render_to_response(
        'admin/qualification_packs.html',
        {'qualification_packs': qualification_packs},
        context_instance=RequestContext(request)
    )


def view_qualification_pack(request, code, version=None):
    """
    Render Qualfication Pack from QP Code

    :param request: request object
    :param code: qualification pack code
    :param version: version of qualification pack
    """
    filter = {'code': code, 'is_draft': False}
    if version:
        filter['version'] = version
    qualification_packs = QualificationPack.objects.filter(**filter)
    if qualification_packs:
        return render_to_response(
            'admin/qualification_pack.html',
            {'qualification_pack': qualification_packs.latest('version')},
            context_instance=RequestContext(request),
        )
    raise Http404


def view_qualification_pack_id(request, id):
    """
    Render Qualfication Pack from QP ID

    :param request: request object
    :param id: id
    """
    qualification_pack = QualificationPack.objects.filter(id=id)
    if not qualification_pack:
        raise Http404

    return render_to_response(
        'admin/qualification_pack_id.html',
        {'qualification_pack': qualification_pack.get()},
        context_instance=RequestContext(request),
    )
