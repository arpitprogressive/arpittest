# -*- coding: utf-8 -*-
"""
    admin.models.occupation

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin

__all__ = ['Occupation']


class Occupation(models.Model):
    '''
        Occupation model
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'

    name = models.CharField(
        max_length=50, default=None, unique=True, db_index=True,
    )
    sub_sector = models.ForeignKey('SubSector', db_index=True)

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return "%s/%s" % (self.sub_sector, self.name)

    @property
    def sector(self):
        """
        Returns the sector for occupation
        """
        return self.sub_sector.sector


class OccupationAdmin(admin.ModelAdmin):
    '''
        Occupation for admin
    '''
    list_display = ('name', 'sub_sector')


admin.site.register(Occupation, OccupationAdmin)
