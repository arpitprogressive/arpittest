# -*- coding: utf-8 -*-
"""
    account.views

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """
    Renders profile page.
    """
    return render_to_response(
        'account/profile.html', {}, context_instance=RequestContext(request)
    )
