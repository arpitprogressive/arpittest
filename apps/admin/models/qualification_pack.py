# -*- coding: utf-8 -*-
"""
    admin.models.qualification_pack

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin
from django.contrib import messages
from haystack import indexes

from .validators import validate_qp_code, validate_version

__all__ = ['QualificationPack', 'QualificationPackIndex']


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
        max_length=9, default=None, validators=[validate_qp_code],
        db_index=True,
    )
    version = models.CharField(
        max_length=8, default=None, validators=[validate_version],
        db_index=True,
    )
    is_draft = models.BooleanField(default=True, verbose_name="Draft")
    occupation = models.ForeignKey('Occupation', default=None, db_index=True)

    job_role = models.CharField(max_length=50, default=None, db_index=True)
    alias = models.TextField(default=None)
    role_description = models.TextField(default=None)
    nveqf_level = models.CharField(max_length=5, default=None)
    min_educational_qualification = models.CharField(
        max_length=50, default=None,
    )
    max_educational_qualification = models.CharField(
        max_length=50, default=None,
    )
    training = models.TextField()
    experience = models.TextField(default=None)
    os_compulsory = models.ManyToManyField(
        'OccupationalStandard', related_name='os_compulsory',
        verbose_name='Occupational Standard (Compulsory)',
    )
    os_optional = models.ManyToManyField(
        'OccupationalStandard', related_name='os_optional',
        verbose_name='Occupational Standard (Optional)', null=True, blank=True,
    )
    attachment = models.FileField(upload_to='qp_attachments')

    drafted_on = models.DateTimeField(auto_now_add=True)
    last_reviewed_on = models.DateTimeField(auto_now=True)  # Write date
    next_review_on = models.DateField()

    def __unicode__(self):
        '''
            Returns object display name. This comprises code and version.
            For example: SSC/Q2601-V0.1
        '''
        return "%s-V%s%s (%s)" % (
            self.code, self.version, "draft" if self.is_draft else "",
            self.job_role,
        )

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


class QualificationPackAdmin(admin.ModelAdmin):
    '''
        Oqualification Pack for Admin
    '''
    exclude = ('is_draft',)
    list_display = (
        '__unicode__', 'occupation', 'drafted_on',
        'last_reviewed_on', 'next_review_on', 'is_draft',
    )
    list_filter = (
        'code', 'occupation', 'is_draft',
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
        return (obj.sub_sector.sector.name).replace(' ', '_')

    def prepare_sub_sector(self, obj):
        "Fetch sub sector name for indexing"
        return (obj.sub_sector.name).replace(' ', '_')

    def prepare_os_compulsory(self, obj):
        "Fetch os_compulsory name for indexing"
        return "\n".join([f.title for f in obj.os_compulsory.all()])

    def prepare_occupation(self, obj):
        "Fetch occupation name for indexing"
        return (obj.occupation.name).replace(' ', '_')

    def prepare_os_optional(self, obj):
        "Fetch os_optional name for indexing"
        return "\n".join([f.title for f in obj.os_optional.all()])

    def prepare_text(self, obj):
        "Prepare primary document for search"
        pattern = ("{code}\n\n{sector}\n\n{subsector}\n\n{occupation}\n\n"
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
