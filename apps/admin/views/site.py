# -*- coding: utf-8 -*-
"""
    admin.views.site

    Site View

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.shortcuts import render


def home(request):
    "Render site home page"
    return render(request, "home.html")


def contact_us(request):
    "Render contact us page"
    return render(request, "contact.html")
