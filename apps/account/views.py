# -*- coding: utf-8 -*-
"""
    account.views

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from account.models import UserProfile


@login_required
def profile(request):
    """
    Renders profile page.
    """
    userprofile = get_object_or_404(UserProfile, user=request.user.id)
    Profile, ProfileForm = userprofile.get_profile_model_form()

    profile, created = \
        Profile.objects.get_or_create(user_profile=request.user.userprofile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = ProfileForm(instance=profile)

    return render_to_response(
        'account/profile.html', {'form': form},
        context_instance=RequestContext(request)
    )
