# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_radianthuman_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='radianthuman',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='radianthuman',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='radianthuman',
            name='homepage_thumbnail',
            field=models.ImageField(blank=True, help_text='Image should be 638x666 px (width x height)', upload_to='radiant-human/'),
        ),
    ]
