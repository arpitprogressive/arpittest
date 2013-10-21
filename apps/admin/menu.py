# -*- coding: utf-8 -*-
"""
    admin.menu

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from menus.base import Modifier
from menus.menu_pool import menu_pool
from cms.models.pagemodel import Page


class NodeModifier(Modifier):
    "NodeModifier"
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        """
        Add attribute to point to page instance in NavigationMode
        """
        for node in nodes:
            node.page = Page.objects.filter(pk=node.id)[0]
        return nodes

menu_pool.register_modifier(NodeModifier)
