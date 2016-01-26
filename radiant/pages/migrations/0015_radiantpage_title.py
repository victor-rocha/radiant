# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20160125_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='title',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
    ]
