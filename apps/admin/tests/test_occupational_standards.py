# -*- coding: utf-8 -*-
"""
    test_occupational_standards

    Tests for occupational standards

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from datetime import datetime

from django.test import TestCase
from admin.models import OccupationalStandard, OSVersion, \
    OSPerformanceCriterion, OSKnowledgeRecord, OSSkill


class TestOccupationalStandard(TestCase):
    """
        Test occupational standard
    """
    def create_defaults(self):
        """
            Create default for test
        """
        # Create an Occupational Standard
        os_ = OccupationalStandard.objects.create(code="SSC/Q2601")
        self.assert_(os_.pk)

        # Create an Occupational Standard version
        os_version = OSVersion.objects.create(
            occupational_standard=os_,
            title="test title",
            scope="test scope",
            description="test description",
            version="0.1",
            drafted_on=datetime.today().date(),
            last_reviewed_on=datetime.today().date(),
            next_review_on=datetime.today().date(),
        )
        self.assert_(os_version.pk)
        return {
            'os': os_,
            'os_version': os_version,
        }

    def test_create_performance_criterion(self):
        """
            Test creation of performance criterion
        """
        default = self.create_defaults()
        # Create a Performance Criterion
        self.assertTrue(len(default['os_version'].performance_criteria) == 0)
        os_performance = OSPerformanceCriterion.objects.create(
            os_version=default['os_version'],
            sequence=1,
            description="dummy description",
        )
        self.assertTrue(
            os_performance in default['os_version'].performance_criteria
        )

    def test_create_knowledge_requirement(self):
        """
            Test creation of knowledge requirement for os version
        """
        default = self.create_defaults()
        # Create a Knowledge requirement
        self.assertTrue(len(default['os_version'].knowledge) == 0)
        os_knowledge = OSKnowledgeRecord.objects.create(
            os_version=default['os_version'],
            sequence=1,
            description="dummy description",
            category="OC",
        )
        self.assertTrue(os_knowledge in default['os_version'].knowledge)

    def test_create_skill_requirement(self):
        """
            Test creation of skill for os version
        """
        default = self.create_defaults()
        # Create a Skill requirement
        self.assertTrue(len(default['os_version'].skills) == 0)
        os_skill = OSSkill.objects.create(
            os_version=default['os_version'],
            title="CC",
            sequence=1,
            description="dummy description",
            category="CS",
        )
        self.assertTrue(os_skill in default['os_version'].skills)
