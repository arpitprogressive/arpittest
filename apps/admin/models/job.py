# -*- coding: utf-8 -*-
"""
    admin.models.job

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin
from haystack import indexes
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField
from account.models import IndustryProfile
from analytics.models import State
from admin.common import html2text

__all__ = ['Job', 'JobIndex']


class Job(models.Model):
    '''
        Job
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'

    job_title = models.CharField(max_length=50, db_index=True)
    is_internship = models.BooleanField(verbose_name="Internship")
    job_role = models.ForeignKey('QualificationPack', db_index=True)
    industry = models.ForeignKey(IndustryProfile, db_index=True)
    job_description = HTMLField()
    location = models.ForeignKey(State, db_index=True)
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    @property
    def company(self):
        '''
            Compny to which job belongs to.
        '''
        return self.industry.company

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return "%s - %s" % (self.company, self.job_title)

    def get_absolute_url(self):
        '''
            get absolute url
        '''
        return reverse('render_job', args=(self.id,))

    def get_brief(self):
        '''
            return brief description string
        '''
        return html2text(self.job_description)[:250] + '...'

    def _json(self):
        '''
            return serializable dict of this object
        '''
        return {
            'url': self.get_absolute_url(),
            'id': self.id,
            'title': self.job_title,
            'description': self.job_description,
            'internship': self.is_internship,
            'job_role': {
                'url': self.job_role.get_absolute_url(),
                'title': self.job_role.job_role,
            },
        }


class JobAdmin(admin.ModelAdmin):
    '''
        Company view for admin
    '''
    list_display = (
        '__unicode__', 'job_title', 'is_internship'
    )


admin.site.register(Job, JobAdmin)


class JobIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Job Index for Haystack
    """
    text = indexes.CharField(document=True)
    job_title = indexes.CharField(model_attr='job_title')
    company = indexes.CharField(model_attr='company')
    is_internship = indexes.CharField()
    job_role = indexes.CharField()

    def get_model(self):
        "Return model class for current index"
        return Job

    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return self.get_model().objects.all()

    def prepare_model_type(self, obj):
        "Fetch model type"
        return "Job"

    def prepare_is_internship(self, obj):
        "Fetch internship"
        return str(obj.is_internship)

    def prepare_company(self, obj):
        "Fetch company"
        return obj.company.name

    def prepare_job_role(self, obj):
        "Fetch job role"
        return obj.job_role.job_role

    def prepare_text(self, obj):
        "Prepare primary document for search"
        pattern = "{title}\n{internship}\n{company}\n{roles}\n{description}"
        return pattern.format(
            title=obj.job_title,
            internship='Internship' if obj.is_internship else '',
            company=obj.company.name,
            roles=obj.job_role.job_role,
            description=obj.job_description,
        )
