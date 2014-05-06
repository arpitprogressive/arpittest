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
    version='1.5',
    description='Django - Pursuite',
    author='Openlabs Technologies & Consulting (P) Limited',
    author_email='info@openlabs.co.in',
    url='http://www.openlabs.co.in',
    install_requires=[
        'django>=1.5,<1.6',
        'mysql-python',
        'django-tinymce',
        'django-cms>=2.4,<2.5',
        'django-hvad',
        'django-reversion',
        'djangocms_admin_style',
        'PIL',
        'django-haystack',
        'pyelasticsearch',
        'html2text',
        'requests>1.0,<2.0',
        'django-allauth',
        'requests_oauthlib>0.3,<0.4',
        'sphinx',
        'raven',
        'nltk',
        'jinja2',
        'django-pagination',
        'django-storages',
        'boto',
        'django-s3-folder-storage',
    ],
)
