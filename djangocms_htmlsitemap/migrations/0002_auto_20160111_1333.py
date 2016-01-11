# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_htmlsitemap', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='htmlsitemap',
            options={'verbose_name': 'DjangoCMS HTML Sitemap plugin', 'ordering': ('level_min', 'level_max'), 'verbose_name_plural': 'DjangoCMS HTML Sitemap plugins'},
        ),
        migrations.RemoveField(
            model_name='htmlsitemap',
            name='in_navigation',
        ),
        migrations.RemoveField(
            model_name='htmlsitemap',
            name='match_created_by',
        ),
        migrations.RemoveField(
            model_name='htmlsitemap',
            name='match_language',
        ),
        migrations.RemoveField(
            model_name='htmlsitemap',
            name='match_title',
        ),
        migrations.RemoveField(
            model_name='htmlsitemap',
            name='match_url',
        ),
    ]
