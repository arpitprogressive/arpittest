# -*- coding: utf-8 -*-
"""
    admin.views.job

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from admin.models.job import Job
from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext


@cache_page(0)
def render(request, id):
    """
        Render job

    :param id: job id
    """
    job = get_object_or_404(Job, pk=id)
    return render_to_response(
        'admin/job.html',
        {'job': job}, context_instance=RequestContext(request),
    )
