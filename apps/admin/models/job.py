# -*- coding: utf-8 -*-
"""
    admin.models.job

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin
from haystack import indexes

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

    job_title = models.CharField(max_length=50, blank=True, db_index=True)
    is_internship = models.BooleanField(verbose_name="Internship")
    job_role = models.ForeignKey(
        'QualificationPack', default=None, db_index=True,
    )
    company = models.ForeignKey('Company', default=None, db_index=True)
    job_description = models.TextField(blank=True)

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return "%s - %s" % (self.company, self.job_title)


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
