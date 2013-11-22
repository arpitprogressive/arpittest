# -*- coding: utf-8 -*-
"""
    admin.models.job

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin

__all__ = ['Job']


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
