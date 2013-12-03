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
from django.conf import settings

from account.models import UserProfile, StudentProfile


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


@login_required
def check_competency(request):
    """
    Render the competency (BS) of the person
    """
    user_profile = get_object_or_404(UserProfile, user=request.user.id)

    student_profile = matching_jobs = None

    if user_profile.role == 'S':
        student_profile = StudentProfile.objects.get(user_profile=user_profile)
        matching_jobs = student_profile.find_matching_jobs()

    return render_to_response(
        'account/competency.html', {
            'user_profile': user_profile,
            'student_profile': student_profile,
            'matching_jobs': matching_jobs,
            'debug': settings.DEBUG,
        },
        context_instance=RequestContext(request)
    )
