# -*- coding: utf-8 -*-
"""
    analytics.models

    Models for Demand and Supply data

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""


from django.db import models
import django.contrib.admin

from admin.models import Occupation, Institution, Company


__all__ = ['DEGREE_CHOICES', 'REGION_CHOICES', 'State', 'City', 'SupplyBase',
        'DemandData']


DEGREE_CHOICES = (
    ('UG', 'Undergraduate Degree'),
    ('PG', 'Postgraduate Degree'),
    ('DOC', 'Ph.D/M.Phil'),
    ('PSD', 'Post School Diploma'),
    ('PGD', 'Post Graduate Diploma'),
    ('UNK', 'Unknown'),
)


REGION_CHOICES = (
    ('NORTH', 'North'),
    ('SOUTH', 'South'),
    ('EAST', 'East'),
    ('WEST', 'West'),
    ('NORTH_EAST', 'North East'),
    ('NORTH_WEST', 'North West'),
    ('SOUTH_EAST', 'South East'),
    ('SOUTH_WEST', 'South West'),
    ('CENTRAL', 'Central'),
)


class State(models.Model):
    """
    States
    """
    name = models.CharField(max_length=50, default=None, unique=True)
    region = models.CharField(max_length=12, choices=REGION_CHOICES)

    class Meta:
        unique_together = ('name', 'region',)

    def __unicode__(self):
        """
        Returns object display name
        """
        return self.name


class City(models.Model):
    """
    Cities
    """
    name = models.CharField(max_length=50, default=None)
    state = models.ForeignKey('State')

    class Meta:
        unique_together = ('name', 'state',)
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%s,%s" % (self.name, self.state)


class SupplyBase(models.Model):
    """
    Demand supply data
    """
    year = models.IntegerField()
    city = models.ForeignKey('City')
    occupation = models.ForeignKey(Occupation)
    institution = models.ForeignKey(Institution)
    degree = models.CharField(max_length=3, choices=DEGREE_CHOICES,
            default=None)
    supply = models.IntegerField()

    class Meta:
        unique_together = ('year', 'city', 'occupation', 'institution',
                'degree',)
        verbose_name_plural = 'SupplyBase'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s,%s" % (self.year, self.city, self.occupation,)


class DemandData(models.Model):
    """
    Demand data
    """
    year = models.IntegerField()
    city = models.ForeignKey('City')
    occupation = models.ForeignKey(Occupation)
    company = models.ForeignKey(Company)
    demand = models.IntegerField()

    class Meta:
        unique_together = ('year', 'city', 'occupation', 'company',)
        verbose_name_plural = 'DemandBase'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s,%s" % (self.year, self.city, self.occupation,)


django.contrib.admin.site.register(State)
django.contrib.admin.site.register(City)
django.contrib.admin.site.register(SupplyBase)
django.contrib.admin.site.register(DemandData)
