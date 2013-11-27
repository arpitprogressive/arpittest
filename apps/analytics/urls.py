# -*- coding: utf-8 -*-
"""
    analytics.urls

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from django.conf.urls import url, patterns

urlpatterns = patterns('analytics.views',
    url(r'^$', 'home', name="analytics"),

    url(r'^demand/(?P<year>\d{4})/$', 'demand', name="demand"),
    url(r'^data/demand/(?P<year>\d{4})/$', 'demand_by_state',
        name="demand_by_state"),
    url(r'^data/demand/(?P<year>\d{4})/(?P<state_id>\d+)/$',
        'demand_in_state', name="demand_in_state"),

    url(r'^supply/(?P<year>\d{4})/$', 'supply', name="supply"),
    url(r'^data/supply/(?P<year>\d{4})/$', 'supply_by_state',
        name="supply_by_state"),
    url(r'^data/supply/(?P<year>\d{4})/(?P<state_id>\d+)/$', 'supply_in_state',
        name='supply_in_state'),

    ########  Analytics #1 ########

    #revenue
    url(r'^data/revenue-company/(?P<year>\d{4})', 'revenue_company',
        name='revenue_company'),
    url(r'^data/revenue-company-type/(?P<year>\d{4})', 'revenue_company_type',
        name='revenue_company_type'),

    # headcount and hiring
    url(r'^data/headcount-contribution/(?P<year>\d{4})',
        'headcount_contribution', name='headcount_contribution'),
    url(r'^data/hiring-contribution/(?P<year>\d{4})',
        'hiring_contribution', name='hiring_contribution'),
    url(r'^data/hiring-subsector-trend',
        'hiring_subsector_trend', name='hiring_subsector_trend'),

    url(r'^analytics-1/(?P<year>\d{4})', 'analytics1', name='analytics1'),

    ########  Analytics #5 ########
    url(r'^data/diversity-ratio-subsector/(?P<year>\d{4})',
        'diversity_ratio_subsector', name='diversity_ratio_subsector'),
    url(r'^data/diversity-ratio-level/(?P<year>\d{4})', 'diversity_ratio_level',
        name='diversity_ratio_level'),
    url(r'^diversity-ratio/(?P<year>\d{4})', 'diversity_ratio',
        name='diversity_ratio'),
)
