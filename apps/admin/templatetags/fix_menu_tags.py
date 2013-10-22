# -*- coding: utf-8 -*-
"""
    admin.fix_menu_tags

    This file is picked up from django-cms trunk version to convert root_level
    to Argument from IntegerArgument.

    Refer commit: https://github.com/divio/django-cms/commit/f6ab31697876a27ae6f3f910e06c40c0e2b25992

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""

# flake8:noqa
from __future__ import with_statement

from classytags.arguments import IntegerArgument, Argument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template
from menus.menu_pool import menu_pool


register = template.Library()

def cut_after(node, levels, removed):
    """
    given a tree of nodes cuts after N levels
    """
    if levels == 0:
        removed.extend(node.children)
        node.children = []
    else:
        removed_local = []
        for child in node.children:
            if child.visible:
                cut_after(child, levels - 1, removed)
            else:
                removed_local.append(child)
        for removed_child in removed_local:
            node.children.remove(removed_child)
        removed.extend(removed_local)


class ShowSubMenu(InclusionTag):
    """
    show the sub menu of the current nav-node.
    - levels: how many levels deep
    - root_level: the level to start the menu at
    - nephews: the level of descendants of siblings (nephews) to show
    - template: template used to render the navigation
    """
    name = 'fix_show_sub_menu'
    template = 'menu/dummy.html'

    options = Options(
        IntegerArgument('levels', default=100, required=False),
        Argument('root_level', default=None, required=False),
        IntegerArgument('nephews', default=100, required=False),
        Argument('template', default='menu/sub_menu.html', required=False),
    )

    def get_context(self, context, levels, root_level, nephews, template):
        # Django 1.4 doesn't accept 'None' as a tag value and resolve to ''
        # So we need to force it to None again
        if not root_level and root_level != 0:
            root_level = None
        try:
            # If there's an exception (500), default context_processors may not
            # be called.
            request = context['request']
        except KeyError:
            return {'template': 'menu/empty.html'}
        nodes = menu_pool.get_nodes(request)
        children = []
        # adjust root_level so we cut before the specified level, not after
        include_root = False
        if root_level is not None and root_level > 0:
            root_level -= 1
        elif root_level is not None and root_level == 0:
            include_root = True
        for node in nodes:
            if root_level is None:
                if node.selected:
                    # if no root_level specified, set it to the selected nodes
                    # level
                    root_level = node.level
                    # is this the ancestor of current selected node at the root
                    # level?
            is_root_ancestor = (node.ancestor and node.level == root_level)
            # is a node selected on the root_level specified
            root_selected = (node.selected and node.level == root_level)
            if is_root_ancestor or root_selected:
                cut_after(node, levels, [])
                children = node.children
                for child in children:
                    child.parent = None
                    if child.sibling:
                        cut_after(child, nephews, [])
                        # if root_level was 0 we need to give the menu the
                        # entire tree
                    # not just the children
                if include_root:
                    children = menu_pool.apply_modifiers(
                        [node], request, post_cut=True
                    )
                else:
                    children = menu_pool.apply_modifiers(
                        children, request, post_cut=True
                    )
        context.update({
            'children': children,
            'template': template,
            'from_level': 0,
            'to_level': 0,
            'extra_inactive': 0,
            'extra_active': 0
        })
        return context


register.tag(ShowSubMenu)
