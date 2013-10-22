# -*- coding: utf-8 -*-
"""
    test_occupational_standards

    Tests for occupational standards

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from datetime import datetime

from django.test import TestCase
from django.core.management import call_command
from haystack.query import SearchQuerySet
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

    def test_haystack(self):
        '''
            Test Haystack full-text search
        '''
        defaults = self.create_defaults()
        sub_sector = defaults['sub_sector']

        OccupationalStandard.objects.create(
            code="SSC/Q2602",
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
            is_draft=False,
        )

        OccupationalStandard.objects.create(
            code="SSC/Q2603",
            sub_sector=sub_sector,
            title="test title with steroid",
            scope="test scope with Python",
            description="test description of superman",
            version="0.1",
            drafted_on=datetime.today().date(),
            last_reviewed_on=datetime.today().date(),
            next_review_on=datetime.today().date(),
            performace_criteria="test performance with flash",
            knowledge="test knowledge with xavior",
            skills="test skills with superman",
            is_draft=False,
        )

        call_command('rebuild_index', verbosity=1, interactive=False)
        # check total number of records indexed (is_draft=False records)
        self.assertEqual(len(SearchQuerySet().all()), 2)
        self.assertEqual(len(SearchQuerySet().filter(content='superman')), 1)
