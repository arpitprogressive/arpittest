# -*- coding: utf-8 -*-
"""
    admin.models.qualification_pack

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django import forms
from django.db import models
from django.contrib import admin
from django.contrib import messages
from haystack import indexes
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from .validators import validate_qp_code, validate_version

__all__ = ['QualificationPack', 'QualificationPackIndex']

LEVEL_CHOICES = (
    (10, 'Entry Level 1'),
    (20, 'Entry Level 2'),
    (30, 'Middle Level 1'),
    (40, 'Middle Level 2'),
    (50, 'Middle Level 3'),
    (60, 'Middle Level 4'),
    (70, 'Middle Level 5'),
    (80, 'Leadership Level 1'),
    (90, 'Leadership Level 2'),
    (100, 'Leadership Level 3'),
    (110, 'Leadership Level 4'),
    (120, 'Leadership Level 5'),
)


class QualificationPack(models.Model):
    '''
        Qualification Pack(QP)
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'
        unique_together = ('code', 'version')

    code = models.CharField(
        max_length=9, validators=[validate_qp_code], blank=True,
        db_index=True,
    )
    version = models.CharField(
        max_length=8, validators=[validate_version], db_index=True,
        blank=True,
    )
    is_draft = models.BooleanField(default=True, verbose_name="Draft")
    occupation = models.ForeignKey('Occupation', default=None, db_index=True)

    level = models.IntegerField(default=10, choices=LEVEL_CHOICES)

    @classmethod
    def get_major_level(cls, value):
        if value >= 80:
            return 'll'
        elif value >= 30 and value < 80:
            return 'ml'
        return 'el'

    tracks = models.ManyToManyField('Track', blank=True, null=True)
    next_jobs = models.ManyToManyField(
        'QualificationPack', blank=True, null=True,
    )

    job_role = models.CharField(max_length=50, default=None, db_index=True)
    alias = models.TextField(blank=True)
    role_description = models.TextField(blank=True)
    nveqf_level = models.CharField(max_length=5, blank=True)
    min_educational_qualification = models.CharField(
        max_length=50, blank=True,
    )
    max_educational_qualification = models.CharField(
        max_length=50, blank=True,
    )
    training = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    os_compulsory = models.ManyToManyField(
        'OccupationalStandard', related_name='os_compulsory',
        verbose_name='Occupational Standard (Compulsory)', blank=True,
    )
    os_optional = models.ManyToManyField(
        'OccupationalStandard', related_name='os_optional',
        verbose_name='Occupational Standard (Optional)', null=True, blank=True,
    )
    attachment = models.FileField(upload_to='qp_attachments', blank=True)

    drafted_on = models.DateTimeField(auto_now_add=True)
    last_reviewed_on = models.DateTimeField(auto_now=True)  # Write date
    next_review_on = models.DateField()

    def __unicode__(self):
        '''
            Returns object display name. This comprises code and version.
            For example: SSC/Q2601-V0.1
        '''
        if self.code:
            return "%s-V%s%s (%s)" % (
                self.code, self.version, "draft" if self.is_draft else "",
                self.job_role,
            )
        return "%s%s" % ("(draft) " if self.is_draft else "", self.job_role)

    @property
    def sector(self):
        """
        Returns sector corresponding to qualification pack
        """
        return self.occupation.sector

    @property
    def sub_sector(self):
        """
        Returns sub-sector corresponding to qualification pack
        """
        return self.occupation.sub_sector

    def get_absolute_url(self):
        '''
            get absolute url
        '''
        if self.level < 30:
            # for Entry level qp
            return reverse('qualification_pack', args=(self.code,))
        return reverse('qualification_pack', args=(self.id,))


class QualificationPackForm(forms.ModelForm):
    "Verify Qualification Pack"

    class Meta:
        """
            Meta data for this form
        """
        model = QualificationPack

    def clean(self):
        """
            Verify Qualification data
        """
        super(QualificationPackForm, self).clean()
        os_compulsory = self.cleaned_data.get('os_compulsory', [])
        os_optional = self.cleaned_data.get('os_optional', [])
        next_jobs = self.cleaned_data.get('next_job', [])
        level = self.cleaned_data.get('level')

        if os_compulsory and os_compulsory.all().filter(is_draft=True):
            raise ValidationError(
                'Some of Compulsory Occupational Standards are in draft.'
            )

        if os_optional and os_optional.all().filter(is_draft=True):
            raise ValidationError(
                'Some of Optional Occupational Standards are in draft.'
            )
        if set(os_compulsory) & set(os_optional):
            raise ValidationError(
                'Some Occupational Standards are common in compulsory and \
                optional Occupational Standards'
            )
        if next_jobs and next_jobs.filter(level__lt=level):
            # Check all next_jobs levels are not below current
            raise ValidationError(
                'Some Job roles in Next Job are of low level.'
            )
        return self.cleaned_data


class QualificationPackAdmin(admin.ModelAdmin):
    '''
        Oqualification Pack for Admin
    '''
    exclude = ('is_draft',)
    list_display = (
        '__unicode__', 'occupation', 'level', 'drafted_on',
        'last_reviewed_on', 'next_review_on', 'is_draft',
    )
    list_filter = (
        'code', 'occupation', 'is_draft',
    )
    list_per_page = 20
    search_fields = ['code', 'job_role', 'role_description']
    save_as = True
    form = QualificationPackForm

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
        return self.readonly_fields + ('code',) if obj else ()


admin.site.register(QualificationPack, QualificationPackAdmin)


class QualificationPackIndex(indexes.SearchIndex, indexes.Indexable):
    '''
        Qualification Pack Index for Haystack
    '''
    text = indexes.CharField(document=True)
    code = indexes.CharField(model_attr='code')
    sector = indexes.CharField(model_attr='sector', faceted=True, indexed=False)
    sub_sector = indexes.CharField(model_attr='sub_sector', faceted=True,
            indexed=False)
    occupation = indexes.CharField(model_attr='occupation', faceted=True,
            indexed=False)
    job_role = indexes.CharField(model_attr='job_role')
    alias = indexes.CharField(model_attr='alias')
    role_description = indexes.CharField(model_attr='role_description')
    training = indexes.CharField(model_attr='training')
    experience = indexes.CharField(model_attr='experience')
    os_compulsory = indexes.CharField(model_attr='os_compulsory')
    os_optional = indexes.CharField(model_attr='os_optional')
    model_type = indexes.CharField(faceted=True)

    def get_model(self):
        "Return model class for current index"
        return QualificationPack

    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return self.get_model().objects.filter(is_draft=False)

    def prepare_sector(self, obj):
        "Fetch sector name for indexing"
        return (obj.sub_sector.sector.name).replace(' ', '_').replace('&', '_')

    def prepare_sub_sector(self, obj):
        "Fetch sub sector name for indexing"
        return (obj.sub_sector.name).replace(' ', '_').replace('&', '_')

    def prepare_os_compulsory(self, obj):
        "Fetch os_compulsory name for indexing"
        return "\n".join([f.title for f in obj.os_compulsory.all()])

    def prepare_occupation(self, obj):
        "Fetch occupation name for indexing"
        return (obj.occupation.name).replace(' ', '_').replace('&', '_')

    def prepare_os_optional(self, obj):
        "Fetch os_optional name for indexing"
        return "\n".join([f.title for f in obj.os_optional.all()])

    def prepare_text(self, obj):
        "Prepare primary document for search"
        pattern = (u"{code}\n\n{sector}\n\n{subsector}\n\n{occupation}\n\n"
                   "{job_role}\n\n{role_description}\n\n{alias}")
        return pattern.format(
            code=obj.code,
            subsector=obj.sector.name,
            sector=obj.sub_sector.sector.name,
            occupation=obj.occupation.name,
            job_role=obj.job_role,
            role_description=obj.role_description,
            alias=obj.alias,
        )

    def prepare_model_type(self, obj):
        "Fetch model"
        return "Qualification_Pack"
