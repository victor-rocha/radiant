# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20160115_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiantpage',
            name='mp4_url',
            field=models.FileField(max_length=255, upload_to='radiant-human/videos/', blank=True),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='ogg_url',
            field=models.FileField(max_length=255, upload_to='radiant-human/videos/', blank=True),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='webm_url',
            field=models.FileField(max_length=255, upload_to='radiant-human/videos/', blank=True),
        ),
    ]
