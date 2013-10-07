# -*- coding: utf-8 -*-
"""
    admin.models.validators

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
import re

from django.core.exceptions import ValidationError

__all__ = ['validate_os_code', 'validate_qp_code', 'validate_version']


def validate_os_code(value):
    '''
        Validate occupational standard code
    '''
    if not re.match(r'^[A-z]{3}/[NO]\d{4}$', value):
        raise ValidationError(
            u"Invalid Format. Example: SSC/O0101 or SSC/N0101"
        )


def validate_qp_code(value):
    '''
        Validate qualification pack code
    '''
    if not re.match(r'^[A-z]{3}/Q\d{4}$', value):
        raise ValidationError(u"Invalid Format. Example: SSC/Q0101")


def validate_version(value):
    '''
        Validate code
    '''
    if not re.match(r'^~{0,1}\d+\.\d+$', value):
        raise ValidationError(u"Invalid Format. Example: 0.1")
