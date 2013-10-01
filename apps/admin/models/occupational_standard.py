# -*- coding: utf-8 -*-
"""
    occupational_standard

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models

__all__ = [
    'PursuiteModel', 'OccupationalStandard', 'OSVersion', 'OSKnowledgeRecord',
    'OSPerformanceCriterion', 'OSSkill',
]


class PursuiteModel(models.Model):
    '''
        Model class for admin
    '''
    class Meta:
        abstract = True
        app_label = 'admin'


class OccupationalStandard(PursuiteModel):
    '''
        Occupational Standard
    '''
    code = models.CharField(max_length=9, default=None)

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.code

    @property
    def versions(self):
        '''
            Returns active records of all versions of this Occupational
            Standards.
        '''
        return OSVersion.objects.filter(occupational_standard=self.pk)


class OSVersion(PursuiteModel):
    '''
        Occupational Standard Version
    '''
    occupational_standard = models.ForeignKey('OccupationalStandard')
    title = models.CharField(max_length=50, default=None)
    description = models.TextField(default=None)
    scope = models.TextField(default=None)

    # Version information
    version = models.CharField(max_length=8, default=None)
    is_draft = models.BooleanField(default=True)
    drafted_on = models.DateField(auto_now_add=True)  # Create date
    last_reviewed_on = models.DateField(auto_now=True)  # Write date
    next_review_on = models.DateField()

    def __unicode__(self):
        '''
            Returns object display name. This comprises code and version.
            For example: SSC/Q2601-V0.1
        '''
        return self.occupational_standard.code + "-V" + self.version

    @property
    def performance_criteria(self):
        '''
            Returns active records of all performance criterion of this
            Occupational Standard version.
        '''
        return OSPerformanceCriterion.objects.filter(os_version=self.pk)

    @property
    def knowledge(self):
        '''
            Returns active records of all knowledge and understanding
            requirements of this Occupational Standard version.
        '''
        return OSKnowledgeRecord.objects.filter(os_version=self.pk)

    @property
    def skills(self):
        '''
            Returns active records of all skill requirements of this
            Occupational Standard version.
        '''
        return OSSkill.objects.filter(os_version=self.pk)


class OSPerformanceCriterion(PursuiteModel):
    '''
        Occupational Standard Performance Criterion
    '''
    os_version = models.ForeignKey('OSVersion')
    sequence = models.IntegerField(default=10)
    description = models.TextField(default=None)

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.description


class OSKnowledgeRecord(PursuiteModel):
    '''
        Occupational Standard Knowledge and Understanding
    '''
    CATEGORY_CHOICES = {
        ('OC', 'Organizational Context'),
        ('TK', 'Technical Knowledge'),
    }

    os_version = models.ForeignKey('OSVersion')
    sequence = models.IntegerField(default=10)
    description = models.TextField(default=None)
    category = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES, default=None
    )

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.description


class OSSkill(PursuiteModel):
    '''
        Occupational Standard Skill
    '''
    CATEGORY_CHOICES = {
        ('CS', 'Core Skills'),
        ('PS', 'Professional Skills'),
        ('TS', 'Technical Skills'),
    }
    TITLE_CHOICES = {
        ('WS', 'Writing Skills'),
        ('RS', 'Reading Skills'),
        ('OC', 'Oral Communication'),
        ('DM', 'Decision Making'),
        ('PO', 'Plan and Organize'),
        ('CC', 'Customer Centricity'),
        ('PS', 'Problem Solving'),
        ('AT', 'Analytical Thinking'),
        ('CT', 'Critical Thinking'),
        ('AD', 'Attention to Detail'),
        ('TW', 'Team Working'),
    }

    os_version = models.ForeignKey('OSVersion')
    sequence = models.IntegerField(default=10)
    title = models.CharField(max_length=2, choices=TITLE_CHOICES, default=None)
    description = models.TextField(default=None)
    category = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES, default=None
    )

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.description
