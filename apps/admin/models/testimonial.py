# -*- coding: utf-8 -*-
"""
    admin.models.testimonial

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib import admin

__all__ = ['Testimonial']


class Testimonial(models.Model):
    '''
        Testimonial
    '''
    class Meta:
        '''
            Meta properties for this model
        '''
        app_label = 'admin'
        verbose_name_plural = 'Testimonials'
    name = models.CharField(
        max_length=20, default=None, db_index=True, unique=True,
    )
    content = models.TextField(default=None)
    display_pic = models.FileField(upload_to='testimonial_images')

    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        '''
            Returns object display name
        '''
        return self.name


class TestimonialAdmin(admin.ModelAdmin):
    '''
        Testimonial view for admin
    '''
    list_display = (
        '__unicode__',
    )

admin.site.register(Testimonial, TestimonialAdmin)
