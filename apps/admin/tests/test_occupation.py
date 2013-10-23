# -*- coding: utf-8 -*-
"""
    admin.tests.test_occupation

    Tests for occupation

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.test import TestCase
from admin.models import Sector, SubSector, Occupation


class TestOccupation(TestCase):
    """
        Test occupation
    """
    def create_defaults(self):
        """
            Create default for test
        """
        # Create Sector
        sector = Sector.objects.create(name="IT-ITeS")
        self.assert_(sector.pk)

        # Create Sub Sector
        sub_sector = SubSector.objects.create(
            sector=sector,
            name="Business Process Management",
        )
        self.assert_(sub_sector.pk)

        # Create Occupation
        occupation = Occupation.objects.create(
            name="Test Occupation",
            sub_sector=sub_sector,
        )
        self.assert_(occupation.pk)

        return {
            'sector': sector,
            'sub_sector': sub_sector,
            'occupation': occupation,
        }

    def test_creation(self):
        '''
            Test creation of record
        '''
        defaults = self.create_defaults()
        occupation = defaults['occupation']

        self.assertEqual(
            str(occupation),
            "IT-ITeS/Business Process Management/Test Occupation",
        )
