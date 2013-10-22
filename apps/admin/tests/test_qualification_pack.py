# -*- coding: utf-8 -*-
"""
    admin.tests.test_qualification_pack

    Tests for qualification pack

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from datetime import datetime

from django.test import TestCase
from django.core.management import call_command
from haystack.query import SearchQuerySet
from admin.models import OccupationalStandard, Sector, SubSector, \
    QualificationPack, Occupation


class TestQualificationPack(TestCase):
    """
        Test qualification pack
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

        # Create an Occupational Standard
        os_ = OccupationalStandard.objects.create(
            code="SSC/O2601",
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
        qp = QualificationPack.objects.create(
            code="SSC/Q0101",
            version="0.1",
            occupation=occupation,
            job_role="Associate - CRM",
            alias="Customer Service Associate",
            role_description="test description",
            nveqf_level="4-9",
            min_educational_qualification="12th",
            max_educational_qualification="Master's in any discipline",
            training="test training",
            experience="0-1 year of work experience/internship",
            next_review_on=datetime.today().date(),
        )
        self.assert_(qp.pk)
        qp.os_compulsory.add(os_)
        self.assertTrue(os_ in qp.os_compulsory.all())
        return {
            'os': os_,
            'sector': sector,
            'sub_sector': sub_sector,
            'qp': qp,
            'occupation': occupation,
        }

    def test_creation(self):
        '''
            Test creation of record
        '''
        self.create_defaults()

    def test_haystack(self):
        '''
            Test creation of record
        '''
        defaults = self.create_defaults()
        sub_sector = defaults['sub_sector']
        occupation = defaults['occupation']

        OccupationalStandard.objects.create(
            code="SSC/O2602",
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
        QualificationPack.objects.create(
            code="SSC/Q0102",
            version="0.1",
            occupation=occupation,
            job_role="Associate - CRM",
            alias="Customer Service Associate",
            role_description="test description",
            nveqf_level="4-9",
            min_educational_qualification="12th",
            max_educational_qualification="Master's in any discipline",
            training="test training",
            experience="0-1 year of work experience/internship",
            next_review_on=datetime.today().date(),
            is_draft=False,
        )

        call_command('rebuild_index', verbosity=1, interactive=False)
        self.assertEqual(len(SearchQuerySet().all()), 2)
        self.assertEqual(len(SearchQuerySet().filter(content='Associate')), 1)
