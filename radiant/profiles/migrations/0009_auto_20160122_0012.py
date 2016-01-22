# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20160110_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='homepage_thumbnail',
            field=models.ImageField(upload_to='radiant-human/', blank=True),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='og_description',
            field=models.CharField(help_text='Facebook share description', max_length=255, null=True, verbose_name='og:description', blank=True),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='og_title',
            field=models.CharField(help_text='Facebook share title', max_length=255, null=True, verbose_name='og:title', blank=True),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='thumbnail',
            field=models.ImageField(upload_to='radiant-human/', blank=True),
        ),
    ]
