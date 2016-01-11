# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models


class HtmlSitemapPlugin(CMSPluginBase):

    """ HTML Sitemap CMS plugin. """

    name = _('DjangoCMS HTML Sitemap')
    model = models.HtmlSitemap
    render_template = 'djangocms_htmlsitemap/sitemap.html'

plugin_pool.register_plugin(HtmlSitemapPlugin)
