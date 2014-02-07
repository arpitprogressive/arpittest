# -*- coding: utf-8 -*-
"""
    admin.models.training

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField
from account.models import TrainingProfile
from analytics.models import State
from admin.common import html2text

__all__ = ['Training']


class Training(models.Model):
    '''
        Training
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'

    TRAINING_CHOICES = {
        ('T', 'Trainers'),
        ('S', 'Students'),
    }
    training_title = models.CharField(max_length=100, db_index=True)
    job_role = models.ForeignKey(
        'QualificationPack', related_name="training_provider", db_index=True
    )
    provider = models.ForeignKey(TrainingProfile, db_index=True)
    training_for = models.CharField(max_length=1, choices=TRAINING_CHOICES)
    description = HTMLField()
    location = models.ForeignKey(State, db_index=True)
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return "%s - %s" % (self.provider, self.training_title)

    def get_absolute_url(self):
        '''
            get absolute url
        '''
        return reverse('render_training', args=(self.id,))

    def get_brief(self):
        '''
            return brief description string
        '''
        return html2text(self.description)[:250] + '...'

    def _json(self):
        '''
            return serializable dict of this object
        '''
        return {
            'url': self.get_absolute_url(),
            'id': self.id,
            'title': self.training_title,
            'description': self.description,
            'job_role': {
                'url': self.job_role.get_absolute_url(),
                'title': self.job_role.job_role,
            },
        }


class TrainingAdmin(admin.ModelAdmin):
    '''
        Training view for admin
    '''
    list_display = (
        '__unicode__', 'training_title',
    )


admin.site.register(Training, TrainingAdmin)
