# -*- coding: utf-8 -*-
"""
    admin.views.common

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from admin.models.sector import SubSector
from admin.models.occupation import Occupation
from admin.models.qualification_pack import QualificationPack
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.utils import simplejson


@cache_page(500)
def wfmis_json(request):
    """
    Returns json for WFSMIS

    :param request: request object
    """
    response = {}
    sub_sectors = SubSector.objects.all()
    occupations = Occupation.objects.all()
    qualification_packs = QualificationPack.objects.filter(is_draft=False).all()
    response["sub-sectors"] = [
        {
            'name': sub_sector.name,
            'sector': sub_sector.sector.name,
            'code': sub_sector.pk,
        }
        for sub_sector in sub_sectors
    ]
    response["occupations"] = [
        {
            'name': occupation.name,
            'sub-sector': occupation.sub_sector.pk,
            'code': occupation.pk,
        }
        for occupation in occupations
    ]
    response["job-roles"] = [
        {
            'name': qp.job_role,
            'occupation': qp.occupation.pk,
            'url': qp.get_absolute_url(),
        }
        for qp in qualification_packs
    ]
    return HttpResponse(simplejson.dumps(response))
