# -*- coding: utf-8 -*-
"""
    admin.views.qualification_pack

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from admin.models.qualification_pack import QualificationPack
from admin.models import Job


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
        qp = qualification_packs.latest('version')
        jobs = Job.objects.filter(job_role=qp)
        inters = jobs.filter(is_internship=True)
        jobs = jobs.filter(is_internship=False)
        return render_to_response(
            'admin/qualification_pack.html',
            {'qualification_pack': qp, 'jobs': jobs, 'interns': inters},
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
