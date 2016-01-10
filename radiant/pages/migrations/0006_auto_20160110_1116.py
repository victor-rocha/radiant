# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20160109_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiantpage',
            name='og_description',
            field=models.CharField(max_length=255, null=True, verbose_name='og:description', blank=True),
        ),
        migrations.AddField(
            model_name='radiantpage',
            name='og_image',
            field=models.ImageField(upload_to='ogtags/', help_text='An image has to be at least 50px by 50px, but preferably bigger than 200px by 200px. Plus, the image can’t be more than 5 MB in size.', blank=True),
        ),
        migrations.AddField(
            model_name='radiantpage',
            name='og_title',
            field=models.CharField(max_length=255, null=True, verbose_name='og:title', blank=True),
        ),
        migrations.AddField(
            model_name='radiantpage',
            name='og_type',
            field=models.CharField(null=True, max_length=255, default='article', verbose_name='og:title', blank=True),
        ),
    ]
