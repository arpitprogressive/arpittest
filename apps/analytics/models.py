# -*- coding: utf-8 -*-
"""
    analytics.models

    Models for Demand and Supply data

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""


from django.db import models
import django.contrib.admin

from admin.models import Occupation, Institution, Company, SubSector


__all__ = ['DEGREE_CHOICES', 'REGION_CHOICES', 'State', 'City', 'SupplyBase',
        'DemandData', 'CompanyYearData', 'DiversityRatioLevel',
        'DiversityRatioSubsector', 'GenderDiversity', 'ITSpend',
        'RevenueSubsector', 'RevenueOccupation', 'RevenueTotal']


DEGREE_CHOICES = (
    ('UG', 'Undergraduate Degree'),
    ('PG', 'Postgraduate Degree'),
    ('DOC', 'Ph.D/M.Phil'),
    ('PSD', 'Post School Diploma'),
    ('PGD', 'Post Graduate Diploma'),
    ('UNK', 'Unknown'),
)


REGION_CHOICES = (
    ('NORTH', 'North'),
    ('SOUTH', 'South'),
    ('EAST', 'East'),
    ('WEST', 'West'),
    ('CENTRAL', 'Central'),
)


class State(models.Model):
    """
    States
    """
    name = models.CharField(max_length=50, default=None, unique=True)
    region = models.CharField(max_length=12, choices=REGION_CHOICES)

    class Meta:
        unique_together = ('name', 'region',)

    def __unicode__(self):
        """
        Returns object display name
        """
        return self.name


class City(models.Model):
    """
    Cities
    """
    name = models.CharField(max_length=50, default=None)
    state = models.ForeignKey('State')

    class Meta:
        unique_together = ('name', 'state',)
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%s,%s" % (self.name, self.state)


class SupplyBase(models.Model):
    """
    Demand supply data
    """
    year = models.IntegerField()
    city = models.ForeignKey('City')
    occupation = models.ForeignKey(Occupation)
    institution = models.ForeignKey(Institution)
    degree = models.CharField(max_length=3, choices=DEGREE_CHOICES,
            default=None)
    supply = models.IntegerField()

    class Meta:
        unique_together = ('year', 'city', 'occupation', 'institution',
                'degree',)
        verbose_name_plural = 'SupplyBase'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s,%s" % (self.year, self.city, self.occupation,)


class DemandData(models.Model):
    """
    Demand data
    """
    year = models.IntegerField()
    city = models.ForeignKey('City')
    occupation = models.ForeignKey(Occupation)
    company = models.ForeignKey(Company)
    demand = models.IntegerField()
    headcount = models.IntegerField()

    class Meta:
        unique_together = ('year', 'city', 'occupation', 'company',)
        verbose_name_plural = 'DemandBase'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s,%s" % (self.year, self.city, self.occupation,)


class CompanyYearData(models.Model):
    """
    Revenue, Headcount data for companies annually
    """
    year = models.IntegerField()
    company = models.ForeignKey(Company)
    revenue = models.IntegerField()

    class Meta:
        unique_together = ('year', 'company', )
        verbose_name_plural = 'Company Annual Data'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s" % (self.year, self.company, )


class DiversityRatioLevel(models.Model):
    """
    Diversity ratio for levels
    """
    year = models.IntegerField(unique=True)
    male_leadership = models.IntegerField(
        verbose_name='Percent Male in Leadership roles'
    )
    male_entry = models.IntegerField(
        verbose_name='Percent Male in Entry Level roles'
    )
    male_middle = models.IntegerField(
        verbose_name='Percent Male in Middle Level roles'
    )

    @property
    def female_leadership(self):
        "Percent Females in leadership level roles"
        return 100 - self.male_leadership

    @property
    def female_entry(self):
        "Percent Females in entry level roles"
        return 100 - self.male_entry

    @property
    def female_middle(self):
        "Percent Females in middle level roles"
        return 100 - self.male_middle

    class Meta:
        verbose_name_plural = 'Diversity Ratio for Experience Levels'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d" % (self.year, )


class DiversityRatioSubsector(models.Model):
    """
    Diversity ratio for subsector
    """
    year = models.IntegerField()
    subsector = models.ForeignKey(SubSector, verbose_name='Sub-sector')
    male = models.IntegerField(verbose_name='Percent males in subsector')

    @property
    def female(self):
        "Percent Females in subsector"
        return 100 - self.male

    class Meta:
        unique_together = ('year', 'subsector', )
        verbose_name_plural = 'Diversity Ratio for Subsector'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d, %s" % (self.year, self.subsector, )


class GenderDiversity(models.Model):
    """
    Gender diversity as per course
    """
    year = models.IntegerField()
    category = models.CharField(max_length=60)
    male = models.IntegerField()

    class Meta:
        unique_together = ('year', 'category', )
        verbose_name_plural = 'Gender Diversity'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s" % (self.year, self.category, )


class ITSpend(models.Model):
    """
    IT Spend data
    """
    year = models.IntegerField()
    sub_sector = models.ForeignKey(SubSector, verbose_name='Sub-sector')
    world_spend = models.IntegerField(verbose_name='World IT Spend')
    india_revenue = models.IntegerField(verbose_name='Indian IT Revenue')

    class Meta:
        unique_together = ('year', 'sub_sector', )
        verbose_name_plural = 'IT Spend'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s" % (self.year, self.sub_sector, )


class RevenueSubsector(models.Model):
    """
    Revenue per subsector
    """
    year = models.IntegerField()
    sub_sector = models.ForeignKey(SubSector)
    revenue = models.IntegerField()

    class Meta:
        unique_together = ('year', 'sub_sector', )
        verbose_name_plural = 'Revenue by Subsector'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s" % (self.year, self.sub_sector, )


class RevenueOccupation(models.Model):
    """
    Revenue by occupation
    """
    year = models.IntegerField()
    occupation = models.ForeignKey(Occupation)
    revenue = models.IntegerField()
    cagr_next_7_years = models.IntegerField(
        verbose_name='CAGR % for next 7 years'
    )

    class Meta:
        unique_together = ('year', 'occupation', )
        verbose_name_plural = 'Revenue by occupation'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%s" % (self.year, self.occupation, )

    @property
    def revenue_after_7year(self):
        return int(self.revenue * (1 + self.cagr_next_7_years / 100.0) ** 7)


class RevenueTotal(models.Model):
    """
    Total revenue
    """
    year = models.IntegerField(unique=True)
    revenue = models.IntegerField()
    most_likely_growth = models.IntegerField(
        verbose_name='Most likely growth percent',
        blank=True,
        null=True
    )
    optimistic_growth = models.IntegerField(
        verbose_name='Optimisitc growth percent',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = 'Total Revenues'

    def __unicode__(self):
        """
        Returns object display name
        """
        return "%d,%d" % (self.year, self.revenue, )

    @property
    def growth_series(self):
        """
        Return growth and most likely series
        """
        resultset = RevenueTotal.objects.filter(year__lte=self.year)
        optimistic_series = []
        most_likely_series = []
        years = []
        for result in resultset:
            most_likely_series.append(result.revenue)
            optimistic_series.append(result.revenue)
            years.append(result.year)

        for i in range(7):
            optimistic_series.append(
                int(optimistic_series[-1] *
                        (1 + self.optimistic_growth / 100.0))
            )
            most_likely_series.append(
                int(most_likely_series[-1] *
                    (1 + self.most_likely_growth / 100.0))
            )
            years.append(years[-1] + 1)

        return {
            'years': years,
            'optimistic_series': optimistic_series,
            'most_likely_series': most_likely_series,
        }


django.contrib.admin.site.register(State)
django.contrib.admin.site.register(City)
django.contrib.admin.site.register(SupplyBase)
django.contrib.admin.site.register(DemandData)
django.contrib.admin.site.register(CompanyYearData)
django.contrib.admin.site.register(DiversityRatioLevel)
django.contrib.admin.site.register(DiversityRatioSubsector)
django.contrib.admin.site.register(GenderDiversity)
django.contrib.admin.site.register(ITSpend)
django.contrib.admin.site.register(RevenueSubsector)
django.contrib.admin.site.register(RevenueOccupation)
django.contrib.admin.site.register(RevenueTotal)
