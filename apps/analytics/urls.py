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

    ######################## Demand Analytics ########################

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

    url(r'^demand-1/(?P<year>\d{4})', 'demand_1', name='demand_1'),

    ########  Analytics #4 ########
    url(r'^data/demand-supply-region/(?P<year>\d{4})$',
        'demand_supply_region', name='demand_supply_region'),
    url(r'^data/it-spend/(?P<year>\d{4})$',
        'it_spend', name='it_spend'),

    url(r'^demand-4/(?P<year>\d{4})', 'demand_4', name='demand_4'),

    ########  Analytics #5 ########
    url(r'^data/diversity-ratio-subsector/(?P<year>\d{4})',
        'diversity_ratio_subsector', name='diversity_ratio_subsector'),
    url(r'^data/diversity-ratio-level/(?P<year>\d{4})', 'diversity_ratio_level',
        name='diversity_ratio_level'),
    url(r'^demand-5/(?P<year>\d{4})', 'demand_5', name='demand_5'),

    ######################## Supply Analytics ########################

    ########  Analytics #1 ########
    url(r'^data/university-in-states$',
        'university_in_states', name='university_in_states'),
    url(r'^supply-1$', 'supply_1', name='supply_1'),

    ########  Analytics #3 ########
    url(r'^data/gender-diversity/(?P<year>\d{4})',
        'gender_diversity_data', name='gender_diversity_data'),
    url(r'^supply-3/(?P<year>\d{4})', 'supply_3', name='supply_3'),

    ########  Analytics #5 ########
    url(r'^data/supply-split-stream-trend',
        'supply_split_stream_trend', name='supply_split_stream_trend'),
    url(r'^supply-5/(?P<year>\d{4})', 'supply_5', name='supply_5'),
)
