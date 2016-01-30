# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_radiantpage_page_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='mata_description',
            field=models.CharField(blank=True, max_length=144),
        ),
    ]
