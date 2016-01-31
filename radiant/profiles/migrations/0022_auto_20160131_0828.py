# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import radiant.common.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20160129_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='title',
            field=models.CharField(max_length=255, blank=True, help_text='This is the title for articles, etc.'),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='mp4_video',
            field=models.FileField(blank=True, max_length=255, upload_to=radiant.common.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='name',
            field=models.CharField(max_length=255, help_text='e.g. Homepage', verbose_name="Tab's title"),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='ogg_video',
            field=models.FileField(blank=True, max_length=255, upload_to=radiant.common.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='webm_video',
            field=models.FileField(blank=True, max_length=255, upload_to=radiant.common.models.get_upload_path),
        ),
    ]
