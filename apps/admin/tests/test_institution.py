# -*- coding: utf-8 -*-
"""
    admin.tests.test_institution

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.test import TestCase
from admin.models import Institution


class TestInstitution(TestCase):
    '''
        Test Institution
    '''
    def test_creation(self):
        '''
            Test creation of record
        '''
        institute = Institution(
            name='ABC Institute',
            url='http://openlabs.co.in',
        )
        institute.save()
        self.assert_(institute.pk)
