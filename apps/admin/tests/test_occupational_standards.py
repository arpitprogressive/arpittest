# -*- coding: utf-8 -*-
"""
    test_occupational_standards

    Tests for occupational standards

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from datetime import datetime

from django.test import TestCase
from admin.models import OccupationalStandard, Sector, SubSector


class TestOccupationalStandard(TestCase):
    """
        Test occupational standard
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

        # Create an Occupational Standard
        os_ = OccupationalStandard.objects.create(
            code="SSC/Q2601",
            sector=sector,
            sub_sector=sub_sector,
            title="test title",
            scope="test scope",
            description="test description",
            version="0.1",
            drafted_on=datetime.today().date(),
            last_reviewed_on=datetime.today().date(),
            next_review_on=datetime.today().date(),
            performace_criteria="test performance",
            knowledge="test knowledge",
            skills="test skills",
        )
        self.assert_(os_.pk)
        return {
            'os': os_,
            'sector': sector,
            'sub_sector': sub_sector,
        }

    def test_creation(self):
        '''
            Test creation of record
        '''
        self.create_defaults()
