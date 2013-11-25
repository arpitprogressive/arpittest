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

    @property
    def qualification_packs(self):
        """
        Return the qualification packs in the same track
        """
        from admin.models.qualification_pack import QualificationPack
        return QualificationPack.objects.filter(
            tracks__id__exact=self.id,
            is_draft=False,
        ).all()

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.name


admin.site.register(Track)
