# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_radiantpage_template_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiantpage',
            name='url',
            field=models.CharField(verbose_name='URL', max_length=255, blank=True, help_text="Once set, this shouldn't be changed."),
        ),
    ]
