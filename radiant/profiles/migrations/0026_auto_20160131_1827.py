# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0025_auto_20160131_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radianthuman',
            name='blurb_image',
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='homepage_blurb',
            field=models.ImageField(verbose_name='blurb_image', blank=True, upload_to='radiant-human/'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='team/', help_text='image size 380x380 px'),
        ),
    ]
