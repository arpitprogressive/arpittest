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

    name = models.CharField(
        max_length=100, default=None, unique=True, db_index=True,
    )
    url = models.URLField(max_length=100, unique=True)
    international = models.BooleanField(default=False)

    def __unicode__(self):
        '''
            Returns object display name.
        '''
        return self.name


class InstitutionAdmin(admin.ModelAdmin):
    '''
        Institution view for admin
    '''
    list_display = ('name', 'url', 'international')
    list_filter = ('international',)
    list_per_page = 20
    search_field = ['name', 'url']


admin.site.register(Institution, InstitutionAdmin)
