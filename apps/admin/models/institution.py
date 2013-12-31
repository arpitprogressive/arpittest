# -*- coding: utf-8 -*-
"""
    admin.models.institution

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin

__all__ = ['Institution']


class Institution(models.Model):
    '''
        Institution
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'

    UNIVERSITY_CHOICES = (
        ('CU', 'Central University'),
        ('SU', 'State University'),
        ('DU', 'Deemed University'),
        ('PU', 'Public University'),
        ('INI', 'Institute of National Importance'),
    )

    name = models.CharField(
        max_length=100, default=None, unique=True, db_index=True,
    )
    url = models.URLField(max_length=100, unique=True)
    international = models.BooleanField(default=False)
    city = models.ForeignKey('analytics.City', null=True, blank=True)
    is_university = models.BooleanField()
    university_type = models.CharField(
        max_length=3, choices=UNIVERSITY_CHOICES, null=True, blank=True
    )
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        '''
            Returns object display name.
        '''
        return self.name


class InstitutionAdmin(admin.ModelAdmin):
    '''
        Institution view for admin
    '''
    list_display = ('name', 'url', 'international', )
    list_filter = ('international',)
    list_per_page = 20
    search_field = ['name', 'url']


admin.site.register(Institution, InstitutionAdmin)
