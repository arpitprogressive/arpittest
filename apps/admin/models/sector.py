# -*- coding: utf-8 -*-
"""
    admin.models.sector

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin

__all__ = ['Sector', 'SubSector']


class Sector(models.Model):
    '''
        Sector/Industry model
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'
        index_together = [["name"]]

    name = models.CharField(
        max_length=9, default=None, unique=True, db_index=True,
    )

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.name

    @property
    def sub_sectors(self):
        '''
            Returns active records of all the sub sectors of this sector
        '''
        return SubSector.objetcs.filter(sector=self)


class SubSector(models.Model):
    '''
        Sub-Sector/Industry Sub-Sector model
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'
        unique_together = ('sector', 'name')
        index_together = [["name", "sector"]]

    sector = models.ForeignKey('Sector')
    name = models.CharField(max_length=50, default=None, db_index=True)

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.name


class SubSectorAdmin(admin.ModelAdmin):
    '''
        Subsector for admin
    '''
    list_display = ('name', 'sector')


admin.site.register(SubSector)
admin.site.register(Sector)
