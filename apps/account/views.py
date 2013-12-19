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
from admin.common import get_cms_page_url

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


def check_competency(request):
    """
    Render the competency (BS) of the person
    """
    user_profile = UserProfile.objects.filter(user=request.user.id)
    if not user_profile:
        # No user_profile. i.e. user must be django_admin user
        return HttpResponseRedirect(get_cms_page_url('check-your-competency'))

    user_profile = user_profile.get()

    if user_profile.role != 'S':
        # Not a student profile
        return HttpResponseRedirect(get_cms_page_url('check-your-competency'))

    student_profile = matching_jobs = None
    student_profile = StudentProfile.objects.filter(user_profile=user_profile)
    if not student_profile:
        # Student profile yet to be created.
        return HttpResponseRedirect(
            get_cms_page_url('check-your-competency-student')
        )

    student_profile = student_profile.get()
    matching_jobs = student_profile.find_matching_jobs()

    if not matching_jobs:
        # No Key_skills in profile
        return HttpResponseRedirect(
            get_cms_page_url('check-your-competency-student')
        )

    return render_to_response(
        'account/competency.html', {
            'user_profile': user_profile,
            'student_profile': student_profile,
            'matching_jobs': matching_jobs,
            'debug': settings.DEBUG,
        },
        context_instance=RequestContext(request)
    )
