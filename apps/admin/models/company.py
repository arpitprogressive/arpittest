# -*- coding: utf-8 -*-
"""
    admin.models.company

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin
from django.core.validators import RegexValidator

__all__ = ['Company']


class Company(models.Model):
    '''
        Company
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'
        verbose_name_plural = 'Companies'

    # FIXME: Write Acronym of abbreviations
    TRAINING_PROVIDER_CHOICES = {
        ('NO', 'No'),
        ('LTP', 'LTP'),
        ('ATP', 'ATP'),
    }
    name = models.CharField(
        max_length=100, default=None, unique=True, db_index=True,
    )
    url = models.URLField(max_length=100, unique=True)
    nasscom_membership_number = models.CharField(
        max_length=20, verbose_name='Nasscom Membership Number',
        default='N/A', validators=[
            RegexValidator(
                r'^((N/A)|([0-z]*))$',
                message='Membership number should be Alphanumeric.',
                code='invalid_membership_number',
            ),
        ],
    )
    training_provider = models.CharField(
        max_length=3, choices=TRAINING_PROVIDER_CHOICES, default='NO',
    )

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.name


class CompanyAdmin(admin.ModelAdmin):
    '''
        Company view for admin
    '''
    list_display = (
        '__unicode__', 'nasscom_membership_number', 'training_provider',
    )


admin.site.register(Company, CompanyAdmin)
