# -*- coding: utf-8 -*-
"""
    analytics.views

    Views for analytics

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import json
from django.template import Context
from django.http import HttpResponse
from django.db import connection
from django.template import RequestContext
from django.shortcuts import render_to_response


def get_latest_year():
    return '2013'


def home(request):
    "Main analytics page"
    year = int(get_latest_year())
    c = Context({
        'analytics_year': year
    })
    return render_to_response('analytics.html', c,
            context_instance=RequestContext(request))


def demand_supply_by_state(request, year):
    "Returns a list of states"
    cursor = connection.cursor()
    cursor.execute('''
        SELECT DemandT.year AS year,
           StateT.id AS state_id,
           StateT.name AS state,
           sum(DemandT.demand) AS demand
        FROM analytics_demanddata AS DemandT,
             analytics_state AS StateT,
             analytics_city AS CityT
        WHERE year = %d AND CityT.id = DemandT.city_id
                        AND CityT.state_id = StateT.id
        GROUP BY state;
    ''' % int(year))

    states = {}
    demand_data = {}
    for _, state_id, state, demand in cursor.fetchall():
        demand = int(demand)
        demand_data[state] = demand
        states[state] = state_id

    cursor.execute('''
        SELECT SupplyT.year AS year,
            StateT.name AS state,
            sum(SupplyT.supply) AS supply
        FROM analytics_supplybase AS SupplyT,
            analytics_state AS StateT,
            analytics_city AS CityT
        WHERE year = %d AND CityT.id = SupplyT.city_id
                        AND CityT.state_id = StateT.id
        GROUP BY state;
    ''' % int(year))

    supply_data = {}
    for _, state, supply in cursor.fetchall():
        supply = int(supply)
        supply_data[state] = supply

    return HttpResponse(json.dumps({
        'year': year,
        'states': states,
        'demand_data': demand_data,
        'supply_data': supply_data,
    }))


def demand_supply_in_state(request, year, state_id):
    "Returns a list of states"
    cursor = connection.cursor()
    cursor.execute('''
        SELECT DemandT.year AS year,
           CityT.name AS city,
           CityT.id AS city_id,
           sum(DemandT.demand) AS demand
        FROM analytics_demanddata AS DemandT,
             analytics_city AS CityT
        WHERE year = '%d' AND CityT.state_id = '%d'
                          AND CityT.id = DemandT.city_id
        GROUP BY DemandT.city_id;
    ''' % (int(year), int(state_id),))

    cities = {}
    demand_data = {}
    for _, city, city_id, demand in cursor.fetchall():
        demand = int(demand)
        demand_data[city] = demand
        cities[city] = city_id

    cursor.execute('''
        SELECT DemandT.year AS year,
           CityT.name AS city,
           sum(DemandT.demand) AS demand
        FROM analytics_demanddata AS DemandT,
             analytics_city AS CityT
        WHERE year = '%d' AND CityT.state_id = '%d'
                          AND CityT.id = DemandT.city_id
        GROUP BY DemandT.city_id;
    ''' % (int(year), int(state_id),))

    supply_data = {}
    for _, city, supply in cursor.fetchall():
        supply = int(supply)
        supply_data[city] = supply

    return HttpResponse(json.dumps({
        'year': year,
        'state_id': state_id,
        'cities': cities,
        'demand_data': demand_data,
        'supply_data': supply_data,
    }))
