# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import radiant.common.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_remove_radiantpage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='title',
            field=models.CharField(max_length=255, blank=True, help_text='This is the title for articles, etc.'),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='mp4_video',
            field=models.FileField(blank=True, max_length=255, upload_to=radiant.common.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='name',
            field=models.CharField(max_length=255, help_text='e.g. Homepage', verbose_name="Tab's title"),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='ogg_video',
            field=models.FileField(blank=True, max_length=255, upload_to=radiant.common.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='webm_video',
            field=models.FileField(blank=True, max_length=255, upload_to=radiant.common.models.get_upload_path),
        ),
    ]
