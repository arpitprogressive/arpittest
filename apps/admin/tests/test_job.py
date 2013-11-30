# -*- coding: utf-8 -*-
"""
    admin.tests.test_job

    Tests for jobs

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from datetime import datetime
from django.test import TestCase
from admin.models import Job, QualificationPack, Sector, SubSector, Occupation,\
        Company, OccupationalStandard
from django.contrib.auth.models import User
from account.models import UserProfile, IndustryProfile
from analytics.models import State


class TestJob(TestCase):
    """
        Test job
    """
    def create_defaults(self):
        """
            Create default for test
        """
        # Create User
        user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword'
        )
        userprofile = UserProfile.objects.create(
            role='S',
            user=user,
        )

        # Create State
        state = State.objects.create(name='Delhi', region="Nort")

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

        # Create non nasscom member
        company = Company(
            name='Openlabs',
            url='http://openlabs.co.in',
        )
        company.full_clean()  # No exception means, accepted
        company.save()
        self.assert_(company.pk)

        industry_profile = IndustryProfile.objects.create(
            user_profile=userprofile,
            name='test name',
            est_year=2013,
            industry_type="O",
            sub_sector="IT-ITeS",
            contact_person="Cyrus",
            email="cyrus@ol.com",
            mobile_phone="9874563210",
            company=company,
            is_approved=True,
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
            'company': company,
            'state': state,
            'industry_profile': industry_profile,
        }

    def test_creation(self):
        '''
            Test creation of record
        '''
        defaults = self.create_defaults()
        job = Job.objects.create(
            job_title="Software Engineer",
            is_internship=False,
            job_role=defaults['qp'],
            job_description="test description",
            location=defaults['state'],
            industry=defaults['industry_profile'],
        )
        self.assert_(job.pk)
