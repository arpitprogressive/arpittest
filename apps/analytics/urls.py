# -*- coding: utf-8 -*-
"""
    analytics.urls

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from django.conf.urls import url, patterns

urlpatterns = patterns('analytics.views',
    url(r'^$', 'home'),

    url(r'^demand/(?P<year>\d{4})$', 'demand'),
    url(r'^data/demand/(?P<year>\d{4})$', 'demand_by_state'),
    url(r'^data/demand/(?P<year>\d{4})/(?P<state_id>\d+)$',
        'demand_in_state'),

    url(r'^supply/(?P<year>\d{4})$', 'supply'),
    url(r'^data/supply/(?P<year>\d{4})$', 'supply_by_state'),
    url(r'^data/supply/(?P<year>\d{4})/(?P<state_id>\d+)$',
        'supply_in_state'),
)
