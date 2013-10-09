# -*- coding: utf-8 -*-
"""
    admin.tests.test_company

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.test import TestCase
from admin.models import Company


class TestCompany(TestCase):
    '''
        Test Company and Training providers
    '''
    def test_creation(self):
        '''
            test creation of company and training providers
        '''
        # Create non nasscom member
        company = Company(
            name='Openlabs',
            url='http://openlabs.co.in',
        )
        company.save()
        self.assert_(company.pk)

        # make it nasscom member
        company.nasscom_membership_number = 'openlabs1800'
        company.save()
        self.assert_(company.nasscom_membership_number)

        # make it LTP
        company.training_provider = 'LTP'
        company.save()
        self.assert_(company.training_provider)
