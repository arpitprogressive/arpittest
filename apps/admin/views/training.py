# -*- coding: utf-8 -*-
"""
    admin.views.training

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
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

from admin.models import Training
from account.models import TrainingProfile, UserProfile


class TrainingForm(forms.ModelForm):
    '''
        Form for Job
    '''
    class Meta:
        model = Training
        exclude = ('provider')
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }


@csrf_exempt  # Disable CSRF for api call
def render(request, id):
    """
        Render training

    :param id: job id
    """
    training = get_object_or_404(Training, pk=id)
    form = TrainingForm(request.POST or None, instance=training)
    if request.method == 'POST' and \
            training.provider.user_profile.user == request.user:
        if form.is_valid():
            training = form.save()
            if request.is_ajax():
                # Api call response for success save
                return HttpResponse(
                    simplejson.dumps(training._json()),
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
            simplejson.dumps(training._json()),
            content_type="application/json",
        )
    return render_to_response(
        'admin/training.html', {'form': form},
        context_instance=RequestContext(request),
    )


def render_list(request):
    """
        Render trainings list
    """
    filter = {}
    if request.GET.get('job_role'):
        filter['job_role__id__exact'] = request.GET.get('job_role')
    if request.GET.get('provider'):
        filter['provider__id__exact'] = request.GET.get('provider')
    if request.GET.get('location'):
        filter['location__id__exact'] = request.GET.get('location')
    if request.GET.get('for'):
        filter['training_for__exact'] = request.GET.get('for')
    if request.GET.get('type'):
        filter['provider__trainer_type__exact'] = request.GET.get('type')

    if request.GET.get('my') == 'true':
        try:
            filter['provider__id__exact'] = \
                request.user.userprofile.trainingprofile.id
        except ObjectDoesNotExist:
            # Pass if industry profile not found
            pass
    training_list = Training.objects.filter(**filter)

    paginator = Paginator(training_list, 10)  # Show 10 jobs per page
    page = request.GET.get('page')

    try:
        trainings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        trainings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        trainings = paginator.page(paginator.num_pages)

    if request.is_ajax():
        result = {
            'total_count': paginator.count,
            'num_pages': paginator.num_pages,
            'page_range': paginator.page_range,
            'trainings': [training._json() for training in trainings]
        }
        return HttpResponse(
            simplejson.dumps(result), content_type="application/json",
        )
    return render_to_response(
        'admin/trainings.html',
        {'trainings': trainings}, context_instance=RequestContext(request),
    )


@login_required
@csrf_exempt  # Disable CSRF for api call
def new_training(request):
    '''
        Web handler to add new training
    '''
    provider = get_object_or_404(
        TrainingProfile,
        is_approved=True,
        user_profile=get_object_or_404(UserProfile, user=request.user)
    )
    form = TrainingForm(request.POST or None)
    if form.is_valid():
        training = form.save(commit=False)
        training.provider = provider
        training.save()
        return HttpResponseRedirect(training.get_absolute_url())
    return render_to_response(
        'admin/new-training.html', {'form': form},
        context_instance=RequestContext(request)
    )


@login_required
@csrf_exempt  # Disable CSRF for api call
def delete_training(request, id):
    '''
        Delete Training
    '''
    if request.method != 'POST':
        return HttpResponse("<h1>Method not allowed</h1>", status=405)
    training = get_object_or_404(Training, pk=id)
    if training.provider.user_profile.user != request.user:
        raise Http404
    training.delete()
    if request.is_ajax():
        return HttpResponse(
            simplejson.dumps({
                "status": "deleted"
            }), content_type="application/json",
        )
    return HttpResponseRedirect(reverse('render_trainings'))
