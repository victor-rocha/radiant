# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_auto_20160131_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='radianthuman',
            old_name='thumbnail',
            new_name='slider_image',
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='blurb_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='homepage_blurb',
            field=models.ImageField(default=1, blank=True, upload_to='radiant-human/'),
            preserve_default=False,
        ),
    ]
