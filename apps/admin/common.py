# -*- coding: utf-8 -*-
"""
    admin.common

    Common utility functions

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""

import html2text as h2t


def html2text(html):
    """
    Convert HTML to Text
    """
    h = h2t.HTML2Text()
    return h.handle(html)
