# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20160124_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiantpage',
            name='url',
            field=models.CharField(verbose_name='URL', blank=True, max_length=255, help_text="e.g. contact/ (notice that this value shouldn't start with an /"),
        ),
    ]
