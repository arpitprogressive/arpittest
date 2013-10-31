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

from analytics.models import State, City, DemandData, SupplyBase
from admin.models import SubSector


def home(request):
    "Home page. What to show?"
    demand_years = sorted([
        k['year'] for k in DemandData.objects.values('year').distinct()
    ], reverse=True)
    supply_years = sorted([
        k['year'] for k in SupplyBase.objects.values('year').distinct()
    ], reverse=True)

    c = Context({
        'analytics_demand_years': demand_years,
        'analytics_supply_years': supply_years
    })
    return render_to_response('analytics.html', c,
            context_instance=RequestContext(request))


def demand(request, year):
    "Main demand page"
    year = int(year)
    c = Context({
        'analytics_year': year
    })
    return render_to_response('demand.html', c,
            context_instance=RequestContext(request))


def supply(request, year):
    "Main supply page"
    year = int(year)
    c = Context({
        'analytics_year': year
    })
    return render_to_response('supply.html', c,
            context_instance=RequestContext(request))


def demand_by_state(request, year):
    "Returns a list of states and their demand"
    year = int(year)

    cursor = connection.cursor()
    cursor.execute('''
        SELECT DemandT.year AS year,
           StateT.id AS state_id,
           StateT.name AS state,
           sum(DemandT.demand) AS demand
        FROM analytics_demanddata AS DemandT,
             analytics_state AS StateT,
             analytics_city AS CityT
        WHERE year = %s AND CityT.id = DemandT.city_id
                        AND CityT.state_id = StateT.id
        GROUP BY state;
    ''', (year,))

    states = {}
    demand_data = {}
    for _, state_id, state, demand in cursor.fetchall():
        demand = int(demand)
        demand_data[state] = demand
        states[state] = state_id

    return HttpResponse(json.dumps({
        'year': year,
        'states': states,
        'data': demand_data,
    }), content_type='text/json')


def demand_in_state(request, year, state_id):
    "Returns complete JSON data to drilldown in given state"
    year = int(year)
    state_id = int(state_id)
    state_name = State.objects.get(pk=state_id).name

    cursor = connection.cursor()
    cursor.execute('''
        SELECT
            DemandT.city_id AS city_id,
            CityT.name AS city,
            sum(demand) AS demand
        FROM
            analytics_demanddata AS DemandT,
            analytics_city AS CityT,
            analytics_state AS StateT
        WHERE
            DemandT.year = %s AND
            StateT.id = %s AND
            CityT.state_id = StateT.id AND
            DemandT.city_id = CityT.id
        GROUP BY city_id;
    ''', (year, state_id))

    cities = []
    data = []

    for city_id, city, demand in cursor.fetchall():
        cities.append(city)
        data.append({
            'y': int(demand),
            'drilldown': _demand_subsector(year, int(city_id))
        })

    json_data = {
        'name': "Demand in %s (%d)" % (state_name, year),
        'categories': cities,
        'data': data,
    }

    return HttpResponse(json.dumps({
        'year': year,
        'state': state_name,
        'data': json_data,
    }), content_type='text/json')


def _demand_subsector(year, city_id):
    "Return drilldown JSON data for given subsector"

    city = City.objects.get(pk=city_id)
    city_name = city.name
    state_name = city.state.name

    cursor = connection.cursor()
    cursor.execute('''
        SELECT
            SubSectorT.id AS subsector_id,
            SubSectorT.name AS subsector,
            sum(demand) AS demand
        FROM
            analytics_demanddata AS DemandT,
            admin_subsector AS SubSectorT,
            admin_occupation AS OccupationT
        WHERE
            DemandT.year = %s AND
            DemandT.city_id = %s AND
            OccupationT.id = DemandT.occupation_id AND
            SubSectorT.id = OccupationT.sub_sector_id
        GROUP BY subsector_id;
    ''', (year, city_id))

    subsectors = []
    data = []

    for subsector_id, subsector, demand in cursor.fetchall():
        subsectors.append(subsector)
        data.append({
            'y': int(demand),
            'drilldown': _demand_occupation(year, city_id, int(subsector_id))
        })

    json_data = {
        'name': "Demand in %s, %s (%d) by Sub Sector" %
                        (city_name, state_name, year),
        'categories': subsectors,
        'data': data,
    }
    return json_data


def _demand_occupation(year, city_id, subsector_id):
    "Return drilldown JSON data for given subsector"

    city = City.objects.get(pk=city_id)
    city_name = city.name
    state_name = city.state.name
    subsector_name = SubSector.objects.get(pk=subsector_id).name

    cursor = connection.cursor()
    cursor.execute('''
        SELECT
            DemandT.occupation_id AS occupation_id,
            OccupationT.name AS occupation,
            sum(demand) AS demand
        FROM
            analytics_demanddata AS DemandT,
            admin_subsector AS SubSectorT,
            admin_occupation AS OccupationT
        WHERE
            DemandT.year = %s AND
            DemandT.city_id = %s AND
            SubSectorT.id = %s AND
            OccupationT.id = DemandT.occupation_id
        GROUP BY occupation_id;
    ''', (year, city_id, subsector_id))

    occupations = []
    data = []

    for occupation_id, occupation, demand in cursor.fetchall():
        occupations.append(occupation)
        data.append({
            'y': int(demand)
        })

    json_data = {
        'name': "Demand in %s, %s (%d) by Occupations for %s" %
                        (city_name, state_name, year, subsector_name),
        'categories': occupations,
        'data': data,
    }
    return json_data


def supply_by_state(request, year):
    "Returns a list of states and their supply"
    year = int(year)

    cursor = connection.cursor()
    cursor.execute('''
        SELECT SupplyT.year AS year,
            StateT.id AS state_id,
            StateT.name AS state,
            sum(SupplyT.supply) AS supply
        FROM analytics_supplybase AS SupplyT,
            analytics_state AS StateT,
            analytics_city AS CityT
        WHERE year = %s AND CityT.id = SupplyT.city_id
                        AND CityT.state_id = StateT.id
        GROUP BY state;
    ''', (year,))

    states = {}
    supply_data = {}
    for _, state_id, state, supply in cursor.fetchall():
        supply = int(supply)
        supply_data[state] = supply
        states[state] = state_id

    return HttpResponse(json.dumps({
        'year': year,
        'states': states,
        'data': supply_data,
    }), content_type='text/json')


def supply_in_state(request, year, state_id):
    "Returns complete JSON data to drilldown in given state"
    year = int(year)
    state_id = int(state_id)
    state_name = State.objects.get(pk=state_id).name

    cursor = connection.cursor()
    cursor.execute('''
        SELECT
            SupplyT.city_id AS city_id,
            CityT.name AS city,
            sum(supply) AS supply
        FROM
            analytics_supplybase AS SupplyT,
            analytics_city AS CityT,
            analytics_state AS StateT
        WHERE
            SupplyT.year = %s AND
            StateT.id = %s AND
            CityT.state_id = StateT.id AND
            SupplyT.city_id = CityT.id
        GROUP BY city_id;
    ''', (year, state_id))

    cities = []
    data = []

    for city_id, city, supply in cursor.fetchall():
        cities.append(city)
        data.append({
            'y': int(supply),
            'drilldown': _supply_subsector(year, int(city_id))
        })

    json_data = {
        'name': "Supply in %s (%d)" % (state_name, year),
        'categories': cities,
        'data': data,
    }

    return HttpResponse(json.dumps({
        'year': year,
        'state': state_name,
        'data': json_data,
    }), content_type='text/json')


def _supply_subsector(year, city_id):
    "Return drilldown JSON data for given subsector"

    city = City.objects.get(pk=city_id)
    city_name = city.name
    state_name = city.state.name

    cursor = connection.cursor()
    cursor.execute('''
        SELECT
            SubSectorT.id AS subsector_id,
            SubSectorT.name AS subsector,
            sum(supply) AS supply
        FROM
            analytics_supplybase AS SupplyT,
            admin_subsector AS SubSectorT,
            admin_occupation AS OccupationT
        WHERE
            SupplyT.year = %s AND
            SupplyT.city_id = %s AND
            OccupationT.id = SupplyT.occupation_id AND
            SubSectorT.id = OccupationT.sub_sector_id
        GROUP BY subsector_id;
    ''', (year, city_id))

    subsectors = []
    data = []

    for subsector_id, subsector, supply in cursor.fetchall():
        subsectors.append(subsector)
        data.append({
            'y': int(supply),
            'drilldown': _supply_occupation(year, city_id, int(subsector_id))
        })

    json_data = {
        'name': "Supply in %s, %s (%d) by Sub Sector" %
                        (city_name, state_name, year),
        'categories': subsectors,
        'data': data,
    }
    return json_data


def _supply_occupation(year, city_id, subsector_id):
    "Return drilldown JSON data for given subsector"

    city = City.objects.get(pk=city_id)
    city_name = city.name
    state_name = city.state.name
    subsector_name = SubSector.objects.get(pk=subsector_id).name

    cursor = connection.cursor()
    cursor.execute('''
        SELECT
            SupplyT.occupation_id AS occupation_id,
            OccupationT.name AS occupation,
            sum(supply) AS supply
        FROM
            analytics_supplybase AS SupplyT,
            admin_subsector AS SubSectorT,
            admin_occupation AS OccupationT
        WHERE
            SupplyT.year = %s AND
            SupplyT.city_id = %s AND
            SubSectorT.id = %s AND
            OccupationT.id = SupplyT.occupation_id
        GROUP BY occupation_id;
    ''', (year, city_id, subsector_id))

    occupations = []
    data = []

    for occupation_id, occupation, supply in cursor.fetchall():
        occupations.append(occupation)
        data.append({
            'y': int(supply)
        })

    json_data = {
        'name': "Supply in %s, %s (%d) by Occupations for %s" %
                        (city_name, state_name, year, subsector_name),
        'categories': occupations,
        'data': data,
    }
    return json_data
