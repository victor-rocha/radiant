# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20160123_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='youtube_url',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
    ]
