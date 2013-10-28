# -*- coding: utf-8 -*-
"""
    cmsindex.search_indexes

    Haystack Index for Django CMS

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""

from haystack import indexes
from cms.models import Page, Title
from cms.models.pluginmodel import CMSPlugin

from admin.common import html2text

__all__ = ['DjangoCMSPageIndex']


class DjangoCMSPageIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Django CMS Index for Haystack
    """
    text = indexes.CharField(document=True)
    pub_date = indexes.DateTimeField(model_attr='publication_date', null=True)
    login_required = indexes.BooleanField(model_attr='login_required')
    title = indexes.CharField()
    site_id = indexes.IntegerField(model_attr='site_id')
    model_type = indexes.CharField(faceted=True)

    def get_model(self):
        "Return model class for current index"
        return Page

    def index_queryset(self, using=None):
        "Used when entire index for model is updated"
        return self.get_model().objects.filter(
            published=True,
            publisher_is_draft=False,
        ).distinct()

    def prepare_text(self, obj):
        "Prepare primary document for search"
        placeholders = obj.placeholders.all()
        plugins = CMSPlugin.objects.filter(placeholder__in=placeholders)
        title, = Title.objects.values('title').filter(page_id=obj.pk)
        text = title['title'] + '\n\n'
        for plugin in plugins:
            instance, _ = plugin.get_plugin_instance()
            if hasattr(instance, 'search_fields'):
                text += ' '.join(getattr(instance, field)
                                    for field in instance.search_fields)
        return html2text(text)

    def prepare_title(self, obj):
        "Fetch title for indexing"
        try:
            title, = Title.objects.values('title').filter(page_id=obj.pk)
            return title['title']
        except:
            return ""

    def prepare_model_type(self, obj):
        "Fetch model"
        return "Page"

    def should_update(self, obj):
        "Checks if record 'obj' be indexed or not"
        return obj.published and (not obj.publisher_is_draft)
