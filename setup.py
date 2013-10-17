#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    setup

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from setuptools import setup

setup(
    name='Pursuite',
    version='0.1',
    description='Django - Pursuite',
    author='Openlabs Technologies & Consulting (P) Limited',
    author_email='info@openlabs.co.in',
    url='http://www.openlabs.co.in',
    install_requires=[
        'django>=1.5,<1.6',
        'mysql-python',
        'django-tinymce',
        'django-cms',
        'django-hvad',
        'django-reversion',
        'djangocms_admin_style',
        'PIL',
        'django-haystack',
        'pyelasticsearch',
        'html2text',
        'sphinx',
        'raven',
    ],
)
