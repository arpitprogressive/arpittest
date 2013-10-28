# -*- coding: utf-8 -*-
"""
    admin.common

    Common utility functions

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""

import nltk


def html2text(html):
    """
    Convert HTML to Text
    """
    return nltk.clean_html(html.encode('utf-8'))
