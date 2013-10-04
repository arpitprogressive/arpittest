# -*- coding: utf-8 -*-
"""
    admin.models.validators

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
import re

from django.core.exceptions import ValidationError

__all__ = ['validate_code', 'validate_version']


def validate_code(value):
    '''
        Validate code
    '''
    if not re.match(r'^[A-z]{3}/[A-z]\d{4}$', value):
        raise ValidationError(u"Invalid Format. Example: SSC/O2951")


def validate_version(value):
    '''
        Validate code
    '''
    if not re.match(r'^~{0,1}\d+\.\d+$', value):
        raise ValidationError(u"Invalid Format. Example: 0.1")
