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
    tracks = models.ManyToManyField('Track', blank=True, null=True)
    slug = models.SlugField(unique=True)
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

    @property
    def qps(self):
        """
        Returns a list of objects of the jobs in this occupation
        """
        from admin.models.qualification_pack import QualificationPack
        return QualificationPack.objects.filter(
            occupation=self, is_draft=False
        )


class OccupationAdmin(admin.ModelAdmin):
    '''
        Occupation for admin
    '''
    list_display = ('name', 'sub_sector', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Occupation, OccupationAdmin)
