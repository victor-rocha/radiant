# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='is_homepage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='radiantpage',
            name='url',
            field=models.CharField(max_length=255, verbose_name='URL', help_text='Leave empty for homepage'),
        ),
    ]
