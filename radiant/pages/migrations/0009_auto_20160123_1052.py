# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20160123_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='radiantpage',
            old_name='mp4_url',
            new_name='mp4_video',
        ),
        migrations.RenameField(
            model_name='radiantpage',
            old_name='ogg_url',
            new_name='ogg_video',
        ),
        migrations.RenameField(
            model_name='radiantpage',
            old_name='webm_url',
            new_name='webm_video',
        ),
    ]
