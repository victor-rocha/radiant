# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20160110_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='og_description',
            field=models.CharField(max_length=255, verbose_name='og:description', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='og_image',
            field=models.ImageField(upload_to='ogtags/', help_text='An image has to be at least 50px by 50px, but preferably bigger than 200px by 200px. Plus, the image can’t be more than 5 MB in size.', blank=True),
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='og_title',
            field=models.CharField(max_length=255, verbose_name='og:title', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='og_type',
            field=models.CharField(max_length=255, verbose_name='og:title', blank=True, null=True, default='article'),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='name',
            field=models.CharField(max_length=255, help_text='e.g. Homepage'),
        ),
    ]
