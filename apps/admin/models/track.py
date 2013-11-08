# -*- coding: utf-8 -*-
"""
    admin.models.track

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin

__all__ = ['Track']


class Track(models.Model):
    '''
        Track
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'

    name = models.CharField(
        max_length=50, default=None, unique=True, db_index=True,
    )

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.name


admin.site.register(Track)
