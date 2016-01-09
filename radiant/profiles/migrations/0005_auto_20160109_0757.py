# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_quote_radiant_human'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='ogg_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='webm_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
