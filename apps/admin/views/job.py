# -*- coding: utf-8 -*-
"""
    admin.views.job

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from tinymce.widgets import TinyMCE
from django.core.exceptions import ObjectDoesNotExist

from admin.models import Job
from account.models import IndustryProfile, UserProfile


class JobForm(forms.ModelForm):
    '''
        Form for Job
    '''
    class Meta:
        model = Job
        exclude = ('industry')
        widgets = {
            'job_description': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }


@csrf_exempt  # Disable CSRF for api call
def render(request, id):
    """
        Render job

    :param id: job id
    """
    job = get_object_or_404(Job, pk=id)
    form = JobForm(request.POST or None, instance=job)
    if request.method == 'POST' and \
            job.industry.user_profile.user == request.user:
        if form.is_valid():
            job = form.save()
            if request.is_ajax():
                # Api call response for success save
                return HttpResponse(
                    simplejson.dumps(job._json()),
                    content_type="application/json",
                )
            return HttpResponseRedirect(form.instance.get_absolute_url())
        elif request.is_ajax():
            # Api call response for invalid form
            return HttpResponse(
                simplejson.dumps(form.errors),
                content_type="application/json",
            )
    if request.is_ajax():
        # Api call response for get
        return HttpResponse(
            simplejson.dumps(job._json()),
            content_type="application/json",
        )
    return render_to_response(
        'admin/job.html', {'form': form},
        context_instance=RequestContext(request),
    )


def render_list(request):
    """
        Render jobs list
    """
    filter = {}
    if request.GET.get('internship', False):
        filter['is_internship'] = True
    if request.GET.get('job_role'):
        filter['job_role__id__exact'] = request.GET.get('job_role')
    if request.GET.get('company'):
        filter['industry__company__id__exact'] = request.GET.get('company')
    if request.GET.get('location'):
        filter['location__id__exact'] = request.GET.get('location')
    if request.GET.get('my') == 'true':
        try:
            filter['industry__id__exact'] = \
                request.user.userprofile.industryprofile.id
        except ObjectDoesNotExist:
            # Pass if industry profile not found
            pass
    job_list = Job.objects.filter(**filter)

    paginator = Paginator(job_list, 10)  # Show 10 jobs per page
    page = request.GET.get('page')

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jobs = paginator.page(paginator.num_pages)

    if request.is_ajax():
        result = {
            'total_count': paginator.count,
            'num_pages': paginator.num_pages,
            'page_range': paginator.page_range,
            'jobs': [job._json() for job in jobs]
        }
        return HttpResponse(
            simplejson.dumps(result), content_type="application/json",
        )
    return render_to_response(
        'admin/jobs.html',
        {'jobs': jobs}, context_instance=RequestContext(request),
    )


@login_required
@csrf_exempt  # Disable CSRF for api call
def new_job(request):
    '''
        Web handler to add new job
    '''
    industry = get_object_or_404(
        IndustryProfile,
        is_approved=True,
        user_profile=get_object_or_404(UserProfile, user=request.user)
    )
    form = JobForm(request.POST or None)
    if form.is_valid():
        job = form.save(commit=False)
        job.industry = industry
        job.save()
        return HttpResponseRedirect(job.get_absolute_url())
    return render_to_response(
        'admin/new-job.html', {'form': form},
        context_instance=RequestContext(request)
    )


@login_required
@csrf_exempt  # Disable CSRF for api call
def delete_job(request, id):
    '''
    '''
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>", status=405)
    job = get_object_or_404(Job, pk=id)
    if job.industry.user_profile.user != request.user:
        raise Http404
    job.delete()
    if request.is_ajax():
        return HttpResponse(
            simplejson.dumps({
                "status": "deleted"
            }), content_type="application/json",
        )
    return HttpResponseRedirect(reverse('render_jobs'))
