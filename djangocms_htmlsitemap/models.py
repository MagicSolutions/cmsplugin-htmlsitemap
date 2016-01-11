# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class HtmlSitemap(CMSPlugin):

    """Model for HTML Sitemap CMS plugin."""

    level_min = models.PositiveSmallIntegerField(_('starting level'), default=0)
    level_max = models.PositiveSmallIntegerField(_('deepest level'), default=100)

    class Meta:
        verbose_name = _('DjangoCMS HTML Sitemap plugin')
        verbose_name_plural = _('DjangoCMS HTML Sitemap plugins')
        ordering = ('level_min', 'level_max')

    def __unicode__(self):
        return u'HTML Sitemap {0}-{1}'.format(self.level_min, self.level_max)
