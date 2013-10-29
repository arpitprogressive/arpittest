# -*- coding: utf-8 -*-
"""
    analytics.tests

    Tests for analytics

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""


from django.test import TestCase
from admin.models import Sector, SubSector, Occupation, Institution
from analytics.models import State, City, SupplyBase


class TestModels(TestCase):
    def create_defaults(self):
        """
        Tests creation of records
        """

        state_delhi = State(name='Delhi', region='NORTH')
        state_delhi.save()
        self.assert_(state_delhi)
        self.assert_(state_delhi.pk)

        city_newdelhi = City(name='New Delhi', state=state_delhi)
        city_newdelhi.save()
        self.assert_(city_newdelhi.pk)

        sector_it = Sector(name='IT')
        sector_it.save()
        self.assert_(sector_it.pk)

        subsector_services = SubSector(name='Services', sector=sector_it)
        subsector_services.save()
        self.assert_(subsector_services.pk)

        occupation = Occupation.objects.create(
            name="Test Occup",
            sub_sector=subsector_services
        )
        occupation.save()
        self.assert_(occupation.pk)

        institute = Institution(
            name='ABC Institute',
            url='http://openlabs.co.in',
        )
        institute.save()
        self.assert_(institute.pk)

        supplybase = SupplyBase(
            year=2008,
            city=city_newdelhi,
            occupation=occupation,
            institution=institute,
            degree='PG',
            supply=100,
        )
        supplybase.save()
        self.assert_(supplybase.pk)

    def test_create(self):
        self.create_defaults()
