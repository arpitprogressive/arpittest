# -*- coding: utf-8 -*-
"""
    admin.common

    Common utility functions

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""

import nltk

from cms.models.pagemodel import Page
from django.core.exceptions import ObjectDoesNotExist


def html2text(html):
    """
    Convert HTML to Text
    """
    return nltk.clean_html(html)


def get_cms_page_url(reverse_id):
    '''
        Return absolute_url for cms page reverse id.

        :return: url string
    '''
    pages = Page.objects.filter(reverse_id=reverse_id)
    if not pages:
        raise ObjectDoesNotExist
    return pages[0].get_absolute_url()
