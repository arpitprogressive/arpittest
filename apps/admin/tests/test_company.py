# -*- coding: utf-8 -*-
"""
    admin.tests.test_company

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.test import TestCase
from admin.models import Company
from django.core.exceptions import ValidationError


class TestCompany(TestCase):
    '''
        Test Company and Training providers
    '''
    def create_defaults(self):
        '''
            Create defaults for test
        '''
        # Create non nasscom member
        company = Company(
            name='Openlabs',
            url='http://openlabs.co.in',
        )
        company.full_clean()  # No exception means, accepted
        company.save()
        self.assert_(company.pk)
        return {
            'company': company
        }

    def test_membership_no(self):
        '''
            Test Nasscom membership number validation
        '''
        data = self.create_defaults()
        company = data['company']

        # invalid nasscom member
        company.nasscom_membership_number = 'openlabs1800'
        self.assertRaises(ValidationError, company.full_clean)

        # valid nasscom member
        company.nasscom_membership_number = 'NSCM/2011/22/2457'
        company.full_clean()  # No exception means, accepted

    def test_training_provider(self):
        '''
            Test Training provider
        '''
        data = self.create_defaults()
        company = data['company']

        company.training_provider = 'LTP'
        company.full_clean()  # No exception means, accepted
        company.save()
