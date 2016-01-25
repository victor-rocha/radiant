# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20160124_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='radiantpage',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
