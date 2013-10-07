# -*- coding: utf-8 -*-
"""
    admin.models.occupational_standard

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from tinymce.models import HTMLField
from django.db import models
from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import ValidationError

from .validators import validate_code, validate_version

__all__ = ['OccupationalStandard']


class OccupationalStandard(models.Model):
    '''
        Occupational Standard
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'
        unique_together = ('code', 'version')

    code = models.CharField(
        max_length=9, default=None, validators=[validate_code],
        db_index=True,
    )
    version = models.CharField(
        max_length=8, default=None, validators=[validate_version],
        db_index=True,
    )
    is_draft = models.BooleanField(default=True, verbose_name="Draft")
    sector = models.ForeignKey('Sector', db_index=True)
    sub_sector = models.ForeignKey('SubSector', db_index=True)

    title = models.CharField(max_length=50, default=None, db_index=True)
    description = models.TextField(default=None)
    scope = HTMLField(default=None)
    performace_criteria = HTMLField(default=None)
    knowledge = HTMLField(default=None)
    skills = HTMLField(default=None)

    drafted_on = models.DateField(auto_now_add=True)
    last_reviewed_on = models.DateField(auto_now=True)  # Write date
    next_review_on = models.DateField()

    def __unicode__(self):
        '''
            Returns object display name. This comprises code and version.
            For example: SSC/Q2601-V0.1
        '''
        return self.code + "-V" + self.version

    def clean(self):
        '''
            Validate model instance
        '''
        if OccupationalStandard.objects.filter(code=self.code, is_draft=True) \
                .exclude(pk=self.pk):
            # Check one OS should have one version in draft
            raise ValidationError(
                'There is already a version in draft for %s' % self.code
            )
        # Check sector and Subsector


class OccupationalStandardAdmin(admin.ModelAdmin):
    '''
        Occupational Standard for admin
    '''
    exclude = ('is_draft',)
    list_display = (
        '__unicode__', 'sector', 'sub_sector', 'title', 'drafted_on',
        'last_reviewed_on', 'next_review_on', 'is_draft',
    )
    list_filter = (
        'code', 'sector', 'sub_sector', 'is_draft',
    )
    list_per_page = 20
    search_fields = ['code', 'title', 'description']
    save_as = True

    def bump_new_version(modeladmin, request, queryset):
        '''
            Action to bump new version

            Publish version in draft and create new draft from the that version
            with new version: '~' + <old_version>.
        '''
        # filter Draft from selected
        drafts = queryset.filter(is_draft=True).all()
        for draft in drafts:
            if '~' in draft.version:
                # Don't bump if version is invalid
                messages.error(
                    request, 'Cannot bump %s-V%s. Invalid version format' %
                    (draft.code, draft.version)
                )
                continue
            draft.is_draft = False  # Publish previous draft
            draft.save()
            new_draft = draft  # Create new item from last version
            new_draft.pk = None
            new_draft.is_draft = True
            new_draft.version = "~" + new_draft.version
            new_draft.save()  # Save new draft
            messages.success(
                request, 'Bumped %s-V%s.' % (draft.code, draft.version)
            )

    bump_new_version.short_description = "Bump new version"
    actions = [bump_new_version]

    def get_readonly_fields(self, request, obj=None):
        '''
            Returns readonly fields of this admin view
        '''
        if obj and not obj.is_draft:
            return obj._meta.get_all_field_names()
        return self.readonly_fields


admin.site.register(OccupationalStandard, OccupationalStandardAdmin)
