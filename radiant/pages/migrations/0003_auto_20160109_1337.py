# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160109_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiantpage',
            name='url',
            field=models.CharField(blank=True, verbose_name='URL', max_length=255, help_text='Leave empty for homepage'),
        ),
    ]
