# -*- coding: utf-8 -*-
"""
    analytics.urls

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from django.conf.urls import url, patterns

urlpatterns = patterns('analytics.views',
    url(r'^$', 'home'),

    url(r'^data/states/(?P<year>\d{4})$', 'demand_supply_by_state'),
    url(r'^data/states/(?P<year>\d{4})/(?P<state_id>\d+)/$',
            'demand_supply_in_state')
)
