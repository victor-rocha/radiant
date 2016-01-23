# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_radianthuman_homepage_blurb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radianthuman',
            name='mp4_url',
            field=models.FileField(blank=True, max_length=255, upload_to='radiant-human/videos/'),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='ogg_url',
            field=models.FileField(blank=True, max_length=255, upload_to='radiant-human/videos/'),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='webm_url',
            field=models.FileField(blank=True, max_length=255, upload_to='radiant-human/videos/'),
        ),
    ]
